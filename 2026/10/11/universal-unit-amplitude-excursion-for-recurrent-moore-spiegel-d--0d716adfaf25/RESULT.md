# Universal unit-amplitude excursion for recurrent Moore–Spiegel dynamics
## Finding
Consider the Moore–Spiegel oscillator
\[
\dot x=y,\qquad \dot y=z,\qquad \dot z=-z-(T-R+Rx^2)y-Tx,
\]
with \(T>0\) and \(R>0\). For every compactly supported invariant probability measure \(\mu\),
\[
\int z^2\,d\mu\ge T\int y^2\,d\mu,
\qquad
\int x^2y^2\,d\mu\ge\int y^2\,d\mu.
\]
Equality in either inequality occurs exactly for \(\mu=\delta_0\). Therefore every non-origin compact stationary state satisfies both inequalities strictly and
\[
\mu(\{(x,y,z): |x|>1,\ y\ne0\})>0.
\]
Thus every nontrivial compact recurrent statistical state in the physical quadrant \(T,R>0\) must make a genuine excursion beyond the parameter-independent unit-amplitude barrier.

## Assumptions and scope
The result concerns compactly supported invariant Borel probability measures of the displayed smooth flow. The parameters satisfy \(T>0\) and \(R>0\). It applies to invariant measures carried by periodic or chaotic compact sets as well as their mixtures. It does not assert existence of nontrivial recurrent dynamics for every parameter pair.

The first public source date used for the record is 1997-12-01, the day-resolved publication date verified for Balmforth and Craster's full-text study. The original Moore–Spiegel model is older, but the historical source located here was not used to invent a day-level date. The primary classification \(34C28\) is independently supported by bibliographic metadata for later work on the generalized Moore–Spiegel equations.

## Proof
For a compact invariant probability measure, the average Lie derivative of every polynomial vanishes. Earlier work on this same system established the exact balances
\[
\int y^2\,d\mu=T\int x^2\,d\mu
\]
and
\[
\int z^2\,d\mu+(R-T)\int y^2\,d\mu=R\int x^2y^2\,d\mu.
\]
Independently, applying invariance to \(xy\) gives
\[
0=\int L(xy)\,d\mu=\int(y^2+xz)\,d\mu,
\]
so
\[
\int xz\,d\mu=-\int y^2\,d\mu=-T\int x^2\,d\mu.
\]
If \(\int x^2\,d\mu=0\), invariance forces \(x=y=z=0\) almost surely and \(\mu=\delta_0\). Otherwise Cauchy–Schwarz yields
\[
\left(\int xz\,d\mu\right)^2\le\left(\int x^2\,d\mu\right)\left(\int z^2\,d\mu\right),
\]
which, after cancellation, gives
\[
\int z^2\,d\mu\ge T^2\int x^2\,d\mu=T\int y^2\,d\mu.
\]
Substitution into the second balance and division by \(R>0\) gives
\[
\int x^2y^2\,d\mu\ge\int y^2\,d\mu.
\]

It remains to identify equality. Equality in Cauchy–Schwarz forces \(z=-Tx\) almost surely. The support of an invariant measure is invariant, so the constraint \(q=z+Tx=0\) must be tangent to the vector field on the support. Direct differentiation gives, on \(q=0\),
\[
\dot q=R(1-x^2)y.
\]
Hence the support lies where \((1-x^2)y=0\). A trajectory that remains on \(x=1\) or \(x=-1\) must have \(y=0\), while \(y=0\) together with \(z=-Tx\) and \(\dot y=z=0\) forces \(x=z=0\). Thus equality implies the origin atom. Conversely the origin atom attains equality. The second inequality has the same equality condition because its defect is exactly the first defect divided by \(R\).

For every non-origin invariant measure,
\[
\int (x^2-1)y^2\,d\mu>0.
\]
Its positive part is supported in \(\{{|x|>1,\ y\ne0}\}\), so that set has positive \(\mu\)-measure.

## Verification
The accompanying `verify.py` symbolically differentiates the two balance generators, checks \(L(xy)=y^2+xz\), and checks the tangency identity \(L(z+Tx)=R(1-x^2)y\) on \(z=-Tx\). Running the actual packaged file produced `VERIFY_OK`, recorded in `verification_output.txt`.

The strictness argument is analytic rather than experimental: the only equality case permitted by Cauchy–Schwarz and invariance is the origin atom. No finite trajectory sample is used to infer an infinite-time statement.

## Relationship to prior work
Balmforth and Craster study exactly the displayed Moore–Spiegel equations in the physical regime \(T>0\), \(R>0\), including periodic, aperiodic, bifurcation, and periodic-orbit behavior. Their inspected full text does not state an invariant-measure unit-amplitude excursion law. Later generalized-system work studies topology and parity of chaotic solutions rather than this moment inequality.

The closest published finding is “Exact recurrence balances and a strict period floor for the Moore--Spiegel oscillator” (2026-09-20). It supplies the two balance laws used above and, only when \(R>T>0\), deduces the weaker support threshold \(|x|>\sqrt{1-T/R}\). The present claim is not implied by that threshold: it gives the strictly stronger parameter-independent barrier \(|x|>1\), applies throughout the full quadrant \(T,R>0\), and identifies the exact Cauchy–Schwarz rigidity mechanism. Targeted searches for the unit barrier, the weighted moment inequality, and equivalent stationary formulations returned the earlier balance-law record as the only same-object close match and no stronger covering statement.

## Limitations
The result assumes compact support and \(T,R>0\). It is a necessary condition for compact recurrence, not an existence theorem and not a pointwise lower bound along every instant of a trajectory. The conclusion is an excursion statement: positive stationary mass with nonzero velocity lies beyond \(|x|=1\); it does not quantify how much mass or how far beyond the barrier. Later or poorly indexed literature could contain an equivalent inequality; the closest same-object full text and published-finding record inspected did not.

## References
1. N. J. Balmforth and R. V. Craster, “Synchronizing Moore and Spiegel,” *Chaos* **7** (1997), 738–752. DOI: 10.1063/1.166271.
2. C. Letellier and J.-M. Malasoma, “Universalities in the chaotic generalized Moore & Spiegel equations,” *Chaos, Solitons & Fractals* **69** (2014), 40–49. DOI: 10.1016/j.chaos.2014.09.002.
3. “Exact recurrence balances and a strict period floor for the Moore--Spiegel oscillator,” published finding, 2026-09-20, identifier `2026/9/20/SCOPE-moore-spiegel-balance-laws-and-period-floor--8ed8e017fb90`.
