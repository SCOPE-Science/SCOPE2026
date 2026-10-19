# Exact two-by-two Gaussian partial-pivoting growth law and its quadratic endpoint tail

## Finding
Let \(A\in\mathbb R^{2\times2}\) have four independent standard normal entries. Apply Gaussian elimination with partial pivoting (GEPP) in exact arithmetic: in the first column swap the two rows if necessary to use the larger absolute entry as pivot, then eliminate the remaining first-column entry. With \(A^{(0)}=A\), \(A^{(1)}\) the resulting updated matrix and \(M=\max_{i,j}|A_{ij}|\), define the **element growth factor**
\[
\rho=\frac{\max_{k\in\{0,1\},i,j}|A^{(k)}_{ij}|}{M}.
\]
The denominator is positive almost surely. Then \(1\le\rho<2\) almost surely. For every \(1\le r<2\), define
\[
\alpha_0(r)=\arctan(r-1),\qquad c(r,\alpha)=r\cos^2\alpha,
\]
\[
\phi_-(r,\alpha)=\arctan(r-\tan\alpha),\qquad
\phi_+(r,\alpha)=
\begin{cases}
\pi/2,&r=1,\\
\arctan\!\left(\frac{\tan\alpha}{r-1}\right),&1<r<2.
\end{cases}
\]
For \(c>0\) and \(0<z<\pi\), put
\[
F_c(z)=z-\frac{c}{\sqrt{1+c^2}}\operatorname{atan2}
\bigl(\sqrt{1+c^2}\sin z,\,c\cos z\bigr),
\]
where \(\operatorname{atan2}\) is chosen in \((0,\pi)\) for positive first argument and represents the continuous polar angle. The **exact complete survival law** is
\[
\boxed{\mathbb P(\rho>r)=\frac4{\pi^2}
\int_{\alpha_0(r)}^{\pi/4}
\left[F_{c(r,\alpha)}\bigl(\alpha+\phi_+(r,\alpha)\bigr)
-F_{c(r,\alpha)}\bigl(\alpha+\phi_-(r,\alpha)\bigr)\right]d\alpha.}
\]
For \(r<1\) this probability is \(1\), and for \(r\ge2\) it is \(0\). The jump at \(1\) is an atom with mass
\[
\mathbb P(\rho=1)=1-\mathbb P(\rho>1)
\approx0.7968648955923234,
\]
where the decimal is a numerical evaluation, not a separately certified decimal enclosure. There are no atoms in \((1,2]\). The high-growth endpoint has a **sharp exact leading constant**:
\[
\boxed{\mathbb P(\rho>2-\delta)=\frac{\delta^2}{2\pi^2}+O(\delta^3)
\qquad(\delta\downarrow0).}
\]

## Assumptions and scope
The input consists of four independent, identically distributed real \(N(0,1)\) entries and the elimination is in exact arithmetic. Only the first-column partial pivot is performed; no column interchanges are allowed. Pivot ties and singular inputs have probability zero. No floating-point rounding, matrix conditioning assumption, or asymptotic growth in matrix dimension is asserted. The definition counts both the original entries and the updated Schur complement, so \(\rho\ge1\).

## Proof
Write the first column as \((x_1,x_2)^{\mathsf T}\). After the possible swap, call the absolute pivot \(p>0\) and the ratio of the other first-column entry to the signed pivot \(t\), so \(|t|\le1\). Call the correspondingly permuted second-column entries \(y_1,y_2\). The only potentially enlarged element is
\[
s=y_2-t y_1,\qquad
\rho=\max\left\{1,\frac{|s|}{\max(|x_1|,|x_2|,|y_1|,|y_2|)}\right\}.
\]
By rotational invariance, the first-column radius \(R=\sqrt{x_1^2+x_2^2}\) is Rayleigh, independent of its folded angle \(\alpha\), which is uniform on \([0,\pi/4]\) with density \(4/\pi\). The absolute pivot is \(R\cos\alpha\), and \(|t|=\tan\alpha\). The independent permuted second column has Rayleigh radius \(S\) and folded angle \(\phi\) uniform on \([0,\pi/2]\) with density \(2/\pi\): \(|y_1|=S\cos\phi\), \(|y_2|=S\sin\phi\). These two angles and radii are mutually independent. Their signs cause the contributions to \(s\) to reinforce with probability exactly \(1/2\), independently of the absolute values.

In the opposite-sign configuration, \(|s|\le S\max(\sin\phi,\cos\phi)\le M\), so \(\rho=1\). In the reinforcing configuration,
\[
|s|=S(\sin\phi+\tan\alpha\cos\phi)
=\frac{S\sin(\alpha+\phi)}{\cos\alpha}.
\]
For any \(r\ge1\), the two inequalities \(|s|>rS\cos\phi\) and \(|s|>rS\sin\phi\) are equivalent to
\[
\phi>\arctan(r-\tan\alpha),\qquad
\phi<\arctan\!\left(\frac{\tan\alpha}{r-1}\right)
\]
(the upper inequality is automatic for \(r=1\), apart from a null boundary). These bounds admit an angle \(\phi\) precisely when \(\tan\alpha>r-1\), so \(\alpha>\alpha_0(r)\). In particular, no angle is available for \(r\ge2\). The remaining inequality against the first-column maximum is
\[
S>R\,\frac{r\cos^2\alpha}{\sin(\alpha+\phi)}.
\]
For independent standard Rayleigh radii, direct integration of their densities gives, for each \(d\ge0\),
\[
\mathbb P(S>dR)=\int_0^\infty r e^{-r^2/2}e^{-d^2r^2/2}\,dr
=\frac1{1+d^2}.
\]
Consequently, integration over the admissible angles and the independent sign event yields the two-dimensional exact formula
\[
\mathbb P(\rho>r)=\frac4{\pi^2}
\int_{\alpha_0(r)}^{\pi/4}
\int_{\phi_-(r,\alpha)}^{\phi_+(r,\alpha)}
\frac{\sin^2(\alpha+\phi)}
{\sin^2(\alpha+\phi)+r^2\cos^4\alpha}\,d\phi\,d\alpha.
\]
The prefactor is \((4/\pi)(2/\pi)(1/2)=4/\pi^2\). Elementary differentiation of the continuous angle expression shows
\[
\frac{d}{dz}F_c(z)=\frac{\sin^2z}{\sin^2z+c^2},\qquad 0<z<\pi.
\]
Integrating in \(\phi\) proves the stated one-dimensional formula. Its continuity for \(1<r<2\) excludes interior atoms. The upper endpoint is a null event by the strict angular inequalities, so there is no atom at \(2\). The event \(\rho=1\) is the complement of \(\rho>1\); the quadrature at \(r=1\) gives its exact probability.

