from fractions import Fraction
import itertools
import numpy as np

# Exact Boolean face decomposition check on a rational grid.
vals=[Fraction(0),Fraction(1,5),Fraction(2,5),Fraction(3,5),Fraction(4,5),Fraction(6,5)]
for x in itertools.product(vals, repeat=3):
    def g(I):
        return int(sum(x[i] for i in I)>1)
    singles=sum(g((i,)) for i in range(3))
    pairs=0
    for i,j in [(0,1),(0,2),(1,2)]:
        pairs += g((i,j))-g((i,))-g((j,))
    triple=(g((0,1,2))-g((0,1))-g((0,2))-g((1,2))
            +g((0,))+g((1,))+g((2,)))
    assert g((0,1,2))==singles+pairs+triple

# Representative admissible mixed correlation matrix.
r,s=0.3,0.4
R=np.array([[1.0,0.0,-r],[0.0,1.0,-s],[-r,-s,1.0]])
assert np.linalg.eigvalsh(R).min()>0
Ri=np.linalg.inv(R)
assert np.all(Ri>=-1e-12)
assert np.all(np.diag(Ri)>=1-1e-12)

# Coefficient algebra for representative positive simplex weights.
w1,w2,w3=Fraction(1,5),Fraction(3,10),Fraction(1,2)
A_mixed=2*w1*w2
A_ind=2*(w1*w2+w1*w3+w2*w3)
assert A_mixed-A_ind == -2*(w1*w3+w2*w3)
print('VERIFY_OK')
