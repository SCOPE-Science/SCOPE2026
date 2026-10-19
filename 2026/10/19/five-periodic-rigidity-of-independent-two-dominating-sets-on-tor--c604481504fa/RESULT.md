# Five-periodic rigidity of independent two-dominating sets on toroidal grids

## Finding

For every integer \(n\ge3\), let \(G_n=C_5\square C_n\), with fixed vertex coordinates \((i,j)\in\mathbb Z_5\times\mathbb Z_n\). An *independent two-dominating set* (also called a *\((2-d)\)-kernel*) is a set \(S\subseteq V(G_n)\) containing no adjacent vertices such that every vertex outside \(S\) has at least two neighbors in \(S\).

**Theorem.** Such a set exists precisely when \(5\mid n\). When it exists, there are exactly ten, namely
\[
S_{\varepsilon,a}=\{(i,j)\in\mathbb Z_5\times\mathbb Z_n:\ i-\varepsilon j-a\equiv 1\text{ or }-1\pmod5\},
\qquad \varepsilon\in\{-1,1\},\quad a\in\mathbb Z_5.
\]
Every set has \(2n\) vertices. These ten sets are pairwise distinct, with vertex labels fixed.

In particular, \(G_{10}=C_5\square C_{10}\) has ten such sets although its factor orders are unequal and one is odd. This gives a counterexample to the *necessity* direction of Bednarz and Włoch's 2016 Theorem 2.5, which asserted existence only when both cycle orders are even or when they are equal. The other assertions of that paper, outside this comparison, are not evaluated here.

## Assumptions and scope

The cycles are simple undirected cycles, including \(C_3\), and the product is **Cartesian**, not tensor/direct. Thus \((i,j)\) is adjacent to \((i\pm1,j)\) and \((i,j\pm1)\), modulo \(5\) and \(n\). Each of those four neighbors is distinct for \(n\ge3\). The two-domination condition applies only to vertices outside \(S\), exactly as in the source's definition. We count individual labelled subsets of the fixed graph, without identifying rotations or reflections. There are no claims for other first-factor cycle lengths.

## Proof

Fix a candidate \(S\). For each \(j\in\mathbb Z_n\), define its cross-section \(A_j=\{i\in\mathbb Z_5:(i,j)\in S\}\). Independence of \(S\) forces \(A_j\) to be independent in \(C_5\), hence \(|A_j|\le2\).

First, \(A_j\) is never empty: if it were, every vertex in this column would have no vertical neighbor in \(S\); its only two possible dominating neighbors would both have to belong to \(S\). That forces all five vertices of each neighboring column into \(S\), impossible by independence. Second, \(A_j\) cannot be a singleton \(\{r\}\). The two rows \(r+2\) and \(r-2\) modulo five have no selected neighbor inside their column; two-domination forces both of those rows to be selected in **each** neighboring column. But \(r+2\) and \(r-2\) are adjacent on \(C_5\), again contradicting independence. Therefore \(|A_j|=2\) for every \(j\).

The five independent pairs of \(C_5\) each have a unique center: \(A_j=\{t_j-1,t_j+1\}\) for a unique \(t_j\in\mathbb Z_5\). Two consecutive columns must be disjoint because of the Cartesian horizontal edges. For independent pairs of this form, disjointness is equivalent to
\[
t_{j+1}-t_j\equiv +1\text{ or }-1\pmod5.
\]
Now examine the unselected vertex \((t_j+2,j)\). It has exactly one selected neighbor inside its column, namely \((t_j+1,j)\), so it requires a selected neighbor in at least one adjacent column. Among the two allowed neighboring centers, \(t_j+1\) supplies that neighbor, whereas \(t_j-1\) does not. Similarly, the vertex \((t_j-2,j)\) requires at least one neighboring center to be \(t_j-1\). Thus the two neighboring centers must be different. Since each lies in \(\{t_j-1,t_j+1\}\), necessarily
\[
\{t_{j-1},t_{j+1}\}=\{t_j-1,t_j+1\}.
\]
In particular, if \(\delta_j=t_{j+1}-t_j\in\{-1,+1\}\), this equality implies \(\delta_j=\delta_{j-1}\). Hence one fixed \(\varepsilon\in\{-1,+1\}\) satisfies \(t_j=a+\varepsilon j\pmod5\) for all columns. Cyclic consistency requires \(n\varepsilon\equiv0\pmod5\), equivalently \(5\mid n\).

