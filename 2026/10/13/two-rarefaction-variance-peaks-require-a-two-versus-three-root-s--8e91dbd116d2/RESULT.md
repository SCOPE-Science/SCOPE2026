# Two rarefaction-variance peaks require a two-versus-three root split on five ultrametric taxa

## Finding
Let a rooted full binary ultrametric tree have five distinct leaves, with every edge strictly positive and all root-to-tip distances equal. Draw an unordered set of \(k\) leaves uniformly without replacement, and let \(V_k\) be the population variance of rooted Faith phylogenetic diversity, the sum of lengths in the union of paths from the original root to the sampled leaves. Then the variance sequence has two strict local maxima (at depths \(2\) and \(4\)) **only if the root separates two leaves from three**. This shape supports two strict maxima, while either root-one-versus-four shape cannot.

For the two-versus-three shape, write \(H\) for the common root-to-tip height, \(a\) for the age (distance backward from tips) of the two-tip cherry, \(c\) for the age of the three-tip clade, and \(b\) for the age of its nested cherry. Assume \(0<a<H\) and \(0<b<c<H\). Put \(u=a-b\), \(v=c-b>0\), and \(w=H-c>0\). Define
\[
F=-12u^2+8uv-18uw-8v^2+16vw+15w^2,
\quad
G=3u^2+8uv-6uw-8v^2-8vw-9w^2.
\]
There are two strict local maxima **if and only if** \(F>0\) and \(G>0\), because \(100(V_2-V_3)=F\) and \(100(V_4-V_3)=G\).

The fully binary tree with \((H,a,b,c)=(10,1,6,7)\) has all edge lengths positive and
\[
(V_1,V_2,V_3,V_4,V_5)
=\left(0,\frac{789}{100},\frac{171}{25},\frac{174}{25},0\right).
\]
Thus it has two strict maxima. Five is the smallest possible number of tips among ultrametric trees with this behavior.

## Assumptions and scope
A rooted full binary tree has every internal vertex (including the root) with exactly two children; labels distinguish its leaves but only its unlabeled shape matters here. Its positive edge lengths are ultrametric when every root-to-tip path has the same length. Each leaf is observed exactly once in the finite reference community. For each \(1\le k\le n\), the sample is uniformly selected from all \(\binom nk\) unordered size-\(k\) subsets. The variance is \(\mathbb E[(D_k-\mathbb E D_k)^2]\) conditional on this fixed tree, not the variance of an estimator fitted to random environmental data. A strict local maximum means \(V_k>V_{k-1}\) and \(V_k>V_{k+1}\), with only interior depths \(2\le k\le n-1\) considered.

For the root-two-versus-three shape, denote the two-tip clade by \(\{0,1\}\); in the three-tip clade, let \(2\) be the unmatched tip and \(\{3,4\}\) its cherry. The eight positive edge lengths (specified by descendant masks and lengths) are
\[
\begin{array}{c|cccccccc}
\text{descendants}&\{0\}&\{1\}&\{0,1\}&\{2\}&\{3\}&\{4\}&\{3,4\}&\{2,3,4\}\\
\text{length}&a&a&H-a&c&b&b&c-b&H-c.
\end{array}
\]

## Proof
For an edge with leaf-descendant set \(C\) and length \(\ell_C\), define \(I_C(S)=1\) if the sampled leaf set \(S\) intersects \(C\), and \(0\) otherwise. The rooted diversity is exactly \(D(S)=\sum_C\ell_C I_C(S)\). Consequently its mean and variance at any fixed depth are exact finite sums over the size-\(k\) subsets; no stochastic independence between edge indicators is assumed. This identity is the established starting point, not asserted as a new sampling formula.

**Two-versus-three algebra.** Substitute the displayed eight edges and enumerate the \(\binom5k\) subsets. Directly centering the diversity values gives
\[
\begin{aligned}
100V_2={}&24H^2-12Ha-12Hb-24Hc+9a^2-2ab-4ac+9b^2-4bc+16c^2,\\
100V_3={}&9H^2+6Ha-14Hb-10Hc+21a^2-18ab-30ac+21b^2-10bc+25c^2,\\
100V_4={}&8(3a^2-4ab-2ac+3b^2-2bc+2c^2).
\end{aligned}
\]
On substituting \(H=b+v+w\), \(a=b+u\) and \(c=b+v\), subtraction cancels the common terminal-age shift and gives \(100(V_2-V_3)=F\), \(100(V_4-V_3)=G\). Ultrametricity makes \(D_1=H\) constant; sampling all leaves makes \(D_5\) constant, hence \(V_1=V_5=0\). Since depths \(2\) and \(4\) are the only pair of nonadjacent interior depths for five leaves, both are strict maxima exactly under the two displayed strict inequalities.

