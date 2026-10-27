# Exponential inverse-stepsize moments amid vanishing loss for a stochastic oracle rule

## Finding

The ideal local-variance oracle stepsize can converge in expected objective value while the expectation of its reciprocal grows at least exponentially. This occurs for two uniformly sampled, strongly convex scalar quadratic losses, with no noisy estimation of the stepsize.

For \(f_{\xi}(x)=\tfrac12(x-\xi)^2\), where each fresh \(\xi\in\{-1,+1\}\) is equally likely, define \(F(x)=\mathbb E f_\xi(x)=\tfrac12(x^2+1)\), and apply the local signal-to-total-gradient-energy oracle step
\[
\alpha_n=\frac{|F'(x_n)|^2}{L\,\mathbb E_{\xi}|f'_{\xi}(x_n)|^2}=\frac{x_n^2}{1+x_n^2},\qquad
x_{n+1}=x_n-\alpha_n f'_{\xi_n}(x_n),\quad L=1.
\]
For every fixed \(x_0\in(0,1)\), all iterates satisfy \(0<x_n<1\), and for every integer \(n\ge0\)
\[
\mathbb E[F(x_n)-F(0)]=\tfrac12\mathbb E[x_n^2]
\le \frac{1}{2(n+x_0^{-2})}.
\]
Moreover \(x_n\to0\) almost surely. Nevertheless, for every real \(p>1\), there is an explicit \(D(x_0)\in(0,\infty)\) such that
\[
\liminf_{n\to\infty}2^{-(p-1)n}\mathbb E[\alpha_n^{-p/2}]
\ge D(x_0)^{-p}>0.
\]
In particular \(\mathbb E[1/\alpha_n]\) grows at least on the scale \(2^n\). This is a statement about inverse-gain moments, **not** about divergence of the optimizer or its objective value.

## Assumptions and scope

All operations are in exact real arithmetic. The observations \(\xi_0,\xi_1,\ldots\) are independent and each takes \(+1\) and \(-1\) with probability \(1/2\). The two component losses are as above, with unit curvature and unit-magnitude displacement of their minimizers. The initialization may be any deterministic \(x_0\in(0,1)\); no endpoint is included. The oracle step uses the *true* mean gradient and *true* current-sample second moment before the sample is drawn. It is equation (3.2) of the motivating preprint, not the estimated-and-safeguarded practical Algorithm 5.

The definition of the constant is as follows. Let \(y_0=x_0\) and \(y_{k+1}=y_k(1+y_k)/(1+y_k^2)\). Then
\[
D(x_0)=(1-x_0)\prod_{k=0}^{\infty}\frac{2}{1+y_k^2},
\]
and the proof below establishes that this product is finite and strictly positive.

## Proof

**Exact random maps.** With \(T_s(x)=x(1+s x)/(1+x^2)\), for \(s=\pm1\), the oracle recursion is \(x_{n+1}=T_{\xi_n}(x_n)\). For \(0<x<1\), \(0<T_-(x)<x<T_+(x)<1\): indeed
\[
T_+(x)-x=\frac{x^2(1-x)}{1+x^2}>0,
\qquad 1-T_+(x)=\frac{1-x}{1+x^2}>0.
\]
The analogous inequalities for \(T_-\) are immediate. Consequently each finite iterate belongs to \((0,1)\), and every inverse oracle step is well-defined.

**Expected objective and almost-sure convergence.** Conditional on \(x_n=x\),
\[
\mathbb E[x_{n+1}^2\mid x_n=x]
=\frac{x^2}{(1+x^2)^2}\frac{(1+x)^2+(1-x)^2}{2}
=\frac{x^2}{1+x^2}.
\]
Set \(m_n=\mathbb E[x_n^2]>0\). Concavity of \(t\mapsto t/(1+t)\) on \([0,\infty)\) implies
\[
m_{n+1}\le\frac{m_n}{1+m_n},
\qquad\frac1{m_{n+1}}\ge\frac1{m_n}+1,
\]
so \(m_n\le(n+x_0^{-2})^{-1}\). The bounded nonnegative process \(x_n^2\) is a supermartingale. It converges almost surely; dominated convergence and \(m_n\to0\) imply that its limit vanishes. Because \(x_n>0\), we obtain \(x_n\to0\) almost surely.

