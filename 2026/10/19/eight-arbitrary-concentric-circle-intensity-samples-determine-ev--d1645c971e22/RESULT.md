# Eight arbitrary concentric-circle intensity samples determine every complex quadratic

## Finding
Let \(P(z)=a+bz+cz^2\) be a complex polynomial of degree at most two. Choose **any** five distinct points on \(|z|=1\), and **any** three distinct points on \(|z|=R\), where \(R>0\) and \(R\neq1\). The eight intensity values \(|P(z)|^2\) determine the full coefficient triple \((a,b,c)\) up to a common unimodular scalar, including when some coefficients vanish. No seven complex-linear intensity measurements on \(\mathbb C^3\) can recover every vector up to phase, so eight is globally minimal.

In fact, the real-linear measurement lift from the nine-dimensional space of Hermitian \(3\times3\) matrices has rank eight and **exactly** the kernel
\[
 \ker_{\mathbb R}\mathcal L=\mathbb R D_R,
 \qquad D_R=\operatorname{diag}(R^2,-(1+R^2),1).
\]
The kernel is independent of both angular configurations. Within this five-plus-three sampling family, the radii must be distinct and all sampling points on each circle must be distinct for universal recovery.

There is also an exact sharp rank-two transversality estimate. For all Hermitian \(H\) of rank at most two, with \(\Pi_{D_R^\perp}\) the orthogonal Frobenius projection away from the kernel,
\[
 \|\Pi_{D_R^\perp}H\|_F^2\ \ge\
 \frac{\min\{1,R^4\}}{2(R^4+R^2+1)}\,\|H\|_F^2.
\]
The constant is attained by an indefinite rank-two Hermitian matrix; it is an exact **kernel-angle** bound, not an angularly uniform numerical lower frame bound for the eight output measurements.

## Assumptions and scope
The measurement sites are arbitrary, not required to be equally spaced or rational. The polynomial coefficients are arbitrary complex numbers. The two circles are concentric, centered at the origin, of positive unequal radii. By the invertible coefficient change induced by scaling the variable, the first radius can be set to one without loss of generality. The assertion is about recovery up to global phase, not recovery of arbitrary Hermitian matrices.

For \(H=(H_{jk})_{0\le j,k\le2}=H^*\), define
\[
 \mathcal L(H)(z)=\sum_{j,k=0}^2 H_{jk}z^j\overline z^{\,k}.
\]
For a coefficient vector \(x\), the measured intensity is \(\mathcal L(xx^*)(z)=|\sum_{j=0}^2x_jz^j|^2\). The Frobenius inner product is \(\langle H,K\rangle_F=\operatorname{tr}(HK)\) on Hermitian matrices. A projection \(\Pi_{D_R^\perp}\) is orthogonal with respect to this real inner product.

## Proof
**Step 1: five samples force every first-circle Fourier coefficient to vanish.** Suppose \(H\) lies in the intensity-lift kernel. On the unit circle \(z=e^{i\theta}\), \(\mathcal L(H)(z)\) is a real trigonometric polynomial with frequencies between \(-2\) and \(2\). Multiplication by \(z^2\) produces an ordinary polynomial of degree at most four. Five distinct zeros on the unit circle therefore imply \(\mathcal L(H)\equiv0\) on that circle. Comparison of Fourier coefficients gives
\[
 H_{02}=0,\qquad H_{01}+H_{12}=0,\qquad H_{00}+H_{11}+H_{22}=0.
\]
The Hermitian conjugate relations hold automatically.

**Step 2: three second-circle samples eliminate the first harmonic.** Substituting the preceding identities into \(\mathcal L(H)(R e^{i\theta})\) yields
\[
 H_{00}+R^2H_{11}+R^4H_{22}
 +2\operatorname{Re}\!\left(R(1-R^2)H_{01}e^{-i\theta}\right).
\]
This is a real trigonometric polynomial of degree at most one. Such a polynomial, multiplied by \(e^{i\theta}\), has degree at most two, so vanishing at three distinct second-circle angles forces all three Fourier coefficients to be zero. Since \(R>0\) and \(R\neq1\), this gives \(H_{01}=H_{12}=0\) and
\[
 H_{00}+R^2H_{11}+R^4H_{22}=0.
\]
Solving the two diagonal equations yields precisely \(H=tD_R\) for a real scalar \(t\). Conversely, this matrix vanishes identically under \(\mathcal L\) on both circles, so the kernel and rank are exactly as asserted.

