# Complete visibility and maximality spectra of three-row rook graphs

## Finding

**Theorem.** For every integer \(n\geq3\), let \(R_{3,n}=K_3\square K_n\). Write \(\mathcal V_n(z)=\sum_S z^{|S|}\), where the sum is over every mutual-visibility set \(S\subseteq V(R_{3,n})\); and write \(\mathcal M_n(z)=\sum_{S\text{ inclusion-maximal}}z^{|S|}\). Then

\[
\begin{aligned}
\mathcal V_n(z)={}&(1+3z)^n+n(3z^2+z^3)(1+3z)^{n-1}\\
&+3n(n-1)z^4(1+3z)^{n-2}\\
&+n(n-1)(n-2)z^6(1+3z)^{n-3},\\[2mm]
\mathcal M_n(z)={}&\bigl(n3^{n-1}+3n(n-1)\bigr)z^{n+2}\\
&+n(n-1)(n-2)3^{n-3}z^{n+3}.
\end{aligned}
\]

Every inclusion-maximal set belongs to precisely one of the three families described below, and these families are exhaustive. Under the action of \(S_3\times S_n\), independently permuting rows and columns, the number of maximal-set orbits is
\[
p_{\leq3}(n-1)+1+p_{\leq3}(n-3),
\]
where \(p_{\leq3}(k)\) counts partitions of \(k\) into at most three parts, including the empty partition of zero. In particular, maximal sets have exactly the two cardinalities \(n+2\) and \(n+3\); the fraction of inclusion-maximal sets of size \(n+3\) tends to one as \(n\to\infty\).

## Assumptions and scope

All graphs are finite, simple, undirected. Identify vertices with grid cells \((i,j)\in[3]\times[n]\), adjacent exactly when they share one coordinate and differ in the other. A subset \(S\) is a *mutual-visibility set* when for any distinct \(u,v\in S\), some shortest \(u,v\)-path has all internal vertices outside \(S\). It is *inclusion-maximal* when adding any vertex destroys the property (not merely when its size is largest). Let \(C_j=\{i:(i,j)\in S\}\subseteq[3]\) be the occupied rows of column \(j\). A *double column* has \(|C_j|=2\); a *triple column* has \(|C_j|=3\). A double column has a *pair type*: its two occupied rows.

The three disjoint families of inclusion-maximal sets are:

1. **Triple column:** exactly one column contains all three rows; each other column is any singleton.
2. **Two double columns:** exactly two columns contain distinct row pairs \(P,Q\), the unique remaining pair \(T\subseteq[3]\) is absent, and every other column is the singleton row outside \(T\).
3. **Three double columns:** exactly three columns carry, in arbitrary order, all three distinct row-pair types; every other column is any singleton.

No other columns are empty in an inclusion-maximal set. The listed family descriptions apply for every \(n\ge3\).

## Proof

**Visibility criterion.** Two occupied cells in a common row or column are adjacent and therefore mutually visible. If their row and column coordinates both differ, their distance is two and they have exactly two common neighbors, the other corners of the associated \(2\)-by-\(2\) rectangle. Both shortest paths are blocked if and only if these other two corners belong to \(S\). Consequently,
\[
S\text{ is mutual-visible}\quad\Longleftrightarrow\quad
|C_j\cap C_k|\le1\quad\text{for every }j\ne k.
\]
Equivalently, no pair of row indices occurs in two different column subsets. This equivalence is also the known graph-product criterion from Cicerone--Di Stefano--Klavžar (Lemma 3.5), and is proved here directly for the stated graph.

**All-size polynomial.** The three row pairs are the only resources consumed by columns containing at least two occupied vertices. Either there is one triple column (using all three pairs), or there are \(t\in\{0,1,2,3\}\) double columns whose pair types are all distinct; all other columns have cardinality zero or one. When \(t=0\), the contribution is \((1+3z)^n\). Choosing one triple column contributes \(nz^3(1+3z)^{n-1}\). Choosing one double contributes \(3nz^2(1+3z)^{n-1}\). Choosing two distinct double types and two distinct columns contributes \(3n(n-1)z^4(1+3z)^{n-2}\). Choosing all three types in three distinct columns contributes \(n(n-1)(n-2)z^6(1+3z)^{n-3}\). Summing the disjoint alternatives establishes \(\mathcal V_n(z)\) coefficient by coefficient.

**Maximality.** A column of cardinality zero can always receive any single vertex, so no maximal set has an empty column. If every column is a singleton, enlarging any column creates one new pair type without violating the criterion. If there is exactly one double, its missing third row may be added in that same column: the other columns have at most one element, so no pair type is repeated. Thus these cases are not maximal. A triple column forbids adding any other row to any singleton column, proving the first family.

