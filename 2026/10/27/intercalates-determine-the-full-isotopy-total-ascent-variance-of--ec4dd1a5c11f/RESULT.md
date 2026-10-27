# Intercalates determine the full-isotopy total-ascent variance of a Latin square

## Finding
Let \(L\) be any Latin square of integer order \(n\ge2\), with rows, columns, and symbols all indexed by \(\{0,\ldots,n-1\}\). Let \(I(L)\) count its intercalates, namely sets of two distinct rows and two distinct columns whose entries form a subsquare \(\left(\begin{smallmatrix}a&b\\b&a\end{smallmatrix}\right)\) for distinct symbols \(a,b\). Let \(\rho,\sigma\) be **independent, uniformly distributed** row and symbol permutations, and define the random total-ascent count
\[
X=\sum_{i=0}^{n-2}\sum_{j=0}^{n-1}\mathbf 1\{\sigma(L_{\rho(i),j})<\sigma(L_{\rho(i+1),j})\}.
\]
Then, **exactly for every Latin square and every \(n\ge2\),**
\[
\boxed{\mathbb E X=\frac{n(n-1)}2,\qquad
\operatorname{Var}(X)=\frac{n(n+1)}{12}-\frac{(n+1)I(L)}{3n(n-1)}.}
\]
Independently uniformly permuting the columns would not change \(X\). Consequently the variance of the total-ascent statistic over the complete row/column/symbol isotopy orbit, with isotopisms counted equally, depends on the square **only through its intercalate count**.

Moreover, the variance is zero if and only if \(L\) is isotopic to the Cayley table of an elementary abelian \(2\)-group. In particular, constant total ascents over an isotopy orbit can occur only when \(n\) is a power of \(2\); that extremal intercalate characterization was previously known, and its novelty is **not** claimed here.

## Assumptions and scope
A Latin square means each symbol appears exactly once in each row and column. An intercalate is a \(2\)-by-\(2\) subsquare on two symbols, as defined above. There are \(\binom n2\) unordered row pairs, and for each pair its relative row permutation has a number of disjoint directed \(2\)-cycles equal to the number of intercalates supported by that pair. The random group elements act on the fixed labelled square; probabilities are taken over the \((n!)^2\) independent row/symbol permutations, **not** over uniformly random Latin squares, not over a uniformly chosen set of distinct isotopic squares (though orbit stabilizers make that distribution equivalent), and not over row permutations alone. The theorem concerns a second moment rather than the entire ascent distribution.

## Proof
**1. Conditional variance from adjacent row comparisons.** Fix a symbol relabelling \(\sigma\). For ordered distinct rows \(a,b\), let
\[
w_{ab}=\#\{j:\sigma(L_{a,j})<\sigma(L_{b,j})\},\qquad y_{ab}=w_{ab}-n/2.
\]
Then \(y_{ab}=-y_{ba}\). Furthermore every row contains every symbol once, so for any fixed row \(a\), the \(n-1\) other rows collectively contain each symbol other than \(L_{a,j}\) once within each column. Thus
\[
\sum_{b\ne a}w_{ab}=\sum_{j=0}^{n-1}\big(n-1-\sigma(L_{a,j})\big)=n(n-1)/2,
\]
where the relabelled symbols are \(0,\ldots,n-1\). In particular, \(\sum_{b\ne a}y_{ab}=0\).

Set \(T=\sum_{a\ne b}y_{ab}^2\). For uniformly random row order \(\rho\),
\[
X-\frac{n(n-1)}2=\sum_{i=0}^{n-2}y_{\rho(i),\rho(i+1)}.
\]
The expectation is zero by skew symmetry. For \(n\ge3\), each ordered consecutive-row summand has second moment \(T/[n(n-1)]\). Two consecutive summands have expectation \(T/[n(n-1)(n-2)]\): summing \(y_{ab}y_{bc}\) over distinct \(a,b,c\), the vanishing row/column sums cancel all terms except \(\sum_{a\ne b}y_{ab}^2=T\). Nonconsecutive summands have expectation zero, since after fixing their first two rows the remaining pair \(c,d\) can be reversed without changing the conditioning or its frequency and \(y_{cd}=-y_{dc}\). Consequently
\[
\operatorname{Var}_\rho(X\mid\sigma)=\frac{T}{n}+\frac{2T}{n(n-1)}=\frac{(n+1)T}{n(n-1)}.
\]
At \(n=2\), the only row-pair comparison count is always one, so \(T=0\), and the same displayed conditional-variance identity holds trivially.

**2. Averaging the symbol comparisons.** For each ordered pair \(a\ne b\), the columns give a permutation \(p_{ab}\) of the symbols: \(p_{ab}(L_{a,j})=L_{b,j}\). This permutation has no fixed point. Let \(h_{ab}\) be its number of two-cycles. Exactly \(h_{ab}\) intercalates have their two rows \(a,b\); hence \(\sum_{a\ne b}h_{ab}=2I(L)\).

