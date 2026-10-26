# Endpoint classification and edge spectrum of four-way confluent finite intuitionistic chains

## Finding
For every integer \(n\ge 1\), equip \(W_n=\{1,\ldots,n\}\) with its ordinary order. Consider arbitrary binary relations \(R\subseteq W_n\times W_n\) satisfying **all four** forward, backward, downward and upward confluence conditions of Balbiani--Gencer. The following statements constitute one classification theorem.

1. Besides the empty relation, these are exactly the relations with no empty row or column whose row-minimum, row-maximum, column-minimum, and column-maximum sequences are all weakly increasing. Conversely, every such array satisfies all four conditions.
2. Define \(E_n(z)=\sum_R z^{|R|}\), summing over this class. The explicit finite endpoint formula below computes the entire polynomial without testing modal formulas. Its values \(E_n(1)\) for \(n=1,\ldots,6\) are exactly \(2,5,34,538,23415,3567130\).
3. The possible cardinalities \(|R|\) are **exactly** \(0\) and every integer from \(n\) through \(n^2\). The identity relation is the only nonempty member with \(n\) edges.
4. Although all four constraints are imposed simultaneously, the class has full binary-matrix entropy:
\[
\lim_{n\to\infty}\frac{\log_2 E_n(1)}{n^2}=1.
\]

## Assumptions and scope
All worlds are labelled and the chain order is fixed, not counted up to isomorphism. No reflexivity, symmetry, transitivity or seriality is imposed on \(R\) beyond the four confluences; their joint conditions themselves force either \(R=\varnothing\) or nonempty rows and columns. Composition follows the convention \((A\circ B)(u,v)\iff\exists w\,(uAw\wedge wBv)\). The conditions are
\[
\ge\circ R\subseteq R\circ\ge,\quad
R\circ\le\subseteq\le\circ R,\quad
\le\circ R\subseteq R\circ\le,\quad
R\circ\ge\subseteq\ge\circ R.
\]

For a nonempty row \(i\) set \(a_i=\min\{j:iRj\}\) and \(b_i=\max\{j:iRj\}\). For a nonempty column \(j\) set \(c_j=\min\{i:iRj\}\) and \(d_j=\max\{i:iRj\}\). Each of \(a,b,c,d\) must be nondecreasing, with \(1\le a_i\le b_i\le n\) and \(1\le c_j\le d_j\le n\).

Let \(\mathcal Q_n\) be the finite set of quadruples \((a,b,c,d)\) meeting these monotonicity and range conditions. For each such quadruple define
\[
P=\{(i,j):a_i\le j\le b_i\ \text{and}\ c_j\le i\le d_j\},
\]
\[
F=\{(i,a_i),(i,b_i):i\in W_n\}\cup
\{(c_j,j),(d_j,j):j\in W_n\}.
\]
Use only quadruples for which \(F\subseteq P\). The exact polynomial is
\[
\boxed{E_n(z)=1+\sum_{(a,b,c,d)\in\mathcal Q_n:\,F\subseteq P}
 z^{|F|}(1+z)^{|P\setminus F|}.}
\]
In particular, the coefficient of \(z^k\) is an exact count of \(k\)-edge relations on the fixed labelled chain.

## Proof
**Endpoint equivalence.** Suppose \(R\ne\varnothing\). Forward confluence says that whenever \(i\ge h\) and \(hRj\), some \(k\ge j\) satisfies \(iRk\). Thus nonemptiness propagates upwards among rows, and successive row maxima increase weakly. Downward confluence similarly propagates nonemptiness downwards among rows and makes successive row minima increase weakly. Hence all rows are nonempty, with both endpoint sequences weakly increasing. By the two column-wise compositions, backward confluence propagates nonemptiness to the right and makes column maxima weakly increasing, while upward confluence propagates it to the left and makes column minima weakly increasing. Thus all columns are nonempty. Conversely, for any of the four confluence conditions, the required successor exists by taking the appropriate row or column extreme. This proves the characterization, including the separate empty case.

**Endpoint polynomial.** In a relation with the specified four sequences, every edge lies in \(P\), and every row and column endpoint edge in \(F\) must occur. Thus \(F\subseteq R\subseteq P\). Conversely, for an allowed endpoint quadruple any choice of edges in \(P\setminus F\), together with all \(F\), has exactly those four endpoint sequences, and hence satisfies all four confluences. Distinct relations produce distinct quadruples of actual extrema, so no term double-counts. Giving each mandatory edge weight \(z\) and each optional edge weight \(1+z\) yields the formula.