Conversely, if \(5\mid n\), both orientations and all five shifts define well-defined cyclic column patterns \(A_j=\{a+\varepsilon j-1,a+\varepsilon j+1\}\). Each column is independent and neighboring columns are disjoint. Each unselected row in a column is one of \(t_j\), \(t_j+2\), \(t_j-2\). The first has two selected neighbors within its own column. Each of the other two has one selected neighbor within its column and one in an adjacent column because the neighboring centers are \(t_j\pm1\). Therefore every unselected vertex has at least two selected neighbors, proving the converse.

Finally, the center \(t_0=a\) and the signed increment \(t_1-t_0=\varepsilon\) can be uniquely recovered from the set; hence all ten sets are distinct. Every column has two selected vertices, giving \(|S|=2n\). This proves all assertions for every \(n\ge3\).

**Concrete published-criterion counterexample.** On \(C_5\square C_{10}\), choose \(\varepsilon=1\) and \(a=0\). Select precisely the pairs of vertices with row indices \(j-1\) and \(j+1\) modulo five in column \(j\); the ten-column pattern repeats the five-column sequence. This is an explicitly independent two-dominating set on cycles of unequal orders with an odd factor, contradicting the necessity in Bednarz–Włoch Theorem 2.5.

## Verification

Two independently organized, ordinary Python 3 programs accompany this report. Run `python verify_direct.py` and `python verify_transfer.py` from the extracted package directory. The former constructs every graph edge, exhaustively enumerates independent vertex subsets for \(3\le n\le6\), and checks the defining domination predicate at every outside vertex; it also tests all ten formula sets directly for every multiple of five from 5 through 80. The latter uses an independent 11-state column-mask alphabet, all 81 admissible ordered neighboring pairs, and local triple compatibility. Its transfer-matrix trace counts every cyclic configuration for all \(3\le n\le40\) and recovers two directed five-cycles as its only recurrent cycles. Complete program outputs are included. These finite checks corroborate but do not replace the arbitrary-\(n\) proof above.

## Relationship to prior work

Nagy (arXiv:1504.03224, initially public 2015-04-13) studies \(k\)-dominating independent sets, including extremal counts and Cartesian products of complete graphs. That work establishes context but does not give this \(C_5\square C_n\) characterization. Bednarz, Hernández-Cruz, and Włoch (2015) study existence and enumeration of \((2-d)\)-kernels; the portions inspected do not cover this precise product classification. Włoch (2012) develops the parameter for individual graphs and cycles, not this Cartesian two-cycle family.

The closest direct comparison is Bednarz and Włoch, *On (2-d)-kernels in the cartesian product of graphs* (2016), especially Theorem 2.5, Corollary 2.6, and their proofs on pp. 4–5. Their theorem states an incorrect necessary condition for products of two cycles. The present infinite family supplies a sharp counterexample and an exact classification along the five-cycle factor. The known \(C_5\square C_5\) case (ten patterns) is included for completeness and **is not represented as a new count**; the contradicted unequal-order cases and their all-\(n\) classification are the retained contribution. Their Cartesian product symbol is \(\times\), but the definition agrees with \(\square\) here.

## Limitations

This is a theorem for the specified \(C_5\)-factor family, not a correction of every statement in the 2016 paper, a full classification of \(C_m\square C_n\), or a result for directed/tensor graph products. The 2016 paper's existence criterion is compared using its printed full-text statement, not by inferring intent. A literature/database search cannot certify priority; equivalent reformulations in unpublished or unindexed material are a residual risk. Finite enumeration is not treated as an infinite proof.

## References

1. Z. L. Nagy, *On the number of k-dominating independent sets*, arXiv:1504.03224v1 (2015-04-13), https://arxiv.org/abs/1504.03224 ; journal DOI 10.1002/jgt.22042.
2. P. Bednarz and I. Włoch, *On (2-d)-kernels in the cartesian product of graphs*, Annales UMCS Sectio A 70(2) (2016), 1–8, DOI 10.17951/a.2016.70.2.1, https://journals.umcs.pl/a/article/download/4513/3256 . Especially Theorem 2.5 and Corollary 2.6, pp. 4–5.
3. P. Bednarz, C. Hernández-Cruz, and I. Włoch, *On the existence and the number of (2-d)-kernels in graphs*, Ars Combinatoria 121 (2015), 341–351, https://combinatorialpress.com/ars-articles/volume-121-ars-articles/on-the-existence-and-the-number-of-2-d-kernels-in-graphs/ .
4. A. Włoch, *On 2-dominating kernels in graphs*, Australasian Journal of Combinatorics 53 (2012), 273–284, https://ajc.maths.uq.edu.au/pdf/53/ajc_v53_p273.pdf .
