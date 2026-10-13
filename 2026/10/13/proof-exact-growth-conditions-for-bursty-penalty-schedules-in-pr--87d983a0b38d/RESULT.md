# Proof-exact growth conditions for bursty penalty schedules in proximal augmented Lagrangian methods
## Finding

Consider the growth function used by the proximal bounded augmented Lagrangian method of Adeoye--Latafat--Bemporad. The paper assumes
\[
\limsup_{k\to\infty}
\frac{\varphi(k+1)}{\varphi(k)}
<
\infty,
\qquad
\frac{k}{\varphi(k)}
\longrightarrow0.
\]

For the finite-\(\varepsilon\)-KKT proof of its proximal algorithm, the bounded-successive-ratio requirement can be replaced by the weaker pair
\[
\frac{k}{\varphi(k)}
\longrightarrow0,
\qquad
\frac{k\,\varphi(k+1)}{\varphi(k)^2}
\longrightarrow0.
\]

The two channels separate further. If different growth functions are used for the equality penalty, inequality penalty, and proximal parameter, as the paper explicitly permits, then the proof only needs

\[
\frac{k}{\varphi_\gamma(k)}
\longrightarrow0
\]
for the proximal-parameter channel, while each penalty channel \(q\in\{\rho,\nu\}\) only needs
\[
\frac{k}{\varphi_q(k)}
\longrightarrow0,
\qquad
\frac{k\,\varphi_q(k+1)}{\varphi_q(k)^2}
\longrightarrow0.
\]

These conditions allow schedules with unbounded one-step growth ratios.

For example, define a positive sequence by
\[
\varphi(k)=(k+1)^4
\]
for ordinary indices and
\[
\varphi(2^m+1)=(2^m+2)^5
\]
for integers \(m\ge1\). Then
\[
\frac{k}{\varphi(k)}\to0
\]
and
\[
\frac{k\,\varphi(k+1)}{\varphi(k)^2}\to0,
\]
but along \(k=2^m\),
\[
\frac{\varphi(k+1)}{\varphi(k)}
=
\frac{(k+2)^5}{(k+1)^4}
\sim k,
\]
so the published bounded-ratio condition fails.

Thus the proof supports rare aggressive penalty bursts that the stated Assumption II excludes.

## Assumptions and scope

The statement concerns the proof of finite-\(\varepsilon\)-KKT termination for the proximal bounded augmented Lagrangian method in arXiv:2509.02894v1.

All problem assumptions, the feasible initialization, the primal inexactness tolerance, multiplier updates, and penalty-update rules are unchanged. Only the asymptotic assumptions imposed on the positive growth functions are weakened.

The result is proof-exact in the following sense: every invocation of the source growth assumption in the multiplier, scaled-primal-residual, feasibility, complementarity, and subsequence arguments is implied by the displayed weaker limits.

The claim does not assert that these two limits are necessary for convergence of the algorithm itself. It identifies the exact asymptotic limits sufficient for the published argument.

## Proof

The source multiplier estimate gives, for a constant \(C>0\),
\[
\frac{1}{\gamma_k^2}
\|x^{k+1}-x^k\|^2
\le
\frac{C(k+1)+O(1)}{\gamma_k}.
\]
Since the update guarantees
\[
\gamma_k\ge \widehat\gamma\,\varphi_\gamma(k),
\]
the scaled primal residual vanishes whenever
\[
\frac{k}{\varphi_\gamma(k)}\to0.
\]
No quotient involving \(\varphi_\gamma(k+1)\) enters this estimate.

For the equality and inequality penalties, the source feasibility and complementarity estimates have the common form
\[
R_{k+1}^2
\le
C_1
\max\left\{
\frac{\xi}{\varphi(k)},
\frac{\varphi(k+1)}{\varphi(k)^2}
\right\}
A_{k+1}
+
C_2\frac{A_k}{\varphi(k)},
\]
where
\[
A_k=O(k).
\]
Hence the right-hand side tends to zero under
\[
\frac{k}{\varphi(k)}\to0
\]
and
\[
\frac{k\,\varphi(k+1)}{\varphi(k)^2}\to0.
\]
These are precisely the two asymptotic expressions appearing after multiplication by the linear-growth factor \(A_k\).

The remaining subsequence argument only propagates those already-vanishing feasibility and complementarity quantities through factors bounded by powers of the fixed contraction parameter \(\beta\in(0,1)\). It introduces no further condition on \(\varphi\).

