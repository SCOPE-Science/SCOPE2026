# The DPham tail is lighter than every geometric tail
## Finding
For the discrete Pham (DPham) law with parameters
\[
\alpha>0,\qquad \mu>1,
\]
the published survival-function discretization gives
\[
\Pr(X\ge n)
=
\exp\!\left\{1-\mu^{n^\alpha}\right\},
\qquad n=0,1,2,\ldots .
\]
Equivalently,
\[
\Pr(X=n)
=
\exp\!\left\{1-\mu^{n^\alpha}\right\}
-
\exp\!\left\{1-\mu^{(n+1)^\alpha}\right\}.
\]

Its one-step tail ratio satisfies
\[
\frac{\Pr(X\ge n+1)}{\Pr(X\ge n)}
=
\exp\!\left[
-\left\{\mu^{(n+1)^\alpha}-\mu^{n^\alpha}\right\}
\right]
\longrightarrow0 .
\]
Consequently,
\[
e^{cn}\Pr(X\ge n)\longrightarrow0
\qquad\text{for every }c>0,
\]
and the discrete hazard
\[
h_n
=
\Pr(X=n\mid X\ge n)
=
1-\frac{\Pr(X\ge n+1)}{\Pr(X\ge n)}
\]
obeys
\[
h_n\longrightarrow1.
\]

Every positive exponential moment is finite:
\[
\mathbb E[e^{tX}]<\infty
\qquad\text{for every }t>0.
\]
Thus the DPham family is not heavy-tailed under the standard definition based on failure of all positive exponential moments. It is also not long-tailed in the usual discrete sense, because a long-tailed survival would require the one-step ratio to approach \(1\), whereas here it approaches \(0\).

The upper quantile has the exact integer representation
\[
Q(1-q)
=
\left\lceil
\left\{
\frac{\log[1+\log(1/q)]}{\log\mu}
\right\}^{1/\alpha}
\right\rceil-1
\]
away from the immaterial convention at exact jump points. Hence
\[
Q(1-q)
\sim
\left\{
\frac{\log\log(1/q)}{\log\mu}
\right\}^{1/\alpha}
\qquad(q\downarrow0).
\]

If \(M_m=\max(X_1,\ldots,X_m)\) for iid DPham variables and
\[
a_m=
\left\{
\frac{\log\log m}{\log\mu}
\right\}^{1/\alpha},
\]
then
\[
\frac{M_m}{a_m}\longrightarrow1
\qquad\text{in probability}.
\]
Thus the largest observation grows only on a power of the doubly logarithmic sample-size scale.

These statements qualify the source's claims that the model addresses heavy-tailed counts and can exhibit long-tailed persistence. Small \(\alpha\) or \(\mu\) close to \(1\) can produce substantial finite-range extremes, but no admissible parameter pair changes the asymptotic tail class.

## Assumptions and scope
The parameter domain is exactly the one used for the DPham model:
\[
\alpha>0,\qquad \mu>1.
\]
The survival convention is
\[
\Pr(X\ge n)=S_{\mathrm{Pham}}(n),
\]
which is the survival-function discretization used to obtain the published probability mass function.

“Heavy-tailed” means that the moment generating function is infinite for every positive argument, equivalently that the right tail is not exponentially bounded. “Long-tailed” for this lattice law means
\[
\frac{\Pr(X\ge n+1)}{\Pr(X\ge n)}\to1.
\]
The result concerns asymptotic tail class. It does not claim that the model cannot fit a finite dataset containing large observations, nor does it compare likelihood fit against the paper's competitors.

## Proof
Set
\[
L=\log\mu>0.
\]
First,
\[
\frac{\mu^{n^\alpha}}{n}
=
\exp\!\left\{L n^\alpha-\log n\right\}
\longrightarrow\infty,
\]
because \(n^\alpha\) dominates \(\log n\) for every \(\alpha>0\). Therefore, for any fixed \(c>0\),
\[
\log\!\left[e^{cn}\Pr(X\ge n)\right]
=
cn+1-\mu^{n^\alpha}
\longrightarrow-\infty,
\]
which proves that the survival is lighter than every geometric or exponential sequence.

For the adjacent-tail ratio, let
\[
f(x)=\mu^{x^\alpha}.
\]
By the mean-value theorem,
\[
f(n+1)-f(n)
=
\alpha L\,\xi_n^{\alpha-1}\mu^{\xi_n^\alpha}
\]
for some \(\xi_n\in(n,n+1)\). Taking logarithms,
\[
\log\!\left[
\alpha L\,\xi_n^{\alpha-1}\mu^{\xi_n^\alpha}
\right]
=
\log(\alpha L)
+
(\alpha-1)\log\xi_n
+
L\xi_n^\alpha
\longrightarrow\infty.
\]
Thus
\[
\mu^{(n+1)^\alpha}-\mu^{n^\alpha}\longrightarrow\infty,
\]
and the displayed tail ratio tends to zero. The hazard limit follows immediately.

For any \(t>0\),
\[
\Pr(X=n)\le\Pr(X\ge n)
=
\exp\!\left\{1-\mu^{n^\alpha}\right\}.
\]
Choose \(N\) so large that
\[
\mu^{n^\alpha}\ge2tn
\qquad(n\ge N).
\]
Then
\[
e^{tn}\Pr(X=n)
\le
e^{1-tn}
\qquad(n\ge N),
\]
and the right-hand side is summable. Hence
\[
\mathbb E[e^{tX}]<\infty
\]
for every \(t>0\).

