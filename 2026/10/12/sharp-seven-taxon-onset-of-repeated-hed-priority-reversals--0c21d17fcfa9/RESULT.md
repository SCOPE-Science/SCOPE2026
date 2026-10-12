# Sharp seven-taxon onset of repeated HED priority reversals

## Finding

**Theorem (smallest repeated pairwise HED ranking reversal).** Let \(T\) be a finite, rooted, fully binary, ultrametric phylogenetic tree with \(n\geq2\) distinct terminal taxa and strictly positive real edge lengths. Suppose all nonfocal taxa independently become extinct with one common probability \(q\in(0,1)\). Write \(\psi_x(q)\) for the heightened evolutionary distinctiveness (HED) of taxon \(x\), namely its expected marginal contribution to rooted phylogenetic diversity among the independently surviving other taxa.

If \(2\leq n\leq6\), the sign of \(\psi_x(q)-\psi_y(q)\) changes at most once on \((0,1)\), for every pair of taxa. At \(n=7\), at most two changes are possible, and this maximum is attained by an explicitly specified fully binary ultrametric tree with positive rational lengths, with strict sign changes at exactly \(q=3/10\) and \(q=4/5\). For every \(n>7\), such a two-change example also exists. Identical scores over all \(q\) are not counted as strict changes.

This theorem concerns two fixed taxa on one fixed phylogeny as the *common* extinction-risk parameter varies. It does not assert two changes in a complete taxon ranking or in scores recomputed after actual leaf deletions.

## Assumptions and scope

For a leaf subset \(S\), define rooted phylogenetic diversity \(\mathrm{PD}(S)\) as the sum of lengths of edges in the union of root-to-leaf paths for leaves of \(S\), with \(\mathrm{PD}(\varnothing)=0\). For a focal leaf \(x\), let \(S_x\) be the random set of surviving leaves other than \(x\). All of these other taxa survive independently with probability \(1-q\). The HED score is
\[
\psi_x(q)=\mathbb{E}[\mathrm{PD}(S_x\cup\{x\})-\mathrm{PD}(S_x)].
\]
The focal taxon's own probability of extinction is excluded from this conditional marginal score. We fix the topology and strictly positive edge lengths as \(q\) varies. Ultrametric means all root-to-tip path sums equal one common positive height. A *strict pairwise reversal* is an isolated point within \((0,1)\) across which the HED difference changes sign, not a tangency or an endpoint tie.

## Proof

**1. Edge formula and polynomial reduction.** For an edge \(e\), let \(C(e)\) be its set of descendant taxa and \(\ell_e>0\) its length. The edge adds to the marginal diversity of \(x\) precisely when \(x\in C(e)\) and every other descendant of \(e\) is extinct. Hence, by indicator linearity and independence,
\[
\psi_x(q)=\sum_{e\text{ on the root--}x\text{ path}}\ell_e q^{|C(e)|-1}.
\]
This is the special equal-risk case of the established rooted HED identity; we use it as an input rather than claim it as new.

Fix different taxa \(x,y\), and let \(u\) be their lowest common ancestor. Contributions from edges above \(u\) are the same and cancel. Let \(r,s\) be the sizes of the two child clades of \(u\), with \(x\) on the \(r\)-side and \(y\) on the \(s\)-side. Thus \(r,s\geq1\) and \(r+s\leq n\). For \(m\geq1\), put \(a_m\) (respectively \(b_m\)) equal to the sum of lengths of the edges below \(u\) on the path to \(x\) (respectively \(y\)) having exactly \(m\) descendant tips. Missing terms are zero. All \(a_m,b_m\geq0\), \(a_r>0\), and \(b_s>0\). Furthermore \(a_m=0\) for \(m>r\), and \(b_m=0\) for \(m>s\). Because the tree is ultrametric, the two paths below \(u\) have equal total lengths: \(\sum_m a_m=\sum_m b_m\).

