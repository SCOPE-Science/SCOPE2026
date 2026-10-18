# Three consumers and three resources are the sharp linear-oscillation threshold under common resource relaxation

## Finding
For the externally supplied, bilinear, nonreciprocal consumer–resource model described below, **at least three consumer types and at least three resource types are necessary for a nonzero-frequency imaginary eigenvalue of a strictly positive equilibrium**, when the diagonal resource relaxation rates are equal at that equilibrium. This lower bound is attained by a three-by-three cyclic model with matching supports for resource use and population benefit. Its exact stability threshold is
\[
\delta_c=\frac{3\sqrt{30}}{10}-\frac54>0.
\]
The threshold is a simple, transverse **linear spectral crossing**, not an assertion that a nonlinear Hopf limit cycle exists.

## Assumptions and scope
Let \(n,m\geq 1\) be integers. Consumer densities \(N_i>0\) and resource concentrations \(R_\alpha>0\) satisfy
\[
\dot N_i=N_i\left(\sum_{\alpha=1}^{m}C_{i\alpha}R_\alpha-\mu_i\right),\qquad
\dot R_\alpha=J_\alpha-\delta_\alpha R_\alpha-R_\alpha\sum_{i=1}^{n}D_{i\alpha}N_i.
\]
Assume \(C\in\mathbb R_{\geq0}^{n\times m}\), \(D\in\mathbb R_{\geq0}^{n\times m}\), \(J_\alpha>0\), \(\delta_\alpha>0\), and \(\mu_i>0\). Fix any strictly positive equilibrium \((N^*,R^*)\). The **common resource-relaxation hypothesis** is that
\[
\delta_\alpha+\sum_i D_{i\alpha}N_i^*=h>0\quad\text{for all }\alpha.
\]
The conclusion excludes **nonzero imaginary eigenvalues**, not all damped oscillations, all real instabilities, or global nonlinear periodic orbits. The matrices may be nonreciprocal; we additionally ensure matched nonzero support in the sharp example.

## Proof
At equilibrium the consumer growth brackets vanish. Let
\[
P=\operatorname{diag}(N^*)C\geq0,\qquad
Q=\operatorname{diag}(R^*)D^{\mathsf T}\geq0.
\]
The real Jacobian has block form
\[
\mathcal J=\begin{pmatrix}0&P\\-Q&-hI_m\end{pmatrix}.
\]
If \(\lambda=i\omega\) is an eigenvalue with \(\omega\in\mathbb R\setminus\{0\}\), both \(\lambda\) and \(\lambda+h\) are nonzero. Eliminating the resource coordinates gives
\[
\bigl[\lambda(\lambda+h)I_n+PQ\bigr]u=0,
\]
so \(-\lambda(\lambda+h)=\omega^2-i h\omega\) must be a **nonreal eigenvalue** of \(PQ\). Every nonzero eigenvalue of \(PQ\) is also a nonzero eigenvalue of \(QP\) by the elementary rectangular-product eigenvalue identity. Both matrices are entrywise nonnegative. A one-by-one nonnegative matrix has real spectrum, and a two-by-two nonnegative matrix \(\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\) has discriminant \((a-d)^2+4bc\geq0\); thus all its eigenvalues are real. If \(\min(n,m)\leq2\), at least one of \(PQ\) or \(QP\) has order at most two, and their nonzero spectra cannot contain a nonreal value. This contradiction proves the lower bound.

For sharpness, indices now run modulo three, \(i\in\{0,1,2\}\). Let \(S\) be the cyclic permutation satisfying \((SR)_i=R_{i+1}\), and take \(C=4(I+S)\) and \(D=I+\frac14S\). Both have the same nonzero entries. For any \(\delta>0\), consider
\[
\dot N_i=4N_i(R_i+R_{i+1}-2),\qquad
\dot R_i=\delta+\frac54-R_i\left(\delta+N_i+\frac14N_{i-1}\right).
\]
All concentrations \(N_i^*=R_i^*=1\) give a strictly positive equilibrium; supplies are \(\delta+5/4\), and common resource relaxation is \(h=\delta+5/4\). The product \(B=CD^{\mathsf T}\) is the circulant matrix
\[
B=\begin{pmatrix}5&4&1\\1&5&4\\4&1&5\end{pmatrix},\qquad
\det(zI-B)=(z-10)(z^2-5z+13).
\]
Its eigenvalues are \(10\) and \(5/2\pm 3\sqrt3\,i/2\). The full characteristic polynomial therefore factors exactly as
\[
\det(\lambda I-\mathcal J)=
(\lambda^2+h\lambda+10)
\left[(\lambda^2+h\lambda+\tfrac52)^2+\tfrac{27}{4}\right].
\]
The real quadratic is Hurwitz for all \(h>0\). The quartic factor equals
\[
\lambda^4+2h\lambda^3+(h^2+5)\lambda^2+5h\lambda+13.
\]
Its Routh–Hurwitz test has all the elementary positivity inequalities for \(h>0\); the sole potentially failing final determinant is
\[
(2h)(h^2+5)(5h)-(5h)^2-(2h)^2(13)=h^2(10h^2-27).
\]
Hence the quartic is Hurwitz precisely for \(h^2>27/10\). At \(h_c=3\sqrt{30}/10\), it factors further as
\[
(\lambda^2+\tfrac52)(\lambda^2+2h_c\lambda+\tfrac{26}{5}).
\]
Thus there is exactly one simple pair \(\pm i\sqrt{5/2}\), with every other eigenvalue in the open left half-plane. At \(0<h<h_c\), one conjugate pair has positive real part by the Routh criterion, and the other pair remains left of the imaginary axis. The critical roots are transverse: for the branch \(\lambda(h)\) obeying \(\lambda^2+h\lambda+5/2-3\sqrt3\,i/2=0\), the implicit derivative is \(d\lambda/dh=-\lambda/(2\lambda+h)\), and at \(\lambda=i\sqrt{5/2}\), \(h=h_c\),
\[
\frac{d}{dh}\operatorname{Re}\lambda=-\frac{50}{127}<0.
\]
Because \(h=\delta+5/4\) and \(5/4<h_c\), the claimed positive threshold \(\delta_c=h_c-5/4\) and both strict stability regimes follow.

