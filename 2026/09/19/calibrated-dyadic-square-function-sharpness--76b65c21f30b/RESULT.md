# Exact calibration of the critical dyadic square-function sharpness example

## Statement

Let \(N\ge 2\), put \(A=2^N\), and let \((w_N,f_N)\) be the dyadic weight/function pair constructed in Section 2 of Adam Osękowski, *On the weighted weak-type constant for the dyadic square function*, arXiv:2609.14430v1. Let \(\alpha=\alpha_N\) be the positive solution of
\[
(2+A^{-2})\alpha^2-(1-A^{-2})\alpha-3A^{-1}=0.
\]
Define
\[
p_N=\frac{1-A^{-2}}{3},\qquad
\lambda_N=\frac{1+\alpha}{\alpha},\qquad
r_N=p_N\lambda_N,
\]
\[
y_N=\frac43A+\frac{2}{3A},\qquad
\gamma_N=\left(1+\frac{1}{A\alpha}\right)^{-1/2},
\]
and
\[
E_N=\frac{y_N^2}{A(A+\alpha)}.
\]

Then the example admits the following exact calibration.

**Theorem.**
1. Its dyadic \(A_2\) characteristic is
   \[
   \boxed{[w_N]_{A_2^d}=1+\frac{A}{\alpha_N}.}
   \]
2. Its weighted input norm is exactly
   \[
   \boxed{
   \|f_N\|_{L^2(w_N)}^2
   =
   E_N\frac{1-r_N^{A}}{1-r_N}
   +4r_N^{A}\alpha_N^{-1}\gamma_N.
   }
   \]
3. For every fixed \(0<\theta<3/8\),
   \[
   \boxed{
   \liminf_{N\to\infty}
   A^{-1}
   w_N\!\left(\{S^2f_N\ge \theta N A\}\right)
   \ge e^{-4}.
   }
   \]

Consequently,
\[
\alpha_N=\frac12+\frac{3}{A}+O(A^{-2}),\qquad
r_N=1-\frac4A+O(A^{-2}),
\]
and therefore
\[
[w_N]_{A_2^d}=2A+O(1),
\]
\[
\boxed{
\frac{\|f_N\|_{L^2(w_N)}^2}{A}
\longrightarrow
\frac49(1-e^{-4}).
}
\]

If
\[
\mathfrak C_{\rm dyad}
:=
\sup_{\substack{w\in A_2^d\\ f\ne0}}
\frac{\|Sf\|_{L^{2,\infty}(w)}}
{\|f\|_{L^2(w)}
\sqrt{[w]_{A_2^d}\log(1+[w]_{A_2^d})}},
\]
then
\[
\boxed{
\mathfrak C_{\rm dyad}
\ge
e^{-2}
\sqrt{\frac{27}{64(1-e^{-4})\log 2}}
=
0.1065624665\ldots .
}
\]

The final numerical bound is a lower bound for the best universal constant, not a claim that this constant is optimal.

## Context

For the dyadic square function \(S\), the critical weighted weak-\(L^2\) estimate has the form
\[
\|Sf\|_{L^{2,\infty}(w)}
\lesssim
\sqrt{[w]_{A_2^d}\log(1+[w]_{A_2^d})}\,
\|f\|_{L^2(w)}.
\]
The logarithmic factor was known from the work of Domingo-Salazar, Lacey and Rey. Osękowski's 2026 construction proves that the logarithm is necessary and gives the explicit lower constant \(e^{-2}/48\).

The source proof deliberately uses coarse bounds:
\[
\frac12\,2^N\le [w_N]_{A_2^d}\le 6\,2^N,
\qquad
\|f_N\|_{L^2(w_N)}^2\le 8\,2^N,
\]
and extracts only a fixed \(1/3\) fraction of the limiting square-function event. The theorem above keeps the exact state products, sums the iteration contributions exactly, and uses the full limiting concentration already proved in the source. This yields both exact structural formulas for the example and a substantially stronger explicit lower bound for the normalized critical constant.

## Proof

### 1. Exact \(A_2^d\) characteristic

The construction is a finite dyadic martingale in the pair of conditional averages
\[
(\langle w_N\rangle_I,\langle w_N^{-1}\rangle_I).
\]
Every repeated copy of the building block is obtained from the original one by a reciprocal rescaling
\[
(u,v)\mapsto (\lambda u,\lambda^{-1}v),
\]
which preserves the product \(uv\). The final terminal split has product \(1\). Hence it is enough to maximize the products among the states of the unscaled building block.

