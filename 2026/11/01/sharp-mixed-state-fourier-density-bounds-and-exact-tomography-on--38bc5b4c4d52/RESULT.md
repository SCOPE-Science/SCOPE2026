# Sharp mixed-state Fourier-density bounds and exact tomography on finite parabolas

## Finding

For every odd prime power \(q\), a complete quadratic-parabola Fourier sampling system admits an exact Hilbert–Schmidt identity, sharp *spectral-profiled* bounds, and a three-level real singular spectrum. In particular, every orthonormal \(r\)-tuple on the finite parabola has a sharp, attainable fourth-moment range, not merely an upper bound:

\[
 r^2\le \frac1{q^2}\sum_{(x,t)\in\mathbb F_q^2}
 \left(\sum_{j=1}^{r}|\mathcal E f_j(x,t)|^2\right)^2
 \le r^2+r-\frac{r^2}{q},\qquad 1\le r\le q.
\]

The lower extremizers are precisely coordinate-supported subspaces, and the upper extremizers are precisely subspaces whose orthogonal projector has constant coordinate diagonal. The complete linear intensity-lifting map loses **only** the traceless diagonal Hermitian matrices; every off-diagonal entry and the trace are recovered with exact unit Hilbert–Schmidt gain.

## Assumptions and scope

Let \(F=\mathbb F_q\) be a field of odd characteristic, \(q\ge3\). Let \(\psi:F\to\mathbb C\) be any nontrivial additive character. Use counting \(\ell^2(F)\) and normalized counting averages on \(F^2\). Define the parabolic extension operator by

\[
 \mathcal E f(x,t)=\sum_{a\in F} f(a)\psi(xa+ta^2),\quad (x,t)\in F^2.
\]

For any Hermitian \(q\times q\) matrix \(A\), define the real-valued Fourier density

\[
 \rho_A(x,t)=\sum_{a,b\in F}A_{ab}\psi\bigl(x(a-b)+t(a^2-b^2)\bigr).
\]

If \(A\succeq0\) and \(A=\sum_j\lambda_j f_j f_j^*\), with orthonormal \(f_j\) and nonnegative \(\lambda_j\), then \(\rho_A=\sum_j\lambda_j|\mathcal E f_j|^2\). For arbitrary Hermitian matrices, \(\rho_A\) is real but need not be nonnegative. Write \(T=\operatorname{tr}A\), \(Q=\operatorname{tr}(A^2)=\|A\|_{\mathrm{HS}}^2\) and \(J_q(A)=q^{-2}\sum_{x,t}|\rho_A(x,t)|^2\).

We use the real Hilbert space of Hermitian matrices with inner product \(\operatorname{tr}(AB)\), and the real space of functions on \(F^2\) with inner product \(q^{-2}\sum\rho\tau\). All singular values below refer to these explicitly normalized spaces.

## Proof

**1. Difference-fiber injectivity.** For \(a\ne b\), set \(d=a-b\) and \(s=a^2-b^2=d(a+b)\). Since \(2d\) is invertible, given \((d,s)\) with \(d\ne0\), the ordered pair is uniquely reconstructed by

\[
 a=\frac12\left(d+\frac{s}{d}\right),\qquad
 b=\frac12\left(\frac{s}{d}-d\right).
\]

Every diagonal pair \((a,a)\) instead contributes to the single difference \((0,0)\). Thus among the Fourier coefficients of \(\rho_A\), the coefficient at \((0,0)\) equals \(T\), at \((d,s)\) with \(d\ne0\) equals the unique \(A_{ab}\) above, and at \((0,s)\) with \(s\ne0\) equals zero.

**2. Exact identity and equality deficits.** Orthogonality of characters of the additive group \(F^2\), with the specified normalized counting measure, gives

\[
\begin{aligned}
 J_q(A)&=T^2+\sum_{a\ne b}|A_{ab}|^2\\
 &=T^2+Q-\sum_{a\in F}A_{aa}^2.
\end{aligned}
\]

The second equality uses Hermitian symmetry. Since \(\sum_a A_{aa}=T\), Cauchy–Schwarz yields

\[
 \boxed{T^2\le J_q(A)\le T^2+Q-\frac{T^2}{q}}.
\]

These are quantitatively exact: 

\[
 J_q(A)-T^2=\sum_{a\ne b}|A_{ab}|^2,
\quad
 \left(T^2+Q-\frac{T^2}{q}\right)-J_q(A)
 =\sum_a\left(A_{aa}-\frac Tq\right)^2.
\]

Hence lower equality holds exactly when \(A\) is diagonal, and upper equality holds exactly when its diagonal is constant. Fix arbitrary real eigenvalues \(\lambda_1,\ldots,\lambda_q\). The diagonal matrix \(\operatorname{diag}(\lambda_1,\ldots,\lambda_q)\) attains the lower endpoint. Let \(U\) be any unitary complex Hadamard matrix, for example the normalized additive-character Fourier matrix of \(F\). Then \(U\operatorname{diag}(\lambda_j)U^*\) has diagonal \(T/q\) and attains the upper endpoint. Therefore both coefficients are **sharp at every prescribed spectrum**, including spectra of positive semidefinite matrices.

