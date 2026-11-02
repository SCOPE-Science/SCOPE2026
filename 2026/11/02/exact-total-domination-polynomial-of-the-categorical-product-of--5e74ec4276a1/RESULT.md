# Exact total-domination polynomial of the categorical product of two complete graphs

## Finding

For all integers \(m,n\ge 2\), let \(G_{m,n}=K_m\times K_n\) be the direct (categorical, tensor) graph product. Define its total-domination polynomial by
\[
T_{m,n}(z)=\sum_{S\subseteq V(G_{m,n}):\,N(S)=V(G_{m,n})}z^{|S|},
\]
where \(N(S)\) is the union of the *open* neighborhoods of the vertices of \(S\). Define
\[
Q_d(z)=d\big((1+z)^{d-1}-1-(d-1)z\big)\qquad(d\ge2).
\]
Then the polynomial counting **every** total dominating set by cardinality is
\[
\boxed{T_{m,n}(z)=(1+z)^{mn}-B_{m,n}(z)},
\]
with the explicit, symmetric failure polynomial
\[
\begin{aligned}
B_{m,n}(z)={}&1+m\big((1+z)^n-1\big)+n\big((1+z)^m-1\big)-mnz\\
&+\binom m2\binom n2(2z^2+4z^3)\\
&+2z(1+z)\left(\binom m2 Q_n(z)+\binom n2 Q_m(z)\right)\\
&+(1+z)Q_m(z)Q_n(z).
\end{aligned}
\]
Every coefficient is an exact integer, and \(B_{m,n}(z)\) counts precisely the vertex sets that fail total domination.

The inclusion-maximal failing sets are precisely the \(mn\) full row-column crosses, each with \(m+n-1\) vertices. Therefore all subsets of cardinality at least \(m+n\) are total dominating. If \(m=2\), the polynomial simplifies to
\[
T_{2,n}(z)=\big((1+z)^n-1-nz\big)^2,
\]
and symmetrically if \(n=2\). For \(m,n\ge3\), its smallest nonzero term is
\[
6\binom m3\binom n3 z^3;
\]
the minimum total dominating sets are exactly the three-cell partial permutation matrices (three mutually distinct rows and three mutually distinct columns). For a two-row board the minimum size is four, and the number of minimum sets is \(\binom n2^2\).

## Assumptions and scope

All graphs are finite, simple and loopless. Let \([d]=\{1,\ldots,d\}\). Vertices of \(G_{m,n}\) are cells \((i,j)\in[m]\times[n]\). Two distinct cells are adjacent if and only if **both** coordinates differ. Thus this graph is the complement of the Cartesian rook graph \(K_m\square K_n\), not the rook graph itself. Total domination requires \(N(S)=V\), including coverage of vertices *inside* \(S\). The theorem covers every integer \(m,n\ge2\), including the disconnected graph \(K_2\times K_2\).

Call \(X_{i,j}\) the union of row \(i\) and column \(j\). For \(S\subseteq[m]\times[n]\), let \(r\) and \(s\) be respectively the numbers of rows and columns containing a selected cell. An *active* row or column contains at least one cell of \(S\).

## Proof

**1. Cross criterion.** The open neighborhood of a cell \((i,j)\) consists of cells \((a,b)\) with \(a\ne i\) and \(b\ne j\). Consequently \(S\) does not totally dominate precisely when some \((i,j)\) has no neighbor in \(S\). This is equivalent to \(S\subseteq X_{i,j}\). We enumerate the failing sets disjointly by the unique active-row and active-column supports.

**2. Empty and thin supports.** The empty set contributes \(1\). Sets using exactly one active row contribute \(m((1+z)^n-1)\), and sets using exactly one active column contribute \(n((1+z)^m-1)\). Sets with one active row and one active column are single cells, counted in both, hence subtract \(mnz\). Every such set lies in a cross, so is failing.

**3. Exactly two active rows and columns.** Fix their row pair and column pair. Since all four row/column labels must appear, a failing set is either one of the two diagonal two-cell matchings or one of the four three-cell subsets of the resulting \(2\times2\) rectangle. The full four-cell rectangle dominates: for each cell its opposite rectangle corner is selected. The contribution is therefore \(\binom m2\binom n2(2z^2+4z^3)\).

**4. Two active rows and at least three active columns.** Such a failing set must have exactly one of its two active rows containing a single selected cell. Indeed, if it is contained in a row-column cross, only the chosen row can contain cells outside the chosen column, and every other active row contains exactly that column's cell. Conversely, that structure lies in a cross. The singleton active row is unique: the other row contains at least two cells. After choosing the active row pair, which row is singleton (two choices), and its column \(j\), the other row must select at least two other columns and may also select \((\text{other row},j)\). The generating polynomial for the choice of \(j\) and at least two other columns is
\[
\sum_{j=1}^{n}z\left((1+z)^{n-1}-1-(n-1)z\right)=zQ_n(z).
\]
The optional center cell supplies \((1+z)\), and the row pair supplies \(\binom m2\); hence this case contributes \(2\binom m2 z(1+z)Q_n(z)\). Interchanging rows and columns contributes \(2\binom n2 z(1+z)Q_m(z)\) for at least three active rows and exactly two active columns.

