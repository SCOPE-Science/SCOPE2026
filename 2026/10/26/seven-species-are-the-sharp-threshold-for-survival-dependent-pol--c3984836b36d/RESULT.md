# Seven species are the sharp threshold for survival-dependent pollinator protection

## Finding

For any connected simple bipartite interaction network whose two guilds consist of nonempty sets of plants and pollinators, there is a single pollinator whose guaranteed preservation maximizes the expected surviving-plant count for every common unprotected-pollinator survival probability \(p\in(0,1)\), **provided the total number of species is at most six**.

At seven species this can fail, and the complete set of failures comprises exactly **two guild-preserving isomorphism classes**. Both have four plants and three pollinators. Label the pollinators \(A,B,C\), and encode each plant's neighborhood by the binary mask \(1,2,4\) for \(A,B,C\). The respective four-plant multisets are
\[
\mathcal G_1=(1,3,6,6),\qquad
\mathcal G_2=(1,6,6,7).
\]
Writing \(q=1-p\), the best achievable expected number of plants surviving in either network is
\[
\max\{4-2q^2,\;4-q\}.
\]
For \(0<q<1/2\), preserving \(A\) is optimal; for \(1/2<q<1\), preserving \(B\) is optimal. At \(q=1/2\) both are optimal; in \(\mathcal G_2\), \(B,C\) tie whenever \(q>1/2\).

Among all \(1795\) labeled connected \(4\times3\) incidence matrices, precisely \(108\) have no single uniformly optimal pollinator: \(72\) belong to \(\mathcal G_1\) and \(36\) to \(\mathcal G_2\).

## Assumptions and scope

The graph is finite, simple, undirected, connected, and bipartite, with distinct plant and pollinator guilds and no isolated vertices. Each pollinator survives independently with the same probability \(p\in(0,1)\), except that an intervention protects **one** designated pollinator with certainty. A plant survives exactly when at least one of its neighboring pollinators survives. Only the expected number of surviving **plants** is maximized; pollinator richness is not added to the objective. Guild-preserving isomorphisms may independently relabel plants and pollinators but may not interchange guilds. There are no weights, correlations, behavioral rewiring, or further extinction cascades.

A *universal target* is a pollinator that maximizes expected surviving-plant richness simultaneously for all \(p\in(0,1)\), allowing ties.

## Proof

**1. Exact target-benefit identity.** Let \(d_i\) be the degree of plant \(i\). Without protection the plant's survival probability is \(1-q^{d_i}\), so the expected surviving-plant richness is
\[
E_0(q)=\sum_{i\in P}(1-q^{d_i}).
\]
If pollinator \(j\) is protected, every adjacent plant then survives with certainty. Thus the exact expected gain is
\[
B_j(q)=\sum_{i\in P:\,i\sim j}q^{d_i},
\qquad E_j(q)=E_0(q)+B_j(q).
\]
Consequently the optimal intervention is precisely a maximizer of the finitely many positive-coefficient polynomials \(B_j\).

**2. The small-guild lemma.** If there are at most two pollinators, each plant touches one or both. For two pollinators, the difference of their benefits is \((a-b)q\), where \(a,b\) count plants that touch only the respective pollinator; common plants cancel. Thus their order cannot change with \(q\). A one-pollinator network is immediate.

Now suppose there are at most three plants, with arbitrarily many pollinators. If a pollinator touches every plant, its benefit dominates every other benefit term by term, for all \(q>0\). Otherwise every pollinator touches one or two plants (the case of one plant being immediate). In a connected network with at least two plants, each plant belongs to at least one two-plant pollinator neighborhood: otherwise it has no path to another plant. Hence a one-plant pollinator is weakly dominated term by term by some two-plant pollinator. On at most three plants, any two distinct two-plant neighborhoods share a plant, so their benefit difference is either zero or
\[
q^{d_a}-q^{d_b},
\]
which has the same weak sign for every \(q\in(0,1)\). Therefore a maximal two-plant pollinator is optimal for the entire interval. The conclusion also covers the case in which all plant neighborhoods of pollinators have size one, because connectedness then forces a single plant.

These arguments imply that a network without a universal target must have at least four plants and at least three pollinators, hence at least seven species.

**3. Exact exhaustive seven-species classification.** At exactly seven species, the only guild sizes not handled by the lemma are four plants and three pollinators. Encode the four labeled plant neighborhoods by integers in \(\{0,\ldots,7\}\); the complete search has \(8^4=4096\) matrices, not a random sample. Reject matrices with an isolated plant/pollinator or a disconnected bipartite graph. Exactly \(1795\) connected matrices remain. For a pollinator \(j\), its target gain is
\[
B_j(q)=a_jq+b_jq^2+c_jq^3,
\]
where the coefficients count its adjacent plants of degrees one, two, and three.

