# Exact critical lines in the two-dimensional nearest-neighbor lattice delta model
## Finding
For the Hiroshima–Muminov–Kuljanov discrete Schrödinger operator on \(\mathbb Z^n\), \(n\ge2\), with dispersion \(E(p)=\sum_{j=1}^n(1-\cos p_j)\), let the paper's lower-threshold constants be \(\lambda_s=1/s(0)\) and \(\lambda_c=1/(c(0)-d(0))\). Then they are not independent: for every \(n\ge2\), \[\frac1{\lambda_s}=\frac1n\left(1-\frac{n-1}{\lambda_c}\right),\qquad \lambda_s=\frac{n\lambda_c}{\lambda_c-(n-1)}.\] In dimension \(n=2\) both constants are elementary, \[\lambda_s=\frac{\pi}{\pi-2},\qquad \lambda_c=\frac{\pi}{4-\pi}.\] Consequently the two distinguished points where the source's right threshold hyperbola \((\lambda-1)(\mu-2)=2\) meets the vertical lines \(S_0\) and \(C_0\) are exactly \[A=\left(\frac{\pi}{\pi-2},\pi\right),\qquad B=\left(\frac{\pi}{4-\pi},\frac{\pi}{\pi-2}\right).\]

These formulas turn the two vertical transition lines and the two named intersection points in the published \(n=2\) phase portrait into closed forms. Numerically,
\[
\lambda_s\approx 2.751938393884109,\qquad
\lambda_c\approx 3.659792366325488.
\]

## Assumptions and scope
The operator is exactly the finite-support lattice model of Hiroshima, Muminov and Kuljanov: on \(\ell^2(\mathbb Z^n)\), the unperturbed part is the standard discrete Laplacian and the potential is supported at the origin and its nearest neighbours. In momentum space the dispersion is
\[
E(p)=\sum_{j=1}^n(1-\cos p_j),\qquad p\in(-\pi,\pi]^n.
\]
Write \(\langle f\rangle=(2\pi)^{-n}\int_{\mathbb T^n}f(p)\,dp\). The source defines
\[
s(0)=\left\langle\frac{\sin^2p_1}{E(p)}\right\rangle,
\qquad
c(0)-d(0)=\frac12\left\langle\frac{(\cos p_1-\cos p_2)^2}{E(p)}\right\rangle,
\]
and \(\lambda_s=1/s(0)\), \(\lambda_c=1/(c(0)-d(0))\). The dimension-wide identity below applies for every \(n\ge2\). The explicit \(\pi\)-formulas and the coordinates of \(A,B\) are specific to \(n=2\).

## Proof
Put \(a_j=1-\cos p_j\), so \(E=\sum_j a_j\), and set
\[
L=c(0)-d(0),\qquad B_2=\left\langle\frac{a_1^2}E\right\rangle,
\qquad C_2=\left\langle\frac{a_1a_2}E\right\rangle.
\]
Permutation symmetry gives
\[
\left\langle\frac{a_1}E\right\rangle=\frac1n,
\]
and, because \(a_1E/E=a_1\) almost everywhere and \(\langle a_1\rangle=1\),
\[
B_2+(n-1)C_2=1.
\]
Since \(\cos p_1-\cos p_2=a_2-a_1\),
\[
L=\frac12\left\langle\frac{(a_1-a_2)^2}E\right\rangle=B_2-C_2.
\]
Solving these two linear equations gives
\[
B_2=\frac{1+(n-1)L}n.
\]
Also \(\sin^2p_1=a_1(2-a_1)\), hence
\[
s(0)=2\left\langle\frac{a_1}E\right\rangle-B_2
=\frac{1-(n-1)L}n.
\]
Substituting \(L=1/\lambda_c\) and \(s(0)=1/\lambda_s\) proves the dimension-wide identity.

