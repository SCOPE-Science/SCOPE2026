# A fourth-vector premature breakdown in inverse-leading extended Krylov construction

## Finding
Let \(A\) be real symmetric and nonsingular. An inverse-leading *mixed-channel* extended Krylov construction can generate its second and third orthonormal basis vectors successfully but fail to generate the fourth, although the *split-channel* construction extends to the fourth vector, for some starting vector **if and only if** \(A\) has eigenvalues of both signs and at least four distinct eigenvalues. Thus dimension four is minimal. The obstruction occurs with a fixed matrix of spectral condition number three.

Precisely, start from a real unit vector \(v\), define
\[
a=v^{\mathsf T}A^{-1}v,\qquad \tau=\|A^{-1}v-av\|_2,
\qquad u=(A^{-1}v-av)/\tau,
\]
assume \(\tau>0\), and set \(m=v^{\mathsf T}Av\), \(c=u^{\mathsf T}Av=(1-am)/\tau\). Let \(P_2\) be orthogonal projection onto \(\operatorname{span}\{v,u\}\), assume \(r=\|(I-P_2)Av\|_2>0\), and put \(w=(I-P_2)Av/r\). When \(a\ne0\), the mixed third vector equals \(w\) up to phase. If \(P_3\) projects onto \(\operatorname{span}\{v,u,w\}\), the split-channel fourth candidate is \(A^{-1}u\), the mixed-channel fourth candidate is \(A^{-1}w\), and
\[
\boxed{(I-P_3)A^{-1}w=-\frac{c}{r}(I-P_3)A^{-1}u.}
\]
Whenever the split residual is nonzero, the mixed fourth residual vanishes exactly when \(am=1\), even though the third mixed residual was nonzero. This is an algorithmic candidate breakdown, not termination of the underlying extended Krylov space.

An exact dimension-four witness is
\[
A=\operatorname{diag}(-1,1,2,3),\qquad
v=\frac1{\sqrt{77}}(\sqrt3,\sqrt{56},3,3)^{\mathsf T}.
\]
It has
\[
a=\frac{11}{14},\quad m=\frac{14}{11},\quad
\tau^2=\frac{103}{539},\quad r^2=\frac{564}{847},\quad
\|(I-P_3)A^{-1}u\|_2^2=\frac{14112}{498623}>0,
\]
while \((I-P_3)A^{-1}w=0\) and \(\kappa_2(A)=3\). By continuity, arbitrarily nearby starts have nonzero but arbitrarily small mixed fourth residual and a split residual bounded away from zero, with successful earlier steps and with the same \(A\).

## Assumptions and scope
The basis is constructed in exact real arithmetic by orthogonalizing the inverse-leading candidates: first \(A^{-1}v\); then the third mixed candidate \(Au\) and third split candidate \(Av\); then the fourth mixed candidate \(A^{-1}w\) and fourth split candidate \(A^{-1}u\). Since \(a\ne0\), the third mixed residual is a nonzero multiple of the third split residual and both methods span the same three-dimensional subspace. The existence characterization is for starting vectors producing a nonzero third residual and nonzero fourth split residual. It is not a statement about all starting vectors or finite-precision floating-point errors.

## Proof
**Candidate identity.** Orthogonal decomposition gives \(Av=mv+cu+rw\). Applying \(A^{-1}\) gives
\[
A^{-1}w=(v-mA^{-1}v-cA^{-1}u)/r.
\]
Because \(A^{-1}v=av+\tau u\), projection orthogonal to \(\operatorname{span}\{v,u,w\}\) kills the first two terms, yielding the displayed identity. The third mixed residual is \((I-P_2)Au=-a(I-P_2)Av/\tau\), so it is nonzero exactly when \(a\ne0\), given \(r>0\). Since \(r,\tau>0\), the fourth mixed residual vanishes with a nonzero fourth split residual precisely when \(c=0\), equivalently \(am=1\). This condition automatically implies \(a\ne0\).

**Active spectral support and dimension.** For a symmetric matrix, a starting vector with nonzero projections on \(s\) distinct eigenvalues has linearly independent vectors \(A^{-2}v,A^{-1}v,v,Av\) if and only if \(s\ge4\): multiplying any linear dependence by \(A^2\) gives a polynomial of degree at most three with every active eigenvalue as a root, and the constant coefficient cannot vanish in a nontrivial dependence of these four Laurent monomials. Thus the fourth split residual is nonzero exactly for at least four distinct active eigenvalues. Similarly the third residual is nonzero for at least three distinct active eigenvalues.

