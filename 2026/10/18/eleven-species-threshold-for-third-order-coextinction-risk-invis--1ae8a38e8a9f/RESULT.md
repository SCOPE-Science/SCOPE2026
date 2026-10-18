# Eleven-species threshold for third-order coextinction risk invisible to pairwise losses

## Finding
Let \(G\) and \(H\) be finite connected simple bipartite plant–pollinator graphs with the same number \(v\) of plant vertices and the same number \(k\) of pollinator vertices. Each pollinator visits exactly three different plants; two distinct pollinators may visit exactly the same three plants. There are no isolated species. For a common \(q\in(0,1)\), every pollinator independently fails with probability \(q\), and a plant is lost if and only if all its pollinators fail. Let \(Z_G(q)\) be the number of lost plants.

Assume plants can be labeled so that for every plant \(i\), and for every unordered pair \(\{i,j\}\), the one- and two-plant joint-loss probabilities in \(G\) and \(H\) agree as functions of \(q\). Then, whenever \(v+k\le10\), the third central moments \(\mathbb E[(Z_G-\mathbb EZ_G)^3]\) and \(\mathbb E[(Z_H-\mathbb EZ_H)^3]\) agree for every \(q\in(0,1)\).

**The bound is sharp.** On six plants \(1,\ldots,6\) and five pollinators, specify their plant neighborhoods, in pollinator order, by
\[
G:(123,145,246,356,123),\qquad
H:(124,135,236,456,123).
\]
Both bipartite graphs are connected; each of the five pollinators has degree three, and corresponding plants have the same degrees and pairwise joint-loss laws. Nevertheless,
\[
\mathbb E[(Z_G-\mathbb EZ_G)^3]
-\mathbb E[(Z_H-\mathbb EZ_H)^3]
=6q^3(1-q)^2>0\qquad(0<q<1).
\]
The mean and variance are identical for all \(q\):
\[
\mathbb EZ_G=\mathbb EZ_H=3q^2+3q^3,
\quad \operatorname{Var}(Z_G)=\operatorname{Var}(Z_H)
=3q^2+9q^3+9q^4-12q^5-9q^6.
\]
Thus their standardized skewnesses also differ for every nontrivial failure probability. At \(q=1/2\), the common mean is \(9/8\), the common variance is \(123/64\), and the central third moments are \(1095/256\) and \(1047/256\).

## Assumptions and scope
A pollinator is a distinct vertex even when another pollinator has the same set of plant neighbors. Repeated triples in the displayed neighborhood lists therefore do **not** represent repeated edges: each graph is a simple bipartite graph. Each independent pollinator-failure indicator has common probability \(q\); there are no direct plant failures, recovery, feedback cascades, interaction weights, or rewiring. The two graphs compared have fixed matching guild sizes. The pairwise matching condition is per corresponding labeled plant and plant pair, not merely equality of unordered degree multisets or aggregate variance.

For a plant subset \(S\), write \(N_G(S)\) for the union of its pollinator neighbors. The event that every plant in \(S\) is lost occurs precisely when all pollinators in \(N_G(S)\) fail, with probability \(q^{|N_G(S)|}\).

## Proof
**Moment identity.** Let \(I_i\) indicate loss of plant \(i\), so \(Z=\sum_{i=1}^v I_i\). Since these are zero-one indicators,
\[
\mathbb EZ=\sum_i q^{|N(i)|},\qquad
\mathbb E[Z(Z-1)]=2\sum_{i<j}q^{|N(\{i,j\})|},
\]
\[
\mathbb E[Z(Z-1)(Z-2)]=6\sum_{i<j<\ell}q^{|N(\{i,j,\ell\})|}.
\]
The first two displayed quantities determine the mean and variance, and the third factorial moment determines the third central moment once the first two match. Thus the precise question is whether two degree-three incidence systems with the same labeled one- and two-plant union sizes can have different histograms of three-plant union sizes.

**Complete finite cutoff.** For fixed \((v,k)\), an unlabeled set of \(k\) distinct pollinator vertices of degree three is exactly a multiset of \(k\) three-element subsets of \(\{1,\ldots,v\}\). Repetitions are allowed. Generate every such multiset using weakly increasing indices from the complete list of \(\binom v3\) triples. There are exactly \(\binom{\binom v3+k-1}{k}\) multisets before connectivity filtering. Represent each plant's pollinator neighborhood by a \(k\)-bit integer. Retain only candidates with no isolated plants and connected plant-overlap graph (equivalent here to connectedness of the bipartite graph). For each candidate calculate its signature of the \(v\) individual neighborhood sizes and \(\binom v2\) pair-neighborhood union sizes. Group candidates with equal signatures and check that within each group the histogram
\[
(h_0,\ldots,h_k),\qquad h_r=\#\{\{i,j,\ell\}:i<j<\ell,\ |N(\{i,j,\ell\})|=r\}
\]
is identical. This comparison uses exact integers only.

