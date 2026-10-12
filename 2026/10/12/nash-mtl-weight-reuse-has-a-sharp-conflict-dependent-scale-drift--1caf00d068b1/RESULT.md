# Nash-MTL weight reuse has a sharp conflict-dependent scale-drift window
## Finding

Nash-MTL is designed to be invariant to task-gradient scale, and its defining algorithm recomputes the bargaining weights from the current gradients at every step. The same paper proposes a practical speedup that updates those weights only once every few iterations and reuses them between refreshes.

For two nonzero linearly independent gradients at a refresh, write
\[
g_1=a u_1,
\qquad
g_2=b u_2,
\]
where
\[
a,b>0,
\qquad
\lVert u_1\rVert_2=
\lVert u_2\rVert_2=1,
\]
and
\[
\rho=\langle u_1,u_2\rangle\in(-1,1).
\]

The source Nash equation is
\[
G^\top G\alpha=1/\alpha,
\qquad
\alpha_1,\alpha_2>0.
\]
For two tasks it has the exact solution
\[
\boxed{
\alpha_1=
\frac{1}{a\sqrt{1+\rho}},
\qquad
\alpha_2=
\frac{1}{b\sqrt{1+\rho}}
}.
\]
Therefore the fresh Nash direction is
\[
\boxed{
d_{\rm fresh}
=
\frac{u_1+u_2}{\sqrt{1+\rho}}
}
\]
up to an irrelevant common positive scale. In particular, changing either gradient magnitude while recomputing the Nash weights does not change the update direction.

Now keep the same directions and cosine but change the gradient magnitudes to
\[
g_1'=s_1a u_1,
\qquad
g_2'=s_2b u_2,
\qquad
s_1,s_2>0.
\]
If the old weights are reused, the direction becomes
\[
\boxed{
d_{\rm stale}
=
\frac{s_1u_1+s_2u_2}{\sqrt{1+\rho}}
}.
\]
If the Nash weights were recomputed instead, the direction would still be proportional to
\[
u_1+u_2.
\]
Thus relative magnitude drift alone is enough to destroy the exact independent scale invariance of the fresh two-task Nash direction.

The taskwise first-order improvements of the stale direction are
\[
\langle g_1',d_{\rm stale}\rangle
=
\frac{s_1a}{\sqrt{1+\rho}}
(s_1+\rho s_2)
\]
and
\[
\langle g_2',d_{\rm stale}\rangle
=
\frac{s_2b}{\sqrt{1+\rho}}
(s_2+\rho s_1).
\]

If
\[
\rho\ge0,
\]
both are strictly positive for every positive scale drift.

If
\[
-1<\rho<0,
\]
put
\[
q=\frac{s_1}{s_2}.
\]
Then the reused direction is strict common descent exactly when
\[
\boxed{
-\rho<q<-\frac1\rho
}.
\]
At
\[
q=-\rho
\]
task 1 is first-order neutral, and at
\[
q=-1/\rho
\]
task 2 is first-order neutral. Below the first threshold task 1 is harmed; above the second threshold task 2 is harmed.

Because the two endpoints are reciprocals, the same condition can be written as
\[
\boxed{
|\log q|<-\log(-\rho)
}.
\]
As
\[
\rho\to-1^+,
\]
the permissible log-scale drift tends to zero. For strongly conflicting tasks, even a modest change in their relative gradient magnitudes can therefore make reused Nash weights lose the non-conflicting property, despite the gradient directions themselves remaining unchanged.

For example, at
\[
\rho=-0.8,
\]
the exact safe interval is
\[
0.8<q<1.25.
\]
A relative magnitude change outside that narrow window makes one task increase to first order under the stale update, whereas a fresh Nash solve remains common descent.

## Assumptions and scope

The theorem is pointwise and concerns two linearly independent task gradients.

Between the weight refresh and the stale update, the unit gradient directions are assumed unchanged; only their magnitudes change. This deliberately isolates the effect of stale scale information from angular drift.

The claim uses the exact positive Nash equation from the defining paper. A common positive rescaling of all task weights or a later positive clipping of the aggregate norm does not change the direction or the taskwise sign conclusions.

The source practical speedup reuses task weights between refreshes. The theorem does not assert that every empirical reuse interval is harmful; it gives the exact condition under which pure relative magnitude drift is already sufficient to break common descent.

## Proof

