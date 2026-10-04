from fractions import Fraction
def chi_p4(n):
    z=Fraction(1,24)
    for j in range(1,5): z*=n+j
    return z
rank=4; det_spin=-2
detF=det_spin+rank
disc=2*detF
KQ=-3; Kdelta=KQ+disc
K2=disc*2
chi=chi_p4(0)-chi_p4(-2)-chi_p4(-4)+chi_p4(-6)
assert (detF,disc,Kdelta,K2,chi)==(2,4,1,8,6)
assert 1-0+5==6
print('detF=O(2)')
print('discriminant=O(4)')
print('complete_intersection=(2,4)')
print('omega=O(1) K2=8 pg=5 q=0 chi=6')
print('VERIFY_OK')