The standalone exhaustive verifier covers every \(v\ge3,k\ge1\) with \(v+k\le10\), including empty cases after filtering. The numbers of connected candidate multisets at each total order from four through ten are respectively \(1,1,7,32,162,1083,7588\): in all, \(8874\) candidates. At order ten, the nontrivial six-plant/four-pollinator family has \(5040\) connected candidates but only \(5025\) distinct one-/two-plant signatures; **even across collisions** all three-plant union histograms agree. Every other checked group likewise has a unique triple histogram. The generation is exhaustive by its multiset bijection, and the algorithm itself is supplied in `verify_coextinction.py`, so this proves the lower bound without inferring an infinite assertion from finite tests.

**Eleven-species witness.** The pollinator lists in the finding give plant-degree sequence \((3,3,3,2,2,2)\) in both graphs and the identical plant-pair shared-pollinator matrix
\[
\begin{pmatrix}
3&2&2&1&1&0\\
2&3&2&1&0&1\\
2&2&3&0&1&1\\
1&1&0&2&1&1\\
1&0&1&1&2&1\\
0&1&1&1&1&2
\end{pmatrix}.
\]
Its diagonal is the individual degree; each pair union size is the sum of the corresponding diagonal entries minus its intersection entry. Therefore every individual and pairwise loss probability matches.

Among the twenty plant triples, their pollinator-neighborhood union-size histograms differ: for \(G\) the nonzero counts are \(h_3=1,h_4=3,h_5=16\), and for \(H\) they are \(h_4=5,h_5=15\). Hence
\[
\sum_{i<j<\ell}\left(q^{|N_G(\{i,j,\ell\})|}-q^{|N_H(\{i,j,\ell\})|}\right)
=q^3-2q^4+q^5=q^3(1-q)^2.
\]
Using \(Z^3=Z+3Z(Z-1)+Z(Z-1)(Z-2)\), and subtracting equal lower moments to centralize, gives the asserted \(6q^3(1-q)^2\). Direct elementary expansion of the first two factorial moments gives the stated mean and variance.

## Verification
Run `python3 verify_coextinction.py` with Python 3 and no third-party packages. It enumerates all required multisets and verifies each proposed one-/two-plant signature collision against its triple-union histogram. It separately enumerates all \(2^5=32\) pollinator-failure patterns of each witness at \(q=1/2\). The resulting distributions of lost-plant counts \(0,1,2,3,4,5,6\), multiplied by \(32\), are respectively \((13,12,0,6,0,0,1)\) and \((14,9,3,5,0,0,1)\). These independently reproduce the same mean, variance and distinct third central moments. All arithmetic is integer or exact rational; no sampling, tolerance, or solver timeout is used as a proof.

## Relationship to prior work
Memmott, Waser and Price (2004) modeled secondary plant losses after pollinator removals and examined extinction tolerance of empirical networks. The present independent-failure model is a simple alternative risk distribution, not their random-without-replacement removal process. Bane, Pocock and James (2018) studied distributions of integrated network robustness under different knockout procedures and emphasized effects of degree heterogeneity. Their robustness statistic and its distribution over extinction sequences differ from the third central moment of a fixed-\(q\) coextinction count computed here. Neither inspected study supplies the stated pairwise-indistinguishable sharp eleven-species classification.

The four-block pair-balanced *Pasch trade* is classical; no novelty is claimed for its balanced-pair identity. The witness uses the two sides of such a trade plus one additional pollinator of neighborhood \(123\). The particular third-order coextinction polynomial, connected degree-three risk interpretation, and complete minimum-order claim are the assessed contribution. A known finite trade identity does not itself assert the eleven-species cutoff under the stated stochastic observation condition.

## Limitations
The cutoff is only for connected simple bipartite networks whose **every pollinator has exactly three plant partners**, under identical independent pollinator-failure probabilities, and comparison of all labeled one- and two-plant loss laws. It makes no minimum claim if parallel-neighborhood pollinator species are forbidden, if pollinator degree differs from three, or if only weaker aggregate moment matching is required. The first example has two distinct pollinator species visiting the same three plants; this is essential to the exhibited construction. Neither generic empirical relevance nor consequences for weighted, dependent, dynamical, or multistage coextinction systems are asserted. Originality remains subject to independent bibliographic review.

## References
1. J. Memmott, N. M. Waser and M. V. Price, *Tolerance of pollination networks to species extinctions*, Proceedings of the Royal Society B 271 (2004), 2605–2611. Published online 6 December 2004. https://doi.org/10.1098/rspb.2004.2909
2. M. S. Bane, M. J. O. Pocock and R. James, *Effects of model choice, network structure, and interaction strengths on knockout extinction models of ecological robustness*, Ecology and Evolution 8 (2018), 10794–10804. https://doi.org/10.1002/ece3.4529
3. *Pasch configuration*, Encyclopedia of Mathematics, https://encyclopediaofmath.org/wiki/Pasch_configuration (classical pair-balanced trade terminology and construction).
