#!/usr/bin/env python3
"""Independent exhaustive length-four forbidden-factor cyclic-cover check.
This checker enumerates indexed binary circles of lengths 15 and 16;
there are no longer optimality claims for order four.
"""
import json,sys
PATS=('0000','0001','0010','0011','0101','0110')

def windows(x,L):
    mask=(1<<L)-1
    bits=format(x,'0%db'%L)
    return {''.join(bits[(i+j)%L] for j in range(4)) for i in range(L)}

def main(p):
    cert=json.load(open(p,encoding='utf-8'))
    listed={c['pattern']:c['required']+c['additional'] for c in cert['cases'] if c['n']==4}
    assert set(listed)==set(PATS)
    answers={p:None for p in PATS}
    # A 4-window circle contains at most L distinct words; 15 required words.
    for L in (15,16):
        for x in range(1<<L):
            obs=windows(x,L)
            for pat in PATS:
                if answers[pat] is None and all(format(y,'04b') in obs for y in range(16) if format(y,'04b')!=pat):
                    answers[pat]=L
        if all(v is not None for v in answers.values()):break
    assert answers==listed,(answers,listed)
    print('CROSSCHECK_OK',answers)
if __name__=='__main__':main(sys.argv[1])
