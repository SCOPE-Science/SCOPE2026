# Finite-\(n\) phase boundary for the equal-mean Samuels extremizers
## Finding
Let \(n\ge 2\) and \(\delta>0\). Consider independent nonnegative random variables \(X_1,\ldots,X_n\) with \(\mathbb E X_i=1\). Ling's theorem resolving Samuels' conjecture gives the exact candidate family in the equal-mean case, and prior work reduces the minimum of that family to its two endpoints. Thus
\[
\inf \Pr\!\left\{\sum_{i=1}^n X_i<n+\delta\right\}
=
\min\left\{
\frac{\delta}{1+\delta},
\left(\frac{n+\delta-1}{n+\delta}\right)^n
\right\}.
\]
The new point is a complete finite-\(n\) description of where the sharp extremal mechanism changes. There is exactly one \(\delta_n>0\) satisfying
\[
\frac{\delta_n}{1+\delta_n}
=
\left(\frac{n+\delta_n-1}{n+\delta_n}\right)^n.
\]
For \(0<\delta<\delta_n\), the one-active-coordinate endpoint is the smaller sharp value. For \(\delta>\delta_n\), the all-active \(n\)-coordinate endpoint is the smaller sharp value. At \(\delta=\delta_n\), both endpoint constructions are sharp. Furthermore,
\[
\delta_n
=
\frac1{e-1}
+
\frac{e(3-e)}{2(e-1)^3}\frac1n
+O(n^{-2}).
\]
For example, \(\delta_2=(\sqrt5-1)/2\).

## Assumptions and scope
The statement is only for the equal-mean specialization \(\mathbb E X_i=1\) of the independent nonnegative-variable problem and thresholds \(n+\delta\). Scaling gives the analogous common-mean version. The result does not classify the unequal-mean Samuels candidates, prove uniqueness of probability laws attaining an endpoint, or supply a stability theorem near the transition.

The exact product formula is due to Ling, and the reduction of the equal-mean product candidates to the two endpoint expressions is prior context rather than a novelty claim here. The contribution isolated here is the unique finite-\(n\) switching point and its first explicit large-\(n\) correction.

## Proof
Write the two endpoint values as
\[
A(\delta)=\frac{\delta}{1+\delta},
\qquad
B_n(\delta)=\left(\frac{n+\delta-1}{n+\delta}\right)^n,
\]
and define their logarithmic ratio
\[
F_n(\delta)
=
\log\frac{\delta}{1+\delta}
-
n\log\frac{n+\delta-1}{n+\delta}.
\]
The switching points are exactly the positive zeros of \(F_n\). Differentiation gives
\[
F_n'(\delta)
=
\frac1{\delta(1+\delta)}
-
\frac{n}{(n+\delta-1)(n+\delta)}.
\]
After multiplication by the positive denominator \(\delta(1+\delta)(n+\delta-1)(n+\delta)\), the numerator factors as
\[
(n-1)(n+\delta-\delta^2).
\]
Hence \(F_n\) is strictly increasing up to the positive root of \(n+\delta-\delta^2=0\), and strictly decreasing afterwards. Also
\[
\lim_{\delta\downarrow0}F_n(\delta)=-\infty,
\qquad
F_n(1)>0,
\]
because
\[
\left(\frac n{n+1}\right)^n<\frac12
\]
for \(n\ge2\). Finally,
\[
F_n(\delta)=\frac{n-1}{\delta}+O(\delta^{-2})
\]
as \(\delta\to\infty\), so the decreasing tail approaches zero from above. Therefore \(F_n\) has exactly one positive zero \(\delta_n\); its sign is negative below that zero and positive above it. Since \(F_n=\log(A/B_n)\), this proves the phase classification.

