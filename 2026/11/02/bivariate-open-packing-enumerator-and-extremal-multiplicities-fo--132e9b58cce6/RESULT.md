# Bivariate open-packing enumerator and extremal multiplicities for Cartesian clique–path graphs

## Finding

Let \(m\geq 3\), \(n\geq 1\), and \(G_{m,n}=K_m\square P_n\). An **open packing** is a vertex set \(S\) such that \(N(u)\cap N(v)=\varnothing\) for every distinct \(u,v\in S\). Define the bivariate polynomial
\[
Q_{m,n}(x,y)=\sum_{S\text{ an open packing of }G_{m,n}}x^{|S|}y^{|E(G_{m,n}[S])|}.
\]
Thus the exponent of \(y\) records how many adjacent pairs occur inside an open packing. With \(Q_{m,0}(x,y)=1\) as a formal empty-path convention, the entire two-parameter family has the rational generating function
\[
\boxed{\sum_{n\geq0}Q_{m,n}(x,y)t^n=\frac{1+mtx+t^2x+mt^2x^2y+t^3x^2y}{1-t+(1-m)t^2x+\big((1-m)x^2y-x\big)t^3-t^4x^2y}.}
\]
In particular, the largest possible size of an open packing is \(k_n=\lceil2n/3\rceil\), and the exact number \(M_{m,n}=[x^{k_n}]Q_{m,n}(x,1)\) of maximum open packings is
\[
\boxed{M_{m,3q+2}=m(m-1)^q\quad(q\geq0),\qquad M_{m,3q+1}=(q+1)m(m-1)^q\quad(q\geq0),}
\]
\[
\boxed{M_{m,3}=m(m+1),}
\]
and, for every \(q\geq2\),
\[
\boxed{M_{m,3q}=\binom{q+1}{2}m(m-1)^q+2m(m-1)^{q-1}+(q-1)m^2(m-1)^{q-2}.}
\]
The formulas count subsets of the fixed labeled graph; they do not quotient by its automorphisms.

## Assumptions and scope

The complete graph \(K_m\) has vertices \(1,\ldots,m\). The path \(P_n\) has ordered columns \(1,\ldots,n\); two vertices \((a,i)\) and \((b,j)\) of the Cartesian product are adjacent precisely when either \(i=j\) and \(a\ne b\), or \(a=b\) and \(|i-j|=1\). All graphs are finite, undirected and simple. Empty open packings contribute the constant term one. For an open packing the induced subgraph has maximum degree at most one, so the \(y\)-statistic counts disjoint edges.

The theorem holds for all integers \(m\geq3\), \(n\geq1\). Width \(m=2\) is excluded: a two-vertex clique column admits two simultaneously selected vertices, invalidating the local encoding used here.

## Proof

**Step 1: exact local word model.** For \(m\geq3\), any two distinct vertices in the same clique column share a third vertex of that column as a neighbor. Thus an open packing selects at most one vertex per column. Encode a selected vertex \((a,i)\) by the symbol \(a\in\{1,\ldots,m\}\), and an empty column by \(0\). Distinct selected vertices in consecutive columns have a common neighbor precisely when their row labels differ; consequently nonzero adjacent symbols must coincide. Vertices selected in columns two apart have a common neighbor precisely when their row labels coincide; consequently nonzero symbols at distance two must differ. Columns farther apart cannot have a common neighbor. These conditions are necessary and sufficient, since every possible common neighbor produces a path of length two. In particular, three consecutive symbols cannot all be nonzero, and two consecutive nonzero symbols always have the same label. Each adjacent nonzero pair contributes one factor \(y\).

**Step 2: transfer proof of the complete generating function.** Introduce two leading virtual zero symbols, which are not counted as columns. After each appended symbol the admissible last-two-symbol states are \(00\), \(0a\), \(a0\), \(aa\), with \(a\) denoting any fixed nonzero row label; all transition multiplicities are independent of the actual value of \(a\). In that order, with row-to-column convention, the weighted transition matrix is
\[
T=\begin{pmatrix}
1&mx&0&0\\
0&0&1&xy\\
1&(m-1)x&0&0\\
0&0&1&0
\end{pmatrix}.
\]
For example, appending a nonzero symbol after \(a0\) has exactly \(m-1\) choices, whereas appending after \(0a\) must repeat \(a\), producing a selected edge. The unique initial state is \(00\), and every final state is allowed. Hence
\[
Q_{m,n}(x,y)=e_{00}^{\mathsf T}T^n\mathbf1,
\qquad \sum_{n\geq0}Q_{m,n}(x,y)t^n=e_{00}^{\mathsf T}(I-tT)^{-1}\mathbf1.
\]
Taking the rational inverse of this explicit four-by-four matrix yields the displayed numerator and denominator. The identity is one of formal power series with integer-polynomial coefficients; the denominator has constant term one, so no analytic convergence assumption is required.