For the quantile, \(F(n)\ge1-q\) is equivalent to
\[
\Pr(X>n)
=
\exp\!\left\{1-\mu^{(n+1)^\alpha}\right\}
\le q.
\]
Solving this inequality gives the displayed ceiling formula. Since the ceiling error is bounded while the threshold diverges, the asymptotic equivalent follows.

Finally, fix \(\varepsilon\in(0,1)\) and put
\[
n_-=(1-\varepsilon)a_m,
\qquad
n_+=(1+\varepsilon)a_m.
\]
Ignoring integer rounding, which is negligible relative to \(a_m\),
\[
\mu^{n_\pm^\alpha}
=
(\log m)^{(1\pm\varepsilon)^\alpha}.
\]
For the lower threshold,
\[
m\Pr(X\ge n_-)
=
\exp\!\left[
\log m+1-(\log m)^{(1-\varepsilon)^\alpha}
\right]
\longrightarrow\infty,
\]
so
\[
\Pr(M_m<n_-)
\le
\exp[-m\Pr(X\ge n_-)]
\longrightarrow0.
\]
For the upper threshold,
\[
\Pr(M_m\ge n_+)
\le
m\Pr(X\ge n_+)
\longrightarrow0,
\]
because \((1+\varepsilon)^\alpha>1\). This proves
\[
M_m/a_m\to1
\]
in probability.

## Verification
The accompanying checker evaluates the exact published survival and probability mass functions for several parameter pairs, including small \(\alpha\) and \(\mu\) close to \(1\).

It verifies numerically that the one-step survival ratio tends toward zero, that
\[
\mu^{(n+1)^\alpha}-\mu^{n^\alpha}
\]
grows without bound, and that positive-exponential summands eventually decay geometrically. It also checks the exact integer quantile formula against the published CDF and verifies the deterministic upper/lower maximum concentration bounds on logarithmic scale.

These finite calculations are consistency checks only. The tail classification, moment existence, quantile asymptotic, and maximum law are established analytically above.

## Relationship to prior work
Elshahhat, Abo-Kasem, and Mohammed introduce DPham by applying survival-function discretization to the continuous Pham law. Their abstract and introduction motivate the model using heavy-tailed counts and long-tailed persistence, while their Section 2 gives
\[
S_{\mathrm{Pham}}(y)
=
\exp\!\left\{1-\mu^{y^\alpha}\right\}
\]
and the resulting DPham mass function. Their order-statistic discussion further describes \(\alpha\) as a tail-thinning parameter. The paper does not state the asymptotic classification proved here.

Pham's continuous reliability law already has the same survival form before lattice discretization. Standard references on that model emphasize its V-tub-shaped hazard and reliability behavior, not a heavy-tail classification.

Djeumeni, Nadarajah, Engoulou, Fono, and Wansouwe study many mathematical properties of the continuous Pham distribution, including moment and extreme-value properties. The available abstract does not state the DPham lattice-tail ratio, all-positive-exponential-moment result, or the discrete maximum law. Its full text was not publicly accessible during this comparison, so it remains a residual source risk rather than being treated as not covering.

A standard heavy-tail definition classifies a nonnegative law as heavy-tailed when its moment generating function is infinite for every positive argument. The DPham result goes in the opposite direction: its moment generating function is finite for every positive argument.

## Limitations
The finding classifies asymptotic tails, not finite-range appearance. When \(\mu\) is close to \(1\) or \(\alpha\) is small, the onset of the asymptotic regime can be delayed, and finite samples can still contain numerically large counts.

No claim is made that tail-class terminology alone determines empirical model quality. The paper's goodness-of-fit comparisons and inference procedures are not reassessed here.

The closest broad continuous-Pham study was available only at abstract level during the literature comparison. A full-text statement there could reduce the originality of the continuous analogue, although it would not itself constitute a statement about the newly introduced DPham lattice law unless the discretization implication is made explicit.

## References
1. A. Elshahhat, O. E. Abo-Kasem, and H. S. Mohammed, “A new discrete Pham model for nonmonotone aging and overdispersion: theory, inference, optimization, and three scientific applications,” AIMS Mathematics 11 (2026), 9942–9988. DOI: 10.3934/math.2026411.
2. H. Pham, “A Vtub-shaped hazard rate function with applications to system safety,” International Journal of Reliability and Applications 3 (2002), 1–16.
3. L. Djeumeni, S. Nadarajah, B. M. Engoulou, L. A. Fono, and E. Wansouwe, “On the (Hoang) Pham Distribution,” International Journal of Reliability, Quality and Safety Engineering 33 (2026), 2550048. DOI: 10.1142/S0218539325500482.
4. B. Merz, B. Basso, G. Fischer, D. Lun, G. Blöschl, B. Merz, A. Guse, A. Viglione, S. Vorogushyn, and U. Wietzke, “Understanding heavy tails of flood peak distributions,” Water Resources Research 58 (2022), e2021WR030506. DOI: 10.1029/2021WR030506.
