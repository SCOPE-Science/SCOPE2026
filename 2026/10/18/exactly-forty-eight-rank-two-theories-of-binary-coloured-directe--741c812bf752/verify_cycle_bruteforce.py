#!/usr/bin/env python3
"""Direct two-round atomic-pair-game check, brute cyclic words, independent of the state recurrence."""
from collections import Counter

def two_round_type(w):
    n=len(w)
    root_set=set()
    for i in range(n):
        pairs=set()
        for j in range(n):
            atom=(int(w[i]),int(w[j]),int(i==j),int((i+1)%n==j),int((j+1)%n==i))
            pairs.add(atom)
        root_set.add(frozenset(pairs))
    return frozenset(root_set)

def direct_formula(w):
    n=len(w);z=w.count('0');o=n-z
    types=set()
    for i in range(n):
        p=int(w[(i-1)%n]);x=int(w[i]);s=int(w[(i+1)%n]);
        other=(int(z-(p==0)-(x==0)-(s==0)>0),int(o-(p==1)-(x==1)-(s==1)>0))
        types.add((p,x,s,other))
    return frozenset(types)

def linear_summary(w):
    factors={w[i:i+3] for i in range(len(w)-2)}
    code=0
    for t in factors:
        code |= (1<<int(t,2))
    return (w[:2],w[-2:],min(4,w.count('0')),min(4,w.count('1')),code)

def main():
    alltypes=set(); best={}; perlength={}; raw_to_formula={}; formula_to_raw={}
    for n in range(3,16):
        sigs=set()
        for mask in range(1<<n):
            w=''.join('1' if (mask>>i)&1 else '0' for i in range(n))
            typ=two_round_type(w)
            sig=direct_formula(w)
            # The two signatures must be in bijection on the tested cyclic words.
            prev=best.get(typ)
            if prev is None:best[typ]=w
            if typ not in alltypes:alltypes.add(typ)
            sigs.add(sig)
            assert len(typ)==len(sig)
            if typ in raw_to_formula: assert raw_to_formula[typ]==sig
            else: raw_to_formula[typ]=sig
            if sig in formula_to_raw: assert formula_to_raw[sig]==typ
            else: formula_to_raw[sig]=typ
        perlength[n]=len(sigs)
    cnt=Counter(map(len,best.values()))
    assert len(best)==len(raw_to_formula)==len(formula_to_raw)==48,(len(best),cnt)
    assert cnt=={3:4,4:6,5:6,6:9,7:10,8:9,9:4},cnt
    # Independent exhaustive generation of every summary state at lengths 2..15.
    # This is a finite inductive certificate: the reached set contains all seeds
    # and is closed under both letters, hence contains all longer summaries.
    summaries={}
    for n in range(2,16):
        for bits in range(1<<n):
            w=format(bits, f'0{n}b')
            s=linear_summary(w)
            summaries.setdefault(s,w)
    assert len(summaries)==758, len(summaries)
    for s,w in summaries.items():
        assert linear_summary(w+'0') in summaries
        assert linear_summary(w+'1') in summaries
    print('EXHAUSTIVE_SUMMARY_STATES',len(summaries),'CLOSED_UNDER_BOTH_APPEND_OPERATIONS',True)
    print('BRUTE_ALL_WORDS_THROUGH_LENGTH',15)
    print('RANK2_THEORIES',len(best))
    print('SHORTEST_REP_DISTRIBUTION',sorted(cnt.items()))
    print('THEORIES_AT_EACH_LENGTH',sorted(perlength.items()))
    print('VERIFY_OK')

if __name__=='__main__':main()
