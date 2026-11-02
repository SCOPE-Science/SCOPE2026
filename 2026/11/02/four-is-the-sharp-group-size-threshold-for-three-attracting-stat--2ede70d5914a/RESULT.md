# Four is the sharp group-size threshold for three attracting states in a two-volunteer game

## Finding

Consider an infinitely large, well-mixed population of unconditional cooperators and defectors, with population cooperator frequency \(x\in[0,1]\). Each interaction is a random group of size two with *experienced* probability \(p\), or size four with probability \(1-p\). A shared benefit \(B>0\) is generated for everyone in a group if and only if **at least two** members cooperate; every cooperator pays an individual cost \(C\), whether or not the threshold is reached. Let \(0<C<B\), and write \(\kappa=C/B\).

**Sharp three-attractor theorem.** The replicator dynamics have three distinct locally asymptotically stable equilibria—full defection, a strictly mixed population, and full cooperation—if and only if

\[
0<p<\frac12,
\qquad
H_p(x_+)<\kappa<\min\{H_p(x_-),p\},
\]
where
\[
H_p(x)=p x+3(1-p)x(1-x)^2,
\qquad
x_\pm=\frac{2\pm\sqrt{(1-2p)/(1-p)}}3.
\]
In that regime there are exactly three distinct interior equilibria; the middle one is attracting, the other two are repelling, and both pure population states are attracting. All five equilibrium points are hyperbolic relative to the one-dimensional population flow.

**Minimal-size boundary.** No fixed group size, and no mixture supported only on group sizes two and three, can have three distinct locally attracting states in this two-helper threshold game. Consequently, size four is the smallest admissible maximum group size producing the three-attractor phenomenon. This statement concerns the exact threshold-two, two-strategy, well-mixed, constant-cost model; it does not assert a universal minimum size for all public-good games.

**Exact rational witness.** With \(p=11/23\) and \(\kappa=10/23\),
\[
H_p(x)-\kappa=
\frac{(2x-1)(3x-2)(6x-5)}{23}.
\]
The five equilibria are \(0,\tfrac12,\tfrac23,\tfrac56,1\). The attracting equilibria are precisely \(0,\tfrac23,1\); the other two are repelling. A corresponding observer-level group-count distribution puts probability \(11/17\) on size two and \(6/17\) on size four.

## Assumptions and scope

Groups are formed at random, and conditional on the focal individual's *experienced* group size, other players independently cooperate with probability \(x\). Group-size distribution does not depend on the focal strategy, time, or population composition. Group sizes one and zero are excluded; the contribution threshold is exactly two for every group. The benefit is nonrivalrous and not divided by group size. Cooperators pay a nonrefundable cost, even in unsuccessful groups. The dynamics are the deterministic, continuous-time, two-strategy replicator equation. Stability means local asymptotic stability in the population state space \([0,1]\), including one-sided stability at the pure states. All claims are for exact parameters, not statistical estimates.

The experienced group-size law must not be confused with the observer's group-count law. If a uniformly sampled interaction has group-count probabilities \(g_2\) and \(g_4\), the focal individual's size-two probability is \(p=2g_2/(2g_2+4g_4)\). For the exact witness, \((g_2,g_4)=(11/17,6/17)\), giving \(p=11/23\).

## Proof

**1. Derive the incentive function.** Suppose a focal cooperator and defector are compared against the same random arrangement of other group members. If exactly one other player cooperates, changing the focal strategy from defect to cooperate completes the two-person threshold and generates benefit \(B\). For zero or at least two other cooperators, changing the focal strategy does not change receipt of benefit. In all cases the cooperating focal individual pays \(C\). Hence
\[
\pi_C(x)-\pi_D(x)
=B\Pr\{\text{exactly one cooperating coplayer}\}-C.
\]
For a size-two group this probability is \(x\), while for a size-four group it is \(3x(1-x)^2\). Averaging over experienced group sizes gives
\[
\dot x = Bx(1-x)[H_p(x)-\kappa].
\]
Thus all interior equilibria are exactly the roots of \(H_p(x)=\kappa\).

