"""Exact checks of two-site habitat-fragment identifiability on trees.

Standard-library only. These computations supplement (not replace) the proof.
"""
import json
from collections import Counter, defaultdict
from fractions import Fraction
from heapq import heapify, heappop, heappush
from itertools import product
from math import comb
from pathlib import Path

A = [(0,1),(0,7),(0,10),(1,2),(1,6),(2,3),(2,4),(2,5),(7,8),(8,9)]
B = [(0,1),(0,7),(1,2),(1,5),(1,6),(2,3),(2,4),(7,8),(7,10),(8,9)]

def degrees(n, edges):
    d = [0] * n
    for a,b in edges:
        assert 0<=a<n and 0<=b<n and a!=b
        d[a]+=1; d[b]+=1
    return d

def verify_tree(n,edges):
    assert len(edges)==n-1 and len(set(tuple(sorted(e)) for e in edges))==len(edges)
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    seen={0};queue=[0]
    for x in queue:
        for y in adj[x]-seen:
            seen.add(y);queue.append(y)
    assert len(seen)==n
    return adj

def hist(n,edges):
    d=degrees(n,edges)
    return Counter(tuple(sorted((d[u],d[v]))) for u,v in edges)

def edge_sums(n,edges):
    d=degrees(n,edges)
    return Counter(d[u]+d[v] for u,v in edges)

def coefficients_pair_components(n, edges):
    adj=verify_tree(n,edges)
    result=[0]*(n+1)
    for bits in range(1<<n):
        unseen={v for v in range(n) if bits & (1<<v)}
        pairs=0
        while unseen:
            start=unseen.pop(); stack=[start]; size=1
            while stack:
                for v in adj[stack.pop()] & unseen:
                    unseen.remove(v); stack.append(v); size+=1
            pairs+=(size==2)
        result[bits.bit_count()]+=pairs
    return result

def exact_expected(coeffs,n,p):
    q=1-p
    return sum(Fraction(coeffs[k])*p**k*q**(n-k) for k in range(n+1))

def polynomial_coeffs_in_p(n,edges):
    # E = sum over edges p^2(1-p)^(deg(u)+deg(v)-2)
    c=edge_sums(n,edges)
    ans=[0]*(n+1)
    for s,v in c.items():
        for j in range(s-1):
            ans[j+2]+=v*((-1)**j)*comb(s-2,j)
    return ans

def poly_from_fixed_coeffs(n,coeffs):
    # Exhaustive induced component counts by quota, convert q^(n-k) to p polynomial.
    ans=[0]*(n+1)
    for k,v in enumerate(coeffs):
        for j in range(n-k+1):
            ans[k+j]+=v*((-1)**j)*comb(n-k,j)
    return ans

def from_prufer(n,word):
    d=[1]*n
    for x in word: d[x]+=1
    leaves=[i for i,x in enumerate(d) if x==1];heapify(leaves)
    edges=[]
    for x in word:
        y=heappop(leaves)
        edges.append((y,x));d[y]-=1;d[x]-=1
        if d[x]==1:heappush(leaves,x)
    last=sorted(leaves)
    edges.append(tuple(last))
    return edges

def invert_subcubic(n,edges):
    d=degrees(n,edges)
    if max(d)>3:return False
    ns=Counter(d)
    cs=edge_sums(n,edges)
    m12=cs[3];m23=cs[5];m33=cs[6]
    m22=(2*ns[2]-m12-m23)//2
    assert (2*ns[2]-m12-m23)%2==0
    m13=cs[4]-m22
    expected=Counter({(1,2):m12,(1,3):m13,(2,2):m22,(2,3):m23,(3,3):m33})
    actual=hist(n,edges)
    return all(expected[t]==actual[t] for t in expected)


def run():
    checks={"method":"exact integer enumeration of all retained subsets plus independent event-polynomial algebra", "program":"verify_fragment.py"}
    types=((1,2),(1,3),(1,4),(2,2),(2,3),(2,4),(3,3),(3,4),(4,4))
    for edges in [A,B]:verify_tree(11,edges)
    assert Counter(degrees(11,A))==Counter(degrees(11,B))=={1:6,2:2,3:2,4:1}
    expected_sums={3:1,4:3,5:4,6:1,7:1}
    assert edge_sums(11,A)==edge_sums(11,B)==expected_sums
    da=hist(11,A);db=hist(11,B)
    kernel=[da[t]-db[t] for t in types]
    assert kernel==[0,-1,1,1,-1,-1,1,0,0],kernel
    checks["joint_degree_delta"]={f"{i}{j}":da[(i,j)]-db[(i,j)] for i,j in types}
    assert sum(da.values())==sum(db.values())==10
    ca=coefficients_pair_components(11,A)
    cb=coefficients_pair_components(11,B)
    assert poly_from_fixed_coeffs(11,ca)==polynomial_coeffs_in_p(11,A)
    assert poly_from_fixed_coeffs(11,cb)==polynomial_coeffs_in_p(11,B)
    assert ca==cb, (ca,cb)
    assert exact_expected(ca,11,Fraction(1,2))==Fraction(59,128)
    for p in [Fraction(1,10),Fraction(1,3),Fraction(1,2),Fraction(3,4),Fraction(9,10)]:
        q=1-p
        predicted=sum(p*p*pow(q,s-2)*m for s,m in expected_sums.items())
        assert exact_expected(ca,11,p)==exact_expected(cb,11,p)==predicted
    checks["11_vertex_subsets_enumerated_per_tree"]=2048
    checks["11_vertex_fixed_quota_component_sum_by_k"]=ca
    checks["closed_formula_at_p_half"]="59/128"
    checks["degree_histogram"]={str(k):v for k,v in sorted(Counter(degrees(11,A)).items())}
    checks["degree_sum_histogram"]={str(k):v for k,v in sorted(expected_sums.items())}
    tested=0
    by_n={}
    for n in range(3,7):
        cnt=0
        for prufer in product(range(n),repeat=n-2):
            edges=from_prufer(n,prufer)
            if max(degrees(n,edges))<=3:
                assert invert_subcubic(n,edges)
                cnt+=1
        by_n[n]=cnt
        tested+=cnt
    checks["labeled_subcubic_trees_checked"]={str(k):v for k,v in by_n.items()}
    checks["total_labeled_subcubic_trees_checked"]=tested
    checks["proof_limitations"]="This finite computation is not a proof of the all-tree uniqueness theorem or sharp n>=11 lower bound; those are established algebraically in RESULT.md."
    return checks

if __name__ == '__main__':
    certificate=run()
    print(json.dumps(certificate,indent=2,sort_keys=True))
