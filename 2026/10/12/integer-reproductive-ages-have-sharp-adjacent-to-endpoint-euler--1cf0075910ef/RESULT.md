# Integer reproductive ages have sharp adjacent-to-endpoint Euler–Lotka growth bounds
## Finding
Consider a strict age-class population model whose survivorship-weighted reproductive contributions are
\[
p_L,p_{L+1},\ldots,p_U,
\qquad
1\le L<U,
\qquad
p_j\ge0.
\]
Define the net reproductive rate
\[
R_0=\sum_{j=L}^{U}p_j>0
\]
and normalize the reproductive schedule to a probability law
\[
q_j=\frac{p_j}{R_0}.
\]
Its mean age at reproduction is
\[
\mu=\sum_{j=L}^{U}j q_j.
\]

The finite growth factor \(\lambda>0\) is the unique Euler–Lotka solution
\[
\sum_{j=L}^{U}p_j\lambda^{-j}=1.
\]

Fix \(R_0\) and \(\mu\). If one reproductive-age law is a mean-preserving spread of another, then its Euler–Lotka growth factor is at least as large. More precisely, if
\[
A\le_{\mathrm{cx}} B
\]
in convex order and the two laws have the same mean, then
\[
\lambda_A\le\lambda_B.
\]
When \(R_0\ne1\), the inequality is strict for distinct finite laws.

This gives exact sharp lattice extremizers. Put
\[
k=\lfloor\mu\rfloor,
\qquad
\theta=\mu-k.
\]
The smallest possible growth factor is attained by the adjacent-age law
\[
q_{\min}=(1-\theta)\delta_k+\theta\delta_{k+1},
\]
with the obvious degeneration to \(\delta_\mu\) when \(\mu\) is an integer.

The largest possible growth factor is attained by the endpoint law
\[
q_{\max}
=
\frac{U-\mu}{U-L}\delta_L
+
\frac{\mu-L}{U-L}\delta_U.
\]
Thus every admissible integer-age schedule satisfies
\[
\lambda_{\min}\le\lambda\le\lambda_{\max}.
\]
For \(R_0\ne1\), equality at either end characterizes the corresponding extremal law.

The result strictly sharpens the usual Jensen lower benchmark when the observed mean age is not an integer. The continuous-age Jensen comparison gives
\[
\lambda\ge R_0^{1/\mu}.
\]
But if
\[
\mu\notin\mathbb Z
\]
and
\[
R_0\ne1,
\]
then a point mass at \(\mu\) is impossible on the integer age lattice, and
\[
\lambda_{\min}>R_0^{1/\mu}.
\]

For a concrete example, take
\[
R_0=2,
\qquad
L=1,
\qquad
U=4,
\qquad
\mu=\frac52.
\]
The minimum schedule places half the reproductive contribution at age \(2\) and half at age \(3\). Its growth factor is the positive root of
\[
\lambda^3-\lambda-1=0,
\]
namely
\[
1.3247<\lambda_{\min}<1.3248.
\]
The maximum schedule places half at age \(1\) and half at age \(4\). Its growth factor is the positive root of
\[
\lambda^4-\lambda^3-1=0,
\]
with
\[
1.3802<\lambda_{\max}<1.3803.
\]
The continuous Jensen benchmark is only
\[
2^{2/5}\approx1.31951.
\]

## Assumptions and scope
The reproductive-age variable takes positive integer values in a fixed finite interval \(\{L,\ldots,U\}\). This is the natural strict Leslie-matrix age-class setting.

The quantities \(p_j\) are expected reproductive contributions at age \(j\) after survival to that age has been incorporated. The theorem therefore acts directly on the Euler–Lotka contribution schedule; it does not separately constrain fecundity and survivorship components that multiply to \(p_j\).

Net reproductive rate \(R_0\) and mean reproductive age \(\mu\) are fixed. When \(R_0=1\), every admissible schedule has \(\lambda=1\), so the strict part of the theorem is intentionally restricted to \(R_0\ne1\).

Convex order is used in its standard mean-preserving-spread sense: \(A\le_{\mathrm{cx}}B\) means the two random ages have the same mean and
\[
\mathbb E[\phi(A)]\le\mathbb E[\phi(B)]
\]
for every convex \(\phi\) for which the expectations exist.

The result is deterministic. It does not address sampling error in estimated vital rates, environmental stochasticity, density dependence, or stage structure that cannot be reduced to a strict age schedule.

## Proof
Write \(A\) for the random reproductive age with law \(q\). Euler–Lotka becomes
\[
R_0\mathbb E[\lambda^{-A}]=1.
\]
For every fixed \(\lambda\ne1\), the function
\[
x\mapsto\lambda^{-x}
\]
is strictly convex, because its second derivative is
\[
(\log\lambda)^2\lambda^{-x}>0.
\]

Suppose \(A\le_{\mathrm{cx}}B\) and let \(\lambda_A\) solve Euler–Lotka for \(A\). If \(R_0\ne1\), then \(\lambda_A\ne1\), and strict convexity gives
\[
\mathbb E[\lambda_A^{-B}]
\ge
\mathbb E[\lambda_A^{-A}],
\]
with strict inequality for distinct finite laws. Therefore
\[
R_0\mathbb E[\lambda_A^{-B}]\ge1.
\]
For any positive-age law, the Euler–Lotka left side
\[
\lambda\mapsto R_0\mathbb E[\lambda^{-B}]
\]
is strictly decreasing on \((0,\infty)\). Hence the root for \(B\) satisfies
\[
\lambda_B\ge\lambda_A,
\]
and the inequality is strict for distinct laws. This proves convex-order monotonicity.

It remains to identify the extremal integer-age laws at fixed mean.