**Sharp edge spectrum.** Every nonempty relation has at least \(n\) edges because no row is empty. If it has exactly \(n\) edges, all rows and columns have one edge, so it is a permutation matrix. Weak increase of the row endpoints forces that permutation to be increasing, hence the identity. To realize every cardinality \(n,n+1,\ldots,n^2\), start with the identity. Add upper diagonals in increasing offset \(h=1,2,\ldots,n-1\); within diagonal \(h\), insert \((i,i+h)\) for \(i=1,\ldots,n-h\). Next add lower diagonals in increasing offset \(h\); within diagonal \(h\), insert \((i,i-h)\) for \(i=h+1,\ldots,n\). At each upper-diagonal insertion, row minima and column maxima do not change. The new row maximum is at most the next row's existing maximum, and the new column minimum is at least the preceding column's existing minimum, by construction of the previous diagonal. The symmetric statements hold for lower-diagonal insertions: column minima and row maxima do not change, and the new row minimum and column maximum remain between their neighbours. Therefore all four endpoint sequences stay weakly increasing after **each** insertion. Every nonempty edge count occurs.

**Entropy.** For \(n\ge2\), require every entry of the first and last rows and first and last columns to be present, and choose the remaining \((n-2)^2\) interior entries freely. Every such relation has constant row minima and maxima \(1,n\) and constant column minima and maxima \(1,n\), so it is four-way confluent. Hence
\[
2^{(n-2)^2}\le E_n(1)\le2^{n^2}.
\]
Taking binary logarithms, dividing by \(n^2\), and passing to the limit proves the entropy assertion.

## Verification
A standalone C99 checker (`four_confluence_verification.c`) checks the defining four quantified relational conditions directly for **every** binary relation for \(n=1,2,3,4\), and separately checks agreement with the endpoint criterion. It then enumerates all sequences of nonempty rows having weakly increasing row extrema through \(n=6\) and filters them by column extrema. It also checks every intermediate relation along the described edge-insertion path through \(n=7\). The exact output, ending with `FOUR_WAY_CONFLUENCE_VERIFICATION_OK`, is reproduced in `VERIFICATION.md`. Exhaustive checks establish the specified finite counts; the all-\(n\) classification, edge-spectrum theorem, and entropy statement follow from the preceding proofs, not finite extrapolation.

## Relationship to prior work
Balbiani and Gencer explicitly formulate the four confluence conditions for intuitionistic modal frames; their work does not give this exact labelled finite-chain polynomial or census. Published finite-chain normal forms for certain *pairs* of confluence conditions provide closely related prior structure: in one case two row extremes are monotone, in another the row maximum and column maximum are monotone. Neither reported pair-class count is the intersection count above: already at four worlds the corresponding pair-class totals are \(2855\) and \(4849\), versus \(538\) for the simultaneous four-condition class. These partial results are acknowledged rather than treated as unrelated literature. The main new assertion is the simultaneous four-extreme polynomial together with its finite counts and edge-spectrum/entropy consequences. The broader matrix-enumeration literature is a priority risk.

## Limitations
This result concerns labelled **chains** only, not arbitrary intuitionistic preorders or posets; it imposes all four relations simultaneously, not a characterization of modal formulas. The polynomial is an exact finite sum, not a claimed simple closed-form generating function or an efficient asymptotic equivalent for \(E_n(1)\). Only \(n\le6\) has been exhaustively counted by the supplied checker; the mathematical statements about all orders are proven symbolically. Novelty is assessed against inspected sources, not guaranteed historical priority; general results on monotone-endpoint binary matrices could subsume the formula. No independent audit has been performed.

## References
1. Philippe Balbiani and Çigdem Gencer, *Four intuitionistic modal connectives*, arXiv:2606.07348v1, first posted 2026-06-05, especially Section 3.2 (four relational confluences), https://arxiv.org/abs/2606.07348.
2. Gisèle Fischer Servi, *Axiomatizations for some intuitionistic modal logics*, Rendiconti del Seminario Matematico Università e Politecnico di Torino 42 (1984), 179–194 (historical forward/backward confluence, cited in Reference 1).
3. *Endpoint normal form and exact census for finite-chain KI frames* (2026), published mathematical research record on the two row-extreme confluences; related partial classification.
4. *Maxima normal form and exact census for chain birelational relations* (2026), published mathematical research record on two row/column-extreme confluences; related partial classification.
