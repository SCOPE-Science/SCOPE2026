#!/usr/bin/env python3
"""Finite checks for the exact attractors of near-dyadic period-doubling prefixes."""
from itertools import combinations

W = ('1','00100','00101','10100','100','001')
BASE_PAIRS = {(4,8),(4,10),(5,10),(6,11),(6,12),(8,12)}

def phi(w):
    return ''.join('01' if c=='0' else '00' for c in w)

def prefix(k):
    z='0'
    for _ in range(k):z=phi(z)
    return z[:-1]

def attractor_pairs(s):
    supports={}
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            f=s[i:j]
            supports[f]=supports.get(f,0)|(((1 << (j-i))-1)<<i)
    masks=set(supports.values())
    return {(i+1,j+1) for i,j in combinations(range(len(s)),2)
            if all(m & ((1<<i)|(1<<j)) for m in masks)}

def signatures():
    table={'odd':set(),'even':set()}
    for ab in ('00','01','10'):
        z=ab
        for _ in range(4): z=phi(z)
        assert len(z)==32
        for i in range(4,28):
            sig=frozenset(w for w in W if any(z[a:a+len(w)]==w for a in range(i-len(w)+1,i+1)))
            table['odd' if i%2==0 else 'even'].add(sig)
    return table

def main():
    assert all(w in prefix(5) for w in W)
    table=signatures()
    assert len(table['odd'])==6,(len(table['odd']), table['odd'])
    assert len(table['even'])==8,(len(table['even']), table['even'])
    assert all('1' not in s for s in table['odd'])
    target=set(W)
    assert all((a|b)!=target for a in table['odd'] for b in (table['odd']|table['even']))
    assert attractor_pairs(prefix(4))==BASE_PAIRS
    for k in range(4,9):
        expected={(a*2**(k-4),b*2**(k-4)) for a,b in BASE_PAIRS}
        actual=attractor_pairs(prefix(k))
        assert actual==expected,(k,actual,expected)
    print('PASS: six base attractors; 6 odd and 8 even finite signatures; no odd-position pair; scaled classification verified at n=4,...,8')

if __name__=='__main__':main()