For \(n=2\), integrate first in the second momentum coordinate. With \(A=2-\cos p\), the elementary contour integral
\[
\frac1{2\pi}\int_{-\pi}^\pi\frac{dq}{A-\cos q}=\frac1{\sqrt{A^2-1}},\qquad A>1,
\]
gives, by the integrable endpoint limit at \(p=0\),
\[
s(0)=\frac1\pi\int_0^\pi\frac{\sin^2p}{\sqrt{(2-\cos p)^2-1}}\,dp.
\]
Set \(t=\sin(p/2)\) and then \(u=t^2\). This becomes
\[
s(0)=\frac2\pi\int_0^1\sqrt{\frac{1-u}{1+u}}\,du.
\]
With \(y=\sqrt{(1-u)/(1+u)}\), the remaining integral is
\[
\int_0^1\sqrt{\frac{1-u}{1+u}}\,du=\frac\pi2-1,
\]
so
\[
s(0)=1-\frac2\pi=\frac{\pi-2}\pi,
\qquad
\lambda_s=\frac\pi{\pi-2}.
\]
The dimension-wide identity with \(n=2\) then yields
\[
c(0)-d(0)=1-2s(0)=\frac4\pi-1=\frac{4-\pi}\pi,
\qquad
\lambda_c=\frac\pi{4-\pi}.
\]
Finally, the source's limiting right hyperbola in dimension two is \((\lambda-1)(\mu-2)=2\). At \(\lambda=\lambda_s\),
\[
\mu=2+\frac2{\lambda_s-1}=\pi,
\]
and at \(\lambda=\lambda_c\),
\[
\mu=2+\frac2{\lambda_c-1}=\lambda_s.
\]
This gives the stated points \(A\) and \(B\).

## Verification
The algebraic reduction uses only permutation symmetry, \(\sum_j a_j/E=1\) away from the single point \(p=0\), and the source's definitions. The singular point has measure zero, and all displayed threshold integrals are finite for \(n\ge2\) as in the source. The one-dimensional integral evaluation for \(n=2\) is reproduced in `verify_threshold_constants.py`; its numerical quadrature agrees with the closed forms to the stated tolerance. The numerical replay is corroborative only and is not used to infer the exact identities.

## Relationship to prior work
Hiroshima, Muminov and Kuljanov define \(c(z)-d(z)\) and \(s(z)\), introduce \(\lambda_c=1/(c(0)-d(0))\) and \(\lambda_s=1/s(0)\), prove the ordering \(\lambda_s\le\lambda_c\), and use the vertical lines \(S_0\) and \(C_0\) together with points \(A\) and \(B\) in their phase diagram. In the inspected arXiv version, those constants remain in integral form; the exact dimension-wide relation, the closed forms \(\pi/(\pi-2)\) and \(\pi/(4-\pi)\), and the exact coordinates above are not stated in the relevant definitions, lemmas, theorem, table, or figure captions.

A later paper by Muminov, Alladustov and Lakaev studies a closely related small-rank perturbation of the discrete Laplacian. Its abstract and indexing metadata were inspected, but a reliable matching full text was not available in this comparison, so it remains a specific originality risk rather than evidence of coverage. Broader two-dimensional lattice Schrödinger papers located in the search concern general existence and eigenvalue asymptotics and do not, in the inspected metadata, state these two finite-support threshold constants.

## Limitations
The result is an exact re-expression of threshold constants for this particular nearest-neighbour finite-support model; it does not extend the source's spectral classification to generic lattice potentials or dispersions. It concerns the lower threshold and does not claim a new upper-threshold classification. The originality assessment is literature-search based rather than a proof that no equivalent formula exists under different notation; the inaccessible closely related 2021 article is the main residual risk.

## References
1. F. Hiroshima, Z. Muminov, U. Kuljanov, *Threshold of discrete Schrödinger operators with delta potentials on \(n\)-dimensional lattice*, arXiv:1804.05339v1 (2018); DOI: 10.1080/03081087.2020.1750547.
2. Z. I. Muminov, Sh. U. Alladustov, Sh. S. Lakaev, *Spectral and threshold analysis of a small rank perturbation of the discrete Laplacian*, J. Math. Anal. Appl. 496 (2021), 124827; DOI: 10.1016/j.jmaa.2020.124827.
3. A. T. Boltaev, F. M. Almuratov, *The Existence and Asymptotics of Eigenvalues of Schrödinger Operator on Two Dimensional Lattices*, Lobachevskii J. Math. 43 (2022), 3460–3470; DOI: 10.1134/S1995080222150082.
