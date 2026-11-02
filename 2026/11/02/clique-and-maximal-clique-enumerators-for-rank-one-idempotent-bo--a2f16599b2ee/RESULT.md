# Clique and maximal-clique enumerators for rank-one idempotent Boolean relations

## Finding
For each integer \(n\geq1\), let \(\mathcal B_n\) be the monoid of binary relations on \([n]\), composed using Boolean matrix multiplication. For nonempty \(A,B\subseteq[n]\), write \(X_{A,B}=A\times B\) for the corresponding nonzero rectangular relation. Consider the simple graph \(\Gamma_n\) whose vertices are all nonzero Boolean-rank-one idempotents \(X_{A,B}\), with distinct vertices adjacent precisely when their Boolean products commute.

Define \(c_{n,k}\) as the number of (unlabeled, unordered) cliques of size \(k\), including the empty clique; define \(m_{n,k}\) as the number of *inclusion-maximal* cliques of size \(k\). For every \(0\leq k\leq n\),
\[
c_{n,k}=\frac{1}{k!}\sum_{j=0}^{k}(-1)^j\binom{k}{j}\bigl(2^{k+1}+k-1-j\bigr)^n.
\]
For every \(1\leq k\leq n\),
\[
m_{n,k}=\frac{1}{k!}\sum_{j=0}^{k}(-1)^j\binom{k}{j}\bigl(2^{k+1}+k-2-j\bigr)^n.
\]
Both counts vanish for \(k>n\), and \(m_{n,0}=0\). In particular \(c_{n,0}=1\). A clique \(\{X_{A_i,B_i}:1\leq i\leq k\}\) is inclusion-maximal if and only if
\[
\bigcup_{i=1}^{k}(A_i\cup B_i)=[n].
\]
Moreover every integer between \(1\) and \(n\) occurs as the size of an inclusion-maximal clique, and there is exactly one clique of size \(n\), namely \(\{X_{\{i\},\{i\}}:i\in[n]\}\). Therefore \(\omega(\Gamma_n)=\chi(\Gamma_n)=n\). The graph is not well-covered when \(n\geq2\).

For example, at \(n=4\) the clique-size distribution for \(k=0,1,2,3,4\) is \((1,175,385,66,1)\), while maximal-clique counts for \(k=1,2,3,4\) are \((65,295,62,1)\). These formulas describe families of mutually commuting nonzero rank-one idempotents, not arbitrary commutative subsemigroups of \(\mathcal B_n\).

## Assumptions and scope
The multiplication is relational composition, equivalently matrix multiplication over the Boolean semiring, with logical OR as addition and logical AND as multiplication. The index \(n\) is any positive integer, and the pair \((A,B)\) ranges over ordered pairs of nonempty subsets of \([n]\). The nonzero rank-one relations are exactly the nonempty rectangles \(A\times B\), with unique such representation. The graph contains only *idempotent* rank-one rectangles, not all rank-one elements of the monoid. All cliques consist of distinct vertices; the ordered-label count in the proof is divided by \(k!\). No asymptotic or field-characteristic assumptions are needed.

## Proof
**Rectangle multiplication and idempotency.** Direct Boolean composition gives
\[
X_{A,B}X_{C,D}=\begin{cases}X_{A,D},&B\cap C\ne\varnothing,\\0,&B\cap C=\varnothing.\end{cases}
\]
In particular \(X_{A,B}^2=X_{A,B}\) exactly when \(A\cap B\ne\varnothing\). Suppose two *distinct* rank-one idempotents commute. If both products were nonzero, they would be \(X_{A,D}\) and \(X_{C,B}\), whose equality forces \(A=C\) and \(D=B\), contradicting distinctness. Since exactly one zero product cannot commute, two distinct vertices commute if and only if both products vanish:
\[
B\cap C=\varnothing\quad\text{and}\quad D\cap A=\varnothing.
\]
Thus different elements of every clique annihilate one another in both orders.

**Coordinate normal form.** Temporarily label \(k\) distinct vertices \(X_{A_i,B_i}\). For each ground-set coordinate \(t\in[n]\), the vanishing cross-products imply that its memberships must be of one of four forms: (i) absent from every \(A_i,B_i\); (ii) present in any nonempty subset of the \(A_i\), but no \(B_i\); (iii) present in any nonempty subset of the \(B_i\), but no \(A_i\); or (iv) present in exactly \(A_i\cap B_i\) for a *single* label \(i\), and absent from every other pair. Indeed, a membership in \(A_i\cap B_j\) with \(i\ne j\) violates commutation, while membership in \(A_i\cap B_i\) excludes membership at any other label. Conversely, any assignment of these forms ensures all cross-products vanish. The allowed coordinate alphabet therefore has size
\[
1+(2^k-1)+(2^k-1)+k=2^{k+1}+k-1.
\]
For each \(i\), idempotency requires the root type (iv) labeled \(i\) to occur at least once. If \(j\) specified root labels are missing, the alphabet shrinks by \(j\) symbols. Inclusion–exclusion gives the number of labeled ordered cliques as
\[
\sum_{j=0}^k(-1)^j\binom{k}{j}(2^{k+1}+k-1-j)^n.
\]
All roots exist, so the labeled vertices are distinct; every unordered clique has exactly \(k!\) labelings. Division proves the first displayed formula, including \(k=0\), which counts the empty clique once.