The source assumption implies the weaker pair because
\[
\frac{k\,\varphi(k+1)}{\varphi(k)^2}
=
\left(
\frac{\varphi(k+1)}{\varphi(k)}
\right)
\left(
\frac{k}{\varphi(k)}
\right).
\]
A bounded first factor and a vanishing second factor make the product vanish.

The implication is strict. For the bursty example
\[
\varphi(k)=(k+1)^4
\]
except at \(k=2^m+1\), where
\[
\varphi(k)=(k+1)^5,
\]
one has
\[
\frac{k}{\varphi(k)}
\le
\frac{k}{(k+1)^4}
\to0.
\]

If \(k\) is not immediately before a spike, then
\[
\frac{k\,\varphi(k+1)}{\varphi(k)^2}
=
O(k^{-3})
\]
or smaller. At \(k=2^m\),
\[
\frac{k\,\varphi(k+1)}{\varphi(k)^2}
=
\frac{k(k+2)^5}{(k+1)^8}
=
O(k^{-2}).
\]
Immediately after a spike the denominator is even larger, so the same quantity tends to zero.

However, at \(k=2^m\),
\[
\frac{\varphi(k+1)}{\varphi(k)}
=
\frac{(k+2)^5}{(k+1)^4}
\sim k
\to\infty.
\]
Therefore the sequence is admitted by the proof-exact conditions and excluded by the published Assumption II.

Finally, suppose a baseline obeys
\[
\varphi(k)\asymp k^p,
\qquad
p>1.
\]
At an isolated burst index, the proof condition is
\[
k\,\varphi(k+1)=o(\varphi(k)^2),
\]
or equivalently
\[
\varphi(k+1)=o(k^{2p-1}).
\]
This gives the stated quadratic burst ceiling. A burst of exact order \(k^{2p-1}\) makes the corresponding proof term order one rather than vanishing, so the source bound alone no longer establishes feasibility or complementarity decay.

## Verification

The standalone script `artifacts/verify_growth_conditions.py` checks the explicit burst schedule at powers of two, verifies the unbounded successive ratio, and evaluates the two proof-exact quantities over large finite ranges.

The quantified proof is analytic. The computation is a consistency check rather than an exhaustive argument.

## Relationship to prior work

The primary paper introduces the growth function specifically to let penalty parameters grow more aggressively than standard linear schedules while limiting later ill-conditioning. It states a bounded-successive-ratio condition together with superlinear growth relative to \(k\), and it permits separate growth functions for the three parameter channels.

The proof itself uses the growth assumption in two distinct ways: the proximal channel only needs the reciprocal-growth term \(k/\varphi_\gamma(k)\), while the feasibility and complementarity estimates additionally contain the term \(k\varphi(k+1)/\varphi(k)^2\).

The inspected broader proximal augmented Lagrangian literature establishes convergence and complexity under different penalty-update frameworks. It does not state this proof-level replacement for the 2025 method or the admissible unbounded-ratio burst family above.

Targeted published-result searches using the source identifier, growth-function terminology, bounded-ratio terminology, penalty bursts, and the exact ratio
\[
\frac{k\,\varphi(k+1)}{\varphi(k)^2}
\]
did not locate an equivalent statement.

## Limitations

The weaker conditions are sufficient for the source proof, not claimed to be necessary for the algorithm itself.

Allowing a mathematically admissible burst does not imply that such a burst is numerically desirable. Very large penalties can still worsen conditioning, which is one of the motivations for the source update design.

The burst ceiling concerns isolated asymptotic growth relative to the current \(\varphi(k)\). More complicated adaptive schedules can be checked directly against the two displayed limits.

## References

1. A. D. Adeoye, P. Latafat, A. Bemporad, *A proximal augmented Lagrangian method for nonconvex optimization with equality and inequality constraints*, arXiv:2509.02894v1, first public 2 September 2025.
2. W. Kong, J. G. Melo, R. D. C. Monteiro, *Iteration Complexity of an Inner Accelerated Inexact Proximal Augmented Lagrangian Method Based on the Classical Lagrangian Function*, SIAM Journal on Optimization 33(1), 2023, DOI: 10.1137/20M136147X.
3. R. T. Rockafellar, *Augmented Lagrangians and Applications of the Proximal Point Algorithm in Convex Programming*, Mathematics of Operations Research 1(2), 1976, DOI: 10.1287/moor.1.2.97.
