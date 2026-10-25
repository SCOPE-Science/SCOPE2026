"""Exact finite checks for a two-quantifier cyclic-group separation claim."""
from itertools import product

def ternary_relation(a,b,c,n):
    return (a+b-c) % n == 0

def matrix(x,y,n):
    return (x != 0 and y != 0 and x != y
            and not ternary_relation(x,x,y,n)
            and not ternary_relation(y,y,x,n)
            and not ternary_relation(x,y,0,n))

def unary_atomic_type(x,n):
    # Complete unary atomic truth data for language {e,R,=},
    # evaluated with terms restricted to x and the constant e.
    terms = (x,0)
    return (x==0,)+tuple(ternary_relation(a,b,c,n)
          for a,b,c in product(terms,repeat=3))

def check_group(n):
    witness = next(((x,y) for x in range(n) for y in range(n)
                     if matrix(x,y,n)),None)
    return witness, {unary_atomic_type(x,n) for x in range(n)}

if __name__ == '__main__':
    base, types_5 = check_group(5)
    assert base is None
    assert len(types_5)==2
    for k in (2,3,4):
        n=5**k
        prescribed_x,prescribed_y=5**(k-2),3*5**(k-2)
        assert matrix(prescribed_x,prescribed_y,n)
        witness,types=check_group(n)
        assert witness is not None
        assert types==types_5
        print(f'CHECK_OK C5_vs_C{n} base=False target=True '
              f'rank1_types={len(types)} witness={prescribed_x},{prescribed_y}')
    print('INFINITE_PROOF_ONLY: witnessed all k>=2 by group arithmetic, not by finite loop')
    print('VERIFY_OK')