**Step 3: phase uniqueness.** All three eigenvalues of \(D_R\) are nonzero. If two coefficient vectors \(x,y\in\mathbb C^3\) give the same eight intensities, the Hermitian difference \(xx^*-yy^*\) has rank at most two and belongs to \(\mathbb RD_R\). The only possible difference is zero. Thus \(xx^*=yy^*\), which implies \(y=e^{i\phi}x\) for nonzero vectors and \(x=y=0\) otherwise.

**Step 4: the global eight-measurement lower bound.** Let \(m\le7\) be any number of complex-linear intensity measurements in dimension three. Their real-linear lift has a kernel of dimension at least \(9-m\ge2\). If their measurement vectors fail to span \(\mathbb C^3\), a nonzero vector orthogonal to all of them is already indistinguishable from zero. Otherwise, no nonzero positive-semidefinite or negative-semidefinite Hermitian matrix is in the kernel: its measured quadratic forms are nonnegative and vanish only if every measurement vector lies in its nullspace. Choose any real two-dimensional plane in the lift kernel. The determinant of a Hermitian matrix is a real, continuous, odd cubic; restricted to the unit circle in that plane it vanishes somewhere by the intermediate value theorem. The resulting nonzero singular Hermitian matrix cannot be semidefinite, so it has signature \((1,1,0)\) and is exactly a difference \(xx^*-yy^*\) of unequal rank-one positive-semidefinite matrices. Hence those two non-phase-equivalent vectors have identical measurements. No \(m\le7\) system is universal.

**Step 5: exact kernel-angle constant.** The eigenvalues of \(D_R\) are \(R^2,-(1+R^2),1\), so its smallest absolute eigenvalue is \(\delta_R=\min\{R^2,1\}\), and \(\|D_R\|_F^2=2(R^4+R^2+1)\). The singular-value trace inequality (or the best rank-two Frobenius approximation theorem) gives for every Hermitian \(H\) of rank at most two
\[
 |\langle H,D_R\rangle_F|^2
 \le\left(\|D_R\|_F^2-\delta_R^2\right)\|H\|_F^2.
\]
Subtracting the squared projection onto the span of \(D_R\) proves the bound. Equality holds for the rank-two diagonal matrix obtained from \(D_R\) by deleting its least-absolute-value eigencomponent. Its two remaining eigenvalues have opposite signs, so equality also occurs among differences of rank-one positive-semidefinite matrices.

**Step 6: necessity within the family.** When \(R=1\), every sample lies on one circle, and the lifted intensity space has real dimension at most five; universal retrieval is impossible. Repetition within either specified group of five or three sites produces at most seven distinct measurements, which are insufficient by Step 4. Distinct positive radii other than one reduce to the proved case by scaling.

## Verification
A standalone exact symbolic checker (`verify.py`) uses rational-coordinate circle nodes at radii \(R=1/2,2,3\), constructs each real \(8\times9\) intensity lift, and verifies rank eight, the exact generator \(D_R\), and the corresponding sharp kernel-angle constants \(1/42,1/42,1/182\). It also checks repeated-node and equal-radius rank defects. Its included execution output is `verification-output.txt`. The arbitrary-site theorem and seven-measurement lower bound are established algebraically above, not inferred from finite witnesses.

## Relationship to prior work
Chalendar and Partington's 2024 paper establishes phase uniqueness for analytic functions from modulus values on entire distinct circles or suitable infinite subsets (Theorems 2.6 and 2.8), and gives related finite-sampling conditions for special inner-function factors (Theorem 2.11). Those results do not state the eight-point, arbitrary-angular-placement, degree-two kernel classification above. Bodmann and Hammen previously established the optimal generic count \(4d-4\) using a specially designed **intersecting-circle** sampling geometry; for \(d=3\) this is also eight samples. The new result is not the already-known number eight but the all-angular-choices concentric-circle geometry and its exact one-dimensional Hermitian obstruction. Jaming and Rathmair's polynomial method couples function and derivative intensities, whereas the present construction uses ordinary evaluations only.

## Limitations
The exact output-space singular values and the best noise-amplification coefficient depend on the angular positions; this theorem does not provide an angular-uniform measurement conditioning bound. It does not treat degrees greater than two, nonconcentric circles, or recovery from fewer than eight arbitrary complex-linear magnitudes. Only same-author mathematical checks are included; independent validation is not asserted.

## References
1. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (first publicly posted 2024-03-24); see Theorems 2.6, 2.8 and 2.11 and Remark 2.10. https://arxiv.org/abs/2403.16255
2. B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487 (2013); see Theorem 2.3. https://arxiv.org/abs/1302.5487
3. P. Jaming and M. Rathmair, *Uniqueness of phase retrieval from three measurements*, arXiv:2205.08753 (2022); see Proposition 3.2. https://arxiv.org/abs/2205.08753
