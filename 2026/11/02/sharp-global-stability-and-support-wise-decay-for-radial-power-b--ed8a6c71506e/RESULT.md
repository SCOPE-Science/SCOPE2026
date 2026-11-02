# Sharp global stability and support-wise decay for radial-power Bregman descent

## Finding

Fix a real exponent \(p>2\), an integer \(d\ge1\), and weights \(a_1,\ldots,a_d>0\). Define the strictly convex objective and radial mirror kernel
\[
f(x)=\frac1p\sum_{i=1}^{d}a_i|x_i|^p,
\qquad
\phi(x)=\frac12\|x\|_2^2+\frac1p\|x\|_2^p.
\]
For constant stepsize \(\eta>0\), exact unconstrained Bregman-gradient descent is the uniquely defined iteration
\[
\nabla\phi(x^{k+1})=\nabla\phi(x^k)-\eta\nabla f(x^k).
\]
Write \(a_{\max}=\max_i a_i\). The following statements hold.

1. **Sharp global convergence frontier.** Every trajectory from every \(x^0\in\mathbb R^d\) converges to the unique minimizer \(0\), and its Euclidean radius strictly decreases at each nonzero step, whenever \(0<\eta\le2/a_{\max}\). This interval is exact: for every \(\eta>2/a_{\max}\), some trajectories diverge in magnitude, so global convergence fails.
2. **Exact axial basin and flip boundary.** On any coordinate axis with \(m_i:=\eta a_i>2\), let
\[
R_i=\left(\frac{2}{m_i-2}\right)^{1/(p-2)}.
\]
From \(x^0=t e_i\), \(|t|<R_i\) implies convergence to \(0\); \(|t|=R_i\) gives an exact nonzero alternating two-cycle \(t e_i,-t e_i\); and \(|t|>R_i\) gives alternating signs and \(\|x^k\|_2\to\infty\). For \(m_i\le2\), every point on that axis converges to \(0\).
3. **Universal support-wise rate inside the stable interval.** Let \(0<\eta\le2/a_{\max}\), and let \(S\) be the set of coordinates that never become identically zero after some finite iteration. For each \(i\in S\), signs eventually stop changing and
\[
\lim_{k\to\infty}k|x_i^k|^{p-2}=\frac1{(p-2)\eta a_i}.
\]
Consequently, when \(S\ne\varnothing\),
\[
\lim_{k\to\infty}k^{p/(p-2)}f(x^k)
=\frac1{p((p-2)\eta)^{p/(p-2)}}
\sum_{i\in S}a_i^{-2/(p-2)}.
\]
A coordinate extinguished at a finite step stays zero. The limits concern surviving coordinates only; finite termination is possible at exceptional initializations.

## Assumptions and scope

All iterates use exact arithmetic, exact gradients, no added stochastic noise, no momentum, and a fixed positive scalar stepsize. The norm in the kernel is Euclidean. The power \(p\) is any fixed real number strictly exceeding \(2\), so the kernel is differentiable and its gradient is globally invertible. The origin is the unique minimizer. The global convergence frontier quantifies over all starting vectors, all dimensions \(d\ge1\), and all strictly positive coefficients \(a_i\). The axis classification does not assert a formula for the full multidimensional basin at unstable stepsizes.

## Proof

Define \(H(r)=1+r^{p-2}\) for \(r\ge0\). Then \(\nabla\phi(x)=H(\|x\|_2)x\). Its radial modulus \(r\mapsto r+r^{p-1}\) is continuous and strictly increasing from zero to infinity. Hence \(\nabla\phi\) is a global homeomorphism, and the iteration is uniquely well-defined. For \(r=\|x\|_2\), let
\[
u_i=\bigl(H(r)-\eta a_i|x_i|^{p-2}\bigr)x_i,
\qquad x^+=(\nabla\phi)^{-1}(u).
\]
For \(x_i\ne0\) and \(0<\eta\le2/a_{\max}\),
\[
0<\eta a_i|x_i|^{p-2}
\le2r^{p-2}<2H(r),
\]
so \(\lvert H(r)-\eta a_i|x_i|^{p-2}\rvert<H(r)\). Summing squares gives \(\|u\|_2<H(r)r\) whenever \(x\ne0\). Monotonicity of the radial inverse implies \(\|x^+\|_2<r\). The radii therefore decrease to a limit. If that limit were positive, a convergent subsequence of directions together with continuity would contradict the strict inequality at its nonzero limit point. Hence all iterates converge to zero.