## Verification
The standalone file `verify.py` checks all symbolic matrix products, the characteristic factorization, the exact Routh–Hurwitz determinant, the critical imaginary eigenvalues, and the transverse derivative using symbolic rational arithmetic. It also numerically checks the rightmost eigenvalues on both sides as a diagnostic, not as proof. Execute `python verify.py` with Python 3, SymPy, and NumPy installed. The dimension cutoff is an analytic all-dimensional argument and not inferred from numerical enumeration.

## Relationship to prior work
Rowland-Chandler, Goyal, and Shou (arXiv:2608.30966, first posted 2026-08-31) study nonreciprocal generalized consumer–resource systems and supply-dependent stability by large-community methods. Their indexed abstract identifies an analytic stability condition but does not resolve the **sharp minimal species/resource dimensions with common finite-dimensional relaxation** or give the above support-matched three-by-three threshold. Because the full document could not be inspected, that comparison is qualified, not represented as a complete exclusion.

Blumenthal, Rocks, and Mehta (arXiv:2308.15757) establish that sufficiently nonreciprocal large consumer–resource systems can transition to chaos; this is related motivation, not an equivalence with the present finite-dimensional spectral claim. Lynn, De Leenheer, and Dalziel (PLOS ONE 20:e0337943, 2025) investigate biofilm-mediated stabilization and report numerical Hopf transitions in a different nonlinear microbial model. The full text of a classical two-consumer/two-resource Tilman-type analysis, *Competition for resources: complicated dynamics in the simple Tilman model* (2015), discusses equilibrium stability in different growth/uptake assumptions; its small-system analysis is not the common-relaxation dimensional obstruction and matched-support witness above. A general block-Jacobian determinant formula alone is not asserted to be new; the novelty claim is the **sharp joint minimality and exact ecologically admissible crossing**.

## Limitations
The theorem is about local linear eigenvalues at strictly positive equilibria and assumes a common diagonal resource-relaxation slope, instantaneous bilinear exchange, no direct consumer density dependence in per-capita growth, and nonnegative benefit and uptake coefficients. Heterogeneous resource slopes, saturating nonlinear uptake, population self-limitation, external delays, and boundary equilibria lie outside the dimension obstruction. Stable complex eigenvalues can still produce **damped oscillations** when fewer than three types are present. A purely imaginary pair at the critical point does **not** establish a nondegenerate Hopf bifurcation or existence of periodic or chaotic attractors. Full-text access to the most closely related 2026 generalized consumer–resource preprint was unavailable; possible equivalent earlier finite-size statements remain a literature risk.

## References
1. J. Rowland-Chandler, A. Goyal, and W. Shou, *Resource supply dynamics control stability and chaos in complex ecosystems*, arXiv:2608.30966 (2026-08-31), https://arxiv.org/abs/2608.30966.
2. E. Blumenthal, J. W. Rocks, and P. Mehta, *Phase transition to chaos in complex ecosystems with non-reciprocal species-resource interactions*, arXiv:2308.15757 (2023), https://arxiv.org/abs/2308.15757.
3. B. K. Lynn, P. De Leenheer, and B. D. Dalziel, *Cooperative environmental engineering via biofilm formation can stabilize consumer-resource systems*, PLOS ONE 20, e0337943 (2025), https://doi.org/10.1371/journal.pone.0337943.
4. *Competition for resources: complicated dynamics in the simple Tilman model*, SpringerPlus (2015), https://doi.org/10.1186/s40064-015-1246-6.