Consequently,
\[
\begin{aligned}
\psi_x(q)-\psi_y(q)
 &=\sum_{m\geq1}(a_m-b_m)q^{m-1}\\
 &=(q-1)P_{x,y}(q),\\
P_{x,y}(q)
 &=\sum_{m\geq2}(a_m-b_m)(1+q+\cdots+q^{m-2}).
\end{aligned}
\]
Only the last polynomial can generate interior strict reversals.

**2. No two interior changes for at most six taxa.** If \(\min\{r,s\}=1\), the path on that side has only a pendant edge below \(u\), while all other-side nonpendant coefficients are nonnegative and its \(m\)-tip attachment edge is positive. Thus \(P_{x,y}\) has a constant strict sign (or vanishes identically when \(r=s=1\)). If both sides have at least two taxa, and \(r+s\leq6\), the only possible unordered pairs are \((2,2),(2,3),(2,4),(3,3)\). Except for \((2,4)\), all nonzero powers in \(P_{x,y}\) have degree at most one, giving at most one sign change. In the remaining case orient \(r=4,s=2\), obtaining
\[
P_{x,y}(q)=a_4(1+q+q^2)+a_3(1+q)+(a_2-b_2),
\qquad
P_{x,y}'(q)=a_4(1+2q)+a_3>0
\]
for \(0<q<1\). Hence it too has at most one zero, establishing the lower bound uniformly over all allowable positive edge lengths and all topologies.

**3. At most two interior changes for seven taxa.** If the lowest-common-ancestor subtree has at most six taxa, the preceding argument applies. Otherwise \(r+s=7\), with unordered splits \((1,6),(2,5),(3,4)\). In the first case the sign is fixed as above. In the second case, orient the five-taxon side as \(x\); then the opposing two-taxon side contributes only a constant to \(P_{x,y}\), while each positive nonpendant term from the five-side is an increasing polynomial on \((0,1)\). The edge entering the five-side has positive length, so \(P_{x,y}\) is strictly increasing and changes sign at most once. In the \((3,4)\) case \(P_{x,y}\) has degree at most two, so it has at most two strict sign changes.

**4. Seven-taxon attainment.** Take leaves \(\{i,a,b,c,j,d,e\}\), root \(\rho\), and internal nodes \(L_4,L_3,L_2,R_3,R_2\). The entire edge set, written as parent, child and exact length, is:

| Parent | Child | Length |
| --- | --- | ---: |
| \(\rho\) | \(L_4\) | \(1\) |
| \(L_4\) | \(L_3\) | \(1/10\) |
| \(L_3\) | \(L_2\) | \(7/5\) |
| \(L_2\) | \(i\) | \(3/2\) |
| \(L_2\) | \(a\) | \(3/2\) |
| \(L_3\) | \(b\) | \(29/10\) |
| \(L_4\) | \(c\) | \(3\) |
| \(\rho\) | \(R_3\) | \(11/5\) |
| \(R_3\) | \(R_2\) | \(3/50\) |
| \(R_2\) | \(j\) | \(87/50\) |
| \(R_2\) | \(d\) | \(87/50\) |
| \(R_3\) | \(e\) | \(9/5\) |

All twelve edges are positive; each of the six internal vertices has two children; and every leaf has total root-to-tip length \(4\). The path/clade formula yields
\[
\psi_i(q)=\frac32+\frac75 q+\frac1{10}q^2+q^3,
\quad
\psi_j(q)=\frac{87}{50}+\frac3{50}q+\frac{11}{5}q^2.
\]
Therefore
\[
\boxed{\psi_i(q)-\psi_j(q)=(q-1)\left(q-\frac3{10}\right)\left(q-\frac45\right).}
\]
Its signs on the three intervals \((0,3/10)\), \((3/10,4/5)\), \((4/5,1)\) are respectively negative, positive, negative. Both crossings are simple, interior and strict. At \(q=1\), all HED scores equal the root-to-tip height; the endpoint tie does not count as a reversal.

