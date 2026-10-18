# A sharp ten-species first-coextinction risk reversal under degree-matched rewiring

## Finding

Consider a connected simple bipartite ecological interaction network, with plants depending on at least one pollinator. After random primary deletion of pollinators, a secondary plant loss occurs precisely when all pollinators adjacent to that plant have disappeared. We study the *first-loss risk*: the probability that at least one plant suffers secondary loss.

**Sharp threshold.** For any two such networks with at most nine species in total, the same number of plants and pollinators, the same multiset of plant degrees, and the same multiset of pollinator degrees, their first-loss risk curves are pointwise ordered for every common independent pollinator-deletion probability \(q\in[0,1]\). Indeed, the vectors of first-loss probabilities under uniform deletion of exactly \(k\) pollinators are coordinatewise comparable, including every feasible \(k\). At ten total species there are two connected, degree-matched networks whose risk ordering reverses precisely at \(q=1/2\), with strict opposite orders on both sides.

Write the four pollinators as \(0,1,2,3\). The two six-plant networks \(G\) and \(H\) are specified by these respective multisets of plant neighborhoods:

\[
G:\quad \{0\},\ \{0\},\ \{0,1\},\ \{1,2\},\ \{1,3\},\ \{2,3\};
\]
\[
H:\quad \{0\},\ \{1\},\ \{0,2\},\ \{1,2\},\ \{0,3\},\ \{1,3\}.
\]

Both are connected, with plant degree multiset \((1,1,2,2,2,2)\) and pollinator degree multiset \((2,2,3,3)\). Let \(R_G(q)\) and \(R_H(q)\) denote their first-loss risks when each pollinator is independently deleted with probability \(q\). Then

\[
\boxed{R_G(q)-R_H(q)=q(1-q)^2(2q-1).}
\]

The associated exact counts of deletion sets of sizes \(k=0,1,2,3,4\) causing at least one plant loss are respectively \((0,1,6,4,1)\) for \(G\) and \((0,2,5,4,1)\) for \(H\). In particular \(R_G(1/4)-R_H(1/4)=-9/128\) whereas \(R_G(3/4)-R_H(3/4)=3/128\).

Despite this reversal, the expected *number* of secondarily lost plants is identical in the two networks, namely \(2q+4q^2\), for all \(q\). The same reversal persists in connected networks of unbounded order: add any number of new degree-one plants adjacent only to pollinator \(0\) in both networks.

## Assumptions and scope

The two guilds contain respectively \(a\ge1\) plants and \(b\ge1\) pollinators. Graphs are finite, simple, bipartite, connected, and have no isolated species. At a fixed deletion depth \(k\), a uniformly selected \(k\)-subset of the \(b\) pollinators is removed; for the independent-deletion model, each pollinator is removed with a common probability \(q\), independently. No plant is a primary deletion, and secondary plant loss is the deterministic *all-neighbors-lost* rule. We quantify the event that **at least one** plant is lost; no further dynamic cascade is modeled. Network pairs have both guild sizes and both guild degree multisets equal. Comparisons include all \(0\le k\le b\), respectively all \(0\le q\le1\).

## Proof

**Exact finite event formula.** Encode a plant's nonempty pollinator neighborhood as a nonzero \(b\)-bit integer \(r_i\). A deletion-set mask \(s\) causes at least one secondary plant loss exactly when there exists \(i\) with \(r_i\mathbin{\&}s=r_i\). Define

\[
c_k(G)=\#\{s:\ |s|=k,\ \exists i,\ r_i\subseteq s\},\qquad
R_G(k)=\frac{c_k(G)}{\binom bk}.
\]

Here \(|s|\) is the cardinality of the deleted pollinator set, and \(R_G(k)\) is conditional risk under exactly \(k\) deletions. Conditioning independent deletion on its size gives the exact Bernstein-basis formula

\[
R_G(q)=\sum_{k=0}^{b}c_k(G)q^k(1-q)^{b-k}.
\]

Thus, if \(c_k(G)\le c_k(H)\) for every \(k\), then \(R_G(q)\le R_H(q)\) for every \(q\in[0,1]\), and similarly with the ordering reversed.

**Exhaustion through nine total species.** For each \(n=a+b\) from \(2\) to \(9\), and each positive guild split, enumerate every weakly increasing \(a\)-tuple of nonzero \(b\)-bit masks. Every simple bipartite graph with these guild sizes is represented because permutation of plant labels allows its mask tuple to be sorted; pollinator labels are retained. Discard disconnected graphs. Group the rest by the **two separately sorted degree multisets**, computed from row popcounts and column sums. Within each group, compute \(c_0,\ldots,c_b\) by iterating all \(2^b\) deletion sets. Compare every pair of distinct count vectors. Each is componentwise comparable (in one direction or the other), so the preceding Bernstein argument establishes the asserted pointwise ordering. The exhaustive finite loop uses integer operations, runs to completion, and is independently reproducible with the attached standard-library program and certificate. The number of enumerated connected mask multisets in nontrivial guild splits \(a,b\ge2\), by \(n=4,5,6,7,8,9\), is respectively \(3,16,87,588,5158,58968\); the numbers of distinct count-vector comparisons within degree classes are respectively \(0,0,0,4,47,397\). All were comparable. Splits with a singleton guild have only one connected network (a star), making any comparison trivial. The counts concern *labeled-pollinator row-multiset representatives*, not unlabeled graph isomorphism classes.

