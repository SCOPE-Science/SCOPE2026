def rho(g,r,d):
    return g-(r+1)*(g-d+r)

g,r,d=8,2,6
assert rho(g,r,d)==-4
expected=3*g-3+rho(g,r,d)
assert expected==17
# Plane sextic arithmetic genus and node count for geometric genus 8.
pa=(d-1)*(d-2)//2
assert pa==10
delta=pa-g
assert delta==2
# Severi dimension modulo PGL_3.
severi_dim=3*d+g-1
assert severi_dim==25
assert severi_dim-8==17
# Trigonal Hurwitz dimension: b=2g+2k-2 simple branch points, modulo PGL_2.
k=3
branch=2*g+2*k-2
assert branch==20
assert branch-3==17
# Non-birational basepoint-free g^2_6: e*k=6, e,k>=2.
pairs=[(e,k) for e in range(2,7) for k in range(2,7) if e*k==6]
assert pairs==[(2,3),(3,2)]
# Haburcak--Teixidor dimension bound for rational image: dim <= 2g-5+2k.
assert 2*g-5+2*2==15 < expected
assert 2*g-5+2*3==17 == expected
# Coppens--Kato nodal-plane criterion (even d): g >= d(d-4)/4 - 1.
threshold=d*(d-4)/4-1
assert threshold==2
assert g>=threshold
assert d-2==4
print("VERIFY_OK rho=-4 expected=17 delta=2 severi=17 trigonal=17 only_nonbirational_k=3 gonality_severi=4")
