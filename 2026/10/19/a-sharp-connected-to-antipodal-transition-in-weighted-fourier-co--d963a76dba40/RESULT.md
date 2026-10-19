# A sharp connected-to-antipodal transition in weighted Fourier concentration

## Finding

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) carry normalized Haar measure, let \(0<\alpha<1\), and for a measurable \(w:\mathbb T\to[0,1]\) of mean \(\alpha\), write
\[
 c_k(w)=\frac{1}{2\pi}\int_0^{2\pi}w(\theta)e^{-ik\theta}\,d\theta.
\]
For arbitrary \(p,q>0\), the exact maximum is
\[
 \boxed{\sup_w\bigl(p|c_1(w)|^2+q|c_2(w)|^2\bigr)
 =\frac{\sin^2(\pi\alpha)}{\pi^2}
 \max\{p+q\cos^2(\pi\alpha),\ q\}.}
\]
Every maximizer is a characteristic function. If \(q\sin^2(\pi\alpha)<p\), its support is exactly one arc of normalized length \(\alpha\), up to rotation and null sets. If \(q\sin^2(\pi\alpha)>p\), its support consists of two antipodal arcs of equal angular length \(\pi\alpha\), again up to rotation and null sets. At the equality threshold \(q\sin^2(\pi\alpha)=p\), these two geometries, and no others, maximize the expression.

For a three-site spatial window \(\Omega=\{0,1,2\}\), a measurable spectral mask \(S\subset\mathbb T\) with Haar mass \(\alpha\), and positive diagonal gains \(0<g_0,g_1,g_2\le1\), let \(T_S\) have entries \(\widehat{\mathbf1_S}(i-j)\), and put \(A_S=G^{1/2}T_SG^{1/2}\), \(G=\operatorname{diag}(g_0,g_1,g_2)\). Define \(p=g_1(g_0+g_2)\) and \(q=g_0g_2\). The sharp weighted trace defect is
\[
 \boxed{\min_{|S|/(2\pi)=\alpha}\operatorname{tr}(A_S-A_S^2)
 =\alpha\sum_{j=0}^{2}g_j-\alpha^2\sum_{j=0}^{2}g_j^2
 -\frac{2\sin^2(\pi\alpha)}{\pi^2}
 \max\{p+q\cos^2(\pi\alpha),q\}.}
\]
The minimizers have exactly the geometries above. In particular, for \(g_0=g_2=1\) and \(g_1=t\in(0,1]\), the transition is at \(2t=\sin^2(\pi\alpha)\); the optimal spectral mask disconnects when \(2t<\sin^2(\pi\alpha)\).

## Assumptions and scope

The Fourier formula concerns all measurable masks with values between zero and one, not only characteristic functions. The measure and coefficient normalizations are specified above. The gains are strictly positive, ensuring both Fourier weights are positive; allowing zero gains introduces additional degeneracies not classified here. Equalities and maximizers are understood modulo changes on null sets. The result is for the three consecutive spatial sites; no arbitrary-length generalization is asserted.

## Proof

**1. A maximizing mask is an indicator of at most two arcs.** The convex weak-* compact class \(\mathcal K_\alpha=\{w\in L^\infty(\mathbb T):0\le w\le1,\ \int w=\alpha\}\) has a maximizer for \(F(w)=p|c_1(w)|^2+q|c_2(w)|^2\), since the objective depends continuously on finitely many weak-* continuous functionals. The indicator of an arc has positive objective, so every maximizer has at least one nonzero coefficient.

For a maximizer \(w\), convexity of \(F\) gives \(F(v)\ge F(w)+DF(w)[v-w]\) for every \(v\in\mathcal K_\alpha\), while maximality gives \(F(v)\le F(w)\). Thus \(DF(w)[v-w]\le0\). Explicitly,
\[
 DF(w)[v-w]=\int_{\mathbb T}\Phi_w(\theta)(v-w)(\theta)\,dm(\theta),
 \quad \Phi_w(\theta)=2p\operatorname{Re}(\overline{c_1(w)}e^{-i\theta})+2q\operatorname{Re}(\overline{c_2(w)}e^{-2i\theta}).
\]
The real trigonometric polynomial \(\Phi_w\) is nonconstant and has degree at most two. The bathtub principle for its linear functional forces \(w\) to be the indicator of an upper-level set of \(\Phi_w\). Each nonconstant degree-two real trigonometric polynomial takes any prescribed value at at most four distinct points on the circle (multiply its Laurent polynomial equation by the square of the circle variable). Hence an upper-level set is a union of at most two arcs, with no fractional mass on the finite level set.

**2. Reduce to at most half the circle.** For \(0<\alpha\le1/2\), each candidate is one arc or two arcs. For \(\alpha>1/2\), replacing \(w\) by \(1-w\) changes the mean to \(1-\alpha\) and changes the sign of both nonzero Fourier coefficients without changing their moduli. This bijection transfers every maximizer and its geometry.

