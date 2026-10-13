from fractions import Fraction as F

# Exact worked example.
L = F(4)
mu = F(1)
kappa = L / mu
r_star = L*mu/(L-mu)
assert r_star == F(4,3)
post1 = L*r_star/(L+r_star)
assert post1 == mu == F(1)

r = F(1,4)
post1 = L*r/(L+r)
assert post1 == F(4,17)
post_cond = mu/post1
assert post_cond == F(17,4)
assert post_cond > kappa

threshold = L*mu*mu/(L*L-mu*mu)
assert threshold == F(4,15)
assert r < threshold

# Exact dimensionless envelope.
eta = r/mu
q = kappa*eta/(kappa+eta)
assert q == F(4,17)
assert 1/q == post_cond

# Determinant of S=P^{-1}+r^{-1} h h^T in the eigenbasis.
# If t=h_1^2 and 1-t=h_2^2, determinant lemma gives
# det(S)=det(P^{-1})*(1+(L*t+mu*(1-t))/r), affine increasing in t.
for LL, mm, rr in [(F(5),F(2),F(3)), (F(7),F(1),F(2)), (F(9),F(4),F(5,2))]:
    assert LL > mm > 0 and rr > 0
    vals=[]
    for t in [F(0),F(1,4),F(1,2),F(3,4),F(1)]:
        detS = F(1,LL*mm) * (1 + (LL*t + mm*(1-t))/rr)
        vals.append(detS)
    assert vals == sorted(vals)
    assert vals[-1] > vals[0]

print('VERIFY_OK')
print('isotropy_noise', r_star)
print('overmeasurement_condition', post_cond)
