#!/usr/bin/env python3
"""Direct finite checks for a run-threshold theorem about Parikh supports.
Scientific verification only; no external dependencies.
"""
from itertools import product
from collections import defaultdict

def parikh_support(word):
    """Direct enumeration of all nonempty contiguous factors."""
    result=set()
    for a in range(len(word)):
        z=o=0
        for b in range(a,len(word)):
            if word[b]=='0':z+=1
            else:o+=1
            result.add((z,o))
    return frozenset(result)

def runs(word):
    return 0 if not word else 1+sum(x!=y for x,y in zip(word,word[1:]))

def predicted_invariants(word):
    sig=parikh_support(word)
    Z=word.count('0'); O=word.count('1')
    m0=max((i for i,j in sig if j==0),default=0)
    m1=max((j for i,j in sig if i==0),default=0)
    if Z and O:
        t0=any(i==Z and j<O for i,j in sig)
        t1=any(j==O and i<Z for i,j in sig)
        return m0,m1,t0,t1
    return m0,m1,False,False

def predicted_five(word):
    # Finite test of the observation formulas, separate from recovery proof.
    n=runs(word)
    if n!=5:return
    if word[0]=='1':word=word.translate(str.maketrans('01','10'))
    a,b,c,d,e=[len(t) for t in __import__('re').findall(r'0+|1+',word)]
    Z=a+c+e;O=b+d; m=max(a,c,e)
    S=parikh_support(word)
    maxz=lambda j:max((i for i,k in S if k==j),default=-1)
    minz=lambda j:min((i for i,k in S if k==j),default=-1)
    assert minz(O)==c,(word,'middle separator')
    assert maxz(max(b,d))==c+max(a,e),(word,'outer max')
    j=min(b,d)
    predicted=max(m,c+(a if b<d else e if d<b else max(a,e)))
    assert maxz(j)==predicted,(word,'orientation',maxz(j),predicted)

def predicted_four(word):
    if runs(word)!=4:return
    if word[0]=='1':word=word[::-1]
    a,b,c,d=[len(t) for t in __import__('re').findall(r'0+|1+',word)]
    S=parikh_support(word);Z=a+c;O=b+d
    minz=lambda j:min((i for i,k in S if k==j),default=-1)
    maxz=lambda j:max((i for i,k in S if k==j),default=-1)
    assert minz(O)==c
    assert min(j for j in range(1,O+1) if maxz(j)==Z)==b
    for j in range(1,b):assert maxz(j)==max(a,c),(word,j,maxz(j),max(a,c))


def recover_low_run_word(spectrum):
    """Deterministic reconstruction of any <=5-run word, modulo reversal."""
    S=set(spectrum)
    Z=max((i for i,j in S),default=0)
    O=max((j for i,j in S),default=0)
    if O==0:return '0'*Z
    if Z==0:return '1'*O
    M0=max(i for i,j in S if j==0)
    M1=max(j for i,j in S if i==0)
    if M0==Z and M1==O:return '0'*Z+'1'*O
    if M0==Z:return '1'*M1+'0'*Z+'1'*(O-M1)
    if M1==O:return '0'*M0+'1'*O+'0'*(Z-M0)
    has_all_zeros_with_partial_ones=any(i==Z and j<O for i,j in S)
    has_all_ones_with_partial_zeros=any(j==O and i<Z for i,j in S)
    maxz=lambda j:max((i for i,k in S if k==j),default=-1)
    minz=lambda j:min((i for i,k in S if k==j),default=-1)
    if has_all_zeros_with_partial_ones and has_all_ones_with_partial_zeros:
        c=minz(O);a=Z-c
        b=next(j for j in range(1,O+1) if maxz(j)==Z)
        d=O-b
        return '0'*a+'1'*b+'0'*c+'1'*d
    if has_all_zeros_with_partial_ones:
        flipped={(j,i) for i,j in S}
        answer=recover_low_run_word(flipped)
        return answer.translate(str.maketrans('01','10'))
    if not has_all_ones_with_partial_zeros:
        raise AssertionError('outside the <=5-run domain')
    c=minz(O)
    highouter=maxz(M1)-c
    lowouter=Z-c-highouter
    shortones=O-M1
    longones=M1
    if highouter==lowouter or shortones==longones:
        return '0'*highouter+'1'*longones+'0'*c+'1'*shortones+'0'*lowouter
    if maxz(shortones)==c+highouter:
        b,d=shortones,longones
    else:
        b,d=longones,shortones
    return '0'*highouter+'1'*b+'0'*c+'1'*d+'0'*lowouter

def main():
    checked=0
    # Exact comparison of FULL support, not only a particular invariant.
    for n in range(1,17):
        seen={}
        for bits in product('01',repeat=n):
            word=''.join(bits)
            if runs(word)>5:continue
            sig=parikh_support(word)
            repr_=min(word,word[::-1])
            assert sig not in seen or seen[sig]==repr_,(n,word,seen[sig])
            seen[sig]=repr_
            assert recover_low_run_word(sig) in (word,word[::-1]),(word,recover_low_run_word(sig))
            if runs(word)==5:predicted_five(word)
            elif runs(word)==4:predicted_four(word)
            checked+=1
    param=0
    for a,b,c,d,e in product(range(1,8),repeat=5):
        word='0'*a+'1'*b+'0'*c+'1'*d+'0'*e
        predicted_five(word)
        assert recover_low_run_word(parikh_support(word)) in (word,word[::-1])
        param+=1
    for t in range(2,70):
        u='0101'+'0'*t+'1'
        v='01'+'0'*t+'101'
        assert len(u)==len(v)
        assert runs(u)==runs(v)==6
        assert u!=v and u!=v[::-1]
        assert parikh_support(u)==parikh_support(v)
        expected=(
            {(i,0) for i in range(1,t+1)}|
            {(i,1) for i in range(t+2)}|
            {(i,2) for i in range(1,t+3)}|
            {(i,3) for i in (t+1,t+2)}
        )
        assert parikh_support(u)==expected,(t,parikh_support(u)^expected)
    for n in range(1,8):
        groups=defaultdict(set)
        for bits in product('01',repeat=n):
            w=''.join(bits)
            groups[parikh_support(w)].add(min(w,w[::-1]))
        if n<7:assert all(len(g)==1 for g in groups.values()),(n,groups)
        else:assert any(len(g)>1 for g in groups.values())
    print(f'VERIFY_OK exhaustive_low_run_words={checked} n=1..16 five_run_parameter_tuples={param} six_run_collision_t=2..69 first_ambiguous_length=7')

if __name__=='__main__':main()
