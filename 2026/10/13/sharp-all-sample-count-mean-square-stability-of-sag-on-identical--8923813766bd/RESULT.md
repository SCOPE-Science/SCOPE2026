# Sharp all-sample-count mean-square stability of SAG on identical SPD quadratics

## Finding

Let \(n\ge2\), \(d\ge1\), and let \(H\) be real symmetric positive definite. In the finite-sum problem with identical summands
\[
f_i(x)=\tfrac12(x-x_\star)^{\mathsf T}H(x-x_\star),\quad i=1,\ldots,n,
\]
consider stochastic average gradient (SAG) with a fixed \(\eta>0\), independent uniform indices \(J_k\in\{1,\ldots,n\}\), and arbitrary deterministic initial iterate \(x_0\) and gradient memory vectors \(y_i^0\). First refresh \(y_{J_k}^{k+1}=H(x_k-x_\star)\), leaving other memories unchanged; then set
\[
x_{k+1}=x_k-\frac{\eta}{n}\sum_{i=1}^n y_i^{k+1}.
\]

**Theorem.** Mean-square convergence \(\mathbb E\|x_k-x_\star\|^2\to0\) for *every* deterministic initialization is equivalent to
\[
\boxed{0<\eta\lambda_{\max}(H)<2.}
\]
In this regime every stored gradient converges to zero in mean square as well. At \(\eta\lambda_{\max}(H)=2\), no nonzero initial state confined to the top eigenspace can converge in mean square. Above that threshold, some deterministic initialization fails to converge. The admissible upper boundary is independent of the number of stored component gradients.

## Assumptions and scope

The index is sampled independently and uniformly **with replacement** each iteration. All component Hessians equal the same symmetric positive-definite matrix \(H\); the component minimizers coincide. All memory entries are refreshed **before** applying the average stored gradient. Stored initial gradients can be arbitrary real vectors, not just zero or consistent gradients. The claim concerns all-initialization mean-square convergence, not almost-sure divergence beyond the threshold or optimization with heterogeneous components.

## Proof

