# Fourteen taxa are the first marginal-rarefaction twins among unrooted binary phylogenies

## Finding

For an unrooted binary phylogenetic tree \(T\) with \(n\) leaves and unit edge lengths, select \(k\) leaves uniformly without replacement and measure their **unrooted phylogenetic diversity** \(L_k(T)\), the total edge length in the smallest connecting subtree. Consider **all separate one-sample-size distributions** \(\{\mathcal L(L_k(T)):0\le k\le n\}\), with \(L_0=L_1=0\).

**Sharp reconstruction theorem.** For every \(3\le n\le13\), these distributions determine the unlabelled unrooted tree shape uniquely. At \(n=14\), among the 135 unlabelled unrooted binary tree shapes, precisely one unordered pair of nonisomorphic shapes has the same complete family of marginal diversity distributions. Hence fourteen tips are the smallest possible counterexample to reconstruction from all marginal phylogenetic-diversity rarefactions in this unit-edge class.

The stronger distinguishing statistic for \(n\le13\) uses only the complete mean-rarefaction curve and the two-tip raw second moment; neither matching all expectations nor matching the two-tip second moment alone is claimed to suffice. The 14-tip pair even agrees on the entire distribution at *each* sample size, not merely on these moments.

An explicit witness is given by the two edge lists in `witness.json`: leaf vertices are the integers 0 through 13, internal vertices 14 through 25, and each of the 25 edges has unit length. The full 69 nonzero coefficients of the common two-variable diversity enumerator are generated and checked by `verify.py`; the reproducible output is `verification_output.txt`.

## Assumptions and scope

A tree is connected and acyclic. Exactly \(n\) vertices have degree one (taxa) and every other vertex has degree three; vertices of degree two are not allowed. All edges have length one. Tree isomorphism may relabel all vertices; taxon labels are not observed as attributes. For each integer sample size \(k\in\{0,1,\dots,n\}\), all \(\binom nk\) leaf subsets are equiprobable. Samples for different values of \(k\) are not jointly observed and no coupled sequence of nested subsets is assumed.

Define the integer polynomial
\[
F_T(z,u)=\sum_{S\subseteq \mathrm{Leaves}(T)}z^{|S|}u^{\mathrm{PD}_T(S)},
\qquad \mathrm{PD}_T(S)=|E(\operatorname{Span}_T S)|,
\]
where the span for zero or one leaf has zero edges. Its coefficient of \(z^ku^j\), divided by \(\binom nk\), is exactly \(\Pr\{L_k(T)=j\}\). The theorem therefore concerns equality and injectivity of \(F_T\) within the stated finite classes.

## Proof

**Cut enumeration.** Deleting an edge \(e\) divides the leaf set into two nonempty sides of cardinalities \(s_e\) and \(n-s_e\). For a sample \(S\) of at least two leaves, the edge belongs to the spanned subtree exactly when \(S\) meets *both* sides. Thus, with \(M_k(T)=\sum_{|S|=k}\mathrm{PD}_T(S)\),
\[
M_k(T)=\sum_{e\in E(T)}\left[\binom nk-\binom{s_e}{k}-\binom{n-s_e}{k}\right],\quad 2\le k\le n,
\]
where binomial coefficients with upper argument below \(k\) are zero. For \(k=2\), the diversity of the sampled leaf pair equals the graph distance between its endpoints. Define the further integer invariant
\[
Q_2(T)=\sum_{\{a,b\}\subseteq\mathrm{Leaves}(T)}d_T(a,b)^2.
\]
Both the full vector \((M_2,\ldots,M_n,Q_2)\) and its entries are determined by \(F_T\), since \(M_k\) is the first raw-moment numerator at sample size \(k\) and \(Q_2\) the second raw-moment numerator for \(k=2\).

**Complete tree census, not sampled trees.** Begin with the unique unrooted degree-three star with three leaves. Every binary unrooted tree with \(n+1\) leaves is obtained by deleting a suitable leaf, suppressing the resulting degree-two vertex, and reversing this operation: subdivide one edge of an \(n\)-leaf tree and attach a new leaf there. `verify.py` performs this operation on **every edge of every shape**, then canonically deduplicates using the exact parenthesized rooted-subtree signature at the one or two centers of the unrooted tree. Recursively sorting the signatures of child subtrees gives an invariant that is equal exactly for isomorphic rooted trees, and center-rooting therefore gives a complete unrooted isomorphism invariant. This standard recursive isomorphism argument proves that no binary shape is omitted or duplicated. The resulting shape counts for \(n=3,4,\ldots,14\) are, in order,
\[
1,1,1,2,2,4,6,11,18,37,66,135.
\]