For the lower extremizer, let
\[
k=\lfloor\mu\rfloor,
\qquad
\theta=\mu-k.
\]
Given any convex function \(\phi\) on the real line, join the integer points
\[
(j,\phi(j))
\]
by straight line segments. The resulting piecewise-linear interpolation is convex. Jensen's inequality applied to that interpolation gives, for every integer-valued age \(A\) of mean \(\mu\),
\[
\mathbb E[\phi(A)]
\ge
(1-\theta)\phi(k)+\theta\phi(k+1).
\]
Therefore the adjacent-age law is below every admissible integer-age law in convex order.

For the upper extremizer, convexity puts every graph point below the chord joining the endpoints:
\[
\phi(j)
\le
\frac{U-j}{U-L}\phi(L)
+
\frac{j-L}{U-L}\phi(U).
\]
Taking expectations yields
\[
\mathbb E[\phi(A)]
\le
\frac{U-\mu}{U-L}\phi(L)
+
\frac{\mu-L}{U-L}\phi(U).
\]
Thus every admissible law is below the endpoint law in convex order.

Applying the first part of the theorem gives the claimed sharp growth interval. If \(\mu\) is noninteger, the adjacent-age law is a nondegenerate mean-preserving spread of a hypothetical continuous point mass at \(\mu\). Strict convexity therefore gives
\[
\lambda_{\min}>R_0^{1/\mu}
\]
whenever \(R_0\ne1\).

## Verification
The embedded `verify_euler_lotka_lattice_bounds.py` uses only the Python standard library and exact rational arithmetic.

It enumerates rational reproductive-age distributions on every integer support
\[
1\le L<U\le7
\]
with probability denominators through \(8\). For each distribution it computes its exact mean and verifies, at four rational values on both sides of \(1\), that
\[
\mathbb E_{q_{\min}}[z^A]
\le
\mathbb E_q[z^A]
\le
\mathbb E_{q_{\max}}[z^A].
\]
The replay performs \(76{,}416\) exact expectation comparisons and \(19{,}104\) strictness checks.

It also certifies the worked example by exact polynomial signs:
\[
1.3247<\lambda_{\min}<1.3248
\]
for \(\lambda^3-\lambda-1=0\), and
\[
1.3802<\lambda_{\max}<1.3803
\]
for \(\lambda^4-\lambda^3-1=0\).

The finite replay is a consistency check. The universal theorem is proved analytically above and does not rely on finite enumeration.

Run:

`python3 verify_euler_lotka_lattice_bounds.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Painter and Marr proved in 1967 that variability in cell interdivision times breaks the naive equality between mean interdivision time and population doubling time. Their result gives the classical strict Jensen-type inequality and a variance approximation for binary-fission growth.

Jonasson and coauthors give the modern strict-Leslie formulation most directly adjacent to the present theorem. They write Euler–Lotka as
\[
\sum_j p_j\lambda^{-j}=1,
\]
define
\[
R_0=\sum_jp_j
\]
and the mean reproductive age \(\mu\), and prove via Jensen's inequality the benchmark
\[
\lambda\ge R_0^{1/\mu}.
\]
Their theorem compares three generation-time definitions, not reproductive-age laws ordered by mean-preserving spread.

Cochran, Oancea and Pirjol derive moment bounds for the Euler–Lotka transform in epidemiology. Their work explicitly identifies the Jensen bound and uses constrained-moment extremal distributions; with a finite time window, this machinery is closely related to endpoint extremizers. That broader continuous moment theory is prior art and is not claimed as new here.

The new finite statement is the integer-age refinement: at fixed \(R_0\) and mean reproductive age, every mean-preserving spread raises \(\lambda\), the exact least-dispersed feasible age-class law is the adjacent pair around a noninteger mean, and this yields a strict lattice correction to the continuous Jensen benchmark. Targeted searches for integer-age, adjacent-age, convex-order, fixed-mean, and Euler–Lotka formulations did not locate this sharp lattice result.

## Limitations
The theorem conditions on \(R_0\), mean reproductive age, and an integer reproductive-age window. Different constraints, such as fixed variance or fixed stage-transition structure, lead to different extremal problems.

The endpoint maximum is consistent with general continuous constrained-moment theory; originality is not claimed for the generic fact that convex moment problems have finitely supported extremizers. The specific accepted contribution is the convex-order growth monotonicity together with the sharp adjacent-age lattice lower extremizer and its strict correction to the continuous Jensen bound.

The theorem does not estimate uncertainty in \(p_j\), \(R_0\), or \(\mu\). In empirical work those quantities are themselves estimated.

## References
1. P. R. Painter and A. G. Marr, “Inequality of Mean Interdivision Time and Doubling Time,” *Journal of General Microbiology* 48, 155–159, published 1 July 1967. DOI: 10.1099/00221287-48-1-155.
2. J. Jonasson, T. Härkönen, L. Sundqvist, S. V. Edwards and K. C. Harding, “A Unifying Framework for Estimating Generation Time in Age-Structured Populations: Implications for Phylogenetics and Conservation Biology,” *The American Naturalist* 200(1), 48–62, published 6 June 2022. DOI: 10.1086/719667.
3. J. Cochran, B. Oancea and D. Pirjol, “Bounding the generation time distribution uncertainty on R0 estimation from exponential growth rates,” *Journal of Biological Dynamics* 18(1), article 2410720, published online 16 October 2024. DOI: 10.1080/17513758.2024.2410720.
4. U. K. Steiner, S. Tuljapurkar and T. Coulson, “Generation Time, Net Reproductive Rate, and Growth in Stage-Age-Structured Populations,” *The American Naturalist* 183(6), 771–783, published online 21 April 2014. DOI: 10.1086/675894.
