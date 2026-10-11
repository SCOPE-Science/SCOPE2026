# The sharp radial-growth trichotomy for entire weighted translations on power Fock spaces

## Finding
Let \(\alpha>0\) and \(m>0\), and write \(\mathcal F^2_{\alpha,m}\) for the Hilbert space of entire functions integrable with the radial squared norm \(\int_{\mathbb C}|f(z)|^2e^{-\alpha|z|^m}\,dA(z)\), up to a positive normalization constant. Fix \(a,b\in\mathbb C\), \(|a|=1\), \(b\ne0\), and an entire function \(\psi\). Define \(W_{\psi,a,b}f(z)=\psi(z)f(az+b)\). The operator is bounded if and only if either \(\psi\equiv0\), or one of the following two mutually exclusive regimes occurs:

1. \(0<m\le1\) and \(\psi(z)=C\) for a nonzero complex constant \(C\).
2. \(m=2\) and \(\psi(z)=C\exp(-\alpha a\overline b z)\) for a nonzero complex constant \(C\).

For \(1<m<2\) and \(m>2\), **no nonzero entire multiplier** yields a bounded weighted translation. Thus the Gaussian exponent is an isolated admissible exponent above the linear-growth threshold. Every nonzero bounded operator in the stated family is automatically invertible. In the Gaussian regime its exact operator norm is \(\|W_{\psi,a,b}\|=|C|e^{\alpha|b|^2/2}\).

## Assumptions and scope
The result is in one complex variable, for the same source and target Hilbert space, and requires a nonzero translation \(b\), a unit-modulus linear coefficient \(a\), a positive exponent and scale, and an arbitrary entire weight \(\psi\) (with no zero-free or exponential ansatz). The zero multiplier is separately bounded for every exponent. No assertion is made about \(|a|<1\), weighted composition between different spaces, or nonradial weights. Primary classification: MSC 2020 47B38.

## Proof
**Kernel prerequisite.** The kernel diagonal is radial and, using the orthogonal monomial basis, is
\[
K_{\alpha,m}(r,r)=\Gamma(2/m)\sum_{n=0}^{\infty}\frac{\alpha^{2n/m}r^{2n}}{\Gamma((2n+2)/m)}.
\]
For \(m>1\), the positive-ray Mittag–Leffler asymptotic (with index \(2/m\in(0,2)\)) gives
\[
K_{\alpha,m}(r,r)\sim\frac m2\Gamma(2/m)\alpha^{1-2/m}r^{m-2}e^{\alpha r^m}\quad(r\to\infty).
\]
Indeed, its leading exponential term has the stated power and positive constant; the remaining algebraic terms are negligible relative to the exponential. Since \(|az+b|/|z|\to1\) uniformly as \(|z|\to\infty\), this asymptotic and positivity of the kernel on compact sets imply
\[
\frac{K_{\alpha,m}(|az+b|,|az+b|)}{K_{\alpha,m}(|z|,|z|)}\ge c\exp\bigl(\alpha(|az+b|^m-|z|^m)\bigr)
\]
for some \(c>0\) and all \(z\in\mathbb C\). Boundedness and \(W^*K_z=\overline{\psi(z)}K_{az+b}\) therefore force
\[
|\psi(z)|\exp\left[\frac\alpha2(|az+b|^m-|z|^m)\right]\le B<\infty.\tag{1}
\]
This necessary estimate is also furnished by the boundedness criterion in Barik–Sen–Paul, Theorem 1.1. For sufficiency at unit slope, the same estimate implies boundedness by the area-preserving substitution \(w=az+b\) in the defining integral.

**The low-growth regime.** If \(0<m\le1\), subadditivity yields \(\big||az+b|^m-|z|^m\big|\le|b|^m\). Consequently the unweighted composition \(C_{az+b}\) and its inverse are bounded on \(\mathcal F^2_{\alpha,m}\). If \(W_{\psi,a,b}\) is bounded, so is \(M_\psi=W_{\psi,a,b}C_{az+b}^{-1}\). Evaluation on normalized kernels gives \(|\psi(z)|\le\|M_\psi\|\) for all \(z\); Liouville's theorem makes \(\psi\) constant. Conversely all constant multipliers produce bounded operators, and nonzero ones are invertible.

**The Gaussian regime.** For \(m=2\),
\[
|az+b|^2-|z|^2=|b|^2+2\operatorname{Re}(a\overline b z).
\]
Estimate (1) is equivalent to boundedness on \(\mathbb C\) of the entire function \(g(z)=\psi(z)e^{\alpha a\overline b z}\); Liouville gives \(g=C\). Conversely, changing variables shows the exact identity
\[
\|W_{C e^{-\alpha a\overline b z},a,b}f\|_{\alpha,2}^2=|C|^2e^{\alpha|b|^2}\|f\|_{\alpha,2}^2.
\]
Thus the operator is invertible for \(C\ne0\) and has the asserted norm.