**Exact lower bound.** For every enumerated shape with \(3\le n\le13\), the program evaluates all \(M_k\) by the cut formula and independently computes \(Q_2\) from all pairs of leaves, using exact integer arithmetic. At each \(n\) these \((M_2,\ldots,M_n,Q_2)\) tuples are all distinct. In consequence, \(F_T\) is injective on all shapes for \(n\le13\): if two shapes had the same \(F_T\), they would have the same tuple, contradicting the checked finite enumeration.

**Exact 14-tip collision and uniqueness.** At \(n=14\), grouping all 135 shapes by the necessary integer invariant \((M_2,\ldots,M_{14},Q_2)\) yields precisely three nonsingleton groups, each containing two shapes. Every possible equal-\(F_T\) pair must lie within one of these groups. For each of the six candidate trees, the verifier considers **all \(2^{14}=16384\) subsets** and computes the exact integer array of coefficients of \(F_T\) from the edge cuts. Exactly one group has identical arrays. The two witness trees in `witness.json` reproduce this group, have distinct center-rooted canonical forms, and agree in every coefficient of \(F_T\). The other two candidate groups differ in at least one exact coefficient. This establishes a nonisomorphic twin pair, its uniqueness at fourteen leaves, and the minimal threshold.

The computation is **finite and exhaustive only for the expressly bounded classes** \(3\le n\le14\). It makes no assertion about higher leaf counts or general unequal edge weights. Recomputing canonical forms, the subset-length arrays, and the candidate grouping is all required to check the certificates; no probabilistic numerical tolerance enters.

## Verification

Run `python3 verify.py` in the directory containing `verify.py` and `witness.json`, using the Python standard library. The script validates that every tree has the required degrees, number of vertices, edges and connectedness; rebuilds the 135 shape representatives from the three-tip star; checks the shape counts and unique signatures through 13; reduces fourteen-tip comparisons to the three necessary-moment candidate groups; and exhaustively checks their full diversity laws. It also verifies that the supplied witness edges yield exactly the identified pair.

The common 14-tip polynomial has exactly 69 nonzero coefficients. A canonical serialization of its integer coefficient array has SHA-256 digest `39dd8ac22976f34cecc7184c4196f401cf3de782053cfc939bb17ff8f397759d`. The certificate `verification_output.txt` gives the exact coefficient rows by sample size. No outside packages, datasets, or random seeds are required.

## Relationship to prior work

Nipperess and Matsen (original 2012 preprint, 2013 journal article) derive exact mean and variance expressions for phylogenetic-diversity rarefaction. Their target is forward moment calculation, not the injectivity of the **entire family of marginal laws** or the minimum size of a full-law collision. Fischer and Liebscher (2015 preprint) study split-size information and related tree invariants, with known ambiguities for weaker split signatures; a collision of split-size counts does not imply a collision of every \(F_T\) coefficient. Evans and Lanoue (2015 preprint) reconstruct certain unit-edge trees, including the regular-valence family, from the **joint law of a nested sampling sequence** of subtree lengths. Their joint law contains correlations across sample sizes and is strictly more informative than the collection of marginals considered here. The present twins do not contradict their identification theorem: the two trees may and under that theorem must differ in their joint nested-sampling law.

Searches for exact marginal rarefaction polynomials, full distribution inverse identification, and fourteen-leaf phylogenetic-tree twins did not identify an earlier result with the same statement, but bibliographic coverage is not a proof of priority.

## Limitations

The invariant uses known and equal unit edge lengths, unrooted binary topology, exact uniform-without-replacement sampling, and theoretically exact marginal distributions. No robustness against sampling error, unequal branches, polytomies, tip labels, nonuniform sampling, or additional leaves is proved. The threshold and uniqueness refer to distinct unlabelled shapes, not all possible labelings. The supplied finite census is independently reproducible source code rather than an external formal proof assistant certificate. Independent scientific and bibliographic validation remains to be performed.

## References

1. D. A. Nipperess and F. A. Matsen IV, *The mean and variance of phylogenetic diversity under rarefaction*, preprint first posted 2012-08-31, arXiv:1208.6552, journal 2013; https://pmc.ncbi.nlm.nih.gov/articles/PMC3699894/ .
2. M. Fischer and V. Liebscher, *On the Balance of Unrooted Trees*, 2015 preprint, arXiv:1510.07882, https://arxiv.org/abs/1510.07882 .
3. S. N. Evans and D. Lanoue, *Recovering a tree from the lengths of subtrees spanned by a randomly chosen sequence of leaves*, first posted 2015-06-03, arXiv:1506.01091, https://arxiv.org/abs/1506.01091 .
