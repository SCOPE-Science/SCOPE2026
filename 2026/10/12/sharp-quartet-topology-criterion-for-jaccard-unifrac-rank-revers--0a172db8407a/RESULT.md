# Sharp quartet topology criterion for Jaccard–UniFrac rank reversal

## Finding

**Theorem (complete four-tip, equal-richness criterion).** Consider a rooted, strictly bifurcating ultrametric phylogenetic tree with at most four tips, positive edge lengths, and crown root at the most recent common ancestor of all its tips. Fix a species richness \(r\): every community compared is a nonempty \(r\)-element subset of the common tip set. A **strict rank reversal** means two unordered pairs of distinct communities \((A,B)\) and \((C,D)\) such that their Jaccard distances and rooted unweighted UniFrac distances rank the pairs in opposite strict orders:
\[
\bigl(J(A,B)-J(C,D)\bigr)\bigl(U(A,B)-U(C,D)\bigr)<0.
\]

Such a reversal is possible if and only if the tree has exactly four tips, \(r=2\), its rooted shape is balanced (two root-descendant cherries), and its two root-to-cherry stem lengths \(aH\) and \(bH\), expressed relative to the common root-to-tip height \(H>0\), obey
\[
0<a,b<1,\qquad (a+b)\bigl(4-\min\{a,b\}\bigr)>4.
\]
No rooted pectinate (caterpillar) ultrametric four-tip tree with positive branches admits a strict reversal between equal-richness communities. In the symmetric balanced case \(a=b=t\), the sharp condition reduces to \(t>2-\sqrt2\). Whenever reversal is possible, it can be witnessed by just three communities, comparing two distances from a common reference.

More quantitatively, on four tips with two-tip communities define the **maximum UniFrac ranking-defect margin**
\[
M(T)=\max_{\substack{|A|=|B|=2\\|A\cap B|=1}}U(A,B)
-\min_{\substack{|C|=|D|=2\\C\cap D=\varnothing}}U(C,D).
\]
The maxima and minima range over distinct pairs of subsets of the same four tips. For a balanced tree,
\[
\boxed{M(T)=\frac{(a+b)(4-m)-4}{(3-m)(4-a-b)},\qquad m=\min\{a,b\}.}
\]
For a pectinate tree, label the isolated root daughter as tip \(1\), the intervening daughter as tip \(2\), and the deepest cherry as tips \(3,4\). If the root-to-three-tip-clade height is \(aH\) and the root-to-deepest-cherry height is \(bH\), so \(0<a<b<1\), then
\[
\boxed{M(T)=-\frac{(4-a)(1-b)}{(3-a)(4-a-b)}<0.}
\]
Thus the formula measures both the sharp reversal threshold and the greatest possible normalized phylogenetic-distance discrepancy opposing the taxonomic ranking.

## Assumptions and scope

The data are binary presence/absence subsets, with no abundance weights. Branch lengths are strictly positive; every tip is exactly distance \(H\) from the crown root, and no ancestral stem above that root is included. In particular, UniFrac always uses **the same fixed rooted reference tree**: a branch contributes to a given comparison exactly when at least one of its descendant tips occurs in either community, even if their union omits another branch of the reference tree. We do not reroot each pair's reduced tree at a different ancestor.

For any distinct nonempty subsets \(A,B\), Jaccard dissimilarity is
\[
J(A,B)=\frac{|A\mathbin\triangle B|}{|A\cup B|}.
\]
For each rooted edge \(e\), write \(D_e\) for its set of descendant tips, and let \(p_e(A)=\mathbf1_{\{D_e\cap A\ne\varnothing\}}\). With edge length \(\ell_e>0\), rooted unweighted UniFrac is
\[
U(A,B)=\frac{\sum_e\ell_e|p_e(A)-p_e(B)|}
{\sum_e\ell_e\max\{p_e(A),p_e(B)\}}.
\]
Every denominator here is positive. UniFrac is invariant under common scaling of all edge lengths, so we use \(H=1\) in the proof. A comparison always involves two distinct communities. Strict reversal excludes ties on either metric. The assertion concerns **existence of two comparisons**, rather than all pairwise distances being equal or globally linearly related.

