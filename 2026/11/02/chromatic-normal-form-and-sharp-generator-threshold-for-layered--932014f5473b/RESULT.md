# Chromatic normal form and sharp generator threshold for layered \(\mathsf{S4}\) complex algebras

## Finding
Let \(P=L_1\oplus\cdots\oplus L_h\) be the ordinal sum of nonempty finite antichains, ordered from bottom to top, with \(n_i=|L_i|\), and let \(R\) be its reflexive order relation. The full modal complex algebra \(\mathcal A(P)=(\mathcal P(P),\Diamond)\) has \(\Diamond X=\{x:\exists y\in X,\ xRy\}\). For \(k\ge0\) named generators \(X_1,\ldots,X_k\subseteq P\), their membership bits give each world a colour \(c(x)\in\{0,1\}^k\); write \(q=2^k\). Define \(\delta_i=1\) precisely when \(i<h\) and \(n_{i+1}=1\), and \(\delta_i=0\) otherwise.

**Exact generation criterion.** The generators produce the entire complex algebra if and only if (i) the colours on each level are injective, and (ii) if \(L_{i+1}=\{y\}\) is a singleton, the colour of \(y\) is absent from \(L_i\). These are precisely the proper-colouring constraints for the graph whose edges form a clique in every level and connect a singleton upper level to all vertices in the immediately lower level.

**Exact generating polynomial and rank.** For every integer \(k\ge0\), the number of ordered \(k\)-tuples of generating subsets is
\[
G_P(k)=\prod_{i=1}^{h}(2^k-\delta_i)_{n_i},\qquad (z)_r=\prod_{j=0}^{r-1}(z-j).
\]
The chromatic polynomial of the stated conflict graph is \(\prod_i(q-\delta_i)_{n_i}\). Consequently the minimum cardinality of a generating family is
\[
\gamma(P)=\left\lceil\log_2\left(\max_{1\le i\le h}(n_i+\delta_i)\right)\right\rceil.
\]
Here \(\gamma(P)=0\) is permitted: the one-point frame needs no generators.

**Quantitative saturation.** For independent uniform bit-values, the probability that the \(k\) subsets generate all of \(\mathcal A(P)\) is exactly
\[
\mathbb P(\mathrm{generate})=q^{-\sum_i n_i}\prod_i(q-\delta_i)_{n_i}.
\]
For fixed \(r\ge2\) and \(h\) levels all of width \(r\), this is \(\big((q)_r/q^r\big)^h\). If \(h\to\infty\) and \(q/h\to c\in(0,\infty)\), it tends to \(\exp[-r(r-1)/(2c)]\). For a chain (all widths one), the exact probability is \((1-1/q)^{h-1}\), and its limit in the same window is \(e^{-1/c}\). The chain specialization is not claimed to be new.

## Assumptions and scope
All levels \(L_i\) are labelled, nonempty and pairwise disjoint, and all comparabilities from a lower to a higher level are present. Same-level distinct worlds are incomparable. \(R\) includes loops and hence is reflexive and transitive, so \(\mathcal A(P)\) is a finite classical Boolean modal \(\mathsf{S4}\)-algebra. Generation is by Boolean operations and the single normal modality \(\Diamond\); \(\Box\) is its Boolean dual. Generators are named and ordered. The empty family is allowed. The number of worlds and number of levels can vary freely; none of the claims concerns arbitrary posets or transitive preorders with mutually accessible distinct worlds.

## Proof
**Step 1: finite modal separation.** For a fixed colouring \(c\), define \(x\sim y\) if every Boolean modal formula in the \(k\) colour-bit predicates has the same truth value at \(x\) and \(y\). A finite Boolean subalgebra of \(\mathcal P(P)\) is all of \(\mathcal P(P)\) exactly when it separates every pair of worlds: given pairwise distinguishing sets, intersect finitely many appropriate sets or complements to define each singleton. On a finite Kripke model, modal equivalence coincides with the largest colour-preserving bisimulation. To see this directly, start with the finite partition by atomic colours and repeatedly refine a block using the set of partition blocks reached by its members. After at most \(|P|-1\) strict refinements this stabilizes; the stable partition is the maximal bisimulation partition. Each refinement block is defined by a formula using the previous-stage defining formulas and \(\Diamond\), while modal formulas are constant on bisimulation classes. Thus the full complex algebra is generated if and only if no two distinct worlds are bisimilar.

**Step 2: necessary constraints.** If two distinct \(x,y\in L_i\) have the same colour, relate \(x\) to \(y\), themselves by identity, and all strictly higher worlds by identity. The successor sets of \(x\) and \(y\) are respectively \(\{x\}\cup\bigcup_{j>i}L_j\) and \(\{y\}\cup\bigcup_{j>i}L_j\). This supplies an explicit colour-preserving bisimulation, so generation fails. Now suppose \(L_{i+1}=\{y\}\) and some \(x\in L_i\) has \(c(x)=c(y)\). The successors of \(x\) are \(\{x,y\}\cup\bigcup_{j>i+1}L_j\), while those of \(y\) are \(\{y\}\cup\bigcup_{j>i+1}L_j\). The relation identifying \(x\) and \(y\) and otherwise acting identically is a bisimulation (every unmatched successor of \(x\) can be paired with \(y\)). Therefore both conditions are necessary.

