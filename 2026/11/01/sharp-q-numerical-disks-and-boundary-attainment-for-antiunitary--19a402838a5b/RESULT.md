# Sharp \(q\)-numerical disks and boundary attainment for antiunitary operators

## Finding

Let \(H\) be a complex Hilbert space of dimension at least three and let \(A:H\to H\) be a conjugate-linear, surjective isometry (an antiunitary). The inner product is linear in its first argument. For any \(q\in\mathbb C\), \(|q|\le1\), define
\[
W_q(A)=\{\langle Ax,y\rangle:\|x\|=\|y\|=1,\ \langle x,y\rangle=q\}.
\]
Set \(s=w(A)=\sup_{\|x\|=1}|\langle Ax,x\rangle|\), \(r=|q|\), \(t=\sqrt{1-r^2}\), and \(a=\sqrt{1-s^2}\). Then \(W_q(A)\) is a centered disk, with **exact outer radius**
\[
R(r,s)=\begin{cases}1,&0\le r\le s,\\ rs+t\sqrt{1-s^2},&s<r\le1.\end{cases}
\]
**Boundary-attainment classification:** the disk is closed exactly when \(r<s\) or \(w(A)\) is attained by a unit vector. If \(r\ge s\) and \(w(A)\) is not attained, the disk is open. A disk of zero radius is understood as \(\{0\}\); in that case the ordinary numerical radius is necessarily attained. In particular, the normalized range contains a unit-modulus value precisely on the norm plateau \(r\le s\), subject at \(r=s\) to the boundary-attainment qualification.

## Assumptions and scope

The Hilbert space can be finite-dimensional or infinite-dimensional, and no separability hypothesis is imposed. The operator must be conjugate-linear and isometric; the result is not asserted for general antilinear contractions or general real-linear maps. The parameter \(q\) may be complex. The orthogonality convention is \(\langle x,y\rangle=q\), and the numerical range is formed using the same unit vectors in the domain and codomain. This is an exact, unscaled set equality, not merely an estimate of the numerical radius.

## Proof

**1. Numerical-overlap interval.** Put \(f(x)=|\langle Ax,x\rangle|\) on the unit sphere. Since \(A\) is an isometry, \(0\le f(x)\le1\). There exists a unit vector with \(f(x)=0\): on any complex two-dimensional subspace, the scalar \(\langle A(x_1+\lambda x_2),x_1+\lambda x_2\rangle\), multiplied by a harmless normalizing denominator, is a polynomial of degree at most two in \(\bar\lambda\). Taking \(x_2\) with nonzero diagonal form when the form is not identically zero gives a nonconstant polynomial with a complex root. If the quadratic form is identically zero there is nothing to prove. The unit sphere is path-connected; therefore every real number \(0\le u<s\) is realized as \(f(x)=u\). The endpoint \(s\) is realized if and only if \(w(A)\) is attained.

**2. Exact constrained pairs.** For \(r<1\), each pair of unit vectors satisfying \(\langle x,y\rangle=q\) has a unique representation
\[
y=\bar q x+t z,\qquad z\perp x,\quad \|z\|=1.
\]
For a fixed unit \(x\), let \(f=f(x)\). Because \(\|Ax\|=1\), the orthogonal component of \(Ax\) relative to \(x\) has norm \(\sqrt{1-f^2}\). As \(\dim(x^\perp)\ge2\), the complex numbers \(\langle Ax,z\rangle\) obtained by varying unit \(z\in x^\perp\) fill the *entire* closed disk of radius \(\sqrt{1-f^2}\). Thus the fiber of \(W_q(A)\) over \(x\) is a disk centered at \(q\langle Ax,x\rangle\) of radius \(t\sqrt{1-f^2}\), and its largest modulus is exactly
\[
F_r(f)=rf+\sqrt{1-r^2}\sqrt{1-f^2}.
\]
When \(r=1\), admissible \(y\) is a unit scalar multiple of \(x\), and the same formula with \(t=0\) holds. Rotating \(x\) by a scalar of modulus one rotates \(\langle Ax,x\rangle\) and all associated values by a unit-modulus phase, so the whole range is circularly symmetric.