## Proof

**1. Minimal number of tips and richness.** If a common tip set has at most three tips and all communities have one fixed positive cardinality, the Jaccard distance between any two distinct such communities is constant. For one-tip communities it is \(1\); for two-tip communities on three tips it is \(2/3\); at full richness there is only one community. Hence strict reversal is impossible. On four tips, cardinalities \(1\) and \(3\) likewise give constant Jaccard distances across distinct pairs, and cardinality \(4\) yields only one community. For \(r=2\), two distinct communities either overlap in one tip, giving \(J=2/3\), or are disjoint, giving \(J=1\). Thus it suffices to determine the largest UniFrac distance among the \(12\) overlapping comparisons and the smallest among the \(3\) disjoint comparisons. A strict reversal occurs precisely when their difference \(M(T)\) is positive.

**2. Balanced quartet.** Relabel the sister-tip pairs as \(\{1,2\}\) and \(\{3,4\}\). Set the crown-to-cherry stems to \(a,b\) and terminal edges to \(1-a,1-a,1-b,1-b\), respectively. Directly substituting each of the six two-tip communities into the edge-incidence formula above gives this *complete multiset* of \(12\) overlapping-comparison UniFrac distances:
\[
\begin{array}{c|c}
\text{score}&\text{multiplicity}\\\hline
f(a)=(2-a)/(3-a)&4\\
f(b)=(2-b)/(3-b)&4\\
g(a)=2(1-a)/(3-a)&2\\
g(b)=2(1-b)/(3-b)&2
\end{array}
\]
and the \(3\) disjoint-comparison distances are \(1\) once and
\[
C=\frac{2(2-a-b)}{4-a-b}
\]
twice. For \(0<x<1\), \(f(x)>g(x)\), and \(f\) strictly decreases. Therefore the largest overlapping distance is \(f(m)\) with \(m=\min\{a,b\}\). The smaller disjoint distance is \(C<1\). Elementary subtraction gives the exact signed margin
\[
f(m)-C=\frac{(a+b)(4-m)-4}{(3-m)(4-a-b)}.
\]
Both denominators are positive. This proves the balanced criterion and margin.

For a same-reference witness when \(a\le b\), compare \(\{1,3\}\) with \(\{2,4\}\) (disjoint) and with \(\{1,2\}\) (overlap). The respective Jaccard distances are \(1\) and \(2/3\); their UniFrac distances are \(C\) and \(f(a)\). If \(b<a\), replace the overlapping comparison by \(\{1,3\}\) versus \(\{3,4\}\), with UniFrac \(f(b)\). Both are strict reversals exactly when the displayed inequality holds. At \(a=b=t\), the numerator is \(2t(4-t)-4\), which is positive in \((0,1)\) precisely for \(t>2-\sqrt2\).

**3. Pectinate quartet.** The six edges have descendant-tip sets and lengths
\[
(\{1\},1),\ (\{2,3,4\},a),\ (\{2\},1-a),\ (\{3,4\},b-a),\ (\{3\},1-b),\ (\{4\},1-b)
\]
with \(0<a<b<1\). Write \(f(x)=(2-x)/(3-x)\) and \(g(x)=2(1-x)/(3-x)\). The complete multiset of UniFrac scores for the twelve overlapping pairs is
\[
\begin{array}{c|c}
\text{score}&\text{multiplicity}\\\hline
f(a)&4\\
g(a)&2\\
f(b)&2\\
g(b)&1\\
2(1-b)/(3-a-b)&1\\
(2-a-b)/(3-a-b)&2
\end{array}
\]
and the three disjoint scores are
\[
\frac{4-2a-b}{4-a-b}\quad\text{once},\qquad
\frac{4-a-2b}{4-a-b}\quad\text{twice}.
\]
Because \(a<b\), one has \(f(a)>f(b)>g(b)\), \(f(a)>g(a)\), and \(f(a)>f(a+b)=(2-a-b)/(3-a-b)\). The last remaining overlapping score is smaller than \(f(a)\), since
\[
f(a)-\frac{2(1-b)}{3-a-b}
=\frac{(4-a)(b-a)+a}{(3-a)(3-a-b)}>0.
\]
Thus the largest overlap score is \(f(a)\). The smallest disjoint score is \((4-a-2b)/(4-a-b)\) because \(b>a\). Their exact difference is
\[
f(a)-\frac{4-a-2b}{4-a-b}
=-\frac{(4-a)(1-b)}{(3-a)(4-a-b)}<0.
\]
This is the asserted pectinate margin and excludes strict rank reversal for **every** allowed pectinate branch-length choice.

