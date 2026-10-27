# The sharp ten-leaf boundary for non-unimodal rooted phylogenetic-diversity variance under rarefaction

## Finding

For rooted full binary trees with unit-length edges, the variance \(V_T(k)\) of rooted phylogenetic diversity under uniform \(k\)-leaf rarefaction is unimodal for every tree with \(1\le n\le9\) leaves, and this cutoff is sharp: the 10-leaf tree whose root children are a perfect balanced 8-leaf subtree and a 2-leaf cherry has \(V_T(1),\ldots,V_T(10)=(16/25,136/225,28/45,1306/2205,1916/3969,3884/11025,2/9,8/81,0,0)\), with \(V_T(1)>V_T(2)<V_T(3)>V_T(4)\), so its variance curve is not unimodal.

## Assumptions and scope

Let \(T\) be a rooted full binary tree with \(n\) leaves, every edge having length one. For each \(k\in\{0,\ldots,n\}\), choose a leaf subset \(S_k\) uniformly from the \(\binom{n}{k}\) subsets of size \(k\). Rooted phylogenetic diversity \(PD_T(S_k)\) is the total length of the smallest rooted subtree containing the root and all leaves in \(S_k\); the empty sample has diversity zero. Write \(V_T(k)=\operatorname{Var}(PD_T(S_k))\). A finite sequence is unimodal when it weakly increases up to some index and then weakly decreases.

The witness has a perfect balanced subtree with eight leaves as one root child and a two-leaf cherry as the other. It has eighteen edges below the root, whose descendant clades have sizes one (ten clades), two (five clades), four (two clades), and eight (one clade).

## Proof

For any rooted tree, let \(\mathcal C\) be the set of descendant-leaf clades corresponding to edges below the root. For a uniform \(k\)-subset \(S_k\), define \(I_A=\mathbf 1\{S_k\cap A\ne\varnothing\}\) for \(A\in\mathcal C\). Then \(PD_T(S_k)=\sum_{A\in\mathcal C} I_A\). Put

\[
q_A(k)=\frac{\binom{n-|A|}{k}}{\binom{n}{k}},
\]

with a binomial coefficient equal to zero when its lower index exceeds its upper index. This is the probability that the sample avoids \(A\). For distinct clades \(A,B\), the covariance of their hit indicators equals the covariance of their avoidance indicators. Therefore

\[
V_T(k)=\sum_{A\in\mathcal C}q_A(k)(1-q_A(k))
+2\sum_{\{A,B\}\subseteq\mathcal C}
\left[\frac{\binom{n-|A\cup B|}{k}}{\binom{n}{k}}-q_A(k)q_B(k)\right].
\]

For the ten-leaf witness, direct exact evaluation gives the sequence in the Finding section. In particular, \(V_T(1)=16/25=144/225\), \(V_T(2)=136/225\), \(V_T(3)=28/45=140/225\), and \(V_T(4)=1306/2205\). Thus the sequence strictly falls from \(k=1\) to \(k=2\), rises from \(k=2\) to \(k=3\), and falls again from \(k=3\) to \(k=4\), which is incompatible with unimodality.

For the lower bound, every rooted full binary tree has a plane embedding. The verifier recursively generates all plane rooted full binary shapes by every split \(i+(n-i)\) and checks every leaf subset for each shape with \(1\le n\le9\). The shape counts are the Catalan numbers \(1,1,2,5,14,42,132,429,1430\). Exact integer sums of diversity and squared diversity give exact rational variances. Every enumerated curve is unimodal, so no rooted full binary tree with fewer than ten leaves is a counterexample.

## Verification

The standalone verifier is `verification/verify_rooted_pd_unimodality.py`. It checks the Catalan shape counts, exhaustively evaluates all subsets for all rooted plane full binary shapes through nine leaves, asserts unimodality for each, confirms the witness clade-size counts, and cross-checks the witness curve both by direct subset enumeration and by the clade-covariance formula. The run returned `EXACT_CHECK_OK`; the exact variance sequence and strict inequalities are printed by the verifier.

## Relationship to prior work

Nipperess and Matsen derived exact mean and variance formulas for rooted and unrooted phylogenetic diversity under fixed-size rarefaction. Their paper supplies the relevant variance framework but does not state a unimodality theorem or a smallest-leaf counterexample. Chao and coauthors developed rarefaction and extrapolation estimators for phylogenetic diversity and used bootstrap uncertainty for estimators; that is a different variance target. Nipperess's later formulation chapter emphasizes expected-PD curves and refers variance calculations back to Nipperess and Matsen. The present result is a finite shape theorem about the conditional variance sequence itself, not a new general variance formula.

## Limitations

The sharp threshold is established only for rooted full binary trees with unit-length edges and uniform fixed-size sampling without replacement. No claim is made for unequal branch lengths, multifurcating trees, unrooted phylogenetic diversity, sampling with replacement, or empirical communities. The witness proves that universal unimodality fails at ten leaves; it does not classify the number or locations of variance peaks for larger trees.

## References

1. D. A. Nipperess and F. A. Matsen IV, “The mean and variance of phylogenetic diversity under rarefaction,” *Methods in Ecology and Evolution* 4(6), 566–572 (2013). First public preprint: arXiv:1208.6552 (2012-08-31). DOI: 10.1111/2041-210X.12042.
2. A. Chao, C.-H. Chiu, T. C. Hsieh, T. Davis, D. A. Nipperess, and D. P. Faith, “Rarefaction and extrapolation of phylogenetic diversity,” *Methods in Ecology and Evolution* 6(4), 380–388 (2015). DOI: 10.1111/2041-210X.12247.
3. D. A. Nipperess, “The Rarefaction of Phylogenetic Diversity: Formulation, Extension and Application,” in *Biodiversity Conservation and Phylogenetic Systematics*, pp. 197–217. DOI: 10.1007/978-3-319-22461-9_10.
