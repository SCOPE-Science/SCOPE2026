# Sharp degree-matched reversal of ecological coextinction variance

## Finding

In the independent-pollinator-loss, all-neighbors-lost model, two simple bipartite networks with identical plant-degree and pollinator-degree sequences cannot reverse their ranking by the variance of total plant coextinctions as the common pollinator extinction probability varies if there are at most three pollinators, regardless of the number of plants. With four pollinators, reversal remains impossible for at most four plants. Four pollinators and five plants suffice, and hence these bounds are sharp for the minimum number of pollinators and, conditional on four pollinators, the minimum number of plants.

A pair with the same labeled margins is given by the five plant neighborhoods on pollinators \(\{1,2,3,4\}\):
\[
G=(\{1\},\{1\},\{1,2\},\{2,3\},\{2,4\}),\qquad
H=(\{1\},\{2\},\{1,2\},\{1,2\},\{3,4\}).
\]
Both have plant degree sequence \((1,1,2,2,2)\), pollinator degree sequence \((3,3,1,1)\), and identical expected coextinction count \(2q+3q^2\) for every \(0\le q\le1\). Nevertheless, with \(V_G(q)\) and \(V_H(q)\) denoting their respective coextinction-count variances,
\[
V_G(q)-V_H(q)=2q(1-q)^2(1-2q).
\]
The first network has strictly larger variance for \(0<q<1/2\), the second for \(1/2<q<1\), and they tie at \(q=1/2\) and at the trivial endpoints.

## Assumptions and scope

A bipartite graph has \(r\ge1\) labeled primary species (pollinators) and \(m\ge1\) labeled secondary species (plants). Every plant and every pollinator has positive degree. Distinct plants may have the same nonempty pollinator neighborhood; parallel edges are forbidden. Each pollinator disappears independently with common probability \(q\in(0,1)\), and a plant goes extinct if and only if **all** its original pollinators have disappeared. There is no further ecological feedback, rewiring, unequal extinction risk, or direct plant mortality. For two networks, equality of both guild degree sequences means equality as multisets; the construction actually has equal labeled sequences. A strict variance-ranking reversal requires two probabilities in \((0,1)\) at which the variance inequalities have opposite strict signs.

## Proof

For plant \(i\) write \(N_i\) for its nonempty pollinator-neighborhood, \(d_i=|N_i|\), and \(X_i\) for the indicator that all partners of plant \(i\) disappear. Put \(X=\sum_iX_i\). Independence of primary extinctions gives \(\mathbb E X_i=q^{d_i}\) and \(\mathbb E X_iX_j=q^{|N_i\cup N_j|}\). Consequently
\[
\operatorname{Var}(X)=\sum_iq^{d_i}+2\sum_{i<j}q^{|N_i\cup N_j|}-\left(\sum_iq^{d_i}\right)^2.\tag{1}
\]
For two graphs \(G,H\) with identical secondary-degree multisets, the first and third terms cancel. Let \(P_G(q)=\sum_{i<j}q^{|N_i\cup N_j|}\). Their variance difference is exactly \(2(P_G-P_H)\).