During Phase I the states have products
\[
P_n=
\left(
\frac13\,2^{N-n}
-\frac13\,2^{n-N}
+\alpha^{-1}
\right)(2^n+\alpha),
\qquad 0\le n\le N.
\]
At \(n=N\),
\[
P_N=\alpha^{-1}(A+\alpha)=1+\frac A\alpha.
\]

We show that \(P_n<P_N\) for \(n<N\). Put
\[
q=2^{N-n}\in(1,A].
\]
A direct simplification gives
\[
P_N-P_n
=
\frac{q-1}{q}
\left[
\frac A\alpha
-\frac{A(q+1)}{3q}
-\frac{\alpha(q+1)}3
\right].
\]
The bracket is positive exactly when
\[
h(q):=A+\frac Aq+\alpha q+\alpha
<
\frac{3A}{\alpha}.
\]
The function \(h\) is convex on \([1,A]\), so its maximum is attained at an endpoint. Since \(A\ge4\) and \(1/2<\alpha<1\),
\[
h(1)=2A+2\alpha<3A\le \frac{3A}{\alpha},
\]
and
\[
h(A)=(A+1)(1+\alpha)<2(A+1)<3A\le \frac{3A}{\alpha}.
\]
Thus the Phase-I maximum is \(P_N\).

During Phase II the products are
\[
Q_k=\alpha(2^k+\alpha^{-1})=1+\alpha2^k,
\qquad 0\le k\le N,
\]
so
\[
Q_k\le 1+\alpha A<1+\frac A\alpha=P_N.
\]
The state \(n=N\) occurs on a dyadic atom of positive probability, hence the supremum is attained and
\[
[w_N]_{A_2^d}=P_N=1+\frac A\alpha.
\]

### 2. Exact weighted \(L^2\) norm

In one unscaled building block, the source construction has
\[
\beta_N=\left(1+\frac{\alpha}{A}\right)^{-1/2}.
\]
On the ordinary terminal set \(uv=1\), the only nonzero terminal values of the third martingale coordinate are
\[
y_N(1-\beta_N),\qquad y_N(1+\beta_N),
\]
each with probability \(2^{-N-1}\), and the corresponding first coordinates are
\[
(1+\beta_N)\alpha^{-1},\qquad
(1-\beta_N)\alpha^{-1}.
\]
Therefore the exact weighted second-moment contribution of one terminating block is
\[
\begin{aligned}
E_N
&=
2^{-N-1}y_N^2\alpha^{-1}
\Big((1-\beta_N)^2(1+\beta_N)
 +(1+\beta_N)^2(1-\beta_N)\Big)\\
&=
2^{-N}y_N^2\alpha^{-1}(1-\beta_N^2)\\
&=
\frac{y_N^2}{A(A+\alpha)}.
\end{aligned}
\]

The exceptional probability of one block is
\[
p_N=\frac{1-A^{-2}}3,
\]
and each continuation rescales \(w\) by
\[
\lambda_N=\frac{1+\alpha}{\alpha}.
\]
Hence, if termination occurs after exactly \(k\) continuations, \(0\le k<A\), the weighted second-moment contribution is exactly
\[
r_N^kE_N,\qquad r_N=p_N\lambda_N.
\]
Summing these disjoint pieces gives
\[
E_N\sum_{k=0}^{A-1}r_N^k
=
E_N\frac{1-r_N^A}{1-r_N}.
\]

After \(A=2^N\) exceptional continuations, the source performs its final symmetric split. Its displayed terminal computation simplifies exactly to
\[
4r_N^A(A+\alpha^{-1})(1-\gamma_N^2)\gamma_N
=
4r_N^A\alpha^{-1}\gamma_N,
\]
because
\[
(A+\alpha^{-1})(1-\gamma_N^2)=\alpha^{-1}.
\]
Adding the two contributions proves the exact norm formula.

### 3. Asymptotics

Writing \(t=A^{-1}\), the defining equation for \(\alpha\) is
\[
(2+t^2)\alpha^2-(1-t^2)\alpha-3t=0.
\]
Expansion of its positive root gives
\[
\alpha=\frac12+3t+O(t^2).
\]
It follows that
\[
r_N
=
\frac{1-A^{-2}}3\frac{1+\alpha}{\alpha}
=
1-\frac4A+O(A^{-2}),
\]
so
\[
r_N^A\to e^{-4},
\qquad
A(1-r_N)\to4.
\]
Also
\[
E_N\to\frac{16}{9},
\qquad
\gamma_N\to1.
\]
The final-split term is \(O(1)\), while the geometric sum is of order \(A\). Hence
\[
\frac{\|f_N\|_{L^2(w_N)}^2}{A}
\to
\frac{16}{9}\cdot\frac{1-e^{-4}}4
=
\frac49(1-e^{-4}).
\]
The exact \(A_2^d\) formula similarly yields
\[
[w_N]_{A_2^d}=2A+O(1).
\]

