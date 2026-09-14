# Second variational Galois obstruction for the sextic Hamiltonian H6

## Context
Target (TARGET route): decide Morales-Ramis-Simo non-integrability for
H6(x,y,px,py)=(px^2+py^2)/2+x^6/6+y^6/6+a x^3 y^3, a in C, a^2 not in {0,1},
along the straight-line solution Gamma: y=0, py=0, x=x0(t), x0''+x0^5=0,
on a generic energy level h=x0'^2/2+x0^6/6 with h!=0.

## Definitions
K=C(x0,x0'): function field of Gamma. VE1/VE2: first/second variational
equations. NVE1/NVE2: normal subsystems. G2: Picard-Vessiot Galois group of
the second variational system; G2^0 its identity component. MRS: the
Morales-Ramis-Simo theorem that meromorphic Liouville integrability implies
G_k^0 abelian for every k. C_h: w^2=2h-x^6/3, smooth hyperelliptic curve of
genus 2 for h!=0. omega0=dx/w, omega3=x^3 dx/w.

## Result
(A) Correction: G2^0 along Gamma is always solvable (unipotent-by-abelian
triangular extension), for every a including a=0. The literal target phrase
"non-solvable identity component" is therefore false as stated; this
impossibility is proved.
(B) Sharp obstruction: for every a!=0, hence every admissible a with a^2 not
in {0,1}, G2^0 is non-abelian, a Heisenberg unipotent extension with nonzero
central commutator proportional to -3a times a nonzero period determinant of
(omega0,omega3) on C_h. By MRS, V_a admits no additional meromorphic first
integral independent of H6 near Gamma. In particular no admissible a admits a
second rational/Darboux-type integral.

## Proof / evidence
VE coefficients by expansion X=x0+e x1+e^2 x2, Y=e y1+e^2 y2:
VE1: x1''+5x0^4 x1=0, y1''=0; VE2: x2''+5x0^4 x2+10x0^3 x1^2=0,
y2''+3a x0^3 y1^2=0. Verified in sympy (verify_ve.py section 1, re-executed).
Tangent operator L=D^2+5x0^4=(D+b)(D-b) with b=x0''/x0' in K, since
b'+b^2=w''/w=-5x0^4, w=x0'. Hence VE1 reducible over K, triangular solvable;
normal block at most Ga. VE2 adjoins only integrals/exponentials of integrals,
so G2^0 is an extension of a solvable group by a vector group, hence solvable.
This proves (A).
For (B), fix NVE1 basis {1,t}. Put phi=x0^3, F'=phi, J'=F. On basis (1,t,F,J),
loop monodromy is N(T,U,C)=[[1,0,0,0],[T,1,0,0],[U,0,1,0],[C,U,0,1]] with
T,U the periods of omega0,omega3 and C the iterated integral. Commutator:
N1 N2-N2 N1 has sole nonzero entry (4,1)=U1 T2-U2 T1=-det(period matrix),
verified entry-by-entry. Thus non-abelian iff the 2x2 period matrix has rank 2.
Lemma: no nonzero combination r0 omega0+r3 omega3 is exact on C_h. Writing a
rational primitive B=u+v w gives 2P v'+P' v=2R with P=2h-x^6/3,
R=r0+r3 x^3. For polynomial v of degree d, LHS leading term
-2b(d/3+1)x^{d+5} nonzero, degree >=5, never a degree<=3 polynomial; generic
finite pole of order m gives pole order m+1 with coefficient -2m p0 c!=0;
branch-point pole gives coefficient 2p1 c(1/2-m)!=0 for m>=1. Hence no rational
v exists; coefficients machine-checked. Residues of omega0,omega3 at infinity
vanish, so vanishing of all periods would imply exactness, contradiction;
thus the period map H1(C_h)->C^2 has rank 2. The involution x->-x with
eigenvalues -1 on omega0 and +1 on omega3 independently forces
non-proportionality. Numerically at h=1/2 on independent root-pair loops,
det=-4.991-2.882i, |det|~5.76 nonzero (periods.py, re-executed), confirming the
rank on explicit loops. Hence for a!=0 the commutator -3a det is nonzero,
G2^0 contains a Heisenberg subgroup, non-abelian. MRS gives meromorphic
non-integrability. First-order Morales-Ramis does not suffice: the Darboux
data here is (k=6,lambda=0), allowed by the Kimura table (case 1, p=0), so the
obstruction genuinely requires order two.

## Limitations
MRS used as published black box. Generic means h!=0 with smooth C_h and
x0' not identically zero. Excluded parameters a^2 in {0,1} as in target:
a=0 trivializes NVE2 to abelian; a=+-1 outside this analysis (no claim made
about those resonant values). Numeric periods are corroboration only; the
exactness/period-rank proof is symbolic. DRAFT's "genus 4" is corrected to
genus 2 here; omega3 is meromorphic with poles at infinity, not holomorphic,
which does not affect the rank argument given vanishing residues.

## Reproducibility
Run output/artifacts/verify_ve.py (sympy VE/factorization/commutator/pole
coefficients) and output/artifacts/periods.py (mpmath 60-digit period matrix
at h=1/2). Both were re-executed at audit.

## References
J. Morales-Ruiz, J.-P. Ramis, C. Simo, Integrability of Hamiltonian systems
and differential Galois groups of higher variational equations, Ann. Sci.
Ec. Norm. Sup. 40 (2007) 845-884.
J. Morales-Ruiz, J.-P. Ramis, A note on non-integrability of Hamiltonians
with homogeneous potential, Methods Appl. Anal. 8 (2001) 113-120.
P. Acosta-Humanez et al., Nonintegrability of the AGK quartic Hamiltonian,
SIAM J. Appl. Dyn. Syst. (2018), arXiv:1710.00227.
