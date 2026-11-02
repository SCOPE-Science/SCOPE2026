#!/usr/bin/env python3
"""Modular sanity checks for the exact weighted two-variable even-power image formula.
Finite congruence checks are not proofs of the infinite 2-adic classification.
"""
def valuation(a):
    return (a&-a).bit_length()-1

def expected_values(n,c,mod):
    s=valuation(n); q=1<<(s+2)
    d=valuation(1+c)
    if d>=s+2: return None
    vals={0}; v=0
    while n*v < mod.bit_length():
        scale=1<<(n*v)
        step=scale*q
        for b in (1,c,1+c):
            for y in range((mod+step-1)//step):
                vals.add(((b+q*y)*scale)%mod)
        v+=1
    return vals

def verify():
    cnt=0
    for n in (4,6,8,10,12,14,16,18,20,24,32):
        for c in (1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31):
            for mod in (64,128,256):
                expect=expected_values(n,c,mod)
                if expect is None:continue
                pows={pow(a,n,mod) for a in range(mod)}
                got={(a+c*b)%mod for a in pows for b in pows}
                if got != expect:
                    raise AssertionError((n,c,mod,len(got),len(expect),sorted(got^expect)[:20]))
                cnt+=1
    # In nonsplit cases, val shell set has at most three residues modulo n.
    shells=0
    for n in range(4,260,2):
        q=1<<(valuation(n)+2)
        for c in range(1,q,2):
            if c==q-1:continue
            d=valuation(c+1)
            assert 1<=d<valuation(n)+2 and d<n
            assert len({0,d % n,(-d)%n}) <=3
            shells+=1
    print('VERIFIER_OK', 'modular_value_set_tests=',cnt, 'nonisotropic_val_shell_tests=',shells)
if __name__=='__main__':verify()