The two rooted bifurcating tree shapes exhaust the possibilities for four tips. Together with step 1 and the witness in step 2, this completes the theorem.

## Verification

The self-contained file `check_unifrac.py` evaluates edge descendant indicators directly with Python's `fractions.Fraction` and recomputes the complete distance multiset, independent of the displayed algebraic scores. Run from the directory containing the file:

```sh
python3 check_unifrac.py
```

The completed execution returned:

```text
VERIFY_OK profiles=2262 classifies_reversal=630 direct_pair_scores=33930
```

It checks both shapes for all relevant pairs of rational branch parameters with denominator \(40\), verifying the complete score-profile multiplicities, the stated reversal criterion, and absence of reversals for one-tip and three-tip communities. It additionally checks a shared-reference witness, including exact values \(J=1\), \(U=2/5\), \(J=2/3\), and \(U=5/9\) for \(a=b=3/4\). These finite tests are **not** substitutes for the algebraic proof covering all real branch lengths.

## Relationship to prior work

Lozupone and Knight (2005) introduced UniFrac as unique phylogenetic branch length divided by branch length present in the union of two communities. Ives and Helmus (2010), particularly their Appendix C, expressed UniFrac in a broader phylogenetic similarity framework and contrasted it with taxonomic similarity and other indices. Jin et al. (2015) empirically compared Jaccard and UniFrac with other measures and discussed dependence on phylogenetic depth. These sources supply the indices and the ecological motivation for controlling community richness. Their inspected statements do **not** give the smallest-tip theorem, the balanced-versus-pectinate distinction, or the exact branch-length margin. The new assertion is an order-theoretic classification derived from, rather than a new definition of, the established measures.

## Limitations

The classification is limited to at most four taxa, **fixed common richness across all communities**, strictly bifurcating rooted ultrametric reference trees with strictly positive edges, and the explicitly defined unweighted rooted UniFrac normalization. An additional ancestral stem, a different pairwise-pruning or root convention, unequal community richness, polytomies, or more than four taxa may change the ordering. Neither environmental inference nor any biological population-dynamic conclusion follows from the rank criterion. Although targeted literature and database searches found no covering exact classification, a broader unindexed result about weighted Jaccard distances on trees could still imply this special case; independent literature audit has not been performed.

## References

1. Lozupone, C. and Knight, R. (2005), *UniFrac: a New Phylogenetic Method for Comparing Microbial Communities*, Applied and Environmental Microbiology **71**, 8228–8235. DOI: 10.1128/AEM.71.12.8228-8235.2005. Public online date: 2005-12-01. https://journals.asm.org/doi/full/10.1128/aem.71.12.8228-8235.2005
2. Ives, A. R. and Helmus, M. R. (2010), *Phylogenetic Metrics of Community Similarity*, The American Naturalist **176**, E128–E142, including Appendix C. DOI: 10.1086/656486. https://www.journals.uchicago.edu/doi/full/10.1086/656486
3. Jin, L. S. et al. (2015), *Phylogenetic turnover patterns consistent with niche conservatism in montane plant species*, Journal of Ecology. DOI: 10.1111/1365-2745.12385. https://besjournals.onlinelibrary.wiley.com/doi/10.1111/1365-2745.12385