**Step 3: sufficient constraints.** Suppose both hold. Prove by downward induction on \(i\) that all points in \(L_i\cup\cdots\cup L_h\) have distinct bisimulation classes. At the top \(L_h\), distinct colours separate distinct points. Assume the higher suffix is separated and let \(x\in L_i\). Another \(x'\in L_i\) has different colour. If \(y\in L_j\) with \(j>i+1\), choose any \(z\in L_{i+1}\); \(xRz\), but all successors of \(y\) lie in levels \(\ge j\), and none is bisimilar to \(z\) by the induction hypothesis. If \(y\in L_{i+1}\) and \(n_{i+1}\ge2\), choose \(z\in L_{i+1}\setminus\{y\}\). Again \(xRz\), whereas \(y\) cannot reach \(z\) nor any world bisimilar to \(z\) by the induction hypothesis. If \(L_{i+1}=\{y\}\), then \(c(x)\ne c(y)\). Hence no new bisimilar pair occurs; downward induction proves sufficiency.

**Step 4: chromatic count.** Colour levels from the top down. The top level has \((q)_{n_h}\) injective colourings. At level \(i<h\), if \(L_{i+1}\) is singleton, exactly one already assigned colour is forbidden, giving \((q-1)_{n_i}\) injective colourings. Otherwise no colour from a higher level is forbidden, yielding \((q)_{n_i}\). Multiplication proves the formula and realizes the chromatic polynomial. Such a colouring exists if and only if \(q\ge n_i+\delta_i\) for all \(i\), which yields the stated generator number.

**Step 5: random-colour law.** There are \(q^{\sum n_i}\) equally likely assignments, giving the exact probability. For fixed \(r\), \(\log((q)_r/q^r)=\sum_{j=0}^{r-1}\log(1-j/q)=-\binom r2/q+O_r(q^{-2})\). Multiplying by \(h\) when \(q/h\to c\) yields \(\exp[-\binom r2/c]\) for \(r\ge2\). For width one, the only restrictions are inequalities across adjacent levels, giving \(q(q-1)^{h-1}\) colourings and the asserted limit.

## Verification
A standalone exhaustive checker, `checker.py`, separately implements: (a) colour-preserving bisimulation partition refinement on the actual reflexive layered relation, (b) the two local generation conditions, (c) exact chromatic-polynomial counting, and (d) direct closure under Boolean operations and \(\Diamond\), without using partition refinement. Its completed execution reports `ALL_CHECKS_OK bisim_valuations= 49510 profiles= 220 direct_closure_valuations= 2340`. The first checks cover all positive level-size compositions of up to six worlds and palettes of one to four colours whenever the assignment count is at most 1500. Direct modal-algebra closure covers every composition with at most four worlds and all four-colour assignments. These finite checks are neither an infinite-size proof nor a substitute for Steps 1–5.

For illustration, the three-world poset \(L_1\oplus L_2\) with \((n_1,n_2)=(2,1)\) has no one-generator realization because its unique upper-world colour must differ from both distinct lower-world colours; with two generators it has \(4(3)_2=24\) generating assignments. Reversing the level sizes to \((1,2)\), one generator suffices and there are \(2(2)_2=4\) generating assignments. This asymmetry distinguishes the order-semantic obstruction from ordinary same-level colour collisions.

## Relationship to prior work
Gabriel Agnew, *On Local Finiteness of Modal K4 Algebras* (arXiv:2606.02941, publicly posted June 1, 2026), establishes a global qualitative local-finiteness classification via modal towers and finite tuned partitions, not the exact number of generating predicate tuples for ordinal sums of antichains; the publicly available full text, including the main theorem and order-theoretic classification, was examined. Finite partition refinement and bisimulation are classical modal-model-theoretic tools, not new ingredients. A separate existing result for uniformly clustered total preorders counts atoms of subalgebras generated by random colourings via a support process; a total preorder has mutually accessible worlds inside its clusters, unlike the distinct incomparable points within an antichain level here. Its single-world-per-level chain case overlaps the simple chain specialization, which is credited but not offered as the novel component. The exact all-width antichain-level proper-colouring criterion, polynomial, and sharp rank formula were not found covered by the inspected primary literature or accessible comparison records. The absence of a matching search result does not establish worldwide priority.

## Limitations
The theorem applies only to finite ordinal sums of antichains with reflexive order accessibility, not arbitrary finite posets, strict-order modalities, or clusters of S4 preorders. It gives counts of ordered named generators, not a classification up to automorphisms. The asymptotic saturation law assumes fixed uniform level width and \(q/h\to c\); it is not a statement for arbitrary growing widths. Potential older algebraic-generator or distinguishing-colouring theorems under different terminology remain a historical-priority risk. The computational tests cover finite ranges only. Independent mathematical audit has not been performed.

## References
1. Gabriel Agnew, *On Local Finiteness of Modal K4 Algebras*, arXiv:2606.02941 (first public posting 2026-06-01), https://arxiv.org/abs/2606.02941.
2. Patrick Blackburn, Maarten de Rijke, and Yde Venema, *Modal Logic*, Cambridge University Press, 2001, DOI:10.1017/CBO9781107050884. Background for bisimulation and finite modal separation.
3. T. Moraschini, *Varieties of positive modal algebras and structural completeness*, arXiv:1908.01659 (2019). Distinct positive-algebra local-finiteness context.