Finally, set \(r=2-\delta\), \(u=\pi/4-\alpha\). The domain is \(0\le u\le\delta/2+O(\delta^2)\); uniformly in that domain the admissible \(\phi\)-interval has width \(\delta-2u+O(\delta^2)\), while its Rayleigh-ratio integrand is \(1/2+O(\delta)\), because \((\alpha,\phi,r)\to(\pi/4,\pi/4,2)\). Uniform smooth Taylor expansions on the shrinking compact region give
\[
\mathbb P(\rho>2-\delta)=\frac4{\pi^2}
\left(\frac12+O(\delta)\right)
\left(\int_0^{\delta/2}(\delta-2u)\,du+O(\delta^3)\right)
=\frac{\delta^2}{2\pi^2}+O(\delta^3).
\]
This proves the endpoint constant and exponent without extrapolating finite experiments.

## Verification
The self-contained accompanying program `CHECK.py` independently evaluates the original two-dimensional Rayleigh-angle integral and the antiderivative-based one-dimensional integral by composite Simpson quadrature. It compares the probabilities at six thresholds, checks the endpoint ratio at three thresholds, and reproduces those probabilities by seeded, independently generated Gaussian matrices. Run using `python3 CHECK.py`; success prints `GEPP_GROWTH_CHECK_OK`. These computations are consistency checks. All quantifiers, the atom, and the asymptotic coefficient are established by the proof above, not by finite Monte Carlo or quadrature.

Illustrative numerical survival probabilities: \(\mathbb P(\rho>1)\approx0.20313510441\), \(\mathbb P(\rho>1.5)\approx0.02194037589\), and \(\mathbb P(\rho>1.9)\approx0.0005608448695\).

## Relationship to prior work
Gaussian-elimination growth and rare large-growth events have a substantial history. Trefethen and Schreiber (1990) analyze approximate average-case behavior and simulations, not an exact finite-dimensional distribution. Higham and Higham (1989) classify worst-case extremal matrices, not Gaussian probability laws. Huang and Tikhomirov (2022) establish high-probability asymptotic guarantees for Gaussian GEPP, not the two-dimensional exact law. Urschel (2026) proves high-dimensional probabilistic growth bounds, not this CDF. Spielman and Yu (2026) prove nontrivial large-growth lower probability bounds for general random matrices; their published theorem does not imply this exact two-by-two distribution or its quadratic endpoint coefficient. Peca-Medlin and Trogdon (2023) derive exact laws for random *butterfly* matrices, which have a different distribution from independent Gaussian entries. The contribution here is the complete exact real-Ginibre base-case law and the sharp rare-event endpoint constant, not the classical deterministic \(2\) upper bound.

## Limitations
The result applies only to independent real Gaussian entries in dimension two, exact arithmetic, and standard partial pivoting. It is not a finite-precision backward-error theorem or a higher-dimensional rare-event estimate. The quadrature-based atom decimal is numerical rather than formally rounded to a certified interval. It is possible that an inaccessible older technical report or an equivalent unindexed formulation already contains this special case; no mathematical uniqueness claim is made.

## References
- D. A. Spielman and X. Yu, *Large Growth Happens: Gaussian Elimination with Partial Pivoting on Random Matrices*, arXiv:2610.08701v1 (first public 2026-10-06), https://arxiv.org/abs/2610.08701.
- J. Urschel, *On the Growth Factor of Random Matrices*, arXiv:2610.06785v1 (2026), https://arxiv.org/abs/2610.06785.
- H. Huang and K. Tikhomirov, *Average-case analysis of the Gaussian Elimination with Partial Pivoting*, arXiv:2206.01726 (2022), https://arxiv.org/abs/2206.01726.
- L. N. Trefethen and R. S. Schreiber, *Average-Case Stability of Gaussian Elimination*, SIAM J. Matrix Anal. Appl. 11 (1990), 335–360, https://people.maths.ox.ac.uk/trefethen/publication/PDF/1990_44.pdf.
- N. J. Higham and D. J. Higham, *Large Growth Factors in Gaussian Elimination with Pivoting*, SIAM J. Matrix Anal. Appl. 10 (1989), 155–164, https://webhomes.maths.ed.ac.uk/~dhigham/Publications/P3.pdf.
- J. Peca-Medlin and T. Trogdon, *Growth factors of random butterfly matrices and stability of avoiding pivoting*, arXiv:2203.15921v2, https://arxiv.org/abs/2203.15921.
