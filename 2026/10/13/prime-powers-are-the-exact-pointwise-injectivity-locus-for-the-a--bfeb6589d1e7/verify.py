from fractions import Fraction

def blocks(n):
    x=n; p=2; out=[]
    while p*p<=x:
        if x%p==0:
            P=1
            while x%p==0:
                x//=p; P*=p
            out.append(P)
        p += 1 if p==2 else 2
    if x>1: out.append(x)
    return out

mixed=pp=0
for n in range(2,10001):
    B=blocks(n)
    if len(B)==1:
        pp+=1; continue
    mixed+=1
    P,Q=B[0],B[1]
    assert Fraction(1,P)-Fraction(1,2*Q) != 0
    assert P != 2*Q
    P,Q=max(B),min(B)
    y=Fraction(P-Q,P)
    assert y>0
    assert Fraction(1,P)+(y-1)/Q == 0
    assert 2*y != 1
    assert P != 2*Q
print(f"VERIFY_OK limit=10000 prime_powers={pp} mixed_support={mixed} both_direction_templates=passed")
