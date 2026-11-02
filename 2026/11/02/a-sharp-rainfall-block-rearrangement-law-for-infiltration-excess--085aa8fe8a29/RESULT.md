# A sharp rainfall-block rearrangement law for infiltration-excess runoff

## Finding
For a finite storm made of prescribed rainfall-intensity/duration blocks, a soil with a positive nonincreasing infiltration capacity depending only on cumulative infiltration absorbs **most** water when the blocks are ordered from highest to lowest rainfall intensity, and **least** water in the reverse order. The corresponding total infiltration-excess runoff has the opposite ranking. This holds for every finite collection of positive-duration blocks, every initial cumulative infiltration, and every locally Lipschitz positive nonincreasing capacity function; there is no restriction to a specific number of storm phases or particular Green–Ampt parameters.

The theorem also gives an exact local equality-versus-strictness test for every adjacent exchange. Consequently it gives an effective criterion for whether a given nonoptimal permutation actually loses infiltration relative to the descending arrangement. The criterion does not declare the sorting inequality strict when infiltration stays entirely supply-limited or entirely capacity-limited.

## Assumptions and scope
Let \(m\ge1\) and let the storm contain blocks \((r_j,d_j)\), with intensities \(r_j\ge0\) and durations \(d_j>0\), for \(1\le j\le m\). Every permutation uses each entire block exactly once. Put \(T=\sum_jd_j\) and let \(F(0)=F_0\ge0\). The cumulative infiltration \(F\) evolves by
\[
\dot F(t)=\min\{r(t),f(F(t))\},\qquad F(0)=F_0,
\]
where \(f:[F_0,\infty)\to(0,\infty)\) is nonincreasing and locally Lipschitz. All rainfall that exceeds instantaneous infiltration is removed immediately as infiltration-excess runoff; there is no surface detention, evaporation, drying, saturation storage, or subsurface lateral exchange. Total excess runoff is
\[
Q=\sum_{j=1}^m r_jd_j-[F(T)-F_0].
\]
Write \(F_\downarrow(T)\) and \(F_\uparrow(T)\) for the final values after sorting the blocks by nonincreasing and nondecreasing intensity, respectively. Then every permutation \(\pi\) obeys
\[
F_\uparrow(T)\le F_\pi(T)\le F_\downarrow(T),
\qquad Q_\downarrow\le Q_\pi\le Q_\uparrow.
\]
Tied rainfall intensities may be ordered arbitrarily.

For the local strictness characterization, consider two consecutive blocks of intensities \(a>b>0\), duration \(s>0\) for \(a\), and duration \(t>0\) for \(b\), from an arbitrary starting infiltration \(x\ge F_0\). Write
\[
v_a(u)=\min\{a,f(u)\},\quad v_b(u)=\min\{b,f(u)\},\quad
h(u)=\int_x^u\frac{dz}{v_b(z)},\quad
R(y)=\frac{v_a(h^{-1}(y))}{v_b(h^{-1}(y))}.
\]
Define \(\Psi_s\) as the time-\(s\) flow of \(y'=R(y)\). On the relevant finite flow interval, the high-then-low block order is **strictly better** exactly when
\[
\int_0^t\left[1-\frac{R(\Psi_s(w))}{R(w)}\right]dw>0.
\]
Equivalently, for some positive-measure set of \(w\in(0,t)\), \(R(\Psi_s(w))<R(w)\). If \(b=0\), exchanging that dry block with any other block gives exact equality. An easily checked sufficient condition for strictness is that \(b<f(x)<a\) and \(f\) is strictly decreasing on a right neighborhood of \(x\).

## Proof
**Existence and order preservation.** Each constant-input vector field \(v_r(u)=\min\{r,f(u)\}\) is locally Lipschitz, bounded by \(r\), and nonnegative. Its forward flow exists uniquely through all finite durations and is strictly increasing as a function of the initial state (solutions cannot meet in finite time). Thus a strict improvement from one adjacent exchange persists through all later blocks.

**The adjacent exchange.** Fix \(a>b>0\). The change of coordinate \(y=h(u)\), with \(h(x)=0\), maps the low-intensity field to the unit-speed translation \(y'=1\); it maps the high-intensity field to \(y'=R(y)\). The ratio \(v_a(u)/v_b(u)\) is nonincreasing in \(u\): it is \(a/b\) when \(f(u)\ge a\), \(f(u)/b\) when \(b<f(u)<a\), and \(1\) when \(f(u)\le b\). Consequently \(R\) is positive, locally Lipschitz, and nonincreasing.

Let \(\Psi_s\) denote the flow for this transformed high-intensity field. By differentiating the scalar flow with respect to its initial value,
\[
\Psi_s'(w)=\exp\left(\int_0^s R'(\Psi_\tau(w))d\tau\right)
=\frac{R(\Psi_s(w))}{R(w)}\le1
\]
(the identity holds almost everywhere for locally Lipschitz \(R\), and by approximation and absolute continuity everywhere in the integrated formula). Since \(R>0\), \(\Psi_s(w)>w\). The transformed high-then-low terminal state is \(\Psi_s(0)+t\); the low-then-high terminal state is \(\Psi_s(t)\). Their difference is
\[
\Psi_s(0)+t-\Psi_s(t)
=\int_0^t\left[1-\frac{R(\Psi_s(w))}{R(w)}\right]dw\ge0.
\]
The integrand is nonnegative and continuous, so this formula proves both the non-strict swap and the stated exact strictness condition. Because \(h^{-1}\) is strictly increasing, the comparison also holds for actual cumulative infiltration. The zero-intensity field is identically zero and its flow commutes with every other field. Equal intensities trivially commute.

