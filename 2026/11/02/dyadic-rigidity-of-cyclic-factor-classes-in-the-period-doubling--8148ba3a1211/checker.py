#!/usr/bin/env python3
"""Finite direct comparison of period-doubling cyclic factor classes."""

def fixed_prefix(power=15):
    s='0'
    for _ in range(power):
        s=''.join('01' if c=='0' else '00' for c in s)
    return s

def minimum_rotation(x):
    # Direct definition, deliberately independent of the morphism argument.
    return min(x[i:]+x[:i] for i in range(len(x)))

def classes(text, n, prefix_starts):
    return {minimum_rotation(text[i:i+n]) for i in range(prefix_starts)}

def main():
    p=fixed_prefix()
    tested=0
    # 4000 starts are independently compared against 8000 starts;
    # this finite agreement is not used to infer completeness at all lengths.
    for n in range(1,101):
        shorter=classes(p,n,4000)
        doubled=classes(p,2*n,4000)
        assert shorter == classes(p,n,8000), (n,'shorter sampling')
        assert doubled == classes(p,2*n,8000), (n,'doubled sampling')
        assert len(shorter)==len(doubled), (n,len(shorter),len(doubled))
        # Check the image map is a bijection on the observed cyclic classes.
        mapped={minimum_rotation(''.join('01' if c=='0' else '00' for c in u)) for u in shorter}
        assert mapped == doubled, (n,'class mapping')
        tested += 1
    examples={n:len(classes(p,n,8000)) for n in (1,2,3,5,6,7,9,10,12,15,24,31,32,33)}
    print('VERIFY_OK: dyadic orbit bijection directly checked for n=1..100')
    print('Class counts:', examples)
    print('Limit: finite samples only; infinite coverage is supplied by the proof.')
if __name__=='__main__':main()
