# Strict DFR and an exact moment sequence for the maximal exponential running average
## Finding
Let \(X_1,X_2,\ldots\) be independent exponential random variables with mean \(1\), define
\[
\overline X_n=\frac{X_1+\cdots+X_n}{n},
\qquad
Z_\infty=\sup_{n\ge1}\overline X_n,
\]
and let \(h\) denote the hazard rate of \(Z_\infty\) on its support \((1,\infty)\).

Then
\[
Z_\infty\stackrel d=\frac{E}{1-e^{-E}},
\qquad E\sim\operatorname{Exp}(1).
\]
If
\[
q=\Pr\{Z_\infty>x\}\in(0,1),
\]
then
\[
x=\frac{-\log q}{1-q}
\]
and
\[
h(x)=\frac{(1-q)^2}{1-q+q\log q}.
\]
The hazard is strictly decreasing on \((1,\infty)\), with
\[
\lim_{x\downarrow1}h(x)=2,
\qquad
\lim_{x\to\infty}h(x)=1.
\]
Hence the maximal running average has a strict decreasing-failure-rate law.

Moreover, for every integer \(m\ge1\),
\[
\mathbb E Z_\infty^m
=
m!\sum_{n=1}^{\infty}
\binom{m+n-2}{m-1}\frac{1}{n^{m+1}}.
\]
In particular,
\[
\mathbb E Z_\infty=\zeta(2)=\frac{\pi^2}{6},
\]
\[
\mathbb E Z_\infty^2=2\zeta(2)=\frac{\pi^2}{3},
\]
and
\[
\operatorname{Var}(Z_\infty)
=
\frac{\pi^2}{3}-\frac{\pi^4}{36}
=
\frac{\pi^2(12-\pi^2)}{36}.
\]

## Assumptions and scope
The parent variables are iid exponential with mean \(1\). The hazard statement concerns the absolutely continuous law of \(Z_\infty\) on \((1,\infty)\). The moment formula is asserted for positive integer orders only.

Affine rescaling of the parent variables gives corresponding rescalings of the result, but no claim is made here for nonexponential parents or for the later-start maximum \(\sup_{n\ge N}\overline X_n\) with \(N\ge2\).

## Proof
Cheliotis and Papadatos proved that the distribution function \(F_\infty\) of \(Z_\infty\) is one-to-one from \((1,\infty)\) onto \((0,1)\) and has inverse
\[
F_\infty^{-1}(u)=\frac{-\log(1-u)}{u},
\qquad 0<u<1.
\]
If \(E\sim\operatorname{Exp}(1)\), then \(U=1-e^{-E}\) is uniform on \((0,1)\). Therefore
\[
F_\infty^{-1}(U)
=
\frac{E}{1-e^{-E}},
\]
which gives the distributional representation.

For the hazard, write
\[
q=1-F_\infty(x).
\]
The inverse-CDF identity becomes
\[
x(q)=\frac{-\log q}{1-q}.
\]
Set
\[
D(q)=1-q+q\log q.
\]
Differentiation gives
\[
\frac{dx}{dq}
=
-\frac{D(q)}{q(1-q)^2}.
\]
Since the density satisfies \(f(x)=-dq/dx\), the hazard \(h(x)=f(x)/q\) is
\[
h(x)=\frac{(1-q)^2}{D(q)}.
\]

It remains to prove strict monotonicity. Direct differentiation yields
\[
\frac{dh}{dq}
=
\frac{(q-1)\bigl((q+1)\log q-2q+2\bigr)}
     {\bigl(1-q+q\log q\bigr)^2}.
\]
Put \(q=e^{-L}\) with \(L>0\). The second factor in the numerator is negative exactly when
\[
\phi(L):=L-2+e^{-L}(L+2)>0.
\]
Now
\[
\phi(0)=0,
\qquad
\phi'(L)=1-e^{-L}(L+1)>0
\]
for every \(L>0\), because \(e^L>1+L\). Hence \(dh/dq>0\). Since \(q\) is strictly decreasing in \(x\), \(h\) is strictly decreasing in \(x\). Taylor expansion at \(q=1\), or equivalently at \(L=0\), gives the left-endpoint limit \(2\); letting \(q\downarrow0\) gives the limit \(1\).

Finally, the transformed-exponential representation gives
\[
\mathbb E Z_\infty^m
=
\int_0^\infty
\frac{t^m e^{-t}}{(1-e^{-t})^m}\,dt.
\]
For integer \(m\ge1\),
\[
(1-e^{-t})^{-m}
=
\sum_{k=0}^{\infty}
\binom{m+k-1}{m-1}e^{-kt}.
\]
All terms are nonnegative, so monotone convergence justifies termwise integration. Using
\[
\int_0^\infty t^m e^{-nt}\,dt=\frac{m!}{n^{m+1}}
\]
and setting \(n=k+1\) gives the stated moment series. The displayed mean, second moment, and variance follow immediately.

## Verification
The accompanying `verify.py` checks the inverse-CDF transformation, the analytic hazard formula against numerical differentiation, strict hazard decrease on a dense deterministic grid, the endpoint limits numerically, and the first three moments against numerical quadrature and their zeta-series values.

The successful terminal line is:
`VERIFY_OK mean=1.644934066848226 variance=0.584060049418607 hazard_endpoints=(2,1)`.

The computations are regression checks only. The uniform hazard monotonicity and all-order moment identity are proved analytically above.

## Relationship to prior work
Cheliotis and Papadatos determined the exact distribution of the maximal exponential sample mean and, most importantly, proved the inverse-CDF formula
\[
F_\infty^{-1}(u)=\frac{-\log(1-u)}{u}.
\]
They use that formula for exact percentiles and a quality-control threshold, and they apply the distribution to a ruin-probability model. Their inspected paper does not state a hazard-rate classification, the transformed-exponential representation, or the all-order moment sequence above.

The present result extracts two structural consequences of that exact inverse law. The strict decreasing-failure-rate property is directly aligned with the source's risk/reliability interpretation, while the moment formula gives a complete sequence of exact quantitative summaries, including a simple zeta value for the mean and a closed variance.

Targeted searches for the source identifier together with `hazard`, `moment`, `zeta`, for the exact transformed-exponential representation, and for decreasing-failure-rate descriptions of this maximal average found no covering published statement. Candidate-specific published-record searches likewise returned no record on this object.

## Limitations
The source inverse-CDF theorem is the essential input; the new contribution is its structural hazard and moment consequences, not a new derivation of the distribution itself.

A targeted literature search cannot exclude an equivalent calculation in older reliability, queueing, or special-function literature under different terminology. The exact moment series is stated for integer orders; no analytic continuation in the order is claimed.

## References
1. D. Cheliotis and N. Papadatos, *On sequential maxima of exponential sample means, with an application to ruin probability*, arXiv:1906.09377v1, first public 2019-06-22, primary MSC 60E05.
