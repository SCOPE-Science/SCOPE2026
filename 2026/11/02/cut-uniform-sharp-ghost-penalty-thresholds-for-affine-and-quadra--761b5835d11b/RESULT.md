# Cut-uniform sharp ghost-penalty thresholds for affine and quadratic two-cell CutFEM

## Finding
For the aligned, one-ghost-face two-cell symmetric-Nitsche model, **all** positive cut fractions have a nonnegative discrete quadratic form for \(p=1\) or \(p=2\) exactly when
\[
\delta\ge p^2+\gamma^{-1},\qquad p\in\{1,2\}.
\]
For fixed \(\delta>p^2\), the exact uniform minimum ghost weight is therefore \(\gamma_{\mathrm{uniform}}=1/(\delta-p^2)\). When \(\delta\le p^2\), no finite positive ghost weight works for every cut fraction. At the uniform boundary, every individual cut with \(\kappa>0\) is actually positive definite, although the coercivity margin can tend to zero as \(\kappa\downarrow0\).

For \(p=1\), a stronger full classification of individual cuts is
\[
\delta\ge T_1(\kappa,\gamma):=\frac{1+\gamma}{\kappa(1+\gamma)+\gamma}.
\]
For \(p=2\), the corresponding exact individual-cut threshold is \(\delta\ge T_2=N/Q\), where
\[
N=12\gamma^2(1+\kappa)^3+\gamma(28\kappa^3+12\kappa^2+3)+4\kappa^3,
\]
\[
Q=3\gamma^2(1+\kappa)^4+\gamma(7\kappa^4+4\kappa^3+3\kappa)+\kappa^4.
\]
Both thresholds are strictly less than \(p^2+\gamma^{-1}\) for every positive cut fraction. These exact continuous-in-cut statements resolve the matching-upper-bound question posed for the two-cell model in the two lowest degrees, not for all degrees.

## Assumptions and scope
Let \(p\in\{1,2\}\), \(0<\kappa<1\), \(\delta>0\), and \(\gamma>0\). The uncut interval is \((-1,0)\), the cut-cell physical interval is \((0,\kappa)\), and the ghost face is at \(0\). Let \(u,q\in\mathbb P_p\), with matching values \(u(0)=q(0)\). The exact (mesh-unit) bilinear energy is
\[
a_{\kappa,\gamma}(u,q)=\int_{-1}^0 (u')^2\,dx+\int_0^\kappa(q')^2\,dx-2q'(\kappa)q(\kappa)+\delta q(\kappa)^2+\gamma\sum_{j=1}^{p}\frac{(q^{(j)}(0)-u^{(j)}(0))^2}{(j!)^2}.
\]
This is precisely the one-dimensional form of Eq. (60) of Wichrowski's aligned two-cell model, with \(\delta=\gamma_D\). The tangentially constant choice attains the reduction and the original source proves equivalence of the positivity question between the aligned higher-dimensional two-cell form and this one-dimensional model. There are no additional assembled-mesh faces or terms.

