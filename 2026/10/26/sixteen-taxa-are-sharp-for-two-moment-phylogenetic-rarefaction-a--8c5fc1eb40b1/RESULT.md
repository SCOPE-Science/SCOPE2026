# Sixteen taxa are sharp for two-moment phylogenetic-rarefaction ambiguity

## Finding

**Theorem.** Among non-plane rooted full binary phylogenetic trees with unit edge lengths and \(n\) distinct tip species, the entire pair of rarefaction curves \((\mathbb E Y_k,\operatorname{Var}Y_k)_{k=1}^n\), where \(Y_k\) is *rooted* phylogenetic diversity of a uniformly sampled \(k\)-subset of tips, distinguishes the unlabelled rooted tree shape for every \(n\le15\), but not for \(n=16\). At \(n=16\) precisely one pair of nonisomorphic unlabelled shapes has identical curves. Nonidentifiability persists at every \(n\ge16\).

Let \(A=(\ast,(\ast,(\ast,\ast)))\) be the four-tip caterpillar and \(B=((\ast,\ast),(\ast,\ast))\) the balanced four-tip tree. The 16-tip witnesses are
\[
T_{\mathrm g}=((A,A),(B,B)),\qquad T_{\mathrm m}=((A,B),(A,B)).
\]
They share the complete first- and second-moment curves, but their two-tip *third raw and centered moments differ*:
\[
\mathbb E Y_2^3(T_{\mathrm g})-\mathbb E Y_2^3(T_{\mathrm m})=-\frac1{20}.
\]
Their two-tip phylogenetic-diversity frequencies (counting the \(\binom{16}{2}=120\) unordered tip pairs) are respectively \((5{:}7,6{:}20,7{:}37,8{:}20,9{:}36)\) and \((5{:}6,6{:}27,7{:}18,8{:}45,9{:}20,10{:}4)\). The example gives a precise limit to topology reconstruction using only the first two diversity-rarefaction curves.

## Assumptions and scope

Every tree is a finite unlabelled *non-plane* rooted full binary shape with \(n\ge2\) distinguishable tips once temporarily indexed for sampling; no degree-two interior vertices, no extra stem above the root, and one unit of length per edge. The biological labels are exchangeable: comparisons concern rooted shape up to isomorphism, not recovery of named tip labels. Sample \(K\) uniformly without replacement from all \(\binom nk\) subsets of size \(k\), for every integer \(1\le k\le n\). Set \(Y_k\) equal to the number of edges in the union of root-to-tip paths for tips in \(K\); in particular singletons have nonzero rooted diversity. The result does not concern unrooted PD, arbitrary branch lengths, abundance-weighted sampling, or stochastic phylogenetic evolution.

## Proof

**1. Exact moment signature.** For each nonroot edge \(e\), let \(S_e\) be its nonempty distal leaf set and \(s_e=|S_e|\). Put
\[
q_k(s)=\frac{\binom{n-s}{k}}{\binom nk},\qquad
\binom rk=0\ \text{for }k>r.
\]
The indicator \(I_e(K)=\mathbf1_{K\cap S_e\ne\varnothing}\) satisfies \(Y_k=\sum_eI_e\). Thus
\[
\mathbb E Y_k=\sum_e(1-q_k(s_e)),
\]
\[
\mathbb E Y_k^2=\sum_e(1-q_k(s_e))+
2\sum_{e<f}[1-q_k(s_e)-q_k(s_f)+q_k(|S_e\cup S_f|)].
\]
These are direct inclusion-exclusion identities. Hence all first and second moments depend only on the multiset of clade sizes and the multiset of pairwise clade-union sizes.

Conversely, for fixed \(n\), equality of the first-moment curves implies equality of clade-size multisets. There are exactly \(n\) unit terminal edges of size \(1\); the other \(n-2\) edges have sizes \(2,\ldots,n-1\). The difference of first-moment curves is a linear combination \(\sum_{s=2}^{n-1} a_s q_k(s)\). Put \(r=n-s\). For \(1\le r,k\le n-2\), the matrix \((\binom rk)\) is lower triangular with diagonal \(1\), after the common nonzero row scalings \(\binom nk^{-1}\); therefore its columns are linearly independent. All \(a_s\) vanish. Once these sizes are known, equality of second-moment curves likewise implies equality of pairwise clade-union histograms for sizes \(2,\ldots,n-1\), by the same triangular argument. The union-size \(n\) count is then fixed by \(\binom{2n-2}{2}\) and the remaining histogram entries. This proves the equivalence: the two entire moment curves agree **if and only if** the two finite multisets agree.