For a coordinate-axis iterate \(x=t e_i\), oddness and radial monotonicity reduce the update to
\[
\psi(t^+)=t+(1-m_i)|t|^{p-2}t,
\qquad\psi(t)=t+|t|^{p-2}t.
\]
For \(t\ne0\), the magnitude decreases exactly when
\[
m_i|t|^{p-2}<2(1+|t|^{p-2}).
\]
If \(m_i>2\), equality is precisely \(|t|=R_i\) and the update there is \(t^+=-t\). Below \(R_i\), magnitudes decrease and must approach zero; above it the update reverses sign, magnitudes strictly increase, and a finite nonzero limiting magnitude is impossible by continuity. Therefore they diverge. If \(m_i\le2\), the strict magnitude-decrease inequality holds at all finite nonzero \(t\), giving convergence. Since a maximum-weight coordinate satisfies \(\eta a_i>2\) whenever \(\eta>2/a_{\max}\), this also proves necessity of the global frontier.

For the rates, put \(y^k=\nabla\phi(x^k)=H(r_k)x^k\), where \(r_k=\|x^k\|_2\to0\). Each dual coordinate obeys the exact scalar recurrence with a *shared* radial factor,
\[
y_i^{k+1}=y_i^k
\left(1-\frac{\eta a_i|y_i^k|^{p-2}}{H(r_k)^{p-1}}\right).
\]
A zero dual coordinate remains zero, so the active set stabilizes after finitely many extinctions. For each surviving coordinate, \(y_i^k\to0\) and the multiplier eventually belongs to \((0,1)\), fixing the eventual sign. Let \(z_k=|y_i^k|>0\), \(q=p-2>0\), and \(c_k=\eta a_i/H(r_k)^{p-1}\to\eta a_i\). Then
\[
\frac1{z_{k+1}^{q}}-\frac1{z_k^{q}}
=z_k^{-q}\left((1-c_k z_k^q)^{-q}-1\right)
\longrightarrow q\eta a_i.
\]
Summation and division by \(k\) yield \(z_k^{-q}/k\to q\eta a_i\). Since \(x_i^k=y_i^k/H(r_k)\) and \(H(r_k)\to1\), the claimed coordinate limit follows. Taking the finite sum defining \(f\) gives the exact objective asymptotic constant.

## Verification

Execute `python3 verify.py` in a standard Python 3 environment; it uses only the standard library. The standalone checks include \(1,920\) radial contraction trials over powers \(3,4,5,6\), dimensions \(1,2,3,5\), randomly scaled positive weights and both interior and endpoint stepsizes; \(12\) exact axial frontier/termination cases; three long-run asymptotic coordinates; and four axial orbit classifications. All completed checks passed when the package was prepared. These numerical checks are finite corroborations; the proof above supplies the all-dimensional and real-exponent claims.

## Relationship to prior work

The Bregman-gradient update and radial polynomial kernel are established tools, not new definitions. Ding, Li and Toh (arXiv:2306.14522, initially public 2023-06-26) use a radial-power kernel, exhibit stepsize robustness and give general stochastic convergence analysis, but do not state this exact deterministic weighted-power global stability frontier, axial basin, or support-wise leading coefficient. Earlier relative-smoothness results of Lu, Freund and Nesterov (arXiv:1610.05708), Bolte and collaborators (arXiv:1706.06461), and quartic-kernel algorithms of Dragomir, d'Aspremont and Bolte (arXiv:1901.10791) address broad descent/complexity or low-rank problems rather than this sharp phase portrait. In particular, relative-smoothness sufficient-step guarantees cannot by themselves certify the necessity or axial divergence part of this theorem. The mathematical formulas here are self-contained, with independent publication-priority confirmation still needed.

## Limitations

No new stochastic convergence guarantee, noisy-gradient bound, momentum analysis, global rate for the unstable multidimensional basin, or wall-clock performance claim is asserted. The polynomial tail describes only surviving coordinates. The proof distinguishes strict decrease of Euclidean radius from any separate claim about objective monotonicity at every iterate. A specialized equivalent dynamical-systems treatment outside the inspected literature could exist.

## References

1. K. Ding, J. Li and K.-C. Toh, *Nonconvex Stochastic Bregman Proximal Gradient Method with Application to Deep Learning*, arXiv:2306.14522, first version 2023-06-26, https://arxiv.org/abs/2306.14522.
2. J. Bolte, S. Sabach, M. Teboulle and Y. Vaisbourd, *First Order Methods beyond Convexity and Lipschitz Gradient Continuity with Applications to Quadratic Inverse Problems*, arXiv:1706.06461, 2017-06-20, https://arxiv.org/abs/1706.06461.
3. R.-A. Dragomir, A. d'Aspremont and J. Bolte, *Quartic First-Order Methods for Low-Rank Minimization*, arXiv:1901.10791, 2019-01-30, https://arxiv.org/abs/1901.10791.
4. H. Lu, R. M. Freund and Y. Nesterov, *Relatively-Smooth Convex Optimization by First-Order Methods, and Applications*, arXiv:1610.05708, 2016-10-18, https://arxiv.org/abs/1610.05708.