**The interval \(1<m<2\).** Replace \(az\) by a complex coordinate \(w\) and rotate so that \(b>0\) is real; the weight remains entire. Write \(F(w)=\psi(a^{-1}w)\). On the closed right half-plane \(\operatorname{Re}w\ge0\), \(|w+b|\ge|w|\), so (1) bounds \(|F(w)|\le B\). On the whole plane the mean-value inequality for \(r^m\) implies \(|w+b|^m-|w|^m\ge-C(1+|w|^{m-1})\). Hence \(|F(w)|\le B\exp(C'(1+|w|^{m-1}))\). Since \(m-1<1\), the half-plane Phragmén–Lindelöf principle (opening angle \(\pi\), growth order strictly below one) propagates the boundary bound into the left half-plane. Liouville now makes \(F\) constant. Along positive real \(w=t b\), however, \(|w+b|^m-|w|^m=((t+1)^m-t^m)|b|^m\to\infty\). Estimate (1) forces that constant to be zero. Thus no nonzero weight exists.

**The regime \(m>2\).** Again set \(F(w)=\psi(a^{-1}w)\) and rotate so \(b>0\). Taking logarithms in (1) and averaging on \(|w|=R\) gives
\[
\frac1{2\pi}\int_0^{2\pi}\log|F(Re^{i\theta})|\,d\theta\le\log B-\frac\alpha2\left(\frac{m^2b^2}{4}R^{m-2}+O(R^{m-3})\right).\tag{2}
\]
The mean expansion follows from the second-order binomial expansion of \((1+2(b/R)\cos\theta+(b/R)^2)^{m/2}\), whose mean quadratic coefficient is \(m^2/4\). It tends to \(-\infty\) on the right of (2). If the entire \(F\not\equiv0\), write \(F(w)=w^kH(w)\) with integer \(k\ge0\) and \(H(0)\ne0\). Jensen's inequality for the subharmonic function \(\log|H|\) gives
\[
\frac1{2\pi}\int_0^{2\pi}\log|F(Re^{i\theta})|\,d\theta\ge k\log R+\log|H(0)|,
\]
a contradiction. This proves the classification for every \(m>0\).

## Verification
The proof checks all exponent boundaries separately: \(m=1\) belongs to subadditivity, \(m=2\) to exact Gaussian compensation, and neither of the contradiction arguments uses a nonuniform limiting assumption at those endpoints. The kernel asymptotic is used only for \(m>1\) and is uniform under bounded shifts because the two radii have ratio tending to one. The log-circle integral in the superquadratic argument is well-defined in the integrable extended sense; isolated zeros contribute integrable logarithmic singularities. The package includes a reproducible independent finite sanity check for the Gaussian square-completion identity and the quartic circle-average coefficient. These checks are illustrative, not substitutes for the Phragmén–Lindelöf and Jensen arguments.

## Relationship to prior work
Barik–Sen–Paul (2026), Theorem 1.1, supplies an overarching boundedness criterion for a given entire weight, and its Section 5 classifies exponential-linear weights and *unweighted* compositions. It does not state the present all-entire-weight existence classification for unit-slope translations. That criterion is a crucial antecedent; the new content is the global feasibility analysis: sublinear Liouville rigidity, subquadratic half-plane Phragmén–Lindelöf exclusion, Gaussian compensation, and superquadratic Jensen exclusion. Mengestie–Takele (2023), Corollary 3.1 and Theorem 3.4, provide broader abstract tests in fast-growing Fock-type weights, including power exponents above two, but not the explicit all-entire-multiplier power-exponent trichotomy. Zhu (2011) proves uniqueness for a prescribed family of Gaussian weighted translations preserving the Hilbert norm; that does not classify bounded single weighted translations for radial powers below two. Trieu Le (2014) treats the classical quadratic Fock case; the Gaussian branch is established antecedent, not new.

## Limitations
The theorem concerns boundedness, not operator compactness, essential norms, or other holomorphic spaces. The arithmetic of the transition values is not a quantitative norm formula outside \(m=2\). The originality claim is for the explicit all-weight phase classification, not the published general boundedness criterion, the unweighted sublinear translation bound, or the Gaussian Weyl formula. An equivalent prior argument for the non-Gaussian rigidity in less discoverable literature remains possible. Independent review has not been performed.

## References
- S. Barik, A. Sen, and K. Paul, *Weighted composition operators on weighted Fock spaces*, arXiv:2607.17170v1, 19 July 2026, Sections 1–2 and 5. https://arxiv.org/html/2607.17170v1
- T. Mengestie and M. H. Takele, *Integral and Weighted Composition Operators on Fock-type Spaces*, *Bull. Malays. Math. Sci. Soc.* 46 (2023), article 80, Corollary 3.1 and Theorem 3.4. https://doi.org/10.1007/s40840-023-01476-4
- K. Zhu, *Translation Invariance of Fock Spaces*, arXiv:1101.4201v1, 21 January 2011, Sections 1 and 4. https://arxiv.org/html/1101.4201v1
- T. Le, *Normal and isometric weighted composition operators on the Fock space*, *Bull. Lond. Math. Soc.* 46 (2014), 847–856. https://doi.org/10.1112/blms/bdu046
