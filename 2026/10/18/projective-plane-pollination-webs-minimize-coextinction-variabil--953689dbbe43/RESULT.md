# Projective-plane pollination webs minimize coextinction variability at every random-loss stage

## Finding

Let \(q\ge 2\) be a prime power, \(v=q^2+q+1\), and \(d=q+1\). Consider any **simple, \(d\)-regular bipartite incidence network** between exactly \(v\) plants and \(v\) pollinators. Exactly \(m\in\{0,1,\ldots,v\}\) distinct pollinators are uniformly removed without replacement. A plant undergoes secondary extinction if and only if all of its pollinators have been removed. Let \(X_m\) count secondary plant extinctions.

Write \(s=v-m\) and use the convention \(\binom ab=0\) if \(b<0\), \(b>a\), or \(a<0\). Put
\[
 a_m=\frac{\binom{v-d}{s}}{\binom vs},\qquad
 b_m(t)=\frac{\binom{v-2d+t}{s}}{\binom vs}.
\]
Then **every** such network satisfies, simultaneously for every \(m\),
\[
 \operatorname{Var}(X_m)\ \ge\ V_m^*
 :=v a_m(1-a_m)+v(v-1)\bigl(b_m(1)-a_m^2\bigr).
\]
Equality for **all** extinction counts \(m\) occurs exactly when the network is the point-line incidence graph of a finite projective plane of order \(q\). Moreover, for each individual stage
\[
 2d-2\le m\le v-2,
\]
equality already characterizes the projective-plane incidence graphs; every other admissible network has strictly larger variance. Indeed, at any such stage its variance exceeds \(V_m^*\) by at least
\[
 \frac{2\binom{v-2d}{v-m-2}}{\binom{v}{v-m}}>0.
\]
Such minimizers exist for every prime power \(q\) by the finite-field construction of projective planes. No assertion of isomorphism uniqueness is made when multiple nonisomorphic projective planes exist.

At the **sharp separation stage** \(m=2d-2\), a projective-plane web loses at most one plant for **every** choice of removed pollinators. In contrast, every other network satisfying the same degree constraints admits an \(m\)-pollinator deletion set that extinguishes at least two plants. Thus exactly the projective-plane webs suppress simultaneous secondary plant losses up to this threshold.

For the seven-plant, seven-pollinator, degree-three case (\(q=2\)), the unique projective-plane incidence type is the Fano configuration. After four random pollinator removals, it has expected secondary extinction count \(4/5\) and variance \(4/25\). A simple degree-preserving two-edge switch keeps the mean \(4/5\), but raises the variance to \(48/175\), producing a positive probability of two plant extinctions. Thus equal mean robustness can conceal sharply different coextinction risk.

## Assumptions and scope

All incidence edges are binary and unweighted. Each plant interacts with exactly \(d\) pollinators and each pollinator serves exactly \(d\) plants. Random removal means a uniformly chosen subset of exactly \(m\) pollinators; the theorem concerns the randomness **within one fixed extinction stage**, not an assumed independent survival process. Plant extinction is the topological loss-of-all-partners rule; pollinators are not rewired or replenished, and no later dynamical feedback is modeled. All results are for this regular-network class, without assuming observed ecological networks are regular.

## Proof

**1. Exact pairwise coextinction kernel.** Let \(N_i\) be the \(d\)-element pollinator neighborhood of plant \(i\), and let \(Y_i\) be the indicator that all members of \(N_i\) were removed. The probability that one specified plant goes extinct is \(a_m\). For two plants \(i,j\), set \(t_{ij}=|N_i\cap N_j|\). Their union has size \(2d-t_{ij}\), so the chance that both plants go extinct is \(b_m(t_{ij})\). Consequently,
\[
 \operatorname{Var}(X_m)=v a_m(1-a_m)
 +2\sum_{i<j}\bigl(b_m(t_{ij})-a_m^2\bigr).
\]
All admissible networks have identical \(a_m\), so only the pairwise intersection profile affects the variance.

**2. A universal intersection budget.** Each pollinator is shared by exactly \(\binom d2\) unordered pairs of plants, hence
\[
 \sum_{i<j}t_{ij}=v\binom d2
 =\binom v2,
\]
using \(v-1=d(d-1)\). Thus the arithmetic mean of all pairwise intersections is exactly one, even when the graph is not a projective plane.

**3. Discrete convexity at every extinction stage.** The upper index \(v-2d+t\) is nonnegative because \(q\ge2\) gives \(v\ge2d\). Pascal's identity yields the exact second finite difference
\[
 b_m(t+2)-2b_m(t+1)+b_m(t)
 =\frac{\binom{v-2d+t}{s-2}}{\binom vs}\ \ge0,
 \qquad 0\le t\le d-2.
\]
For the integer-valued convex sequence \(b_m(t)\), its line through the values at \(t=0,1\) is a supporting line at every nonnegative integer \(t\). Hence
\[
 b_m(t)\ge b_m(1)+(t-1)\bigl(b_m(1)-b_m(0)\bigr).
\]
Summing over plant pairs, the linear term vanishes by Step 2. Substitution in Step 1 proves the displayed variance lower bound.

