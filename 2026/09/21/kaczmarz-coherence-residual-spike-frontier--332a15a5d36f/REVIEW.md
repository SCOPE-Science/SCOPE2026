# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The residual update, scalar reduction, piecewise maximization, sharp construction, and threshold were checked independently from the numerical experiments.

After row normalization, a Kaczmarz step selected at row \(i\) transforms the normalized residual by
\[
(q_+)_j=q_j-q_i\langle b_j,b_i\rangle,
\qquad (q_+)_i=0.
\]
Maximal-distance selection gives \(|q_j/q_i|\le1\). With \(d=m-1\), \(s_j=q_j/q_i\), and \(c_j=\langle b_j,b_i\rangle\), coherence gives \(|c_j|\le\mu\), and therefore
\[
\frac{\|q_+\|_2^2}{\|q\|_2^2}
=\frac{\|s-c\|_2^2}{1+\|s\|_2^2}
\le
\frac{(y+\mu\sqrt d)^2}{1+y^2},
\quad 0\le y=\|s\|_2\le\sqrt d.
\]
The derivative has the sign of \(1-\mu\sqrt d\,y\), producing exactly the stated two branches.

The sharp family
\[
b_1=e_1,\qquad
b_j=-\mu e_1+\sqrt{1-\mu^2}\,e_j
\]
is unit-row, nonsingular for \(\mu<1\), and has coherence exactly \(\mu\). Residual states \((1,t,\ldots,t)^T\) attain the bound with \(t=1\) in the endpoint branch and \(t=(d\mu)^{-1}\) in the interior branch. Because the matrix is nonsingular, these residual states are realized in a consistent homogeneous system. Perturbing \(t=1\) downward gives unique-maximizer witnesses arbitrarily close to the endpoint equality.

Solving the first-branch inequality \(\Gamma_m(\mu)\le1\) yields \(\mu\le\sqrt{m/(m-1)}-1\), which lies below \(1/(m-1)\); the sharp family gives necessity. The \(\theta\)-approximate extension repeats the same scalar maximization on \(0\le y\le\sqrt d/\theta\), giving the stated formulas.

A deterministic NumPy verification reproduced the equality families to machine precision, checked the threshold from both sides, tested the approximate-oracle formula, and found no violations in 6,000 random unit-row cases. These checks support but do not replace the proof.

## Originality

**PASS, to the best of our knowledge.** The classical 1954 relaxation papers establish maximal-distance/maximal-residual projection ideas. Popa's remotest-set work studies maximal-residual control sequences. Du--Gao (2019) is a directly relevant analysis of maximal weighted residual Kaczmarz; its stated purpose is a convergence-rate estimate, and later literature explicitly restates its principal theorem as a solution-error contraction estimate. Nutini et al. (2015) gives a primary-source analysis of Gauss--Southwell coordinate descent in objective/energy terms, including exact coordinate optimization and approximate selection rules.

These results do not by themselves control monotonicity of the complete Euclidean residual/gradient vector. Searches targeted the exact formulas, row coherence/correlation, maximal weighted residual and remotest-set terminology, Kaczmarz--Motzkin variants, Gauss--Southwell gradient-norm behavior, residual monotonicity/increase, and equivalent coordinate-relaxation language. No checked source stated the same sharp piecewise one-step residual factor or the exact coherence threshold \(\sqrt{m/(m-1)}-1\).

Recent literature gives important conceptual overlap. Li--Liu's double-greedy global block Kaczmarz work states that selecting large residual entries can increase smaller ones, calling this the "seesaw effect". Panchal--Behera (2026) likewise treats the seesaw effect as a convergence-stability issue. The present result therefore does **not** claim discovery of the qualitative phenomenon that unselected residual components can increase. Its claimed contribution is the sharp total-normalized-residual amplification law and exact coherence frontier for the single-row maximal-distance rule, together with the matching approximate-oracle extension.

Residual historical risk remains because Southwell-style relaxation, old coordinate-relaxation literature, and the large Kaczmarz literature are broad. The complete Du--Gao theorem body was not available in the checked publisher HTML, although its abstract, introduction, and later explicit restatement were inspected. This uncertainty is material but no concrete evidence of prior coverage of the formulas was found.

## Value

**PASS.** The result turns a qualitative stability issue into an exact, easily interpreted frontier. It separates the always-decreasing solution error of a consistent Kaczmarz projection from the potentially increasing total residual, quantifies the worst spike solely through dimension and row coherence, identifies the exact coherence regime in which the natural normalized residual is guaranteed to decrease at every greedy step, and extends to approximate row-selection oracles. The equivalent Gauss--Southwell statement connects the result to Euclidean gradient-norm diagnostics for exact coordinate descent on correlation quadratics.

## Scientific limitations

- Exact arithmetic and one-step analysis only.
- The controlled norm is the scale-invariant normalized residual \(\|D^{-1}(Ax-b)\|_2\); arbitrary raw row scaling changes the ordinary residual norm.
- Pairwise row coherence is a coarse summary and can be pessimistic for a fixed matrix.
- The theorem is not an iteration-count result and does not analyze finite precision, asynchronous or block variants, noisy/inconsistent convergence, or stopping rules.
- Upper bounds hold without consistency; sharpness is witnessed by square nonsingular consistent systems.
- The Gauss--Southwell interpretation requires full row rank so that the row-space quadratic Hessian is positive definite.
- Older relaxation and coordinate-relaxation sources were not exhaustively inspected theorem by theorem, leaving residual originality uncertainty.
