#!/usr/bin/env python3
"""Finite cross-check of the formula for the full-rotation factor classes.
No computation in this file is used as a substitute for the infinite proof.
"""

def fixed_prefix(radix, min_length):
    word=b'0'
    zero=b'0'*(radix-1)
    while len(word)<min_length:
        word=b''.join(zero+(b'1' if c==48 else b'0') for c in word)
    return word

def classes_from_factors(word,n):
    factors={word[i:i+n] for i in range(len(word)-n+1)}
    seen=set()
    complete=[]
    for w in factors:
        rotations={w[j:]+w[:j] for j in range(n)}
        canonical=min(rotations)
        if canonical not in seen:
            seen.add(canonical)
            if rotations<=factors:
                complete.append(canonical)
    return len(complete), tuple(sorted(complete))

def predicted(radix,n):
    while n%radix==0:
        n//=radix
    return 2 if n<=2*radix-1 else 0

def main():
    checks=0
    for radix in range(2,8):
        word=fixed_prefix(radix,36000)
        # Independent windows in nested prefixes provide a finite stability check.
        for n in range(1,min(85,3*radix*radix)+1):
            long,cl=classes_from_factors(word[:32000],n)
            short,_=classes_from_factors(word[:16000],n)
            expected=predicted(radix,n)
            assert long==short==expected, (radix,n,short,long,expected,cl)
            checks+=1
    print('GENERALIZED_LIE_FINITE_PASS',f'cases={checks}', 'radices=2..7','prefixes=16000,32000')
if __name__=='__main__':main()