If primary pollinator \(j\) has degree \(c_j\), double counting shared partners gives
\[
\sum_{i<k}|N_i\cap N_k|=\sum_{j=1}^r\binom{c_j}{2}.
\]
Thus, for fixed degree sequences of both guilds,
\[
\sum_{i<k}|N_i\cup N_k|=(m-1)\sum_id_i-\sum_j\binom{c_j}{2}
\]
is unchanged by any rewiring. The polynomial \(F=P_G-P_H\) has degree at most \(r\), satisfies \(F(0)=0\) (because neighborhoods are nonempty), \(F(1)=0\), and \(F'(1)=0\). If \(r\le3\), then \(F(q)=a q(1-q)^2\) for a real constant \(a\) (possibly zero). Its sign is constant on \((0,1)\), proving the unrestricted-plant assertion.

For \(r=4\), the same identities force
\[
F(q)=q(1-q)^2(a+bq).\tag{2}
\]
Here \(a\) equals the difference between the numbers of plant pairs whose union has size one, and \(b\) equals the corresponding difference for union size four: they are the coefficients of \(q\) and \(q^4\). An interior sign reversal is therefore equivalent to \(a(a+b)<0\). If \(a=0\) or \(a+b=0\), the sign cannot reverse in the open interval.

For at most four plants, the finite certificate `verify.py` exhausts every possible network with four nonisolated pollinators. Plant neighborhoods are encoded as nonzero four-bit masks. Enumerating nondecreasing multisets of \(m\) masks is complete up to plant permutation; rejecting multisets not covering all four bit positions imposes the no-isolate condition. It groups networks by *both* sorted guild degree sequences (a weaker identification than matching each labeled degree) and records the pair \((u_1,u_4)\) of counts of plant pairs with neighborhood union size one or four. For every unordered pair of distinct such features within a group, the checker tests \(a(a+b)\ge0\), with \(a=\Delta u_1\) and \(b=\Delta u_4\). The complete enumeration visits respectively \(1,40,400,2306\) admissible row-multisets for \(m=1,2,3,4\), in \(1,8,33,103\) degree-signature groups, comparing respectively \(0,0,5,48\) distinct feature pairs. All \(53\) comparisons satisfy the inequality. As every network falls in an enumerated class and (2) determines the whole variance difference from these features, this exhaustively establishes the \(m\le4\) assertion, not merely a sample of probabilities.

For the displayed five-plant construction, its ten unordered plant pairs have union-size histograms \((u_1,u_2,u_3,u_4)=(1,2,7,0)\) for \(G\) and \((0,6,2,2)\) for \(H\). Hence
\[
P_G(q)-P_H(q)=q-4q^2+5q^3-2q^4=q(1-q)^2(1-2q),
\]
which yields the announced strict reversal by (1). Direct expansion also gives
\[
V_G(q)=q(1-q)(9q^2+7q+4),\qquad
V_H(q)=q(1-q)(5q^2+13q+2).
\]
This completes the theorem.

## Verification

Run `python3 verify.py` using Python 3.10+ with no nonstandard packages. The script recomputes all degree signatures and exhaustive feature comparisons, checks both witness union histograms, and independently enumerates all \(16\) primary-extinction outcomes to verify each variance formula at \(19\) rational probabilities. Exact integer and rational arithmetic is used throughout; no numerical tolerance or randomization is involved. A second exhaustive enumeration over **ordered** four-column binary incidence matrices was also performed: it found \(1,79,2161,41503\) nonisolated matrices for \(m=1,2,3,4\), respectively, with the same \(1,8,33,103\) degree-signature groups and no reversals. The unrestricted \(r\le3\) result follows from the polynomial proof rather than a finite experiment.

## Relationship to prior work

Memmott, Waser and Price (2004) introduced simulation-based pollinator-loss comparisons with plants disappearing on the loss of all pollinators; Pastor, Santamaría, Méndez and Galeano (2012) studied effects of network topology on simulated extinction robustness. Kaiser-Bunbury and colleagues (2010) investigated extinction sequences and ecological rewiring. These establish the biological context and model motivation. The present statement concerns an exact **second moment**, a comparison between networks having **both guild degree sequences fixed**, and a sharp minimal structural setting for probability-dependent ranking reversal; it does not claim the earlier basic model or its mean-risk calculations as new. The closest published works inspected do not state this joint criterion or sharp construction; an uninspected full text and unindexed literature remain potential sources of overlap.

## Limitations

The result is a theorem about an idealized binary network with iid pollinator disappearance and an all-partners-lost secondary rule. It does not apply automatically to fixed-number primary removals, nonindependent losses, weighted interactions, plant survival thresholds, cascades with feedback, or actual management outcomes. Identical mean losses do not imply identical full extinction-count distributions. The minima proved here refer to the number of primary species without restriction on plant number, and to plant number **conditional on exactly four primary species**; no universal five-plant lower bound for networks with more primary species is asserted. The finite checker establishes only the stated small-network census and is not an infinite-graph proof. Previously unindexed published equivalents are not excluded.

## References

- J. Memmott, N. M. Waser and M. V. Price, "Tolerance of pollination networks to species extinctions," *Proceedings of the Royal Society B* 271 (2004), 2605–2611, doi:10.1098/rspb.2004.2909. Author-hosted full text: https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf (published online 2004-12-06).
- J. M. Pastor, S. Santamaría, M. Méndez and J. Galeano, "Effects of topology on robustness in ecological bipartite networks," *Networks and Heterogeneous Media* 7 (2012), 429–440, doi:10.3934/nhm.2012.7.429. Full text: https://aimspress.com/aimspress-data/nhm/2012/3/PDF/1556-1801_2012_3_429.pdf.
- C. N. Kaiser-Bunbury, S. Muff, J. Memmott, C. B. Müller and A. Caflisch, "The robustness of pollination networks to the loss of species and interactions," *Ecology Letters* 13 (2010), 442–452, doi:10.1111/j.1461-0248.2009.01437.x (abstract and bibliography inspected; full text not obtained).
- M. S. Bane and collaborators, "Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness," *Ecology and Evolution* (2018), doi:10.1002/ece3.4529 (relevant full-text sections inspected; uses a different robustness measure and extinction process).