The random variable \(w_{ab}\) counts the directed edges of this permutation that point upward in a uniformly random ordering of the symbols. An individual edge has ascent-indicator variance \(1/4\). Indicators on two disjoint-symbol edges have covariance zero. Two distinct directed edges that form a directed two-step path have covariance \(-1/12\) (of the six relative orders of three distinct symbols, one is strictly increasing). Opposite edges of a two-cycle have covariance \(-1/4\). A permutation with \(n\) directed edges and \(h_{ab}\) two-cycles has \(n-2h_{ab}\) unordered, adjacent nonopposite edge pairs and \(h_{ab}\) opposite edge pairs. Therefore
\[
\mathbb E_\sigma y_{ab}^2=\operatorname{Var}_\sigma(w_{ab})
=\frac n4-\frac{n-2h_{ab}}6-\frac{h_{ab}}2
=\frac{n-2h_{ab}}{12}.
\]
Here \(\mathbb E_\sigma w_{ab}=n/2\) by order reversal. Summing over the ordered row pairs gives
\[
\mathbb E_\sigma T=\frac{n^2(n-1)}{12}-\frac{I(L)}3.
\]
The conditional row-order mean is \(n(n-1)/2\), independent of \(\sigma\). The law of total variance now yields exactly the claimed formula.

**3. The zero-variance boundary.** For any row pair, \(h_{ab}\le n/2\), giving the classical upper bound \(I(L)\le n^2(n-1)/4\). Equality in the derived variance formula is equivalent to equality in this intercalate bound, hence every relative row permutation consists solely of disjoint two-cycles. For completeness, relabel columns to make the first row the identity permutation \(f_0\); write the other rows as bijections \(f_a\) from columns to symbols. Every \(f_a\) for \(a\ne0\) is a fixed-point-free involution, and every product \(f_b f_a^{-1}\) is an involution. Hence every pair of the \(f_a\) commute. The generated subgroup \(H\) is elementary abelian, and it acts transitively because a fixed column displays every symbol along the rows. A faithful transitive abelian permutation group is regular: its point stabilizers are all equal and their common kernel is trivial. Thus \(|H|=n\); the \(n\) distinct rows \(f_a\) are exactly the group elements. The square is isotopic to the multiplication table of \(H\). Conversely, all nonidentity row differences in the table of an elementary abelian \(2\)-group are fixed-point-free involutions, yielding maximal intercalates and variance zero.

## Verification
The accompanying standalone `verify.py` independently evaluates \(\mathbb E X\) and \(\mathbb E X^2\) with exact integer sums over **all** \((n!)^2\) row/symbol permutations, then compares with the intercalate formula using exact rational arithmetic. It checks cyclic squares of orders \(2,3,4,5,6\), the elementary-abelian square of order \(4\), and **all 56 reduced order-five Latin squares**. The latter split into six squares with \(I=0\) and variance \(5/2\), and fifty squares with \(I=4\) and variance \(21/10\). The cyclic order-four square has \(I=4\) and variance \(10/9\); the elementary-abelian order-four square has \(I=12\) and variance zero. The verifier is finite corroboration; the all-order statement follows from the preceding proof, not extrapolation.

Run the self-contained verifier with a standard Python 3 interpreter as `python verify.py`. It has no third-party dependencies.

## Relationship to prior work
Mirzavaziri and Yaqubi introduced Latin Eulerian numbers and the total-ascent statistic, and their Theorem 4.9 provides a **deterministic symbol-comparison representation**. Their follow-up treats row permutations of the cyclic Latin square via Eulerian polynomials. Neither inspected paper states or implies by an already-solved variance formula the closed intercalate-dependent variance of the **full** isotopy action on an **arbitrary** Latin square. Computing this variance requires cancellations across overlapping row and symbol comparison indicators.

The bound \(I(L)\le n^2(n-1)/4\) and the elementary-abelian characterization of its equality case are classical; see Gill, Mammoliti, and Wanless. The group rigidity in the last part is therefore identified as a **consequence of the new moment identity plus a known extremal fact**, not as a newly discovered independent classification. Literature priority for the moment identity itself remains to be independently verified.

## Limitations
This theorem computes only the first two moments under independent uniform row/symbol relabellings. It does not characterize every ascent-distribution coefficient, and distinct squares with the same intercalate count may have different higher moments or distributions. No new classification of maximal-intercalate Latin squares is claimed. The originality assessment is based on accessible primary works and current database comparisons, not a proof of absolute historical priority. Independent verification has not been performed.

## References
1. M. Mirzavaziri and D. Yaqubi, *Latin Eulerian Numbers*, arXiv:2609.25100v1 (first public 2026-09-19), https://arxiv.org/abs/2609.25100 .
2. M. Mirzavaziri and D. Yaqubi, *Cyclic Latin Eulerian Numbers*, arXiv:2609.28808v1 (first public 2026-09-23), https://arxiv.org/abs/2609.28808 .
3. M. J. Gill, A. Mammoliti, and I. M. Wanless, *Canonical Labeling of Latin Squares in Average-Case Polynomial Time*, Random Structures & Algorithms 66 (2025), e70015, DOI: 10.1002/rsa.70015, https://doi.org/10.1002/rsa.70015 .