**5. At least three active rows and columns.** If a failing set is contained in a cross \(X_{i,j}\), then its selected-edge incidence graph is a *paired-star configuration*: each other active row contains just its edge in column \(j\), and each other active column contains just its edge in row \(i\). The edge \((i,j)\) may or may not be present. Both centers are uniquely determined, as row \(i\) is the unique row of selected degree at least two and column \(j\) is the unique column of degree at least two. Conversely, every such paired-star configuration lies in \(X_{i,j}\). For a support of \(r\ge3\) rows and \(s\ge3\) columns, choose its \(r\) possible row centers and \(s\) possible column centers. The \(r+s-2\) noncentral edges are compulsory, and the central edge is optional. Summing over supports gives
\[
(1+z)\left(\sum_{r=3}^m\binom mr r z^{r-1}\right)
\left(\sum_{s=3}^n\binom ns s z^{s-1}\right)
=(1+z)Q_m(z)Q_n(z).
\]
These six support regimes are disjoint and exhaustive, giving the displayed formula for \(B_{m,n}\), and subtraction from \((1+z)^{mn}\) proves the theorem.

**6. Extremal consequences.** Every failing set is contained in a cross. Each full cross is itself failing, and adding any outside cell makes it dominating: no different cross can contain a full cross together with an outside cell. Thus precisely the \(mn\) full crosses are inclusion-maximal failures. For \(m=2\), a set totally dominates if and only if each of its two rows contains at least two selected cells: this is necessary and sufficient for a selected cell outside the target row and column. The two row choices are independent, giving the factorization. For \(m,n\ge3\), a three-cell set avoids containment in any cross if and only if all its rows and columns are pairwise distinct; choose three rows, three columns and a bijection, giving \(3!\binom m3\binom n3\). No set of size at most two can dominate, since it is contained in a cross. The two-row minimum count and all high-cardinality claims follow.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The verifier rebuilds every open neighborhood from the adjacency definition and enumerates **1,173,328** vertex subsets across eleven graphs of dimensions \((2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,4),(3,5),(4,4),(4,5)\). It compares each cardinality coefficient with the independently evaluated formula. On three graphs it checks the row-column cross criterion independently for every subset. For 625 additional parameter pairs \(2\le m,n\le26\), it checks the polynomial's symmetry, nonnegativity, leading term, first nonzero coefficient and high-cardinality binomial tail by exact arithmetic. Successful execution reports `VERIFY_OK`. These finite tests corroborate, rather than logically replace, the proof for arbitrary parameters.

For independent probe activation probability \(p\), \(0\le p<1\), the exact probability that all vertices have an active adjacent probe is
\[
\mathbb P(\text{total domination})=(1-p)^{mn}T_{m,n}\!\left(\frac p{1-p}\right).
\]
At \(p=1\), the probability is \(1\). This is a direct consequence of the enumerator, not an extra independence assertion.

## Relationship to prior work

Defant and Iyer (2017, arXiv:1708.01305) and Vemuri (2019, arXiv:1908.02445) study domination and total domination numbers in direct products of complete graphs, particularly scalar bounds and structural threshold cases. Their original text does not present this all-cardinality total-domination polynomial. Hu et al. (2016, arXiv:1607.00400) develop general total-domination-polynomial recurrences and compute other graph-family polynomials; those general recurrences do not evaluate the present family. Mertens (2024, arXiv:2401.00716) evaluates the *ordinary domination polynomial of the Cartesian rook graph*; the underlying graph and neighborhood convention both differ here, so that formula does not count these sets. Earlier work on total domination in tensor graph products also treats numerical optima rather than the full selected-subset distribution. The elementary cross-obstruction equivalence is not asserted as a novel principle independently of this classification and enumeration.

## Limitations

The theorem concerns exactly two complete graph factors, not products of three or more factors or Cartesian products. It does not determine roots, log-concavity or unimodality of the polynomial. Previously known scalar minimum total-domination values and the general definition of a total-domination polynomial are not claimed as new. Publication priority is uncertain: an unindexed equivalent enumeration phrased as edge subsets of a complete bipartite graph, cross avoidance, or the domination polynomial of a complement rook graph might cover some or all of the result. An older relevant product-domination paper was accessible only through bibliographic descriptions, not a verified full-text reading. Independent mathematical audit has not been performed.

## References

1. C. Defant and S. Iyer, *Domination and Upper Domination of Direct Product Graphs*, arXiv:1708.01305, first publicly posted 2017-08-03. https://arxiv.org/abs/1708.01305.
2. H. Vemuri, *Domination in Direct Products of Complete Graphs*, arXiv:1908.02445, first publicly posted 2019-08-07. https://arxiv.org/abs/1908.02445.
3. J. Hu, E. Shan, S. Wang, C. Wang and B. Wei, *Total Domination Polynomials of Graphs*, arXiv:1607.00400, 2016-07-01. https://arxiv.org/abs/1607.00400.
4. S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716, first publicly posted 2024-01-01. https://arxiv.org/abs/2401.00716.
5. M. A. Henning and A. P. Kazemi, *k-Tuple Total Domination in Cross Products of Graphs*, Journal of Combinatorial Optimization 24 (2012), 339–346. DOI:10.1007/s10878-011-9389-z.