**1. Reduction to one eigenmode.** Orthogonally diagonalize \(H\). A scalar eigenmode of curvature \(\lambda>0\) evolves independently given the common sampled index. Let \(s=\eta\lambda\), let \(x\) denote the scalar translated iterate, and let \(b_i\) denote the corresponding stored gradient component divided by \(\lambda\). Define
\[
u=\frac1n\sum_i b_i,\qquad q=\frac1n\sum_i b_i^2.
\]
For one uniformly selected \(J\), put \(u'=u+(x-b_J)/n\), \(q'=q+(x^2-b_J^2)/n\), and \(x'=x-su'\). Direct conditioning gives
\[
\begin{aligned}
\mathbb E[u']&=\frac{x+(n-1)u}{n},\\
\mathbb E[(u')^2]&=\frac{x^2+2(n-1)xu}{n^2}+\frac{n-2}{n}u^2+\frac{q}{n^2},\\
\mathbb E[q']&=\frac{x^2+(n-1)q}{n}.
\end{aligned}
\]
All conditional expectations in the proof are given the current iterate and entire memory.

**2. Exact energy and its definiteness.** For \(0<s\le2\), define
\[
\begin{aligned}
V_{n,s}(x,b)={}&\left(n-1+\frac1s\right)x^2+(n-1)(s-2)xu\\
&+\frac{s(n-2)(2n-1)}2u^2+\frac{s(2n-1)}2q.
\end{aligned}
\]
Substitution of the three conditional identities and \(x'=x-su'\) yields the **exact polynomial identity**
\[
\boxed{\mathbb E[V_{n,s}(x',b')]-V_{n,s}(x,b)=(s-2)x^2.}\tag{1}
\]
To check strict positivity without relying on finite tests, write \(q=u^2+(q-u^2)\), with \(q-u^2=n^{-1}\sum_i(b_i-u)^2\ge0\). The coefficient of \(q-u^2\) is \(s(2n-1)/2>0\). The symmetric \((x,u)\)-quadratic has leading coefficient \(n-1+1/s>0\), second diagonal \(s(n-1)(2n-1)/2>0\), and determinant
\[
\frac{n-1}{4}\bigl[2+(n-1)s(4n+2-s)\bigr]>0
\]
for every \(n\ge2\) and \(0<s\le2\). Thus \(V_{n,s}\) is positive definite in the original \((n+1)\)-dimensional scalar memory-and-iterate state.

**3. Sufficiency and the endpoint.** For \(0<s<2\), take expectations in (1), sum from \(k=0\) to \(N\), and use \(V\ge0\):
\[
(2-s)\sum_{k=0}^N\mathbb E[x_k^2]\le V_{n,s}(x_0,b^0).
\]
The nonnegative summands are summable, so \(\mathbb E[x_k^2]\to0\). The memory recurrence
\[
\mathbb E[q_{k+1}]=\left(1-\frac1n\right)\mathbb E[q_k]+\frac1n\mathbb E[x_k^2]
\]
then implies \(\mathbb E[q_k]\to0\), and consequently the full memory vanishes in mean square. At \(s=2\), (1) instead conserves \(\mathbb E[V]\); if \(\mathbb E[x_k^2]\to0\), the same stable memory recurrence gives \(\mathbb E[q_k]\to0\), hence \(\mathbb E[V_k]\to0\), a contradiction for any nonzero deterministic initial state.

**4. Necessity above the endpoint.** For \(s>2\), the vector of scalar second moments \(m=(\mathbb E[x^2],\mathbb E[xu],\mathbb E[u^2],\mathbb E[q])^{\mathsf T}\) obeys \(m'=T_n(s)m\), where
\[
T_n(s)=\begin{pmatrix}
1-2s/n+s^2/n^2&-2s(n-1)/n+2s^2(n-1)/n^2&s^2(n-2)/n&s^2/n^2\\
1/n-s/n^2&(n-1)/n-2s(n-1)/n^2&-s(n-2)/n&-s/n^2\\
1/n^2&2(n-1)/n^2&(n-2)/n&1/n^2\\
1/n&0&0&(n-1)/n
\end{pmatrix}.
\]
Elementary determinant expansion gives
\[
\boxed{\det(I_4-T_n(s))=-\frac{2s(s-2)}{n^3}.}\tag{2}
\]
For \(s>2\), (2) is negative. Since \(\det(tI_4-T_n(s))\to+\infty\) as \(t\to+\infty\), continuity yields a real eigenvalue \(t>1\). The allowable deterministic initial moment vectors span \(\mathbb R^4\), witnessed by the states \((x;b)=(1;0,\ldots,0)\), \((0;1,\ldots,1)\), \((0;1,-1,0,\ldots,0)\), and \((1;1,\ldots,1)\). If every such deterministic initial state had \(\mathbb E[x_k^2]\to0\), the memory recurrence would imply \(\mathbb E[q_k]\to0\); then \(\mathbb E[u_k^2]\le\mathbb E[q_k]\) and Cauchy–Schwarz would imply \(\mathbb E[x_ku_k]\to0\). Every spanning column \(T_n(s)^k m_0\) would therefore tend to zero, contradicting an eigenvalue above one. This proves failure of the all-initialization assertion whenever \(s>2\).

**5. All matrix dimensions.** Each eigenmode has the scalar update just proved, with \(s_j=\eta\lambda_j(H)\); summing their expected squared errors proves sufficiency when all \(s_j<2\). Necessity follows by initializing only the top-eigenvalue mode. This completes both directions of the theorem.

## Verification

The companion `verify.py` independently constructs the conditional moment matrix symbolically; it checks (1), (2), the positive-definiteness minor, and exact rational conditional updates at several memory lengths and step sizes. The mathematical proof above holds for all integer \(n\ge2\), all real \(s>0\) in the stated regimes, and all matrix dimensions; finite checks supplement but do not replace it. To reproduce: install the version listed in `requirements.txt` and run `python verify.py`.

## Relationship to prior work

Le Roux, Schmidt and Bach first introduced SAG in their 2012 preprint; Schmidt, Le Roux and Bach later analyzed SAG for general convex finite sums, proving convergence with conservative uniform stepsizes rather than this sharp all-initialization threshold on identical positive-definite quadratics. Their published Mathematical Programming presentation has first MSC 90C06. Morin and Giselsson subsequently analyzed biased and unbiased variance-reduced methods using cocoercivity and provide general sufficient stepsize conditions; their theorems do not imply the present exact necessary-and-sufficient boundary with arbitrary initial memory and all \(n\). SAGA uses an unbiased correction absent from the SAG update and is not treated by this theorem. The present claim is deliberately confined to identical quadratic components; it is not an assertion that general SAG shares gradient descent's full allowable step interval.

## Limitations

No conclusion is established for nonidentical component Hessians, nonquadratic functions, nonuniform sampling, without-replacement sampling, stochastic additive gradient noise, or non-symmetric operators. The theorem is an exact mean-square all-initialization stability statement, not a sharp geometric rate formula. The literature search cannot exclude an equivalent historical result formulated in general linear random-systems language. The analysis has not undergone independent validation.

## References

1. N. Le Roux, M. Schmidt, F. Bach, *A Stochastic Gradient Method with an Exponential Convergence Rate for Finite Training Sets*, arXiv:1202.6258v1, first submitted 2012-02-28. https://arxiv.org/abs/1202.6258
2. M. Schmidt, N. Le Roux, F. Bach, *Minimizing Finite Sums with the Stochastic Average Gradient*, arXiv:1309.2388v1, first submitted 2013-09-10. https://arxiv.org/abs/1309.2388
3. M. Schmidt, N. Le Roux, F. Bach, *Minimizing Finite Sums with the Stochastic Average Gradient*, Mathematical Programming, DOI:10.1007/s10107-016-1030-6. Author-available full text: https://www.di.ens.fr/~fbach/sag_mathprog.pdf
4. M. Morin, P. Giselsson, *Cocoercivity, smoothness and bias in variance-reduced stochastic gradient methods*, Numerical Algorithms 91 (2022), 749–772, DOI:10.1007/s11075-022-01280-4. https://link.springer.com/article/10.1007/s11075-022-01280-4
