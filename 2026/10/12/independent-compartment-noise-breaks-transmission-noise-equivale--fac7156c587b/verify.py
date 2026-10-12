from fractions import Fraction

# Factor out S^2 I^2. The source uses g^2=(1/50)(1-alpha)^2 S^2 I^2.
alpha_max = Fraction(17,20)
c2 = Fraction(1,50)
g2_factor = c2 * (1-alpha_max)**2
assert g2_factor > 0

# Covariances divided by g^2.
A_ind = ((1,0),(0,1))
A_common = ((1,-1),(-1,1))
e=(1,1)
def quad(A,v):
    return sum(v[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
assert quad(A_ind,e) == 2
assert quad(A_common,e) == 0
assert A_ind[0][1] == 0 and A_common[0][1] == -1

# Exact source coefficient at alpha_max: (1/50)*(3/20)^2 = 9/20000.
assert g2_factor == Fraction(9,20000)
# Hence printed sum-coordinate qv factor is 2*g^2 = 9/10000 at positive S,I.
assert 2*g2_factor == Fraction(9,10000)
print("VERIFY_OK")
