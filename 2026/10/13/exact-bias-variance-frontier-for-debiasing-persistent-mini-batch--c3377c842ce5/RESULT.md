# Exact bias-variance frontier for debiasing persistent mini-batch gradients
## Finding

Fix an iterate of a finite-sum problem and regard the component gradients at that iterate as deterministic vectors
\[
g_1,\ldots,g_N.
\]
Let \(R\) be a persistent set of size \(r\ge1\), let
\[
C=\{1,\ldots,N\}\setminus R
\]
have size
\[
M=N-r,
\]
and draw a fresh subset \(S\subset C\) uniformly without replacement with size \(s\ge1\). Assume
\[
B=r+s<N.
\]

Write
\[
a=\frac1r\sum_{i\in R}g_i,
\qquad
b=\frac1M\sum_{i\in C}g_i,
\qquad
g=\frac{ra+Mb}{N}.
\]
For the complement dispersion define
\[
V=\frac1M\sum_{i\in C}\|g_i-b\|^2
\]
and
\[
\sigma^2=
\frac{M-s}{s(M-1)}V.
\]

The practical persistent estimator is
\[
U=\frac{ra+s\bar g_S}{B},
\qquad
\bar g_S=\frac1s\sum_{i\in S}g_i.
\]
The unbiased correction proposed in the primary source is
\[
C=\frac{ra+M\bar g_S}{N}.
\]

Introduce
\[
q=\frac{s}{B},
\qquad
p=\frac{M}{N},
\qquad
D=p-q=\frac{r(N-B)}{BN}>0.
\]
Then
\[
\mathbb E[U]-g=D(a-b),
\qquad
\mathbb E[C]=g,
\]
while their conditional sampling variances are
\[
\mathbb E\|U-\mathbb E U\|^2=q^2\sigma^2
\]
and
\[
\mathbb E\|C-g\|^2=p^2\sigma^2.
\]

Thus full debiasing increases the conditional sampling variance by the exact factor
\[
\frac{\operatorname{Var}(C)}{\operatorname{Var}(U)}
=
\left(\frac pq\right)^2
=
\left(\frac{B(N-r)}{Ns}\right)^2
\]
whenever \(V>0\).

More generally, consider the partial-debiasing family
\[
G_t=(1-t)U+tC,
\qquad
0\le t\le1.
\]
Writing
\[
\Delta=\|a-b\|,
\]
its exact conditional mean-squared error relative to the full gradient is
\[
\operatorname{MSE}(t)
=
\mathbb E\|G_t-g\|^2
=
(1-t)^2D^2\Delta^2
+
(q+tD)^2\sigma^2.
\]

If \(\sigma^2>0\), the unique minimizer on \([0,1]\) is
\[
t_*=
\begin{cases}
0,
&
D\Delta^2\le q\sigma^2,
\\[2mm]
\dfrac{D\Delta^2-q\sigma^2}
{D(\Delta^2+\sigma^2)},
&
D\Delta^2>q\sigma^2.
\end{cases}
\]
In particular,
\[
t_*<1
\]
whenever the fresh complement has nonzero sampling variance. Hence the fully unbiased endpoint is never MSE-optimal under that condition.

The fully corrected estimator has smaller MSE than the uncorrected one exactly when
\[
\Delta^2
>
\frac{p+q}{D}\sigma^2.
\]

For \(50\%\) overlap,
\[
r=s=\frac B2.
\]
Then
\[
\frac{\operatorname{Var}(C)}
{\operatorname{Var}(U)}
=
(2-B/N)^2,
\]
which approaches \(4\) when the batch fraction tends to zero. In the same case, full correction beats no correction exactly when
\[
\Delta^2
>
\frac{2(3N-B)}
{B(N-B/2-1)}V.
\]

This gives an exact bias-variance frontier between the practical biased estimator and the source's convergence-oriented unbiased estimator.

## Assumptions and scope

The result is conditional on one fixed iterate. The vectors \(g_i\) are the component gradients evaluated at that iterate, and the only randomness is the source sampling rule: the persistent set \(R\) is fixed while \(S\) is sampled uniformly without replacement from its complement.

The condition
\[
B<N
\]
ensures that the fresh set is a proper subset of the complement, so
\[
M>s
\]
and \(D>0\).

The statement measures Euclidean mean-squared error of the gradient estimator. It does not assert that minimizing one-step gradient MSE optimizes training loss, line-search acceptance probability, or total algorithmic complexity.

For \(t<1\), the estimator is biased unless \(a=b\). Therefore the primary source's convergence proof, which explicitly assumes conditional unbiasedness, does not automatically apply to the MSE-optimal partial correction.

## Proof

Let
\[
d_i=g_i-b,
\qquad i\in C.
\]
Then
\[
\sum_{i\in C}d_i=0.
\]
For a uniformly sampled subset \(S\) of size \(s\),
\[
\mathbb P(i\in S)=\frac{s}{M},
\qquad
\mathbb P(i,j\in S)
=
\frac{s(s-1)}{M(M-1)}
\]
for distinct \(i,j\in C\).

Since
\[
2\sum_{i<j}d_i^{\mathsf T}d_j
=
-\sum_i\|d_i\|^2,
\]
one obtains
\[
\mathbb E
\left\|
\sum_{i\in S}d_i
\right\|^2
=
\frac{s(M-s)}{M-1}V.
\]
Dividing by \(s^2\) gives
\[
\mathbb E\|\bar g_S-b\|^2
=
\frac{M-s}{s(M-1)}V
=
\sigma^2.
\]