**A rare deterministic branch.** Consider a string of \(n-1\) consecutive \(+1\) observations followed by one \(-1\), an event \(E_n\) of probability \(2^{-n}\). Define \(y_k=T_+^k(x_0)\), \(\delta_k=1-y_k\). Then \(y_k\uparrow1\), and exactly
\[
\delta_{k+1}=\frac{\delta_k}{1+y_k^2}.
\]
Since \(y_k\ge x_0\), the bound \(\delta_k\le(1-x_0)(1+x_0^2)^{-k}\) shows that \(\sum_k\delta_k<\infty\). It follows from
\[
\frac{2\delta_{k+1}}{\delta_k}
=\frac{2}{1+y_k^2}
=1+\frac{1-y_k^2}{1+y_k^2}
\]
that the infinite product defining \(D(x_0)\) converges in \((0,\infty)\), because the nonnegative deviations of its factors from one are at most \(2\delta_k\) and thus summable. Therefore \(2^k\delta_k\to D(x_0)\).

On \(E_n\), the final update is
\[
x_n=T_-(y_{n-1})=\frac{y_{n-1}\delta_{n-1}}{1+y_{n-1}^2},
\qquad 2^n x_n\longrightarrow D(x_0).
\]
The last limit is *along the specified finite word as its length varies*; it is not a pathwise limit on a fixed probability-one event.

**Inverse-moment bound.** For any \(p>1\), restrict the expectation to \(E_n\):
\[
\mathbb E[\alpha_n^{-p/2}]
=\mathbb E[(1+x_n^{-2})^{p/2}]
\ge 2^{-n}\bigl(1+[T_-(y_{n-1})]^{-2}\bigr)^{p/2}.
\]
Multiplying by \(2^{-n(p-1)}\) and using \(2^n T_-(y_{n-1})\to D(x_0)\) gives the asserted positive lower limit. The \(p=2\) case is the reciprocal stepsize. No upper asymptotic for inverse moments or exact limiting constant for expected objective error is claimed.

## Verification

The included `verify_oracle.py` uses exact rational arithmetic to compare the stochastic update against the original oracle definition, exhaustively enumerate both choices through eight steps, and verify the conditional second-moment identity. It separately checks the rare-word endpoint and finite-product scaling at increasing lengths. Run with `python3 verify_oracle.py`; no nonstandard dependencies are needed. Its reported successful execution was:

`VERIFY_OK: 15 exact oracle recurrences; 8 complete rational binary trees; 20 rare-event endpoint tests; finite product scaling`

All infinite-horizon claims are established by the proof above, rather than by this finite computation.

## Relationship to prior work

Köhne, Kreis, Schiela and Herzog introduced the ideal local-variance step as equation (3.2) and prove an \(O(1/n)\) expected-objective upper bound in their Theorem 3.4. The expected-loss control in the present example is therefore a direct specialization and refinement of a known guarantee, **not** the originality claim. The additional inverse-moment behavior is not supplied by their discussion of gradient-energy estimates, their convergence theorem, or the practical estimated-and-safeguarded algorithm. The practical algorithm has different dynamics, and no inference about its reciprocal gains is made.

Gürbüzbalaban, Hu, Şimşekli and Zhu analyze heavy-tailed stationary iterates from exogenous constant, cyclic, iid or Markovian learning-rate schedules in least-squares SGD. Their Markovian scheduling assumptions and stationary iterate tails do not imply a lower bound for inverse moments of the **state-dependent** oracle rate on this nonstationary convergent recursion. This provides conceptual context, not a theorem being reproved.

## Limitations

This result is specific to the ideal true-moment oracle and a two-component scalar strongly convex model, without estimation, clipping, rejection, or preconditioning. The rare-event argument proves exponential *lower* growth of inverse-gain moments, not an exact asymptotic growth rate, not a heavy-tail stationary law, and not high-probability stagnation. The expected objective decreases to its optimum; the result does not suggest optimizer divergence. An equivalent statement may exist under different terminology; independent priority verification is outstanding.

## References

1. F. Köhne, L. Kreis, A. Schiela and R. Herzog, *Adaptive Step Sizes for Stochastic Gradient Descent in Hilbert Spaces*, arXiv:2311.16956, first submitted 28 November 2023, version 2 dated 18 September 2024. Equation (3.2), Theorem 3.4, Sections 4–5 and Appendix B. https://arxiv.org/abs/2311.16956
2. M. Gürbüzbalaban, Y. Hu, U. Şimşekli and L. Zhu, *Cyclic and Randomized Stepsizes Invoke Heavier Tails in SGD than Constant Stepsize*, arXiv:2302.05516, first submitted 10 February 2023, version 2 dated 29 August 2023. Sections 2–4 and Appendix B. https://arxiv.org/abs/2302.05516