**3. Sharp scalar optimization.** On \([0,1]\), \(F_r(f)\) increases up to \(f=r\) and decreases thereafter (also follows by Cauchy–Schwarz applied to \((r,t)\) and \((f,\sqrt{1-f^2})\)). Over the available overlap interval \([0,s]\), its supremum equals \(1\) for \(r\le s\) and equals \(rs+t\sqrt{1-s^2}\) for \(r>s\). If \(r<s\), the maximizing overlap \(f=r\) is attained by Step 1. If \(r\ge s\), the maximum is attained precisely when a unit vector realizes \(f=s\). The relevant disk-fiber extremal direction can always be selected, so these conditions are sufficient as well as necessary.

**4. Filling the disk and its boundary.** The admissible pair space is path-connected: for \(r<1\) it is a parametrized complex two-frame Stiefel space, with any two orthonormal pairs joined by a norm-continuous unitary path; for \(r=1\), it is a copy of the connected unit sphere. It is nonempty. It contains a pair with \(\langle Ax,y\rangle=0\): choose \(x\) with \(\langle Ax,x\rangle=0\) and then a unit vector \(z\perp x,Ax\), possible because \(\dim H\ge3\). Consequently the image \(W_q(A)\) is connected, circularly symmetric, contains zero, and has the supremal radius computed in Step 3. It is therefore exactly the open or closed centered disk according to the attainment criterion. When the supremum is zero the range is \(\{0\}\).

**5. Genuine infinite-dimensional boundary transition.** Fix \(0<s_\infty\le1\) and numbers \(0<s_n<s_\infty\) increasing to \(s_\infty\). On \(\bigoplus_{n\ge1}\mathbb C^2\), let \(A\) be the orthogonal direct sum of the antiunitaries
\[
A_n(z_1,z_2)=\left(s_n\bar z_1-\sqrt{1-s_n^2}\,\bar z_2,\ \sqrt{1-s_n^2}\,\bar z_1+s_n\bar z_2\right).
\]
Each block has numerical radius \(s_n\), since its skew-symmetric part vanishes in \(\langle A_nx,x\rangle\). For any unit vector spread among blocks, \(|\langle Ax,x\rangle|\le\sum_n s_n\|x_n\|^2<s_\infty\); nevertheless the supremum is \(s_\infty\). Thus the range at \(r<s_\infty\) is a closed unit disk, while at \(r\ge s_\infty\) its outer boundary is excluded. This proves that the open/closed alternative cannot be dropped in infinite dimension.

## Verification

The proof above is analytical and applies to every admissible antiunitary. The supplementary standard-library Python script `verify.py` checks the piecewise scalar extremization against 220 deterministic sampled parameter pairs and verifies five explicit two-dimensional antiunitary building blocks; it performs 450 finite assertions. Those finite tests are not used to establish the universal theorem.

## Relationship to prior work

Majumdar and Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces* (arXiv:2610.16823v1, 2026-10-12), prove in their Section 6 that for complex dimension at least three the constrained \(q\)-numerical range of every bounded antilinear operator is a centered disk. Their disk-shape theorem does not compute the present exact antiunitary radius, characterize its norm plateau, or separate open from closed boundaries by norm attainment. Kołaczek and Müller (2024) establish that the ordinary numerical range of an antilinear operator on a Hilbert space of dimension at least two is a centered disk, but do not give the higher-dimensional constrained \(q\)-profile or the boundary transition described here. The known two-dimensional antiunitary annulus calculation is a different dimensional case; in dimensions at least three the formerly missing interior is filled, and infinite-dimensional boundary nonattainment arises.

## Limitations

The classification applies to surjective conjugate-linear isometries and cannot be transferred to general bounded antilinear operators merely by substituting their norms. At \(r=s\) the outer radius is one but it is not necessarily attained; in an infinite-dimensional example its full boundary may be missing. The result does not determine the numerical radius \(s\) of a particular antiunitary from its spectral data, and it does not classify operator unitary equivalence. Related earlier work may contain an equivalent radius optimization under different terminology; independent mathematical validation has not been performed.

## References

1. A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, arXiv:2610.16823v1, first public 2026-10-12, especially Section 6 and Theorem 6.6.
2. D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory 96 (2024), article 17, DOI:10.1007/s00020-024-02768-5, first public online 2024-05-21.