**3. Exact singular spectrum and reconstruction.** The Fourier reconstruction in step 1 proves that \(\mathcal D:A\mapsto\rho_A\) is injective on the off-diagonal Hermitian subspace, with norm preservation there; it sends \(cI\) to the constant \(cq\) and annihilates traceless diagonal matrices. These three real subspaces are pairwise orthogonal and exhaust Hermitian matrices. Consequently, the singular values of \(\mathcal D\) are

\[
 \sqrt q\quad(\text{multiplicity }1),\qquad
 1\quad(\text{multiplicity }q(q-1)),\qquad
 0\quad(\text{multiplicity }q-1).
\]

In particular, \(\operatorname{rank}_{\mathbb R}\mathcal D=q^2-q+1\), and exactly the trace and all off-diagonal Hermitian matrix entries can be reconstructed from the density. One explicit formula, for \(a\ne b\), is

\[
 A_{ab}=\frac1{q^2}\sum_{x,t\in F}\rho_A(x,t)
 \overline{\psi(x(a-b)+t(a^2-b^2))}.
\]

No such density system can determine individual diagonal entries beyond their sum: distinct matrices differing by a traceless diagonal matrix have identical data.

**4. Orthonormal tuple and all equality spaces.** Let \(f_1,\ldots,f_r\) be orthonormal in \(\ell^2(F)\) and let \(P\) be their orthogonal projector. Then \(\rho_P=\sum_j|\mathcal E f_j|^2\), \(T=Q=r\), so the displayed sharp range follows. Lower equality is \(P\) diagonal, hence \(P\) projects onto a span of \(r\) coordinate vectors. Upper equality is \(P_{aa}=r/q\) for all \(a\), the equal-leverage condition. Both are attained for every \(1\le r\le q\): for the first choose any coordinate subspace; for the second take the span of any \(r\) columns of an additive-character Fourier matrix. No assertion of an equality classification beyond the specified criterion is needed.

## Verification

The standalone `CHECK.py` uses only the Python 3 standard library. Run `python3 CHECK.py` from the extracted package. On its final package replay it returned `CHECK_OK assertions=1915`. It verifies ordered-difference uniqueness for primes \(3,5,7,11,13,17,19\), random positive semidefinite Hermitian matrices for primes through \(11\), all rank-projection endpoints for those primes, and the full real lifting Gram spectra at primes \(3\) and \(5\). Numerical finite-prime checks do not prove the assertions for all odd prime powers; those follow from steps 1–4 above.

## Relationship to prior work

Cuenin, Denson and Hickman, *Space curve Fourier restriction for orthonormal functions* (first posted 2026-10-01; arXiv:2610.02596), address orthonormal Fourier restriction for **smooth real nondegenerate curves in dimension at least three**, using nonendpoint inequalities and spectral methods. Their Theorem 1.1 does not treat finite-field parabola densities or a complete finite-dimensional singular spectrum. The current problem is a finite-field orthonormal analogue, not a corollary of their real-variable theorem.

González-Riquelme and Oliveira e Silva, *Sharp extension inequalities on finite fields* (arXiv:2405.16647), treat sharp **scalar** extension norms. Their planar parabola endpoint is \(L^2\to L^6\), while their \(L^2\to L^4\) results concern other higher-dimensional varieties. Neither result gives spectral-profiled fourth moments of sums of squared extensions or the Hermitian density map. The scalar \(r=1\) instance of the present fourth-moment bound is also a classical relative-Sidon/planar-set computation and is **not claimed as new**. The assessed contribution is the simultaneous all-spectrum and all-rank formulation, sharp equality classification, exact matrix-lifting spectrum, and reconstruction kernel.

## Limitations

The field must have odd characteristic; the proof uses division by two. It concerns the full \(q^2\) quadratic-phase observation grid and the normalized squared-density fourth moment, not higher moments, continuous curves, noisy measurements, or generic finite surfaces. The density map is not informationally complete for arbitrary Hermitian matrices because the entire traceless diagonal subspace is invisible. Although exact spectra and equal-leverage equality cases are proved, no uniform noise-optimal statistical estimator or generalization to composite rings is claimed. Earlier unindexed results on relative difference sets or lifted Fourier measurements could contain equivalent forms; priority must be independently verified.

## References

1. J.-C. Cuenin, J. Denson, J. Hickman, *Space curve Fourier restriction for orthonormal functions*, arXiv:2610.02596, first posted 2026-10-01. https://arxiv.org/abs/2610.02596
2. C. González-Riquelme, D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first posted 2024-05-26. https://arxiv.org/abs/2405.16647
3. G. Pisier, *On uniformly bounded orthonormal Sidon systems*, arXiv:1602.02430 (context for Sidon terminology; does not supply the present matrix identity). https://arxiv.org/abs/1602.02430