**2. Locate the turning points.** Direct differentiation yields
\[
H_p'(x)=(3-2p)-12(1-p)x+9(1-p)x^2.
\]
For \(0<p<1/2\), its two simple roots are \(x_-\) and \(x_+\) as stated; they satisfy \(0<x_-<x_+<1\). The derivative is positive on \((0,x_-)\), negative on \((x_-,x_+)\), and positive on \((x_+,1)\). Thus \(H_p(x_-)\) is a strict local maximum, \(H_p(x_+)\) a strict local minimum, \(H_p(0)=0\), and \(H_p(1)=p\). In particular \(H_p(x_+)>0\) and
\[
H_p(x_+)<\min\{H_p(x_-),p\},
\]
so the parameter window is nonempty. The horizontal level \(\kappa\in(0,1)\) cuts each of the three strictly monotone intervals once if and only if it lies strictly above the minimum and strictly below both the maximum and the right endpoint value. This is exactly the asserted inequality, and it gives three simple interior roots.

For \(p=0\), \(H_0(x)=3x(1-x)^2\) is unimodal in the open interval; its derivative vanishes only at the interior maximum \(x=1/3\) and at the endpoint. At \(p=1/2\), the derivative is \(\tfrac12(3x-2)^2\), and for \(1/2<p\le1\) it is strictly positive throughout the interval. None of these cases has three distinct interior roots. For \(0<p<1/2\) but a level outside the strict inequality window, no three simple interior roots occur. This proves the complete strict three-root criterion.