**Maximality.** Given a clique, let \(S=\bigcup_i(A_i\cup B_i)\). If \(t\notin S\), the singleton diagonal idempotent \(X_{\{t\},\{t\}}\) is a distinct commuting extension. Conversely, suppose another idempotent \(X_{C,D}\) commutes with each vertex. Choose \(t\in C\cap D\), which is nonempty. Since all products with old vertices are zero, \(B_i\cap C=\varnothing\) and \(D\cap A_i=\varnothing\), so \(t\notin S\). Thus no extension exists exactly when \(S=[n]\). In the coordinate normal form this removes the unique empty symbol. Repeating inclusion–exclusion with alphabet size \(2^{k+1}+k-2\) yields the maximal-clique formula.

**Bounds and all possible sizes.** The \(k\) nonempty root sets \(A_i\cap B_i\) are pairwise disjoint, so \(k\leq n\). For every \(1\leq k\leq n\), choose \(k\) distinct root coordinates, use singleton diagonals for labels \(2,\ldots,k\), and add every remaining coordinate to \(A_1\) only; this produces a clique whose union of supports covers \([n]\), hence a maximal clique of size \(k\). If \(k=n\), all \(n\) roots are distinct singletons and cover \([n]\); no coordinate can belong to any additional set component, so the only size-\(n\) clique is the complete diagonal family. In particular the clique number is \(n\). Color \(X_{A,B}\) by the least element of its nonempty intersection \(A\cap B\); adjacent vertices have disjoint intersections and therefore distinct colors. This is a proper \(n\)-coloring, proving \(\chi=n\). The existence of maximal clique sizes \(1\) and \(n\) proves non-well-coveredness for \(n\ge2\).

## Verification
The standalone \(\texttt{verify.py}\) exhaustively constructs all nonzero rank-one Boolean idempotent matrices for \(1\leq n\leq4\), multiplies every pair using the Boolean operations, builds the commuting graph without the coordinate characterization, and recursively enumerates all graph cliques. It independently tests each clique's inclusion-maximality by checking the full adjacency graph; then it compares observed clique counts, maximal-clique counts, and maximality-versus-support coverage with the formulas. The complete observed distributions are:

| \(n\) | Number of vertices | All clique counts \(k=0,\ldots,n\) | Maximal clique counts \(k=1,\ldots,n\) |
| --- | ---: | --- | --- |
| 1 | 1 | \((1,1)\) | \((1)\) |
| 2 | 7 | \((1,7,1)\) | \((5,1)\) |
| 3 | 37 | \((1,37,24,1)\) | \((19,21,1)\) |
| 4 | 175 | \((1,175,385,66,1)\) | \((65,295,62,1)\) |

Run with \(\texttt{python3 verify.py}\); expected terminal line: \(\texttt{VERIFY_OK}\). These finite checks are independent corroboration for small parameters; the all-\(n\) theorem follows from the proof above.

## Relationship to prior work
The binary-relation semigroup, rank-one Boolean rectangles and their multiplication are established objects; see Kim and Roush (1981). Margolis and Steinberg, first publicly posted February 13, 2023, study minimal faithful degree of the binary-relation monoid through its low-rank ideal, not the clique-size distribution of nonzero rank-one idempotents. Paulista (2025), in a broader theorem about completely \(0\)-simple semigroups, gives a commuting criterion in Lemma 3.2 and determines *clique numbers* in Theorem 5.4. Our local commuting characterization and the numerical clique number are consistent with, and should not be represented as independent advances beyond, that general framework. The narrower additional contribution here is the explicit closed form of **every** ordinary and inclusion-maximal clique coefficient, the support-coverage characterization of maximality, and the classification of attainable maximal-clique sizes in the natural intersection-sandwich example. Dolžan, Kokol Bukovšek and Oblak (2010) address diameters of commuting graphs of full matrix semirings, rather than this induced idempotent-stratum enumerator.

## Limitations
The enumeration is for the induced commuting graph on *nonzero rank-one idempotents*. It does not enumerate all commuting elements, all idempotents, or all maximal commutative subsemigroups of the full relation monoid. The exact closed formulas follow an elementary coordinate-alphabet decomposition; no stronger general Rees-matrix clique enumerator is claimed. A more general or earlier literature formula for all clique coefficients of intersection-sandwich semigroups could imply this specialization; available searches did not establish its absence. Independent literature-priority assessment and independent proof review have not been performed.

## References
1. S. Margolis and B. Steinberg, *On the minimal faithful degree of Rhodes semisimple semigroups*, arXiv:2302.06539v1 (first posted 2023-02-13), https://arxiv.org/abs/2302.06539.
2. K. H. Kim and F. W. Roush, *The algebraic structure of the semigroup of binary relations on a finite set*, Glasgow Mathematical Journal **22** (1981), 57–68, https://doi.org/10.1017/S0017089500004468.
3. T. Paulista, *Commuting graphs of completely 0-simple semigroups*, arXiv:2510.23871 (2025), https://arxiv.org/abs/2510.23871; especially Lemma 3.2 and Theorem 5.4.
4. D. Dolžan, D. Kokol Bukovšek and P. Oblak, *Diameters of commuting graphs of matrices over semirings*, arXiv:1012.5505 (2010), https://arxiv.org/abs/1012.5505.