The two-task Gram matrix is
\[
G^\top G
=
\begin{bmatrix}
a^2&ab\rho\\
ab\rho&b^2
\end{bmatrix}.
\]
The Nash equations are
\[
a^2\alpha_1+ab\rho\alpha_2
=
\frac1{\alpha_1}
\]
and
\[
ab\rho\alpha_1+b^2\alpha_2
=
\frac1{\alpha_2}.
\]
Multiplying the first by \(\alpha_1\), the second by \(\alpha_2\), and subtracting gives
\[
a^2\alpha_1^2=b^2\alpha_2^2.
\]
Positivity implies
\[
a\alpha_1=b\alpha_2.
\]
Let the common value be \(z\). Substitution into either equation gives
\[
z^2(1+\rho)=1,
\]
so
\[
z=(1+\rho)^{-1/2}.
\]
This proves the closed weights and fresh direction.

After the magnitudes change, reusing the same coefficients gives
\[
d_{\rm stale}
=
\alpha_1s_1a u_1+
\alpha_2s_2b u_2
=
\frac{s_1u_1+s_2u_2}{\sqrt{1+\rho}}.
\]
Recomputing the Nash weights with magnitudes \(s_1a\) and \(s_2b\) cancels those magnitudes again and restores the original bisector direction.

The two current task projections are the displayed formulas. Since all prefactors outside the parentheses are positive, their signs are determined by
\[
s_1+\rho s_2
\]
and
\[
s_2+\rho s_1.
\]
For nonnegative \(\rho\), both are positive.

For negative \(\rho\), divide by \(s_2>0\). The first condition is
\[
q> -\rho,
\]
and the second is
\[
1+\rho q>0,
\]
which is
\[
q<-1/\rho.
\]
Since \(-1<\rho<0\), one has
\[
0<-\rho<1<-1/\rho,
\]
so the interval is nonempty and the boundary and outside cases follow exactly.

Taking logarithms of the reciprocal endpoints gives the equivalent symmetric log-drift condition.

## Verification

The accompanying `verify.py` solves the exact two-task Nash equations, reconstructs fresh and stale directions, and checks the sharp sign transition over randomized norms, conflict angles, and scale ratios.

It separately checks both boundary cases and confirms that recomputing the Nash weights removes every pure magnitude change from the direction.

The computation is a transcription guard. The universal statements follow from the algebraic proof above.

## Relationship to prior work

Navon and coauthors define Nash-MTL by solving the current-gradient equation
\[
G^\top G\alpha=1/\alpha
\]
and explicitly motivate the method's invariance to individual gradient scale. Their standard algorithm recomputes the task gradients and weights at every iteration.

The same paper proposes a practical speedup that updates the gradient weights only once every few iterations and reuses them on intervening steps. It reports substantial runtime gains, while also noting that some settings show a noticeable performance drop. The inspected paper does not give a first-order safety condition for those reused weights.

A recent unified theory of multi-objective gradient aggregation identifies non-conflicting directions as a fundamental sufficient condition for convergence and reviews fresh Nash-MTL as a non-conflicting aggregator. Its Nash-MTL discussion still uses weights solved from the current Jacobian and does not analyze stale weight reuse.

Public Nash-MTL implementations expose `update_weights_every` and reuse the previous weight vector on non-refresh steps, matching the practical mechanism analyzed here.

Focused published-record searches for stale Nash-MTL weights, scale drift, two-task closed forms, common descent, and update-frequency guarantees did not identify the sharp interval
\[
-\rho<q<-1/\rho.
\]

## Limitations

The theorem isolates magnitude drift with fixed unit gradient directions. Angular drift can create additional failure modes and is not classified here.

Only two tasks are treated. With three or more tasks, the stale-weight common-descent region is a higher-dimensional cone in relative scale space.

The result is first-order. A taskwise positive gradient projection guarantees an infinitesimal descent direction but does not by itself specify a finite learning-rate guarantee.

No claim is made that less-frequent weight updates are empirically inferior overall; the source documents a substantial compute benefit from reuse.

## References

1. Aviv Navon, Aviv Shamsian, Idan Achituve, Haggai Maron, Kenji Kawaguchi, Gal Chechik, and Ethan Fetaya, “Multi-Task Learning as a Bargaining Game,” arXiv:2202.01017v1, first submitted 2022-02-02; ICML 2022.
2. Zeou Hu, Kelvin Ho, and Yaoliang Yu, “A Unified Framework for Gradient Aggregation in Multi-Objective Optimization,” arXiv:2605.30452v1, 2026.
3. LibMTL, public Nash-MTL implementation documentation and source.
