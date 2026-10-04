from math import isqrt

def delta(a,b):
    return 6*a*b - 4*a - 4*b + 4

def closest_factor(D):
    for a in range(isqrt(D),0,-1):
        if D%a==0:
            return a,D//a
    raise AssertionError

pairs=0
for D in range(1,5001):
    fac=[]
    for a in range(1,isqrt(D)+1):
        if D%a==0:
            b=D//a
            fac.append((a,b,delta(a,b)))
    pairs += len(fac)
    aa,bb=closest_factor(D)
    vals=[z for _,_,z in fac]
    mx=max(vals); mn=min(vals)
    assert delta(aa,bb)==mx
    assert delta(1,D)==mn==2*D
    max_pairs=[(a,b) for a,b,z in fac if z==mx]
    min_pairs=[(a,b) for a,b,z in fac if z==mn]
    assert max_pairs==[(aa,bb)]
    assert min_pairs==[(1,D)]
    for a,b,z in fac:
        assert 2*D <= z
        # squared version of z <= 6D-8sqrt(D)+4 to avoid floating point:
        # 6D+4-z >= 8 sqrt(D), both sides nonnegative.
        lhs=6*D+4-z
        assert lhs>=0 and lhs*lhs >= 64*D
        if lhs*lhs==64*D:
            assert a==b and a*a==D
    if isqrt(D)**2==D:
        s=isqrt(D)
        assert delta(s,s)==6*D-8*s+4

# Symbolic Chern-class coefficients for X=P1xP1:
# c2(X)=4, K.L=-2(a+b), L^2=2ab, so c2(J1(L))=c2+2KL+3L^2.
for a in range(1,101):
    for b in range(a,101):
        jet=4 + 2*(-2*(a+b)) + 3*(2*a*b)
        assert jet==delta(a,b)
        assert delta(a,b)-2*a*b == 4*(a-1)*(b-1)
        # Squared-radical identity is checked after rearranging:
        # (6ab+4-delta)/4 = a+b = 2sqrt(ab)+(sqrt(b)-sqrt(a))^2.
        assert (6*a*b+4-delta(a,b)) == 4*(a+b)

print('VERIFY_OK')
print('D_RANGE=1..5000')
print(f'FACTOR_PAIRS_CHECKED={pairs}')
print('JET_CLASS_GRID=1<=a<=b<=100')
print('MIN_MAX_UNIQUENESS=OK')
print('SHARP_SQRT_ENVELOPE=OK')