### 4. Full limiting square-function event

On the set where all \(A=2^N\) building blocks are exceptional, Osękowski introduces independent random variables \(\xi_1,\ldots,\xi_A\) satisfying
\[
\mathbb P(\xi_j=4^{n-1})
=
\frac{3\,4^{-n}}{1-4^{-N}},
\qquad 1\le n\le N,
\]
and proves
\[
\eta_N:=\frac{\xi_1+\cdots+\xi_A}{NA}
\ \Longrightarrow\ \frac38.
\]
The same argument gives the pointwise lower bound of the truncated square function by \(\xi_1+\cdots+\xi_A\). Consequently, for every \(\theta<3/8\),
\[
\mathbb P\!\left(
\widetilde S^2f_N\ge \theta NA
\mid J_A
\right)\to1.
\]

Before the final split the \(w\)-average on \(J_A\) is
\[
(A+\alpha^{-1})\lambda_N^A,
\]
and
\[
\mathbb P(J_A)=p_N^A.
\]
Since the event above is measurable before the final split, martingale averaging across that split preserves its weighted mass. Thus
\[
\begin{aligned}
w_N\!\left(\{S^2f_N\ge\theta NA\}\right)
&\ge
(A+\alpha^{-1})r_N^A
\mathbb P(\eta_N\ge\theta).
\end{aligned}
\]
After division by \(A\), the right-hand side tends to \(e^{-4}\), proving the tail statement.

### 5. Lower bound for the normalized critical constant

For every \(\theta<3/8\),
\[
\|Sf_N\|_{L^{2,\infty}(w_N)}^2
\ge
\theta NA\,
w_N(\{S^2f_N\ge\theta NA\}).
\]
Using the preceding limits,
\[
\liminf_{N\to\infty}
\frac{\|Sf_N\|_{L^{2,\infty}(w_N)}^2}
{\|f_N\|_{L^2(w_N)}^2
[w_N]_{A_2^d}\log(1+[w_N]_{A_2^d})}
\ge
\frac{\theta e^{-4}}
{2\cdot \frac49(1-e^{-4})\log2}.
\]
Letting \(\theta\uparrow3/8\) gives
\[
\mathfrak C_{\rm dyad}^2
\ge
\frac{27e^{-4}}
{64(1-e^{-4})\log2},
\]
which is the claimed lower bound.

## Reproducibility

`artifacts/calibration_check.py` evaluates the exact formulas, checks numerically for a range of \(N\) that the stated Phase-I/Phase-II maximum equals \(1+2^N/\alpha_N\), and displays convergence of the normalized quantities. The script was executed successfully. It is a consistency check; the theorem is proved analytically above.

## Limitations

- The value \(0.1065624665\ldots\) is only a lower bound for the best universal normalized constant. No optimality of this numerical constant is claimed.
- The tail argument uses the limiting random-sum statement proved in arXiv:2609.14430v1; it does not identify the full distribution of the actual square function.
- The result calibrates the specific 2026 dyadic example. It does not improve the known order \(\sqrt{[w]_{A_2}\log(1+[w]_{A_2})}\), which was already proved sharp by the source.
- No continuous Littlewood-Paley analogue or nondyadic extremizer classification is asserted.

## References

1. A. Osękowski, *On the weighted weak-type constant for the dyadic square function*, arXiv:2609.14430v1 (2026), https://arxiv.org/abs/2609.14430.
2. C. Domingo-Salazar, M. T. Lacey, G. Rey, *Borderline weak-type estimates for singular integrals and square functions*, Bull. Lond. Math. Soc. 48 (2016), 63–73, https://doi.org/10.1112/blms/bdv090.
3. M. T. Lacey, J. Scurry, *Weighted weak-type estimates for square functions*, arXiv:1211.4219, https://arxiv.org/abs/1211.4219.
4. A. Osękowski, *Weighted weak-type inequalities for square functions*, Math. Inequal. Appl. 23 (2020), 267–286, https://doi.org/10.7153/mia-2020-23-21.