**Ten-species witness.** Encode the displayed \(G,H\) neighborhoods as \((1,1,3,6,10,12)\) and \((1,2,5,6,9,10)\), with bits numbered \(0,1,2,3\). Both graphs are connected; direct degree counting gives the same two degree multisets. Explicit enumeration of the \(16\) pollinator-deletion sets yields the displayed count vectors. Their difference in the Bernstein expansion equals

\[
\begin{aligned}
R_G(q)-R_H(q)&=-q(1-q)^3+q^2(1-q)^2\\
&=q(1-q)^2(2q-1).
\end{aligned}
\]

Because each plant's disappearance requires the loss of all its incident pollinators, linearity of expectation gives \(\mathbb{E}[L]=\sum_iq^{\deg(i)}=2q+4q^2\) in both networks. This does not determine the probability that \(L\ge1\).

**Unbounded extension.** Add \(t\ge0\) new plants, each of neighborhood \(\{0\}\), to both networks. Both augmented networks remain connected, their plant and pollinator degree multisets still agree, and their total species number is \(10+t\). In both base networks a plant of neighborhood \(\{0\}\) is already present, hence the Boolean first-loss event is unchanged by adding duplicate singleton neighborhoods. Thus the same crossing persists for every \(t\ge0\).

## Verification

Run `python verify_first_loss.py --compare first_loss_certificate.json` with Python 3, without external dependencies. The checker exhaustively enumerates all the stated nontrivial guild splits through nine species, checks connectedness by breadth-first search, independently enumerates pollinator-deletion subsets, and checks all degree-matched count-vector pairs. It also checks the explicit witness, both degree multisets, exact Bernoulli risks by a second Boolean-outcome implementation, and eleven nontrivial graph extensions. All checks passed. The exact certificate is embedded alongside the script; it is regenerated and compared byte-for-byte. Finite enumeration supports the sharp boundary only because the search domain is exhaustively represented; the unbounded-family statement is proved separately by event equivalence, not by extrapolation.

## Relationship to prior work

Memmott, Waser, and Price (2004) study extinction tolerance of plant–pollinator networks under primary pollinator losses and the classical topological all-neighbors-lost coextinction rule. Burgos and collaborators (2007) study network nestedness and extinction-tolerance curves. Vieira and Almeida-Neto (2015; first online 2014) extend topological coextinction models to interaction-strength-dependent stochastic cascades. Jones, Zurell, and Wiesner (2023) develop analytical mean extinction estimates, in which the expected number of plants lost under random pollinator removals depends on the plant-degree distribution. None of those inspected results establishes the **sharp simultaneous-both-degree-multiset first-loss probability comparison** or its ten-species reversal. The mean alone cannot determine this tail event; the displayed witness has identical means but opposite tail-risk order on two parameter intervals. Related reliability-polynomial identities apply but do not, without an additional classification, imply the sharp size bound. Earlier equivalent hypergraph reliability or network-extinction results remain a bibliographic risk, not a proved absence.

## Limitations

The lower bound through nine total species is a rigorously finite classification; it does not classify all ten-species witnesses or give the maximal number of crossings for larger networks. Only random uniform primary pollinator deletion and deterministic immediate loss of unsupported plants are modeled. Pollinator dependencies, correlated deletions, interaction strengths, and cascades are outside the claim. The family demonstrates mathematical possibility, not a prevalence or effect-size estimate for empirical ecological networks. Independent bibliographic audit and external validation have not been performed.

## References

- Memmott, J., Waser, N. M., and Price, M. V. (2004), "Tolerance of pollination networks to species extinctions," *Proceedings of the Royal Society B*, https://doi.org/10.1098/rspb.2004.2909 (first online 2004-12-06).
- Burgos, E., Ceva, H., Perazzo, R. P. J., Devoto, M., Medan, D., Zimmermann, M., and Delbue, A. M. (2007), "Why nestedness in mutualistic networks?", *Journal of Theoretical Biology*; open author manuscript: https://www.agro.uba.ar/users/mdevoto/Burgos%26al.2007.pdf.
- Vieira, M. C., and Almeida-Neto, M. (2015), "A simple stochastic model for complex coextinctions in mutualistic networks: robustness decreases with connectance," *Ecology Letters* 18:144–152, https://doi.org/10.1111/ele.12394.
- Jones, C., Zurell, D., and Wiesner, K. (2023), "Evaluating The Impact Of Species Specialisation On Ecological Network Robustness Using Analytic Methods," arXiv:2306.15428.
