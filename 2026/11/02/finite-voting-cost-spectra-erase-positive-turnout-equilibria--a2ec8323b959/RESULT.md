# Finite voting-cost spectra erase positive-turnout equilibria

## Finding

**Theorem (finite-spectrum equilibrium dichotomy and discretization instability).** In the two-candidate spatial voting game specified below, suppose voters' ideal points have an atomless, strictly increasing cumulative distribution function \(V\) on \([0,1]\), while independent voting costs have a finite distribution with strictly positive masses and minimum support point \(c_*\geq0\). Define
\[
I_{c_*}=[0,1]\cap[1-c_*,c_*].
\]
The **complete set** of pure Nash equilibrium platform pairs is
\[
\boxed{\operatorname{PNE}=I_{c_*}\times I_{c_*}.}
\]
In particular, no pure equilibrium exists when \(c_*<1/2\); at \(c_*=1/2\) the unique equilibrium is \((1/2,1/2)\); for \(1/2<c_*<1\) the equilibrium set is a square; and for \(c_*\geq1\) all platform pairs are equilibria. **Every equilibrium under finite cost support has zero turnout.** Neither the remaining cost levels, their positive probabilities, nor the shape of \(V\) affects this classification.

The obstruction persists under arbitrarily accurate cost discretization. For \(m\geq2\), let the cost distribution \(K_m\) put probability \(1/m\) on each of \(1/(m+1),\ldots,m/(m+1)\). It has no pure equilibrium for any finite \(m\), although
\[
\sup_{0\leq t\leq1}|K_m(t)-t|=\frac1{m+1}.
\]
For a uniform electorate and the limiting continuous uniform cost law \(K(t)=t\), the platforms \((1/4,3/4)\) form a pure equilibrium. Indeed the candidate payoff functions for \(K_m\) converge **uniformly** to those of \(K\), with error at most \(1/(m+1)\); therefore \((1/4,3/4)\) is a \(2/(m+1)\)-additive approximate equilibrium for every discretized game despite the absence of exact pure equilibria.

## Assumptions and scope

Two candidates simultaneously choose locations \(a,b\in[0,1]\). A voter with ideal point \(x\) evaluates candidate \(i\) by negative distance \(-|x-c_i|\), has an independently drawn nonnegative cost \(\kappa\), and votes for the closer candidate precisely when the advantage over the opponent is **strictly greater** than \(\kappa\); otherwise the voter abstains. Voters with equal distances abstain. Candidate utility is the expected fraction of the **entire electorate** voting for that candidate (not its conditional fraction among ballots cast and not merely its election-winning probability). A cost atom at \(c_j\) has positive mass \(w_j\), the masses sum to one, and there are finitely many distinct atoms. The voter-ideal CDF \(V\) is continuous and strictly increasing on the whole policy interval; costs and ideal points are independent. No incumbent, alienation, or competitiveness terms enter the objective.

All conclusions concern simultaneous pure strategies. The strict participation rule matters at cost-threshold equality, and the payoff normalization is essential.

## Proof

**1. Exact turnout formulas.** Fix platforms \(a<b\), let \(\Delta=b-a\), and consider voters with cost \(c\). Their distance advantage from the left platform is greater than \(c\) exactly when
\[
\Delta>c,\qquad x<\frac{a+b-c}{2}.
\]
Their distance advantage from the right platform is greater than \(c\) exactly when
\[
\Delta>c,\qquad x>\frac{a+b+c}{2}.
\]
These thresholds fall strictly inside \([0,1]\) whenever \(c<\Delta\). Consequently, with \(J(\Delta)=\{j:c_j<\Delta\}\), the two candidate utilities are
\[
U_L(a,b)=\sum_{j\in J(\Delta)}w_j V\left(\frac{a+b-c_j}{2}\right),
\qquad
U_R(a,b)=\sum_{j\in J(\Delta)}w_j\left[1-V\left(\frac{a+b+c_j}{2}\right)\right].
\]
When \(a=b\), no voter strictly prefers either candidate and both utilities are zero.

**2. Active turnout cannot be a pure equilibrium.** Suppose \(\Delta>c_*\), so \(J(\Delta)\) is nonempty. Because the cost support is finite, the left candidate can shift right from \(a\) to \(a+\varepsilon<b\) for a sufficiently small \(\varepsilon>0\) while preserving exactly the same active set \(J(\Delta)\). Every summand in \(U_L\) then increases strictly, since its CDF argument rises by \(\varepsilon/2\) and \(V\) is strictly increasing. Hence the left candidate has a strictly profitable unilateral deviation. Thus every pure equilibrium must have \(|a-b|\leq c_*\), in which case no cost type participates and both utilities are zero.

