#!/usr/bin/env python3
"""Direct factor-language check against a proposed closed-form antidictionary."""
from itertools import product

def literal_maws(word, alphabet):
    factors={word[i:j] for i in range(len(word)) for j in range(i+1,len(word)+1)}
    answer={a+b for a in alphabet for b in alphabet if a+b not in factors}
    # Valid candidates c U d with c U and U d both present; U can be empty.
    for mid in factors:
        for a in alphabet:
            if a+mid not in factors: continue
            for b in alphabet:
                if mid+b in factors and a+mid+b not in factors:
                    answer.add(a+mid+b)
    return answer

def prediction(runs,k,alphabet):
    q=len(runs)
    block=''.join(a*r for a,r in zip(alphabet,runs))
    p=set()
    for i,a in enumerate(alphabet):
        for j,b in enumerate(alphabet):
            if j not in (i,(i+1)%q):p.add(a+b)
        p.add(a*(runs[i]+1))
        for t in range(1,runs[i]):
            p.add(alphabet[(i-1)%q]+a*t+alphabet[(i+1)%q])
    p.add(alphabet[-1]+block*(k-1)+alphabet[0])
    return p

def run():
    c=0
    total=0
    for q,limit,ks in ((3,3,(2,3,4)),(4,2,(2,3)),(5,2,(2,)),(6,1,(2,3))):
        A='abcdef'[:q]
        for runs in product(range(1,limit+1),repeat=q):
            for k in ks:
                block=''.join(a*r for a,r in zip(A,runs))
                word=block*k
                got=literal_maws(word,A)
                expected=prediction(runs,k,A)
                if got!=expected:
                    print('FAIL',q,runs,k,'missing',sorted(expected-got),'extra',sorted(got-expected));raise SystemExit(1)
                if len(expected)!=q*(q-2)+sum(runs)+1:raise AssertionError('count')
                c+=1;total+=len(got)
    print('VERIFY_OK exhaustive_parameter_cases='+str(c)+' compared_minimal_absent_words='+str(total))
if __name__=='__main__':run()