The expectations are
\[
\mathbb E[U]
=
\frac rB a+\frac sB b
\]
and
\[
\mathbb E[C]
=
\frac rN a+\frac MN b
=
g.
\]
Subtracting \(g\) from the first expression gives
\[
\mathbb E[U]-g
=
\left(
\frac rB-\frac rN
\right)(a-b)
=
D(a-b).
\]

The centered stochastic parts are
\[
U-\mathbb E[U]
=
q(\bar g_S-b)
\]
and
\[
C-g
=
p(\bar g_S-b).
\]
The two variance formulas and their ratio follow immediately.

For
\[
G_t=(1-t)U+tC,
\]
the bias is
\[
\mathbb E[G_t]-g
=
(1-t)D(a-b),
\]
and the centered random part is
\[
G_t-\mathbb E[G_t]
=
(q+tD)(\bar g_S-b).
\]
Because the centered random part has mean zero, the bias and variance contributions are orthogonal in expectation, yielding
\[
\operatorname{MSE}(t)
=
(1-t)^2D^2\Delta^2
+
(q+tD)^2\sigma^2.
\]

Differentiating gives
\[
\frac12\operatorname{MSE}'(t)
=
-(1-t)D^2\Delta^2
+
D(q+tD)\sigma^2.
\]
The unconstrained stationary point is
\[
\frac{D\Delta^2-q\sigma^2}
{D(\Delta^2+\sigma^2)}.
\]
If its numerator is nonpositive, convexity places the constrained minimizer at \(t=0\). If its numerator is positive and \(\sigma^2>0\), the stationary point lies strictly between zero and one, giving the displayed formula. Since
\[
\frac12\operatorname{MSE}'(1)
=
Dp\sigma^2>0,
\]
the endpoint \(t=1\) cannot minimize MSE when \(\sigma^2>0\).

Finally,
\[
\operatorname{MSE}(0)
=
D^2\Delta^2+q^2\sigma^2,
\qquad
\operatorname{MSE}(1)
=
p^2\sigma^2.
\]
Thus full correction is better exactly when
\[
D^2\Delta^2
>
(p^2-q^2)\sigma^2
=
D(p+q)\sigma^2,
\]
which is the claimed threshold.

For
\[
r=s=B/2,
\]
substitution yields
\[
p=1-\frac{B}{2N},
\qquad
q=\frac12,
\qquad
D=\frac{N-B}{2N}.
\]
This gives the stated \(50\%\)-overlap formulas.

## Verification

The standalone script `artifacts/verify_persistent_debiasing.py` exhaustively enumerates all fresh subsets for a rational vector population and checks the expectation, variance, MSE, oracle interpolation parameter, and \(50\%\)-overlap variance factor using exact rational arithmetic.

The proof is finite-population algebra and does not rely on the numerical instance. The script is supporting evidence only.

## Relationship to prior work

The primary source introduces mini-batch persistency to make momentum directions more compatible with stochastic line searches. It observes that fixing persistent samples biases the ordinary batch gradient and gives a reweighted conditionally unbiased estimator in Proposition 5.1.

The same source explicitly reports that this correction substantially weakens the intended effect of persistency and performs worse computationally, and it leaves analysis of the biased estimator as future work. The result above quantifies one precise mechanism behind that observation: unbiased reweighting amplifies the fresh-sample variance, and partial reweighting gives an exact conditional MSE compromise.

Horvitz--Thompson sampling theory provides the general inverse-probability principle behind unbiased finite-population estimation. Mini-batch variance has also been studied in stochastic-gradient optimization. Those broader results do not state the source-specific variance inflation factor, the persistent-versus-complement contrast threshold, or the exact partial-debiasing optimizer derived here.

Targeted searches using the primary identifier, data-persistency terminology, unbiased-correction terminology, overlap, variance inflation, Horvitz--Thompson language, and partial debiasing did not locate an equivalent statement for this persistent stochastic-line-search estimator.

## Limitations

The result concerns estimator MSE at one iterate, not convergence of the complete MBCG-DP method.

The oracle value \(t_*\) depends on the unknown contrast
\[
\Delta=\|a-b\|
\]
and complement dispersion \(V\). Estimating those quantities cheaply without defeating the purpose of mini-batching is a separate algorithm-design problem.

A lower one-step gradient MSE need not imply a lower optimization error or better line-search behavior.

The source convergence proof uses conditional unbiasedness, so any choice \(t<1\) generally requires a new convergence analysis.

## References

1. M. Lapucci, D. Pucci, *Effectively Leveraging Momentum Terms in Stochastic Line Search Frameworks for Fast Optimization of Finite-Sum Problems*, arXiv:2411.07102v1, first public 11 November 2024; later published in *Computational Optimization and Applications* 94, 543--569, 2026, DOI: 10.1007/s10589-026-00776-2.
2. D. G. Horvitz, D. J. Thompson, *A Generalization of Sampling Without Replacement from a Finite Universe*, *Journal of the American Statistical Association* 47(260), 663--685, 1952, DOI: 10.1080/01621459.1952.10483446.
3. X. Qian, D. Klabjan, *The Impact of the Mini-batch Size on the Variance of Gradients in Stochastic Gradient Descent*, arXiv:2004.13146v1, first public 27 April 2020.