## Proof
Write \(t=q(\kappa)\), \(z=q'(\kappa)\), and
\[
E=\int_{-1}^0(u')^2\,dx+\int_0^\kappa(q')^2\,dx+\gamma\sum_{j=1}^{p}\frac{(q^{(j)}(0)-u^{(j)}(0))^2}{(j!)^2}.
\]
At fixed derivative coefficients, \(t\) can be chosen arbitrarily, as can the matching common value \(u(0)=q(0)\). Therefore \(a=E-2zt+\delta t^2\). The derivative-energy form \(E\) is strictly positive definite for \(\gamma>0\) and \(\kappa>0\), and the exact condition for \(a\succeq0\) is
\[
\delta\ge T_p(\kappa,\gamma):=\sup_{E>0}\frac{z^2}{E}.
\]
The supremum is attained; when the inequality is strict, the full form is strictly positive definite.

For \(p=1\), set \(u'=a\), \(q'=c\). Then \(E=a^2+\kappa c^2+\gamma(c-a)^2\), \(z=c\). Minimizing over \(a\) gives \(a=\gamma c/(1+\gamma)\), whence \(T_1=(\kappa+\gamma/(1+\gamma))^{-1}\). Plain algebra gives \(T_1<1+1/\gamma\) for every \(\kappa>0\), with equality in the limit \(\kappa\downarrow0\).

For \(p=2\), write \(u'=a+bx\), \(q'=c+dx\). Integration gives the exact positive quadratic form
\[
E=a^2-ab+\tfrac13b^2+\kappa c^2+\kappa^2cd+\tfrac13\kappa^3d^2+\gamma(c-a)^2+\tfrac\gamma4(d-b)^2,
\qquad z=c+\kappa d.
\]
Let \(H\) be its coefficient matrix in \((a,b,c,d)\) and let \(w=(0,0,1,\kappa)^\mathsf T\). Since \(H\succ0\), the Cauchy--Schwarz equality in the \(H\)-inner product yields \(T_2=w^\mathsf TH^{-1}w=N/Q\) with \(N,Q\) given above. Direct expansion, requiring only rational polynomial arithmetic, proves
\[
4+\gamma^{-1}-T_2=\frac{\kappa P}{\gamma Q}>0,
\]
where
\[
P=12\gamma^3(1+\kappa)^3+\gamma^2(31\kappa^3+6\kappa+24)+\gamma(11\kappa^3+3)+\kappa^3.
\]
Every term in \(P,Q\) is nonnegative and both are strictly positive for \(\gamma,\kappa>0\). The expansion gives \(\lim_{\kappa\downarrow0}T_2=4+\gamma^{-1}\). Thus for \(p=1,2\), the supremum of the fixed-cut threshold over all \(0<\kappa<1\) is exactly \(p^2+\gamma^{-1}\), strictly larger than each individual-cut threshold. This proves the iff statement, including the strictly positive boundary and the impossibility for \(\delta\le p^2\).

## Verification
The accompanying self-contained `verify.py` recomputes the derivative-energy matrices directly from the integrals and the derivative jumps, independently evaluates the inverse quadratic forms, checks the exact rational polynomial identity for \(T_2\), and uses 40 exact rational cut/weight pairs to test the positive-definite implication. Running `python verify.py` returns `PASS`. These finite cases supplement the symbolic identity and analytical proof, and are not used as a substitute for quantification over infinitely many cuts.

## Relationship to prior work
Wichrowski, *A Multigrid Method for CutFEM and its Convergence*, arXiv:2609.04067v1 (3 September 2026), Appendix B, gives \(1/(\delta-p^2)\) as an exact threshold **only at a vanishing cut**, and expressly leaves equality with the supremum over all positive cut fractions open. The present result proves that equality for the whole continuum of cuts for \(p=1,2\), and additionally gives the complete individual-cut thresholds. Burman et al.'s foundational CutFEM discussion (2014) and de Prenter et al.'s immersed-methods review (2022) develop cut-uniform coercivity through ghost stabilization, but their inspected treatments do not state these sharp formulas for the aligned source form. Exact finite-dimensional Schur complements are standard and not claimed as new.

## Limitations
Only \(p=1,2\) and the **isolated aligned one-ghost-face two-cell** model are covered. The general-degree matching upper bound, arbitrary cut geometry, full assembled operators, solver convergence, and cut-uniform coercivity *constants* are not established. The precise normalizations in Eq. (60) are essential; changing Nitsche or jump weights changes the formulas. Literature searches cannot exclude every older equivalent two-element calculation; independent mathematical validation has not been performed.

## References
1. M. Wichrowski, *A Multigrid Method for CutFEM and its Convergence*, arXiv:2609.04067v1 (3 September 2026), §6.3 and Appendix B, https://arxiv.org/abs/2609.04067.
2. E. Burman, S. Claus, P. Hansbo, M. G. Larson, and A. Massing, *CutFEM: Discretizing geometry and partial differential equations*, Int. J. Numer. Methods Eng. 104 (2015), 472–501; first online 2014, https://doi.org/10.1002/nme.4823.
3. F. de Prenter, C. Verhoosel, H. van Brummelen, M. G. Larson, and S. Badia, *Stability and conditioning of immersed finite element methods: analysis and remedies*, first public preprint 2022, https://doi.org/10.21203/rs.3.rs-1970859/v1.