**4. Complete equality characterization and gap.** If \(2d-2\le m\le v-2\), then \(2\le s\le v-2d+2\) and
\[
 b_m(2)-2b_m(1)+b_m(0)
 =\frac{\binom{v-2d}{s-2}}{\binom vs}>0.
\]
The supporting-line inequality from Step 3 is strict for each integer \(t\ge2\). If all intersections were at most one, their mean one would force every one to equal one. Therefore any non-projective-plane network has at least one pair with \(t_{ij}\ge2\), strictly increasing the variance. The smallest individual strict surplus is at least the displayed second difference, and the factor two in Step 1 gives the quantitative gap. Conversely, if \(t_{ij}=1\) for every pair, the variance bound is attained for every \(m\).

The condition \(t_{ij}=1\) together with the degree constraints defines a symmetric \(2\)-design with parameters \((v,d,1)\). For completeness, if \(B\) is its square incidence matrix, then \(BB^{\mathsf T}=(d-1)I+J\). As \(B\) is invertible and all its row and column sums are \(d\), its transpose product also satisfies \(B^{\mathsf T}B=(d-1)I+J\). Thus distinct pollinator neighborhoods intersect in exactly one plant as well, establishing the point-line axioms of a projective plane. Conversely, the incidence of the points and lines of \(\mathrm{PG}(2,\mathbb F_q)\) has the required degree and intersection properties for every prime power \(q\).

**5. Sharp deterministic first-double-loss threshold.** Under a projective plane, any two plants have neighborhood union of size \(2d-1\). Removing only \(2d-2\) pollinators cannot extinguish both. In any other network, the fixed intersection budget and Step 4 ensure at least one pair with \(t_{ij}\ge2\), whose neighborhood union has size at most \(2d-2\). Complete this union to a set of \(2d-2\) removed pollinators; the corresponding two plants both go extinct. This is a positive-probability outcome under uniform deletion.

## Verification

The accompanying standalone `VERIFY.py` uses only the Python standard library. It constructs exact projective-plane incidence matrices over the prime fields of orders \(2,3,5,7\), checks all degree and pairwise-intersection identities, performs a degree-preserving incidence switch, and verifies the bound and the strict comparison for every extinction count. For orders \(2\) and \(3\), it **independently enumerates every subset of pollinators** at every extinction stage and computes the complete finite distribution of \(X_m\), agreeing with the covariance formula. It separately checks the Pascal finite-difference identity in exact rational arithmetic. Run `python3 VERIFY.py` in the directory containing the file. These finite computations verify examples and formula implementations; the proof above establishes the result for all prime powers.

## Relationship to prior work

Memmott, Waser, and Price introduced the random-without-replacement removal scenario and the loss-of-all-pollinators secondary-extinction rule for observed mutualistic networks. Their analysis simulated extinction trajectories but did not classify variance-minimizing regular incidence graphs. Jones, Zurell, and Wiesner analytically identified equal plant degrees as optimal for **mean** network robustness and expressly identified the **standard deviation** of secondary extinctions as a further mathematical target. The current result fixes those degrees on both sides and instead completely classifies the variance optimum at **every fixed removal count**, distinguishing networks with the same expected losses. Chabert-Liddell, Barbillon, and Donnet obtained expectation and variance formulas for robustness of **random stochastic-block-model networks**; the present deterministic, degree-constrained simultaneous extremal characterization is a different statement. Projective planes and their incidence properties are classical; their existence and pairwise intersection structure are not claimed as discoveries here.

## Limitations

The theorem minimizes a **variance**, not the mean, worst-case total plant loss after arbitrary large deletion sets, fixation probability, or any dynamical ecological stability metric. Its sharp no-double-loss statement concerns deletion of exactly \(2d-2\) pollinators and implies the corresponding property at smaller deletion counts, not at larger ones. It makes no claim for irregular networks, unequal interaction strengths, temporally correlated removals, rewiring, spatial dispersal, or real pollinator effectiveness. A literature-equivalent result in combinatorial reliability or ecological risk theory cannot be categorically excluded without further independent bibliographic examination; the nearby stochastic-block-model article was not available in full for this comparison.

## References

1. Memmott, J., Waser, N. M., and Price, M. V. (2004). *Tolerance of pollination networks to species extinctions*. Proceedings of the Royal Society B 271, 2605–2611. Published online 6 December 2004. DOI: 10.1098/rspb.2004.2909. Author-accessible full text: https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf
2. Jones, C., Zurell, D., and Wiesner, K. (2024). *Novel analytic methods for predicting extinctions in ecological networks*. Ecological Monographs 94, e1601. DOI: 10.1002/ecm.1601. Open-access full text: https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecm.1601
3. Chabert-Liddell, S.-C., Barbillon, P., and Donnet, S. (2022). *Impact of the mesoscale structure of a bipartite ecological interaction network on its robustness through a probabilistic modeling*. Environmetrics 33, e2709. First preprint posted 11 June 2021, arXiv:2106.06348. DOI: 10.1002/env.2709.