**The one-versus-four obstruction.** There are exactly two rooted full-binary shapes on four leaves, so the root-one-versus-four tree has one of two forms. Express the successive positive internal coalescence gaps (from the most recent merger to the root) by \(x_1,x_2,x_3,x_4>0\), with merger ages \(x_1\), \(x_1+x_2\), \(x_1+x_2+x_3\), and root age \(x_1+x_2+x_3+x_4\). In the four-leaf **caterpillar**, its three nested mergers occur at the first three ages, and exact subset variance enumeration gives
\[
100(V_3-V_2)
=12x_2^2+18x_2x_3+8x_2x_4+15x_3^2+12x_3x_4>0.
\]
In the **balanced four-subtree**, its two cherries merge at ages \(x_1\) and \(x_1+x_2\), the resulting four-leaf clade merges at age \(x_1+x_2+x_3\), and
\[
25(V_3-V_2)
=3x_2^2+2x_2x_3+2x_2x_4+2x_3^2+4x_3x_4>0.
\]
Cherry relabeling handles the reverse order of their ages. Every coefficient on the right sides is nonnegative, and some strictly positive term is present under strictly positive internal edge lengths. Thus no root-one-versus-four tree has \(V_2>V_3\); two separated strict maxima are impossible.

**Sharpness and smaller orders.** For \((H,a,b,c)=(10,1,6,7)\), the eight edge lengths are \((1,1,9,7,6,6,1,3)\), all positive. Substitution yields the displayed sequence, with \(V_2-V_3=105/100>0\) and \(V_4-V_3=12/100>0\). For \(n\le4\), ultrametricity gives \(V_1=0\) and exhaustive sampling gives \(V_n=0\). There are fewer than three interior sample depths, so no two distinct *nonadjacent* strict local maxima can occur. Thus the order-five obstruction and witness are sharp.

## Verification
The accompanying `verify.py` uses only the Python 3 standard library. It constructs the two root-one-versus-four trees and the root-two-versus-three tree with formal rational-linear edge lengths, enumerates all leaf subsets, computes exact quadratic variance polynomials, and compares four critical identities coefficient by coefficient. It also independently reconstructs the eight strictly positive witness edges and directly enumerates the exact witness variances at all five sampling depths. Execute `python3 verify.py` in the directory containing that file; successful output is `VERIFY_OK identities=4 exact_subset_profiles=5 witness_positive_edges=8`. The unrestricted shape theorem follows from the algebraic sign identities; finite witness checks alone would not prove it.

## Relationship to prior work
Nipperess and Matsen (arXiv:1208.6552; published 2013) established the general exact mean and variance formulas for rooted and unrooted phylogenetic diversity under hypergeometric rarefaction. Their rooted variance expression applies to every tree here and is therefore prior coverage of the *formula*, not a new contribution of this result. The present theorem instead classifies the first possible double-modal variance profile by **root topology** and gives necessary and sufficient branch-age inequalities for its nonempty region. Its exclusion of both root-one-versus-four shapes requires the two positivity identities above. Neither the main text, methods, results, discussion, nor appendix of that full text states the root-topology obstruction or this two-peak phase criterion. Chao and collaborators (2015) study rarefaction and extrapolation of expected phylogenetic diversity, with a distinct unconditional estimator-variance problem. O'Dwyer, Kembel and Green (2012) treat metacommunity sampling distributions and variance under a different sampling framework; their inspected discussion does not classify these exact fixed-size five-tip variance profiles.

## Limitations
This is a complete structural theorem for up to five tips only, under fixed-size without-replacement sampling of **distinct species**, strict ultrametricity, and fully binary rooted trees with positive edges. It does not establish a bound on the number of modes for general larger trees, unrooted diversity, sampling with replacement, repeated observations per taxon, estimated phylogenies, uncertain branch lengths, or unconditional estimator variance. General existing formulas may yield further related special cases; a specialized prior classification outside the inspected literature cannot be excluded. No empirical ecological effect is inferred.

## References
1. Nipperess, D. A., and Matsen IV, F. A. (2012 preprint; 2013 article), *The mean and variance of phylogenetic diversity under rarefaction*. arXiv:1208.6552, https://arxiv.org/abs/1208.6552; DOI 10.1111/2041-210X.12042. Original preprint public 2012-08-31 UTC.
2. Chao, A., Chiu, C.-H., and Jost, L. (2015), *Rarefaction and extrapolation of phylogenetic diversity*. Methods in Ecology and Evolution. DOI 10.1111/2041-210X.12247.
3. O'Dwyer, J. P., Kembel, S. W., and Green, J. L. (2012), *Phylogenetic Diversity Theory Sheds Light on the Structure of Microbial Communities*. PLOS Computational Biology 8:e1002832, DOI 10.1371/journal.pcbi.1002832.