**2. An equal-subtree interchange.** Let \(A,B,C,D\) be four arbitrary rooted binary subtrees with the same number \(m\ge1\) of tips, and define \(U=((A,B),(C,D))\), \(V=((A,C),(B,D))\). Their clade-size multisets coincide. Their pairwise clade-union multisets also coincide, as follows. Partition all nonroot edges into the four internal subtree edge collections (including each subtree's incoming edge from its two-block parent) and the two edges entering the two-block parents. Every edge in a fixed subtree retains its size, and any two edges in distinct subtrees have disjoint distal sets with union size equal to the sum of their individual sizes. Pairs wholly within one subtree are unchanged. For an edge with distal size \(s\) in a bottom subtree, the pair with its enclosing two-block edge has union size \(2m\), while the pair with the other two-block edge has union size \(2m+s\), regardless of grouping. The two two-block edges have union size \(4m\); their individual sizes are \(2m\). Therefore all two-edge union multisets agree. Note that the edges entering the four subtrees are included in their fixed collections. Combining with Step 1 proves complete first- and second-moment equality.

For the displayed choice \(C=A\), \(D=B\), with \(m=4\) and \(A\not\cong B\), the two trees are not isomorphic: the root children of \(T_{\mathrm g}\) have respective identical-child splits \((A,A)\), \((B,B)\), while both root children of \(T_{\mathrm m}\) have nonisomorphic child subtrees \((A,B)\).

**3. Exact distinction at third order.** For \(k=2\), direct enumeration of all \(120\) unordered tip pairs yields the histograms displayed in the finding. Each of the two trees has total \(Y_2\)-sum \(898\) and squared sum \(6904\). The cubed totals are \(54370\) and \(54376\), so the raw third-moment gap is \(-6/120=-1/20\). The centered third moments have the same gap because both first and second moments coincide. These counts are reproduced by the standalone exact checker.

**4. Sharp minimality through 16 tips.** A rooted non-plane full binary shape on \(n\) tips is either the singleton when \(n=1\), or a unique unordered pair of shapes on \(a\) and \(n-a\) tips, with \(1\le a\le n-a\), and a canonical tie-breaking order when \(a=n-a\). `pd_moment_checker.py` implements precisely this complete induction and computes each tree's two integer signatures using leaf-set bitmasks. It checks every shape for \(n=2,\ldots,16\). The numbers of shapes are
\[
1,1,2,3,6,11,23,46,98,207,451,983,2179,4850,10905
\]
for \(n=2,\ldots,16\) in order. There are zero colliding unordered pairs of distinct shapes for \(n\le15\), and exactly one for \(n=16\), identified with \((T_{\mathrm g},T_{\mathrm m})\). The theorem's minimality and uniqueness at 16 are exact exhaustive finite statements, with a completely specified enumerable search, not extrapolations from random samples.

**5. All larger tip counts.** If two \(n\)-tip shapes have the same two moment signatures, attach a fresh singleton tip and the original tree as the two children of a new root. Old clades and pairwise unions remain unchanged. The two added edges have clade sizes \(1\) and \(n\); their respective unions with an old clade of size \(s\) have sizes \(s+1\) and \(n\), and with one another have size \(n+1\). These additions depend only on the prior signatures. Moreover the old-tree child remains identifiable as the unique root child of size \(n>1\), so distinct old shapes remain distinct. Induction gives witness pairs for every \(n\ge16\).

## Verification

Run `python3 pd_moment_checker.py` and compare its deterministic JSON output with `pd_moment_certificate.json`. The checker uses no nonstandard Python packages; it creates all non-plane rooted binary shapes through 16 tips, computes complete clade-size and pair-union signatures with exact integer bit operations, identifies the unique 16-tip collision, and independently enumerates all \(2^{16}-1\) nonempty sampled tip subsets for each witness to check equality of moment numerators at every sample size. It separately enumerates all 120 two-tip subsets and checks both histograms and third-moment gap. The analytical equal-subtree interchange and induction handle all larger trees; the exhaustive computation is used only to certify the finite sharp cutoff and explicit histograms.

## Relationship to prior work

Nipperess and Matsen (first publicly posted 31 August 2012; journal 2013) derived the general exact expectation and covariance formulas for phylogenetic diversity under rarefaction. These formulas are established foundations of Step 1, not claimed as new. Fischer, Hamann, and Wicke (2025) examine rooted-tree clade-size sequences and show that distinct nine-tip shapes can already have the same clade-size profile; this explains why the *mean alone* is insufficient, and is not the present claim. Our comparison concerns the stronger pair of *entire first- and second-moment curves*: the 16-tip sharp cutoff, the unique finite collision, its third-moment separation, and the large-tree interchange principle are different assertions. The 2015 rarefaction overview treats use of mean and variance in diversity applications, without this topological cutoff. The originality comparison is subject to literature-indexing limits; an equivalent result in another phylogenetic identifiability literature may exist.

## Limitations

The finite cutoff is established by a reproducible exhaustive canonical enumeration through 16 tips, not a closed classification formula for arbitrary shape families. The extension to all larger sizes is analytic. Moment equivalence is an exact-population property; finite estimates of curves may behave differently. Identifiability is of unlabelled rooted topology conditional on equal unit branch lengths and sampling uniformly from tips. The statement makes no claims about arbitrary edge lengths, different branch-length units across trees, nonbinary trees, unrooted PD, abundance-weighted sampling, or inferential power from data. Independent scientific audit has not been performed.

## References

1. D. A. Nipperess and F. A. Matsen IV, *The mean and variance of phylogenetic diversity under rarefaction* (arXiv:1208.6552, first posted 2012-08-31; Methods in Ecology and Evolution 4, 566–572, 2013), doi:10.1111/2041-210X.12042. https://arxiv.org/abs/1208.6552
2. D. A. Nipperess, *The Rarefaction of Phylogenetic Diversity: Formulation, Extension and Application* (2015), doi:10.1007/978-3-319-22461-9_10.
3. M. Fischer, T. N. Hamann and K. Wicke, *Metaconcepts of Rooted Tree Balance* (2025), doi:10.1007/s11538-025-01509-y.