**Necessity of indefiniteness.** If \(A\) is positive or negative definite, Cauchy–Schwarz applied to its eigenvalue weights gives
\[
(v^{\mathsf T}Av)(v^{\mathsf T}A^{-1}v)\ge1,
\]
with equality only if \(v\) belongs to one eigenspace; such a start fails at the second basis vector. Hence successful third and fourth split steps together with \(am=1\) require indefiniteness and at least four distinct eigenvalues.

**Sufficiency for every indefinite spectrum with four or more distinct eigenvalues.** Choose four distinct eigenvalues containing both signs and a unit starting vector supported on their eigenspaces with strictly positive squared spectral weights. At a two-point distribution on two distinct *same-sign* eigenvalues, strict Cauchy–Schwarz gives \(am>1\). At a two-point distribution with a sufficiently small admixture of an *opposite-sign* eigenvalue into a pure eigenvector, \(am<1\): its derivative from the pure state is \(\lambda_j/\lambda_i+\lambda_i/\lambda_j-2<0\). Two eigenvalues of the same sign exist among any four with both signs. Add arbitrarily small positive weight on any missing selected eigenvalues to both trial distributions; by continuity their strict inequalities persist. Their line segment consists of strictly positive four-point weights. The intermediate value theorem supplies one with \(am=1\). Its four-point support guarantees nonzero second, third, and fourth split residuals, while \(am=1\) makes the mixed fourth residual zero. Necessity and sufficiency follow, and three-dimensional matrices cannot qualify.

**Exact well-conditioned witness.** For the displayed diagonal matrix and vector, direct weighted moments give \(a=11/14\) and \(m=14/11\). Gram–Schmidt orthogonalization gives the stated strictly positive rational squares for the first inverse residual, third split residual, and fourth split residual. The candidate identity forces the mixed fourth residual to be zero. Every residual is a continuous function of the initial vector in a neighborhood where the first three bases exist and the split fourth residual remains positive. Small perturbations away from \(am=1\) therefore give arbitrarily severe local fourth-step mixed-to-split residual separation at fixed spectral condition number three.

## Verification
Run `python check.py` with Python 3, SymPy, and NumPy. It reconstructs every exact rational coefficient and zero/nonzero residual for the four-by-four witness and checks direct projections for nearby starts. These computations support the explicit witness; the fully quantified classification rests on the preceding spectral-support and continuity arguments, not on finite tests.

## Relationship to prior work
Lund and Schweitzer (2026), especially their Algorithms 1–2, Theorem 2.1, Theorem 3.3 and Appendix A, define the mixed and split inverse-leading constructions, compare local normalization robustness for definite matrices, and demonstrate mixed behavior for indefinite matrices. Their recurrence algebra provides the starting point for the fourth-step identity; the contribution here is the **complete spectral existence characterization of an exact fourth-step non-intrinsic breakdown after a successful third step**, with minimal dimension and a condition-three exact witness. Existing earlier third-step cancellation examples do not imply this later-step obstruction. Older work on extended Krylov recurrences by Jagels–Reichel and Mertens–Vandebril is relevant; complete texts of those older sources were not available for comparison and remain a bibliographic uncertainty.

## Limitations
This statement concerns local exact-arithmetic orthogonal residuals, not total loss of orthogonality or approximation error in a particular floating-point implementation. It does not classify fifth and later candidates, nonsymmetric matrices, or arbitrary choices of orthogonalization order. The local cancellation may be avoided by switching to a split-channel candidate. The precise novelty relative to unavailable older recurrence manuscripts merits further external review.

## References
1. K. Lund and M. Schweitzer, *On the stability of basis construction in extended Krylov subspace methods*, arXiv:2610.21603v1, first public October 15, 2026, https://arxiv.org/abs/2610.21603.
2. C. Jagels and L. Reichel, *Recursion relations for the extended Krylov subspace method*, Linear Algebra and its Applications 434 (2011), 1716–1732, https://doi.org/10.1016/j.laa.2010.08.042.
3. C. Mertens and R. Vandebril, *Short recurrences for computing extended Krylov bases for Hermitian and unitary matrices*, Numerische Mathematik 131 (2015), 303–328, https://doi.org/10.1007/s00211-014-0692-3.