**5. Persistence at larger orders.** Given any positive-length fully binary ultrametric \(n\)-tip example of height \(h\), adjoin a new root \(\rho'\) with one child the old root via a length-\(t\) edge, and the other child a new tip via a length-\((t+h)\) edge, where \(t>0\). The resulting tree is fully binary, positive-length and ultrametric. For each of the original two focal taxa the new ancestral edge contributes the identical term \(tq^{n-1}\), so their HED difference is unchanged. Iterating gives a two-crossing example for every \(n\geq7\).

## Verification

The accompanying standalone Python 3 checker `verify.py` uses only standard-library exact rational arithmetic. It reconstructs the twelve edges, descendants and root-to-leaf heights, verifies the individual HED coefficient profiles and polynomial factorization, and independently computes HED as a weighted sum over each of the \(2^6\) surviving-subset possibilities for every one of seven focal taxa at seven rational extinction probabilities: \(3136\) exact survivor-state summands. It checks alternating strict signs and enumerates the rooted binary tree shapes through six leaves to corroborate the possible child-clade size pairs. It returns `VERIFY_OK` when all assertions pass. These computations support, but do not replace, the general algebraic proof.

## Relationship to prior work

Steel, Mimoto and Mooers (2007, Theorem III.1) introduced HED and derived the edge-product formula for heterogeneous extinction probabilities; its equal-risk specialization is the first step of the proof above. Martyn and collaborators (2012) developed efficient HED algorithms and demonstrated empirical sensitivity of HED scores and rankings to risk estimates. Fischer, Francis and Wicke (2021) investigated rankings of the distinct Fair Proportion index after actual species deletions. Kerry Manson's mathematical thesis (chapters on robustness and the outlook) likewise focuses primarily on changes after extinctions to different diversity indices and discusses HED as a related index. None of these inspected results states the present sharp first occurrence of **two interior sign reversals for the same pair under a continuously varying common HED risk**; the conclusion is limited to those materially inspected sources, not a claim of exhaustive worldwide novelty.

## Limitations

The model assumes independent and identical extinction probabilities for nonfocal taxa, one fixed binary ultrametric tree, fixed positive lengths, and rooted HED rather than an unconditional expected-loss score. A real conservation ranking may depend on taxon-specific threats, protection costs, phylogenetic uncertainty, or demographic dependence. The result does not describe the probability of losing biodiversity, full-ranking reversals, actual extinction trajectories, or the maximum number of changes on larger trees. Identification of the earliest counterexample is mathematical and does not imply that two crossings are common in empirical trees. Stronger unindexed comparisons may exist.

## References

1. M. Steel, A. Mimoto, A. Ø. Mooers, *Hedging our bets: the expected contribution of species to future phylogenetic diversity*, arXiv:0704.2649v1 (first publicly posted 20 April 2007), Theorem III.1. https://arxiv.org/html/0704.2649v1
2. I. Martyn, T. S. Kuhn, A. O. Mooers, V. Moulton, A. Spillner, *Computing evolutionary distinctiveness indices in large scale analysis*, Algorithms for Molecular Biology **7**, 6 (2012), doi:10.1186/1748-7188-7-6. https://doi.org/10.1186/1748-7188-7-6
3. M. Fischer, A. Francis, K. Wicke, *Phylogenetic Diversity Rankings in the Face of Extinctions: the Robustness of the Fair Proportion Index*, arXiv:2107.00748v1 (2021). https://arxiv.org/html/2107.00748v1
4. K. Manson, *Mathematical aspects of phylogenetic diversity measures*, doctoral thesis, University of Canterbury, chapters 5 and 8. https://ir.canterbury.ac.nz/server/api/core/bitstreams/3d4d299a-b57b-4cee-bf39-863e1b4ac05a/content