**Global sorting.** Every permutation can be converted to descending intensity order by exchanges of adjacent inverted pairs (in which a smaller-intensity block precedes a larger-intensity block). Each exchange weakly improves the state after the exchanged blocks, and all later forward flows preserve the inequality. Therefore descending order maximizes terminal infiltration. Applying the reverse exchanges proves ascending order minimizes it. The total rainfall \(\sum_j r_jd_j\) is permutation-invariant, so the runoff inequalities follow by mass balance. Strictness for any chosen bubble-sort sequence is equivalent to at least one of its exchanges meeting the local integral condition; a strict gain cannot subsequently vanish because every subsequent scalar flow is strictly increasing.

**Exact witness.** Set \(F_0=0\), \(f(F)=\max\{1,3-F\}\), and let the storm have a high-intensity block \((r,d)=(4,\log(4/3))\) and a low-intensity block \((1,1/4)\). In either arrangement, the high block follows \(\dot F=3-F\), and the low block follows \(\dot F=1\); every encountered state is below \(2\). Write \(q=\exp[-\log(4/3)]=3/4\). High first gives
\[
F_\downarrow(T)=3(1-q)+1/4=1,
\]
whereas low first gives
\[
F_\uparrow(T)=3-(3-1/4)q=15/16.
\]
The same total rain thus causes exactly \(1/16\) more excess runoff in the ascending arrangement.

**Green–Ampt subclass.** For \(K,C,F_0>0\), \(f(F)=K(1+C/F)\) on \(F\ge F_0\) is positive and strictly decreasing. When two consecutive positive rainfall intensities \(a>b\) straddle the current capacity \(b<f(x)<a\), their descending exchange is strictly advantageous for every positive pair of durations. For example, \(K=C=1\), \(F_0=1/2\), \(a=4\), \(b=2\) gives \(f(F_0)=3\). No universal strictness follows if both intensities lie on the same side of capacity throughout the encounter.

## Verification
The self-contained Python file `checker.py` checks the rational witness by exact fraction arithmetic and runs 2,625 numerical ordering comparisons over three nonincreasing capacity families, four randomly generated blocks per configuration, and all 24 permutations. Numerical tests use fourth-order Runge–Kutta integration and an absolute tolerance of \(5\times10^{-7}\); these are stress tests rather than proofs. The argument above proves the infinite-dimensional parameter statement without finite enumeration.

## Relationship to prior work
The decreasing Green–Ampt infiltration-capacity construction is classical. Chu (1978) introduced an unsteady-rain Green–Ampt framework, while Triadis and Broadbridge (2012) examined the theoretical Green–Ampt limit. These underlying models are not claimed as new. Tan and collaborators (2018), in an unsteady-rain numerical model, compared three rainfall patterns and found more cumulative infiltration under their decreasing-intensity example than under steady and increasing-intensity examples. This important qualitative phenomenon is prior evidence, not an original observation here. The mathematical distinction is the universal all-permutation order theorem, its generality for every positive decreasing cumulative-infiltration capacity, and an exact local equality criterion with a rational strict runoff gap. General scalar-flow order and comparison arguments motivate the proof; the result does not claim that conjugating one-dimensional flows is itself new.

## Limitations
The conclusions concern **total infiltration-excess volume**, not runoff peak time, flood stage, downstream flood risk, or the response of spatial Richards-equation models. Neither stored surface water nor soil moisture recovery is permitted. The test code is not a proof. Historical priority remains uncertain where older technically relevant articles on variable rainfall, including Chu (1978) and Philip (1993), could not be inspected in full. General scalar-control rearrangement principles may subsume the abstract flow lemma; originality is limited to the sharp hydrological specialization relative to the inspected references, and independent literature review is still needed.

## References
- Chu, S. T. (1978), “Infiltration during an unsteady rain,” *Water Resources Research*, 14, 461–466. https://doi.org/10.1029/WR014i003p00461 (publisher metadata and abstract accessed; complete technical text not accessed).
- Triadis, D., and Broadbridge, P. (2012), “The Green–Ampt limit with reference to infiltration coefficients,” *Water Resources Research*, 48. First published 18 July 2012. https://doi.org/10.1029/2011WR011747 (accessible full text inspected).
- Tan, J., et al. (2018), “Numerical Investigation on Infiltration and Runoff in Unsaturated Soils with Unsteady Rainfall Intensity,” *Water*, 10, 914. https://doi.org/10.3390/w10070914 (indexed substantive full article sections inspected; direct access restricted).
- Philip, J. R. (1993), “Variable-head ponded infiltration under constant or variable rainfall,” *Water Resources Research*, 29, 2155–2165 (cited here as a related but uninspected model with surface ponding).