Suppose there are two double columns of distinct pair types \(P,Q\). They cannot themselves be enlarged, since a triple would repeat a type already used in the other double. Exactly one pair type \(T\) remains unused. A singleton column with occupied row \(i\) can be enlarged precisely when it can gain an additional row \(j\) with \(\{i,j\}=T\). Therefore every remaining singleton must be the unique row outside \(T\), yielding the second family and proving sufficiency. Finally, when all three pair types occur in different double columns, every possible added vertex produces a repeated pair; this is precisely the third family. These exhaustive cases prove maximality classification.

**Counts.** Family 1 has \(n\) choices of triple column and \(3^{n-1}\) singleton fillings, giving \(n3^{n-1}\) maximal sets of cardinality \(n+2\). Family 2 has three choices of absent pair type, \(n(n-1)\) ordered choices of columns for the other two types, and forced remaining singletons, giving \(3n(n-1)\) additional sets of cardinality \(n+2\). Family 3 assigns all three pair types injectively to three column indices, in \(n(n-1)(n-2)\) ways, and allows \(3^{n-3}\) singleton fillings; those sets have cardinality \(n+3\). This gives \(\mathcal M_n(z)\) and the two sizes.

**Symmetry orbits.** In family 1, a column permutation moves the unique triple column to a reference position. The remaining singleton row multiplicities form an unordered triple of nonnegative counts summing to \(n-1\), with the row permutation identifying exactly reorderings. Hence there are \(p_{\leq3}(n-1)\) orbits. Family 2 is a single orbit: row permutations are transitive on missing pair types and column permutations place the two double columns. In family 3, normalize the three differently typed double columns by row and column permutations. The remaining singleton multiplicities form an unordered triple summing to \(n-3\), so there are \(p_{\leq3}(n-3)\) orbits. Summation gives the formula. Finally, the ratio of the number of size-\(n+2\) maximal sets to the number of size-\(n+3\) maximal sets is
\[
\frac{9}{(n-1)(n-2)}+\frac{3}{(n-2)3^{n-3}},
\]
which tends to zero; the stated fraction tends to one.

## Verification

The accompanying standalone Python 3 standard-library program, `verify.py`, verifies the complete visibility-polynomial coefficients and maximal-set counts for each \(3\le n\le7\) by enumerating all \(8^n\) column patterns; this examines a total of \(2{,}396{,}672\) subsets. For \(3\le n\le5\), it separately checks the visibility property directly from the two possible shortest paths for each chosen vertex pair, covering \(37{,}376\) subsets, and checks the predicted \(S_3\times S_n\) orbit counts. The program's recorded output is `verification_output.txt`, ending in `VERIFICATION_OK`. All finite tests supplement, but do not replace, the proof for all \(n\ge3\).

## Relationship to prior work

The equivalence of mutual visibility in rook graphs with forbidden fully occupied Cartesian rectangles was established in Cicerone, Di Stefano, and Klavžar (2021 preprint), Lemma 3.5; they also reduced the **largest cardinality** to a Zarankiewicz extremal number. Brešar and Yero (2023 preprint), Corollary 7, established the **smallest maximal cardinality** \(m+n-1\) on general rook graphs. The diameter-two analysis of Cicerone et al. (2024 preprint) revisits the maximum-cardinality reduction. Bujtás, Klavžar, and Tian (2025) introduced visibility polynomials and a general inclusion-exclusion identity in terms of maximal sets, with concrete formulas for other graph families. Thus neither the visibility criterion nor the scalar extremal bounds is claimed as new. The specific new assertions assessed here are the complete all-cardinality polynomial, exact maximal-set trichotomy and size enumerator, and orbit count for the three-row family; these are not stated or obtained numerically in the compared results. Equivalent counts under the language of \(C_4\)-saturated subgraphs of \(K_{3,n}\) remain a bibliographic possibility.

## Limitations

The classification is restricted to three rows and \(n\ge3\). It concerns ordinary mutual visibility, not total, outer, dual, or connected variants. The symmetry-orbit count refers to the explicitly named subgroup \(S_3\times S_n\), not to arbitrary automorphisms of small square graphs. The new numerical counts derive from the previously established rectangle criterion, so priority of equivalent enumerations in other terminology is not asserted. No independent scientific audit has been performed.

## References

1. S. Cicerone, G. Di Stefano, S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024 (first public 2021-12-24), Lemma 3.5 and Corollary 3.7. https://arxiv.org/html/2112.13024v2
2. B. Brešar, I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951 (first public 2023-07-06), Corollary 7. https://arxiv.org/html/2307.02951v2
3. S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, *Mutual-visibility problems on graphs of diameter two*, arXiv:2401.02373 (first public 2024-01-04), Theorem 3.13. https://arxiv.org/html/2401.02373v1
4. C. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, Aequationes Math. 99 (2025), 1883–1901, DOI:10.1007/s00010-025-01197-y, Definition 3.1 and Proposition 3.5. https://link.springer.com/article/10.1007/s00010-025-01197-y
