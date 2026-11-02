#!/usr/bin/env python3
"""Reproduce exact central-edge characteristic polynomials and independently enumerate
all single-edge spectral exchanges of double stars in a finite parameter window.
Requires Python 3 and NumPy. The general theorem has a separate symbolic proof.
"""
from functools import lru_cache
from math import sqrt
import numpy as np


def double_star(k, m):
    assert k >= m >= 1
    n = k + m + 2
    edges = {(0, 1)}
    edges.update((0, z) for z in range(2, k+2))
    edges.update((1, z) for z in range(k+2, n))
    return n, frozenset(tuple(sorted(e)) for e in edges)


def spectral_radius(n, edges):
    a = np.zeros((n, n), dtype=float)
    for x, y in edges:
        a[x,y] = a[y,x] = 1.0
    return float(np.linalg.eigvalsh(a)[-1])


def components(n, edges):
    adj = [[] for _ in range(n)]
    for x,y in edges:
        adj[x].append(y); adj[y].append(x)
    seen=set(); cs=[]
    for i in range(n):
        if i in seen: continue
        c=set(); stack=[i];seen.add(i)
        while stack:
            v=stack.pop();c.add(v)
            for w in adj[v]:
                if w not in seen:seen.add(w);stack.append(w)
        cs.append(sorted(c))
    return cs


def classify(k,m,removed,added):
    d = k-m
    if removed == (0,1):
        if m >= 2: return -1
        if k == 1: return 0
        return 0 if added == (0,k+2) else -1
    old_center, leaf = removed
    new_endpoint = added[0] if added[1] == leaf else added[1]
    assert leaf >= 2
    if old_center == 0:
        if new_endpoint == 1:
            if d == 0: return 1
            if d == 1: return 0
        elif k == m == 1 and new_endpoint == 3:
            return 0
        return -1
    assert old_center == 1
    if new_endpoint == 0:
        return 1
    if m == 1 and new_endpoint in range(2,k+2):
        return 0
    return -1


def matching_coefficients(n, edges):
    adj = [0]*n
    for a,b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    @lru_cache(None)
    def rec(mask):
        if mask==0: return (1,)
        b=mask&-mask
        v=b.bit_length()-1
        rest=mask^b
        out=list(rec(rest))
        cand=adj[v]&rest
        while cand:
            low=cand&-cand; w=low.bit_length()-1; cand^=low
            other=rec(rest^(1<<w))
            if len(out)<len(other)+1: out.extend([0]*(len(other)+1-len(out)))
            for j,z in enumerate(other):out[j+1]+=z
        return tuple(out)
    return rec((1<<n)-1)


def expected_poly(n,k,m,typ):
    # Polynomial in lambda: lambda^n -(k+m+1)lambda^(n-2) + ...
    c = [1, -(k+m+1)]
    if typ == 'original': c += [k*m]
    elif typ == 'center_u_to_B_leaf': c += [k*m+m-1]
    elif typ == 'A_leaf_to_center_v': c += [k*m+k-1]
    elif typ == 'leaf_to_leaf': c += [k*m+k+m-2, -(k-1)*(m-1)]
    else: raise ValueError(typ)
    return tuple(c)


def direct_polynomial_checks(max_k=7):
    cnt=0
    for k in range(1,max_k+1):
        for m in range(1,k+1):
            n,original=double_star(k,m)
            parts=[('original',original)]
            cut=original-{(0,1)}
            B_leaf=k+2
            parts += [('center_u_to_B_leaf',cut|{(0,B_leaf)}),
                      ('A_leaf_to_center_v',cut|{(1,2)}),
                      ('leaf_to_leaf',cut|{(2,B_leaf)})]
            for typ,edges in parts:
                coefficients=matching_coefficients(n,edges)
                actual=tuple(((-1)**j)*z for j,z in enumerate(coefficients))
                expected=expected_poly(n,k,m,typ)
                for j in range(max(len(actual),len(expected))):
                    a=actual[j] if j<len(actual) else 0
                    b=expected[j] if j<len(expected) else 0
                    assert a==b,(k,m,typ,j,a,b)
                cnt+=1
    return cnt


def exhaustive_exchange_checks(max_k=12):
    checks=0; parameter_pairs=0
    examples=[]
    for k in range(1,max_k+1):
        for m in range(1,k+1):
            n,orig=double_star(k,m)
            rho0=spectral_radius(n,orig)
            x0=((k+m+1)+sqrt((k+m+1)**2-4*k*m))/2
            assert abs(rho0*rho0-x0)<2e-9,(k,m,rho0,x0)
            counts={-1:0,0:0,1:0}
            for old in sorted(orig):
                cut=orig-{old}
                cs=components(n,cut)
                assert len(cs)==2
                for a in cs[0]:
                    for b in cs[1]:
                        add=tuple(sorted((a,b)))
                        if add==old: continue
                        observed=spectral_radius(n,cut|{add})-rho0
                        sign=1 if observed>1e-8 else (-1 if observed < -1e-8 else 0)
                        expected=classify(k,m,old,add)
                        assert sign==expected,(k,m,old,add,observed,sign,expected)
                        counts[sign]+=1
                        checks+=1
            if m>=2:
                expected_strict=2*k if k==m else m
                expected_neutral=k if k==m+1 else 0
            elif k==1:
                expected_strict,expected_neutral=2,5
            elif k==2:
                expected_strict,expected_neutral=1,5
            else:
                expected_strict,expected_neutral=1,k+1
            assert counts[1]==expected_strict and counts[0]==expected_neutral,(k,m,counts)
            if (k,m) in [(1,1),(2,1),(3,1),(3,2),(3,3),(4,2),(4,3),(4,4),(7,3)]:
                examples.append((k,m,counts[1],counts[0]))
            parameter_pairs+=1
    return checks,parameter_pairs,examples


def main():
    p=direct_polynomial_checks()
    print('EXACT_MATCHING_CHARACTERISTIC_POLYNOMIALS_OK',p)
    checks,pairs,examples=exhaustive_exchange_checks()
    print('INDEPENDENT_ALL_EDGE_EXCHANGES_OK',pairs,checks)
    for k,m,strict,neutral in examples:
        print('SPECTRAL_EXCHANGE_COUNTS_OK',k,m,strict,neutral)
    print('VERIFY_OK')


if __name__=='__main__':main()