**Step 3: largest possible size and complete equality classification.** Because no three consecutive columns can be selected, a partition of the first \(3\lfloor n/3\rfloor\) columns into triples, followed by the at most two remaining columns, gives \(|S|\leq\lceil2n/3\rceil\). The occupancy pattern consisting of consecutive pairs separated by single empty columns, truncated appropriately, attains this size; choose a row label for its first selected run and alternate between two distinct row labels from run to run. Therefore the bound is exact.

For exact maximum-set counts, a **run** means a maximal consecutive string of occupied columns. Every run has length one or two. If two runs have a single empty column between them, their row labels must differ; if there are at least two empty columns between them, their row labels may be chosen independently.

If \(n=3q+2\), a maximum packing has \(2q+2\) occupied columns and \(q\) empty columns. It must comprise exactly \(q+1\) runs, all of length two, separated by exactly one empty column. Its row labels have \(m(m-1)^q\) choices.

If \(n=3q+1\), a maximum packing has \(2q+1\) occupied and \(q\) empty columns. It must comprise \(q+1\) runs separated by exactly one empty column, exactly one of these runs being a singleton. There are \(q+1\) positions for this singleton, with \(m(m-1)^q\) row-labelings per pattern.

If \(n=3q\), a maximum packing has \(2q\) occupied and \(q\) empty columns. Either there are \(q+1\) runs (exactly two singletons, \(q-1\) doubles, and all \(q\) zeros separating runs), or there are \(q\) runs (all doubles, with one surplus zero). The first type gives \(\binom{q+1}{2}m(m-1)^q\) labeled packings. In the second type the surplus zero lies at one of two boundaries, contributing \(2m(m-1)^{q-1}\), or extends one of the \(q-1\) internal gaps to length two, contributing \((q-1)m^2(m-1)^{q-2}\) when \(q\geq2\). At \(q=1\) the latter class is absent and the first two classes contribute \(m(m-1)+2m=m(m+1)\). The classes are disjoint and exhaustive. This proves every formula.

## Verification

The included self-contained `verify_open_packing.py` uses Python standard-library integer arithmetic. It constructs each graph's adjacency masks from its definition and exhaustively examines **every vertex subset** for 16 parameter pairs with \(3\leq m\leq6\) and \(mn\leq18\). It counts open packings by cardinality and actual induced-edge number and compares every coefficient with an independently coded four-state transfer enumerator.

For \(3\leq m\leq8\) and all \(0\leq n\leq26\), it additionally checks the exact fourth-order polynomial recurrence obtained by multiplying the rational generating function by its denominator; for every positive \(n\) it tests the stated maximum-size coefficients. There are 162 recurrence/maximum cases. Executing `python3 verify_open_packing.py` prints:

```
VERIFY_OK: 16 independent all-subset graph cases; 162 exact recurrence/maximum cases
```

These finite verifications support but do not replace the all-parameter bijection, matrix calculation, and equality classification proved above.

## Relationship to prior work

Mojdeh, Peterin, Samadi and Yero established general bounds and an equality criterion for the **open packing number** of Cartesian products; see their Theorem 3.4. For a path factor, its two-independence-number bound already gives the extremal **cardinality** \(\lceil 2n/3\rceil\). That cardinality alone is not asserted to be new. Their results do not state the all-set bivariate generating function or the residue-dependent number of maximizing subsets derived here.

Brešar, Samadi and Yero identified open packings with independent sets of the common-neighbor (two-step) graph while studying injective coloring. Samadi, Soltankhah and Yero subsequently studied injective-coloring parameters for graph products. These frameworks explain why open packing is natural, but their inspected statements do not give this refined labeled-subset enumeration. The proposed contribution is the exact polynomial and full extremal multiplicity profile, not the underlying parameter or a general algorithmic hardness claim.

## Limitations

This result concerns \(K_m\square P_n\) for \(m\geq3\) and does not cover \(K_2\square P_n\), cyclic column boundaries, maximal (as opposed to maximum-cardinality) open packings, or all independent sets of unrelated common-neighbor graphs. The source comparison is based on inspected accessible primary manuscripts and indexed research records; an unindexed or unnoticed equivalent enumeration remains possible. No independent mathematical audit or independent publication-priority certification has been performed.

## References

1. D. A. Mojdeh, I. Peterin, B. Samadi, I. G. Yero, *[Open] packing number of some graph products*, Discrete Mathematics & Theoretical Computer Science 22:4 (2020), DOI 10.23638/DMTCS-22-4-1; arXiv:1901.06813 (first public version 2019-01-21). https://arxiv.org/abs/1901.06813
2. B. Brešar, B. Samadi, I. G. Yero, *Injective coloring of graphs revisited*, Discrete Mathematics 346 (2023), 113348; arXiv:2106.09823. https://arxiv.org/abs/2106.09823
3. B. Samadi, N. Soltankhah, I. G. Yero, *Injective coloring of product graphs*, Bulletin of the Malaysian Mathematical Sciences Society (2024); arXiv:2306.01488. https://arxiv.org/abs/2306.01488