Comparison of two targets after division by the positive \(q\) reduces to a quadratic \(A+Bq+Cq^2\). Such a quadratic is nonnegative on the entire interval \(0\le q\le1\) exactly when both endpoint values are nonnegative and, if \(C>0\) and its vertex \(-B/(2C)\) lies strictly between zero and one, the integer discriminant condition \(4AC-B^2\ge0\) holds. Every coefficient and comparison is an integer; no floating-point grid is used.

A target is universal exactly when it weakly dominates all other target-gain polynomials under this test. The complete enumeration yields \(108\) connected labeled matrices without such a target. Canonicalizing by all plant relabelings (sorting masks) and all six pollinator permutations gives exactly the two classes \((1,3,6,6)\) and \((1,6,6,7)\), of labeled multiplicities \(72\) and \(36\), respectively.

**4. Explicit switching identities.** For \(\mathcal G_1=(1,3,6,6)\), the unprotected baseline and three protection gains are
\[
E_0=4-q-3q^2,\quad
(B_A,B_B,B_C)=(q+q^2,3q^2,2q^2).
\]
Hence
\[
(E_A,E_B,E_C)=(4-2q^2,\ 4-q,\ 4-q-q^2).
\]
For \(\mathcal G_2=(1,6,6,7)\),
\[
E_0=4-q-2q^2-q^3,\quad
(B_A,B_B,B_C)=(q+q^3,2q^2+q^3,2q^2+q^3),
\]
and therefore
\[
(E_A,E_B,E_C)=(4-2q^2,\ 4-q,\ 4-q).
\]
In either case \(E_A-E_B=q(1-2q)\), with its sole interior zero at \(q=1/2\). This proves the claimed sharpness and switch.

## Verification

Run the accompanying standard-library Python program `verify.py` with Python 3, then compare its single-line, sorted JSON output with `certificate.json`. The program enumerates every labeled connected bipartite graph with at most seven species and, using the proved small-guild lemma, applies exact integer quadratic nonnegativity tests to the sole unresolved guild pair. Its output records \(1795\) connected \(4\times3\) labeled graphs, \(108\) switching graphs, and the two canonical classes with sizes \(72\) and \(36\).

The program separately checks both exceptional networks by exhaustive enumeration of all independent pollinator survival states at failure probabilities \(1/4\) and \(3/4\), comparing directly accumulated exact rational expectations with the derived benefit-polynomial identities. These finite checks corroborate, but do not substitute for, the symbolic all-\(q\) argument.

## Relationship to prior work

Memmott, Waser, and Price established plant–pollinator coextinction analysis under systematic and random loss of pollinators, highlighting network redundancy and specialization. Kaiser-Bunbury and coauthors examined further robustness and behavioral effects. Traveset, Tur, and Eguíluz investigated stochastic pollinator coextinction and keystone pollinators. Those forward analyses motivate the present optimization question. The claim here is specifically a **sharp minimum-total-species and complete first-layer classification** of changes in the optimal single guaranteed pollinator under homogeneous independent survival, not a general network robustness formula or a claim that pollinator-prioritization itself is new.

## Limitations

The exact classification applies to connected unweighted binary networks under one-step plant persistence after independent pollinator failures. It does not assert that a particular real ecosystem follows the independence model, that preserving one pollinator is equally costly in every environment, or that degree alone predicts ecological benefit. The classifier was exhaustively checked only through seven species, while the universal-target lemma applies for arbitrarily large networks whenever one guild has at most three plants or at most two pollinators. Related work under different stochastic dependence, intervention-budget, or graph-polynomial terminology could contain equivalent results.

## References

1. Memmott, J., Waser, N. M., and Price, M. V., “Tolerance of pollination networks to species extinctions,” *Proceedings of the Royal Society B* (2004), DOI: 10.1098/rspb.2004.2909. First online 2004-12-06.
2. Kaiser-Bunbury, C. N., Muff, S., Memmott, J., Müller, C. B., and Caflisch, A., “The robustness of pollination networks to the loss of species and interactions: a quantitative approach incorporating pollinator behaviour,” *Ecology Letters* (2010), DOI: 10.1111/j.1461-0248.2009.01437.x.
3. Traveset, A., Tur, C., and Eguíluz, V. M., “Plant survival and keystone pollinator species in stochastic coextinction models: role of intrinsic dependence on animal-pollination,” *Scientific Reports* 7, 6915 (2017), DOI: 10.1038/s41598-017-07037-7.