**3. Classify stability.** Because \(H_p(0)=0<\kappa\), the vector field is negative immediately to the right of zero, making \(x=0\) attracting. In the strict three-root regime the signs of \(H_p(x)-\kappa\), from left to right, are negative, positive, negative, positive. Consequently the first and third interior roots repel and the second attracts. Since \(H_p(1)=p>\kappa\), the flow points toward \(x=1\) from the left, making it attracting. At all five roots the linearized derivative is nonzero: at interior roots it is \(Bx(1-x)H_p'(x)\), while at the pure states it is \(-B\kappa\) at zero and \(-B(p-\kappa)\) at one. Conversely, three distinct hyperbolic attracting equilibria on a one-dimensional interval require two alternating repelling equilibria, hence at least three interior roots here. The preceding turning-point analysis is therefore necessary as well as sufficient.

**4. Prove the sharp maximum-size cutoff.** For any deterministic group size \(n\ge2\), the same pivotal calculation gives
\[
H_n(x)=(n-1)x(1-x)^{n-2}.
\]
For \(n=2\), this is increasing; for \(n\ge3\), its derivative on \((0,1)\) has the sign of \(1-(n-1)x\), so it has just one interior maximum. Therefore a fixed group size can have at most two interior equilibria. If all groups have size two or three, the gain is a weighted average of \(x\) and \(2x(1-x)\), a polynomial of degree at most two; it cannot have three distinct interior roots. But the explicit size-two/size-four example below does. This establishes minimal maximum group size four, without claiming uniqueness of the witnessing group-size mixture.

**5. Check the exact witness.** Substitution of \(p=11/23\) and \(\kappa=10/23\) gives
\[
23(H_p(x)-\kappa)=36x^3-72x^2+47x-10=(2x-1)(3x-2)(6x-5).
\]
The roots lie strictly inside \((0,1)\). The field signs alternate as described, so \(0,2/3,1\) attract, while \(1/2,5/6\) repel. More precisely, for initial conditions \(0\le x(0)<1/2\), the solution approaches zero; for \(1/2<x(0)<5/6\), it approaches \(2/3\); and for \(5/6<x(0)\le1\), it approaches one. Starting exactly at a repelling equilibrium leaves the system there; these exceptional initial conditions are not included in neighboring basins.

## Verification

The companion script `checks/verify.py` uses exact rational arithmetic to enumerate pivotal events for size-two and size-four interactions, check the exact factorization and equilibrium types, and verify the group-count-to-individual conversion. It also performs a deterministic randomized numerical stress test of 500 admissible parameter selections, bracketing all three roots in their monotonicity intervals. The script reports 4,795 successful assertions in the reference execution. These finite checks corroborate but do not replace the analytical proof of the all-parameter theorem. Run `python3 checks/verify.py` from the extracted folder; it uses only the Python standard library.

## Relationship to prior work

The fixed-size threshold-public-good model and its evolutionary bifurcation framework are established by Bach, Helvik and Christiansen (first publicly available 20 July 2005). Peña's group-size-diversity treatment (first published 4 November 2011) explicitly analyzes the one-volunteer model and identifies intermediate volunteer thresholds as a distinct extension. Peña and Nöldeke (preprint available 7 October 2015) provide general gain-function and variability theory, especially for monotone or convex/concave gain sequences; the present two-helper mixed-size incentive has two interior turning points and is not covered by their convexity conclusions. Broom, Pattni and Rychtář (first published 17 December 2018) derive general threshold-volunteer's-dilemma incentive formulas for variable group sizes, then analyze negative-binomial size laws with examples having at most two attracting states. Their general incentive formula specializes to the first step of our proof, but their reported negative-binomial examples and conclusions do not establish the sharp two-atom three-attractor criterion or maximum-size-four boundary.

The present claim concerns that explicit sharp criterion, exact rational witness, and minimal group-size boundary; the underlying replicator equation, pivotal-event calculation, and general threshold-public-good framing are not claimed as new. A comparison based on the accessible technical texts found no published statement implying all these results, but this is not an independent proof of priority. The earliest fixed-size paper could be inspected only through its public abstract; see limitations.

## Limitations

This is deterministic evolutionary game theory, not an observed empirical behavioral pattern. It assumes fixed exogenous experienced group-size probabilities, no assortment, a constant cost and benefit, and a two-cooperator threshold. Multiple stable equilibria here are population dynamical attractors, not evidence that finite stochastic populations possess three absorbing invariant distributions. The strict parameter criterion excludes degenerate bifurcation surfaces, where the asserted five hyperbolic equilibria do not persist. The sharp maximum-size-four result is limited to the stated threshold-two game. The full text of the earlier Bach–Helvik–Christiansen article was not available during the literature comparison, and remaining publication-priority uncertainty requires independent expert review.

## References

1. Bach, L. A., Helvik, T., and Christiansen, F. B., *The evolution of n-player cooperation—threshold games and ESS bifurcations*, Journal of Theoretical Biology 238 (2006), 426–434. DOI: https://doi.org/10.1016/j.jtbi.2005.06.007. Epub 2005-07-20; abstract https://pubmed.ncbi.nlm.nih.gov/16045941/.
2. Peña, J., *Group-size diversity in public goods games*, Evolution 66 (2012), 623–636. DOI: https://doi.org/10.1111/j.1558-5646.2011.01504.x. First published 2011-11-04.
3. Peña, J., and Nöldeke, G., *Variability in group size and the evolution of collective action*. Preprint first posted 2015-10-07: https://doi.org/10.1101/021485.
4. Broom, M., Pattni, K., and Rychtář, J., *Generalized social dilemmas: The evolution of cooperation in populations with variable group size*, Bulletin of Mathematical Biology 81 (2019), 4643–4674. DOI: https://doi.org/10.1007/s11538-018-00545-1. First online 2018-12-17. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC6874626/.
5. Archetti, M., and Scheuring, I., *Coexistence of cooperation and defection in public goods games*, Evolution 65 (2011), 1140–1148. DOI: https://doi.org/10.1111/j.1558-5646.2010.01185.x.
