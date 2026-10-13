# A sharp ten-tip obstruction to single-depth phylogenetic-diversity sampling identification

## Finding

For each integer \(n\), let \(\mathcal T_n\) be the finite set of rooted, unordered, fully binary tree **shapes** with \(n\) leaves. Every edge has length one. Choose exactly \(k\) distinct tips uniformly without replacement, and let \(D_{T,k}\) be the number of edges in the union of the chosen tips' root-to-tip paths. The observation is the full probability distribution of this single integer, with tip identities erased.

**Theorem (sharp ten-tip obstruction and complete first two-depth designs).** For every \(4\le n\le9\), the law of \(D_{T,2}\) distinguishes all members of \(\mathcal T_n\). At \(n=10\), all individual sampling depths \(k\in\{1,\dots,9\}\) have a collision between nonisomorphic trees. The **exact** pairs of depths for which their two full distributions together distinguish all 98 ten-tip shapes are
\[
\{1,3\},\ \{1,4\},\ \{1,5\},\ \{2,3\},\ \{2,4\},\ \{2,5\},\ \{2,6\},\ \{2,7\},\ \{2,8\}.
\]
In particular, the smallest number of leaves at which a single-depth complete distribution fails to identify every shape is ten, and the minimum number of distinct depths at ten leaves is two.

## Assumptions and scope

Tree shapes are nonplane (interchanging either pair of child subtrees does not change the tree), rooted and full binary (each internal vertex has two children). There are no labels, the root has no incoming stem edge, and **every** parent-child edge has length exactly one. These conventions are essential. For nonempty \(S\) of leaves, define rooted phylogenetic diversity by
\[
\operatorname{PD}_T(S)=\Bigl|\bigcup_{v\in S}E(\text{root-to-}v\text{ path})\Bigr|.
\]
For \(k=0\), the diversity is zero. For \(1\le k\le n\), choose \(S\) uniformly from all \(\binom nk\) unordered subsets, and set \(D_{T,k}=\operatorname{PD}_T(S)\). The theorem asks whether the map from *unlabeled shape* to one or two entire sampling laws is injective for fixed \(n\). Exact laws are idealized observations, not finite-sample estimates.

## Proof

**1. Counting polynomial.** Define the bivariate integer polynomial
\[
F_T(z,t)=\sum_{S\subseteq L(T)}z^{|S|}t^{\operatorname{PD}_T(S)}.
\]
For the one-leaf tree \(L\), \(F_L=1+z\). For a root with two children \(U,V\), let \(F_U^{+}=1+t(F_U-1)\), which counts the child-edge length one if and only if at least one leaf in that child is chosen. Independence of the *combinatorial choices*, not of the random variables, gives the exact identity
\[
\boxed{F_{(U,V)}(z,t)=\bigl[1+t(F_U(z,t)-1)\bigr]\bigl[1+t(F_V(z,t)-1)\bigr].}
\]
Thus \([z^kt^d]F_T\) is precisely the number of \(k\)-subsets with diversity \(d\), and their probabilities equal this integer divided by \(\binom nk\). Equality of complete laws is equivalent to equality of these integer coefficient vectors; there is no rounding or statistical approximation.

**2. Exhaustive and nonredundant shape generation.** Recursively construct \(\mathcal T_1=\{L\}\). For each \(n\ge2\), form all pairs \((U,V)\) with \(U\in\mathcal T_a\), \(V\in\mathcal T_b\), \(a+b=n\), and \(a\le b\); when \(a=b\), require the index of \(U\) in the fixed recursive order to be no greater than that of \(V\). Inductively every rooted full binary nonplane shape has such a root split, and this size-and-index ordering gives it exactly once. The resulting counts for \(1\le n\le10\) are
\[
1,1,1,2,3,6,11,23,46,98.
\]
The accompanying integer checker implements the recurrence, this canonical enumeration, and every equality comparison. In a **separate** calculation it forms each root-to-tip edge set, enumerates all \(2^n\) sampled subsets of each shape, and counts the union of edge sets directly. It checks equality of the two resulting full bivariate integer tables for all 192 shapes through ten leaves, namely 131,726 marked subsets overall. The finite statement follows from the exhaustive iteration and its explicit assertions, not from extrapolation of observed patterns.