**3. Two-arc parametrization.** Write two nonempty separated arcs with half-widths \(a,b>0\), \(a+b=L=\pi\alpha\le\pi/2\), and center separation \(d\in[L,2\pi-L]\). Put \(A=\sin a\), \(B=\sin b\), \(u=\cos d\in[-1,\cos L]\). Direct Fourier integration gives
\[
 \pi^2 F=p(A^2+B^2+2ABu)
 +q\bigl(A^2\cos^2a+B^2\cos^2b+2AB\cos a\cos b(2u^2-1)\bigr).
\]
As a function of \(u\), this expression is strictly convex: its quadratic coefficient is \(4qAB\cos a\cos b>0\). The value of any configuration with separated arcs is therefore strictly less than the larger of the values at the endpoints \(u=-1\) (opposite centers) and \(u=\cos L\) (touching arcs). The touching endpoint gives a single arc of half-width \(L\) and yields
\[
 \pi^2 F_{\mathrm{arc}}=\sin^2L\,(p+q\cos^2L).
\]
At opposite centers, set \(c=\cos L\) and \(y=\cos(a-b)\in[c,1]\). The same Fourier formula simplifies to
\[
 \pi^2 F_{\mathrm{opp}}=2p(1+c)(1-y)+q(1-c^2)y^2.
\]
This is a *strictly convex* quadratic in \(y\), since \(q(1-c^2)>0\), so its maximum occurs only at \(y=c\) or \(y=1\). The endpoint \(y=c\) means one arc has zero width, reproducing \(F_{\mathrm{arc}}\). The endpoint \(y=1\) means \(a=b=L/2\), that is two equal antipodal arcs, and yields
\[
 \pi^2 F_{\mathrm{pair}}=q\sin^2L.
\]
No genuinely separated unequal arcs can maximize: strict convexity excludes all interior values of \(u\) and \(y\). Comparing the two endpoints gives
\[
 F_{\mathrm{pair}}-F_{\mathrm{arc}}=\frac{\sin^2L}{\pi^2}(q\sin^2L-p),
\]
which proves the announced sharp threshold and both equality types. Complementation covers \(\alpha>1/2\): the complement of an arc is an arc and the complement of a pair of equal antipodal arcs is another such pair. The first-variation step showed every maximizing soft mask is binary, completing the unrestricted classification.

**4. Weighted concentration formula.** The matrix entries of \(A_S\) equal \(\sqrt{g_i g_j}\,c_{i-j}(\mathbf1_S)\). Therefore
\[
 \operatorname{tr}A_S=\alpha\sum_{j=0}^{2}g_j,\qquad
 \operatorname{tr}(A_S^2)=\alpha^2\sum_{j=0}^{2}g_j^2
 +2\bigl(p|c_1(\mathbf1_S)|^2+q|c_2(\mathbf1_S)|^2\bigr).
\]
Inserting the proved Fourier maximum yields the trace-defect minimum and all minimizing masks. With gains at most one, \(0\le A_S\le I\), hence this is a genuine nonnegative localization defect.

## Verification

The accompanying standalone `check.py` uses deterministic random samples and direct exact arc-integration formulas to examine 18,000 arbitrary two-arc configurations, 2,000 comparisons between the two optimizer families, and 1,000 random piecewise-constant soft-mask comparisons. It reports `PASS 21000 deterministic checks, all bounds hold`. These finite diagnostics do not establish the global theorem; the proof above establishes the continuum and equality statements. The trigonometric formulas are independently reconstructible by integrating each exponential over each arc.

## Relationship to prior work

Mayeli, *Trace-defect bounds for discrete Fourier concentration operators* (September 2026), establishes an exact trace-defect identity and regularity-dependent bounds for large spatial windows; the present result determines a different, finite three-site mask-design optimization with diagonal gains and a sharp connectivity transition. The published published-finding corpus record *Sharpness of all fractional trace-defect regimes for discrete Fourier concentration* (September 2026) concerns fractal constructions that attain those growth regimes, not weighted mask extremizers. Marceca, Romero and Speckbacher establish geometric eigenvalue estimates, again without the present weight-dependent phase diagram.

Abreu and Speckbacher, *Optimal concentration in the Paley-Wiener space* (July 2026), establish that a circle interval maximizes the **largest** concentration eigenvalue for analytic trigonometric polynomials. For the unweighted three-site operator, applying that theorem also to the complementary set yields three-dimensional eigenvalue majorization and consequently the unweighted trace-squared inequality; **the unweighted arc conclusion is therefore not claimed here as new**. The weighted defect depends on \(\operatorname{tr}(G^{1/2}T_SG^{1/2})^2\), not on the unweighted eigenvalues of \(T_S\): interval optimality fails for some positive gains, with the two-arc geometry explicitly superior. Thus the weighted phase transition is neither the unweighted theorem nor its corollary. An unavailable full manuscript could still contain a related weighted theorem, so historical priority remains provisional.

## Limitations

The classification requires strictly positive Fourier weights and concerns a three-site window on the circle. No stability modulus, higher-band transition diagram, or historical priority beyond the inspected material is asserted. Finite checking cannot certify the continuum inequalities, and the July 2026 closest spectral shape manuscript was not available in full text during comparison; its public theorem establishes maximal leading-eigenvalue concentration, not the present weighted quadratic trace functional.

## References

1. A. Mayeli, *Trace-defect bounds for discrete Fourier concentration operators*, arXiv:2609.12226, publicly submitted 2026-09-10. https://arxiv.org/abs/2609.12226
2. L. D. Abreu and M. Speckbacher, *Optimal concentration in the Paley-Wiener space*, arXiv:2607.19192, publicly submitted 2026-07-21. https://arxiv.org/abs/2607.19192
3. F. Marceca, J. L. Romero and M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, arXiv:2301.11685 (2023), published 2024. https://arxiv.org/abs/2301.11685
4. *Sharpness of all fractional trace-defect regimes for discrete Fourier concentration*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-sharp-fractional-discrete-fourier-trace-defects--bbf7e58277be