**3. Exact inactive equilibria.** Hold an opposing platform \(y\) fixed. If \(y>c_*\), a deviation to platform \(0\) creates separation greater than \(c_*\) and wins a positive mass of voters near \(0\). Likewise if \(1-y>c_*\), a deviation to \(1\) wins a positive mass near \(1\). Full support of \(V\) makes these gains strictly positive. Conversely, if \(y\in I_{c_*}\), every candidate location \(z\in[0,1]\) satisfies \(|z-y|\leq c_*\). The reverse triangle inequality implies
\[
\big||x-z|-|x-y|\big|\leq |z-y|\leq c_*
\]
for every voter, so no deviation against \(y\) can induce a single vote. Whenever \(I_{c_*}\) is nonempty, any two platforms inside it are within \(c_*\) of each other: for \(1/2\leq c_*\leq1\) its diameter is \(2c_*-1\leq c_*\), and for \(c_*\geq1\) the diameter is at most one. Hence every pair in \(I_{c_*}^2\) is an inactive equilibrium, and the previous deviation argument excludes all other inactive pairs. This proves the classification for arbitrary \(V\) and all finite positive-mass cost spectra.

**4. Discrete-to-continuous instability.** The empirical CDF \(K_m\) changes by \(1/m\) at \(j/(m+1)\), and comparing its constant value on each intervening interval with the identity CDF gives the stated exact Kolmogorov error \(1/(m+1)\). Since its minimum positive cost is \(1/(m+1)<1/2\), the first part eliminates every pure equilibrium for \(m\geq2\). At an atomic threshold the strict voting rule uses the left limit \(K_m(t-)\), which obeys the same discrepancy bound because the target CDF is continuous. For any candidate profile and any voter position, the absolute difference in turnout probabilities for each candidate under the discretized and continuous cost laws is therefore at most this CDF error. Integrating over voters proves uniform candidate-payoff error at most \(1/(m+1)\).

For the uniform electorate and continuous uniform cost law, direct integration when \(s<t\) yields
\[
U_L(s,t)=(t-s)s+\frac{(t-s)^2}{4},\qquad
U_R(s,t)=(t-s)(1-t)+\frac{(t-s)^2}{4}.
\]
Against a right candidate at \(3/4\), a left-side deviation is maximized uniquely at \(s=(3/4)/3=1/4\), with payoff \(3/16\); any deviation to the right of \(3/4\) has maximum payoff \(1/48\). Reflection proves the symmetric best response for the other candidate, so \((1/4,3/4)\) is a pure equilibrium in the limiting game. Finally, uniform payoff error \(\delta\) converts every exact equilibrium of the limiting game into a \(2\delta\)-additive approximate equilibrium of the approximating game by the two-sided triangle inequality. Taking \(\delta=1/(m+1)\) finishes the proof.

## Verification

The attached standalone `verify_cost_atoms.py` uses exact rational arithmetic and three strictly increasing electorates. It checks 738 strict improving moves at positive-turnout profiles, 1,620 explicit profitable deviations from non-equilibrium no-turnout profiles, and 30,966 zero-profit deviation checks for predicted equilibria. It also checks 2,002 unilateral deviations against the limiting uniform-cost equilibrium and the exact CDF error for 99 discrete distributions. The expected execution output is:

`VERIFY_OK active_strict_improvements=738 zero_turnout_profitable_deviations=1620 no_deviation_checks=30966 continuum_best_response_samples=2002 empirical_cost_distributions=99`

These finite checks are consistency tests, **not** substitutes for the universal proof above. The exact identities in the proof cover all population distributions satisfying the stated hypotheses, all support sizes, and all candidate locations.

## Relationship to prior work

Wolf and Meir (2026) study this spatial participation rule with absolutely continuous voting-cost laws and derive polarized pure equilibria, including the uniform-electorate, uniform-cost quartile benchmark. Their published framing uses a cost density and differentiability-style conditions; the present finite-atomic classification is not a consequence of those existence results, and demonstrates that approximating continuous costs by finite spectra can destroy exact equilibrium despite uniform payoff convergence. The accessible introduction and result descriptions were compared; a complete appendix-level comparison was not available, so unrecognized coverage in that manuscript or related earlier work remains a priority risk.

Classical Hotelling–Downs models without cost-based abstention, and the generalized tournament-game formulation studied by Nikram, use different payoff and participation assumptions. They do not supply the strict-threshold atomic-cost classification. The finding does not claim general nonexistence for continuous, mixed discrete-continuous, or infinite-support voting-cost laws.

## Limitations

The conclusion requires independent, finitely supported costs and an atomless full-support electorate; infinite or mixed distributions may behave differently. It relies on a strict cost threshold and expected **unconditional** vote mass as utility. A different rule for voting exactly at the threshold, a different platform space, or an objective based on winning rather than vote mass may change equilibria. The limiting equilibrium and its approximation bound are asserted for a uniform electorate, not every electorate. Publication-priority uncertainty remains because not every possibly relevant appendix and older spatial-voting article could be inspected in full.

## References

1. G. Wolf and R. Meir, *Costly Voting in the Hotelling–Downs Model*, arXiv:2609.29869v1, first publicly posted September 24, 2026. https://arxiv.org/abs/2609.29869
2. A. Nikram, *A Generalized Hotelling–Downs Model with Asymmetric Candidates*, *Journal of Public Economic Theory*, DOI 10.1111/jpet.12663. https://doi.org/10.1111/jpet.12663
3. R. Barelli, *Competition for a Majority*, *Econometrica* 82 (2014), 271–314, DOI 10.3982/ECTA11008. https://doi.org/10.3982/ECTA11008