**3. One-depth and two-depth collision certificates.** At \(4\le n\le9\), all \(k=2\) coefficient vectors are different. At ten leaves, the numbers of unordered colliding pairs of distinct shapes for respective depths \(k=1,2,3,4,5,6,7,8,9\) are exactly
\[
94,1,13,39,102,232,576,1654,4753.
\]
Every entry is positive, so no single depth is sufficient. For two depths, an ambiguity survives exactly when its unordered shape pair lies in the intersection of the two depth-specific collision sets. Inspecting these nine finite sets for every one of the \(\binom92\) possible depth pairs yields empty intersection at exactly the nine pairs in the theorem, and nonempty intersection at all others. This proves both sufficiency and completeness.

**4. Explicit obstruction at the best single depth.** Write \(L\) for a leaf and \((U,V)\) for a root joining children. The distinct ten-leaf shapes
\[
A=\bigl((L,(L,(L,L))),((L,(L,L)),(L,(L,L)))\bigr),
\]
\[
B=\bigl((L,((L,L),(L,L))),((L,L),(L,(L,L)))\bigr)
\]
have different root subtree sizes: \(4+6\) for \(A\), and \(5+5\) for \(B\); hence they are not isomorphic. Nevertheless their singleton branch-count histogram is the same, with counts \(1,3,6\) at diversities \(2,3,4\). Their two-tip histograms coincide, with count \(1\) at diversity \(4\), \(14\) at \(5\), \(10\) at \(6\), \(12\) at \(7\), and \(8\) at \(8\). The distinct three-tip distributions separate them. The exhaustive collision set at depth two consists **only** of this pair.

## Verification

Run `python3 phylo_sampling_verify.py` with standard Python 3; no dependencies beyond the standard library. The script independently checks every generated shape's dynamic-programming coefficients against direct enumeration of all leaf subsets and validates every theorem assertion, including the one-depth collisions, all 36 two-depth design tests, and the explicit witness. The expected terminal output is

`VERIFY_OK shapes_through_10=192 direct_subsets=131726 pair_ambiguity_10=1 admissible_two_depth_designs=9`

The implementation is a finite exhaustive proof certificate that terminates on the specified domain. Its direct subset enumeration does not claim to establish any infinite-family result.

## Relationship to prior work

Pachter and Speyer reconstruct weighted phylogenetic trees from **labeled** multi-tip subtree weights. Their known-subset-to-weight data retain substantially more information than a histogram with identities erased; therefore that result does not imply single-depth histogram identification. Faller, Pardi and Steel provide exact rooted phylogenetic-diversity distribution algorithms for independent tip survival on a **known** input tree; such forward distribution methods do not answer the reverse injectivity or optimal-depth problem. Nipperess and Matsen develop mean and variance of phylogenetic diversity under rarefaction, which are coarser statistics than the full law analyzed here. The polynomial recurrence is an elementary exact specialization of forward distribution calculations; no novelty is asserted for computing PD laws on a fixed tree. The claimed new finite result is the sharp one-versus-two depth **shape-identification classification**.

## Limitations

The classification is exact for the specified nonplane rooted fully binary *unit-edge* trees of at most ten leaves. It does not extend without proof to unequal or unknown branch lengths, tip-labeled trees, models with multifurcations, phylogenetic diversity using unrooted minimal connecting subtrees, or any number of leaves above ten. The full law is assumed known without estimation error. This work supplies no field-sampling error bounds or ecological reconstruction guarantees under noise. A previously unindexed explicit tree-shape histogram census might subsume the finite classification; the bibliography checks cannot establish absence of all prior results.

## References

1. L. Pachter and D. Speyer, *Reconstructing Trees from Subtree Weights*, arXiv:math/0311156 (first posted 11 November 2003), https://arxiv.org/abs/math/0311156.
2. B. Faller, F. Pardi and M. Steel, *Distribution of Phylogenetic Diversity under Random Extinction*, arXiv:0708.0425 (first posted 2 August 2007), https://arxiv.org/abs/0708.0425.
3. D. A. Nipperess and F. A. Matsen, *The Mean and Variance of Phylogenetic Diversity under Rarefaction*, arXiv:1208.6552 (2012), https://arxiv.org/abs/1208.6552.