For the large-\(n\) expansion, uniformly for \(\delta\) in a fixed compact interval,
\[
n\log\left(1-\frac1{n+\delta}\right)
=
-1+\frac{\delta-1/2}{n}
+
\frac{-\delta^2+\delta-1/3}{n^2}
+O(n^{-3}).
\]
The root equation is therefore
\[
\log\frac{\delta_n}{1+\delta_n}+1
=
\frac{\delta_n-1/2}{n}+O(n^{-2}).
\]
Let
\[
\delta_0=\frac1{e-1},
\qquad
g(\delta)=\log\frac{\delta}{1+\delta}+1.
\]
Then \(g(\delta_0)=0\) and
\[
g'(\delta_0)=\frac1{\delta_0(1+\delta_0)}>0.
\]
The displayed root equation first yields \(\delta_n-\delta_0=O(n^{-1})\). Taylor expansion at \(\delta_0\) then gives
\[
\delta_n-\delta_0
=
\frac{\delta_0(1+\delta_0)(\delta_0-1/2)}{n}
+O(n^{-2})
=
\frac{e(3-e)}{2(e-1)^3}\frac1n+O(n^{-2}).
\]
The coefficient is positive because \(e<3\).

For completeness, the endpoint reduction used as prior context can be reconstructed from
\[
f_\delta(x)=x\log\left(1-\frac1{x+\delta}\right),
\qquad x\ge1,
\]
whose second derivative is
\[
f_\delta''(x)
=
\frac{x(2\delta-1)+2\delta(\delta-1)}{(x+\delta)^2(x+\delta-1)^2}.
\]
Its curvature changes sign at most once, so \(f_\delta\) has no interior minimum on a finite integer interval; the minimum of the candidate values therefore lies at an endpoint. This reconstruction is included to make the argument self-contained, not as an originality claim.

## Verification
All differentiations and factorizations above are exact. The uniqueness proof uses only the sign pattern of \(F_n'\), the endpoint signs, and the positive asymptotic tail; no numerical root finder is part of the proof.

As consistency checks, the unique roots are approximately
\[
\delta_2=0.6180339887,
\quad
\delta_3=0.6063870476,
\quad
\delta_{10}=0.5894567691,
\quad
\delta_{100}=0.5827307718.
\]
The limiting value is
\[
\frac1{e-1}=0.5819767069\ldots,
\]
and the predicted coefficient is
\[
\frac{e(3-e)}{2(e-1)^3}=0.07547378935\ldots.
\]
These numerical values only check the analytic formulas.

## Relationship to prior work
Ling's 2026 theorem gives the sharp product formula for Samuels' conjecture, and its equal-mean specialization produces the candidate family underlying the two displayed endpoint mechanisms. Paulin's 2017 paper already records the one-active and diffuse sharp examples and the familiar \(1/(e-1)\)-scale breakpoint used in bounds for Feige's conjecture. A later reformulation by Han gives another proof framework for Ling's theorem.

The endpoint reduction is therefore treated here as prior context. The inspected sources do not state the unique finite-\(n\) equality point between those two endpoint mechanisms, its exact sign classification for every \(n\ge2\), or the explicit first correction
\[
\frac{e(3-e)}{2(e-1)^3}\frac1n.
\]
Focused searches using Samuels/Feige terminology, equal means, endpoint extremizers, and the \(1/(e-1)\) breakpoint did not locate an implication-equivalent published statement. This is evidence of noncoverage, not a proof that no differently named older formulation exists.

## Limitations
The result is a refinement of the equal-mean sharp formula, not a new proof of Samuels' conjecture. It does not establish monotonicity of \(\delta_n\) in \(n\), a second-order coefficient, unequal-mean phase diagrams, or stability/near-extremizer structure. Older literature using different notation for the endpoint crossing remains the principal originality risk.

## References
1. Z. Ling, *On Samuels' Conjecture*, arXiv:2608.18392v1, first public 2026-08-18.
2. R. Paulin, *On some conjectures of Samuels and Feige*, arXiv:1703.05152v1, 2017.
3. Y. Han, *A Cap-Move Reformulation of Ling's Proof of Samuels' Conjecture*, arXiv:2608.22816v1, 2026.
