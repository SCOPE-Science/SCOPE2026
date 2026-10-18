#!/usr/bin/env python3
"""Independent finite tests of a line-graph power-domination characterization.

Usage: python verify_power_multipartite.py
Only standard library required.
"""
from itertools import product
from math import comb
from collections import defaultdict

def edges_of_multipartite(parts):
    labels = sum(([i] * a for i, a in enumerate(parts)), [])
    return [(u,v) for u in range(len(labels)) for v in range(u+1,len(labels)) if labels[u]!=labels[v]],labels

def power_dominate_line(edges, selected_mask):
    m=len(edges)
    if not selected_mask:return False
    # Simulate the line-graph domination step and all legal propagation steps.
    observed=selected_mask
    for e,(a,b) in enumerate(edges):
        if (selected_mask>>e)&1:
            for f,(c,d) in enumerate(edges):
                if a==c or a==d or b==c or b==d:
                    observed|=1<<f
    while 1:
        changed=False
        for e,(a,b) in enumerate(edges):
            if not ((observed>>e)&1):continue
            unseen=[]
            for f,(c,d) in enumerate(edges):
                if not ((observed>>f)&1) and (a==c or a==d or b==c or b==d): unseen.append(f)
                if len(unseen)>1:break
            if len(unseen)==1:
                observed|=1<<unseen[0];changed=True;break
        if not changed:break
    return observed==(1<<m)-1

def forest_complement_criterion(edges,labels,mask):
    used=set()
    for j,(a,b) in enumerate(edges):
        if mask>>j&1:used.add(a);used.add(b)
    if not used:return False
    amounts=[sum(i not in used and labels[i]==t for i in range(len(labels))) for t in range(max(labels)+1)]
    nonzero=[a for a in amounts if a]
    return len(nonzero)<=1 or (len(nonzero)==2 and min(nonzero)==1)

def poly_from_formula(parts):
    r=len(parts);m=sum(parts[i]*parts[j] for i in range(r) for j in range(i+1,r))
    pol=[0]*(m+1)
    for t in product(*[range(a+1) for a in parts]):
        positive=[x for x in t if x]
        if not (len(positive)<=1 or (len(positive)==2 and min(positive)==1)):
            continue
        b=tuple(a-x for a,x in zip(parts,t))
        if sum(b)<2:continue
        choices=1
        for a,x in zip(parts,t):choices*=comb(a,x)
        for j in product(*[range(x+1) for x in b]):
            u=[x-y for x,y in zip(b,j)]
            exp=sum(u[i]*u[k] for i in range(r) for k in range(i+1,r))
            sign=(-1)**sum(j)
            mult=choices*sign
            for x,y in zip(b,j):mult*=comb(x,y)
            for k in range(exp+1):pol[k]+=mult*comb(exp,k)
    return pol

def run():
    graphs=0;tests=0;subsets=0
    distributions={}
    cases=[]
    for r in range(2,6):
        for parts in product(range(1,5),repeat=r):
            if tuple(sorted(parts))!=parts:continue
            edges,labels=edges_of_multipartite(parts)
            if len(edges)>16:continue
            cases.append(parts)
    for parts in cases:
        edges,labels=edges_of_multipartite(parts)
        brute=[0]*(len(edges)+1)
        for mask in range(1<<len(edges)):
            direct=power_dominate_line(edges,mask)
            predicted=forest_complement_criterion(edges,labels,mask)
            assert direct==predicted,(parts,mask,direct,predicted)
            if direct:brute[mask.bit_count()]+=1
            subsets+=1
        calc=poly_from_formula(parts)
        assert brute==calc,(parts,brute,calc)
        distributions[str(parts)]=brute
        graphs+=1;tests+=1
    for m in range(2,6):
        for n in range(m,7):
            if m*n>20:continue
            edges,labels=edges_of_multipartite((m,n))
            c=poly_from_formula((m,n))
            assert next((k for k,x in enumerate(c) if x),None)==m-1
            top=m*n**(m-1) if m<n else 2*m**m-m*m*__import__('math').factorial(m-1)
            assert c[m-1]==top,(m,n,c,top)
    # Triangle-graph minimum-set formulas checked via exact polynomials.
    for n in range(3,9):
        c=poly_from_formula((1,)*n)
        k=(n-1)//2 if n%2 else (n-2)//2
        from math import factorial
        if n%2==0:
            top=factorial(n)//(2**(n//2)*factorial(n//2-1))
        else:
            top=factorial(n)//(2**k*factorial(k))
            if k>=2:top+=factorial(n)//(2**k*factorial(k-2))
        assert next(i for i,v in enumerate(c) if v)==k
        assert c[k]==top,(n,c[k],top)
    print(f'VERIFICATION_OK graph_profiles={graphs} edge_subset_cases={subsets} inclusion_exclusion_matches={tests} triangular_n=3..8')
    print('Examples:')
    for key in ['(2, 2)','(2, 3)','(3, 3)','(1, 1, 1, 1)','(1, 2, 2)']:
        if key in distributions:print(f'  {key}: {distributions[key]}')
if __name__=='__main__':run()
