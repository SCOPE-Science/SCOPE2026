# Rank-refined clarification spectrum of finite binary formal contexts

## Finding
Let \(r,m\geq 1\). A binary formal context with \(r\) named objects and \(m\) named attributes is represented by an incidence matrix \(K\in\mathbb F_2^{r\times m}\). Let \(A(K)\) be its number of different row vectors (object descriptions), \(B(K)\) its number of different column vectors (attribute extents), and \(D(K)=\operatorname{rank}_{\mathbb F_2}(K)\). Clarification replaces each class of duplicate rows and columns with one representative, retaining \(A(K)\) and \(B(K)\) and preserving \(D(K)\).

For every finite field \(\mathbb F_q\), the complete joint count is
\[
 N_q(r,m;a,b,d)=\left\{\begin{matrix}r\\a\end{matrix}\right\}
 \left\{\begin{matrix}m\\b\end{matrix}\right\}
 \frac{T_q(a,d)T_q(b,d)}{|\operatorname{GL}(d,q)|},
 \tag{1}
\]
where the braces are Stirling numbers of the second kind, \(|\operatorname{GL}(0,q)|=1\), and
\[
 T_q(s,d)=\sum_{j=0}^{d}
 {d\brack j}_q(-1)^{d-j}q^{\binom{d-j}{2}}(q^j)_{\underline{s}},
 \qquad (u)_{\underline{s}}=\prod_{i=0}^{s-1}(u-i).
 \tag{2}
\]
Here \({d\brack j}_q\) denotes the Gaussian binomial coefficient. The count \(N_q\) enumerates all \(r\times m\) matrices over \(\mathbb F_q\) with exactly \(a\) distinct rows, \(b\) distinct columns, and field rank \(d\). It is zero outside \(1\le a\le r\), \(1\le b\le m\), \(0\le d\le\min(a,b)\). At \(q=2\), equation (1) is an exact, non-asymptotic joint distribution for the clarification dimensions and binary incidence rank of every uniformly random binary formal context: divide by \(2^{rm}\).

For \(d\ge1\), a clarified \(a\times b\) context of rank \(d\) exists **if and only if** \(d\le\min(a,b)\) and \(\max(a,b)\le q^d\). At rank zero, clarification has size precisely \(1\times1\). Hence the binary incidence rank of every nonzero clarified context is at least \(\lceil\log_2\max(a,b)\rceil\); combined with \(d\le\min(a,b)\), these bounds are sharp. Here \(\log_2\) means logarithm to base two; this statement concerns algebraic rank, not the Boolean rectangle-cover rank or real rank.

The corresponding trivariate exponential generating function is
\[
 \sum_{r,m\ge1}\sum_{a,b,d}N_q(r,m;a,b,d)\,
 \frac{x^r}{r!}\frac{y^m}{m!}z^d
 =\sum_{d\ge0}\frac{z^d}{|\operatorname{GL}(d,q)|}
 F_{q,d}(e^x-1)F_{q,d}(e^y-1),
 \qquad F_{q,d}(t)=\sum_{s\ge1}T_q(s,d)\frac{t^s}{s!}.
 \tag{3}
\]
Each coefficient is a finite sum. This simultaneously refines the usual finite-field rank census and the known unranked count of matrices with pairwise distinct rows and columns.

## Assumptions and scope
All rows and columns are *named* (labelled), and a pair of equal rows or columns is removed at clarification only as a duplicate, not as an implication-redundant row or column. The full statement (1)--(3) applies to fields of prime-power order \(q\ge2\), with positive integers \(r,m\); \(a,b,d\) are integers. Binary FCA uses \(q=2\). Equality of rows or columns is componentwise equality, and rank means ordinary linear rank **over the stated field**. No statement about rank over \(\mathbb R\) for \(0,1\)-matrices or about nonnegative rank is implied.

## Proof
**1. Canonical clarification quotient.** Equality of rows partitions the \(r\) object labels into \(a\) nonempty classes; equality of columns partitions the \(m\) attribute labels into \(b\) nonempty classes. A matrix is constant on each rectangle formed by a row class and a column class. Selecting one representative per class gives a uniquely determined \(a\times b\) matrix \(H\) with no duplicate rows or columns. Conversely, choosing the two partitions and such a clarified matrix, ordered by the least label of each class, reconstructs the original matrix exactly. The quotient has the same rank as the original because copying rows and columns never changes their spans. There are \(\left\{\begin{smallmatrix}r\\a\end{smallmatrix}\right\}\left\{\begin{smallmatrix}m\\b\end{smallmatrix}\right\}\) partition pairs. Therefore it suffices to enumerate pairwise-row-distinct and pairwise-column-distinct \(a\times b\) matrices of rank \(d\).

**2. Full-rank factorization.** Every \(a\times b\) matrix \(H\) of rank \(d\) factors as \(H=UV\), with \(U\in\mathbb F_q^{a\times d}\) of column rank \(d\) and \(V\in\mathbb F_q^{d\times b}\) of row rank \(d\). The linear map \(u\mapsto uV\) is injective, so the rows of \(H\) are pairwise distinct exactly when the rows of \(U\) are. Likewise the columns of \(H\) are pairwise distinct exactly when the columns of \(V\) are. Every \(H\) has precisely \(|\operatorname{GL}(d,q)|\) such ordered factorizations, since changing a basis by \(G\in\operatorname{GL}(d,q)\) changes \((U,V)\) to \((UG,G^{-1}V)\), and any two full-rank factorizations differ in this way. For \(d=0\) use the unique empty factorization. Thus the clarified rank-\(d\) matrix count equals \(T_q(a,d)T_q(b,d)/|\operatorname{GL}(d,q)|\), where \(T_q(s,d)\) counts ordered \(s\)-tuples of distinct vectors in \(\mathbb F_q^d\) spanning the whole space.

**3. Subspace inversion.** For any subspace \(W\le\mathbb F_q^d\) of dimension \(j\), the number of ordered, pairwise distinct \(s\)-tuples all lying in \(W\) is \((q^j)_{\underline s}\). Möbius inversion over the subspace lattice gives the spanning-tuple count as the sum of \(\mu(W,\mathbb F_q^d)(q^j)_{\underline s}\), where the interval Möbius value is \((-1)^{d-j}q^{\binom{d-j}{2}}\). Grouping subspaces by dimension, of which there are \({d\brack j}_q\), yields equation (2). Combining steps 1--3 proves equation (1).

**4. Existence and generating function.** A tuple of \(a\) distinct spanning vectors in a \(d\)-space exists for \(d\ge1\) exactly when \(d\le a\le q^d\): start with a basis and choose any further distinct vectors. The same holds for \(b\). At \(d=0\), only one vector exists and both dimensions must equal one. Factorization proves all resulting matrices exist. Summing (1) over sizes, then using \(\sum_{r\ge a}\left\{\begin{smallmatrix}r\\a\end{smallmatrix}\right\}x^r/r!=(e^x-1)^a/a!\), yields equation (3).

**5. Independent normalization.** Summing equation (1) over \(a,b\) at a fixed rank \(d\) must give the standard count of rank-\(d\) matrices,
\[
 \sum_{a,b}N_q(r,m;a,b,d)
 ={r\brack d}_q{m\brack d}_q|\operatorname{GL}(d,q)|.
 \tag{4}
\]
Indeed the Stirling sum \(\sum_a\left\{\begin{smallmatrix}r\\a\end{smallmatrix}\right\}T_q(a,d)\) counts *all* length-\(r\) spanning tuples, by partitioning positions according to equal values. That number is \(\prod_{i=0}^{d-1}(q^r-q^i)={r\brack d}_q|\operatorname{GL}(d,q)|\). Applying this for rows and columns gives (4).

## Verification
A standalone standard-library program `verify.py` enumerates **all** \(0,1\) incidence matrices through \(4\times4\), computes duplicated row and column types and the rank directly by finite-field elimination, and compares every nonzero triple count to equation (1). It also enumerates all \(\mathbb F_3\)-matrices through \(2\times2\), checks normalization (4) for \(r,m\le6\) and \(q\in\{2,3\}\), and checks the sharp support condition through \(d=5\) for binary tuples. Executing the included program prints `VERIFY_OK` on success.

For clarified square binary contexts, the nonzero counts by rank \(d\) are:

| Side length | Rank-2 | Rank-3 | Rank-4 | Rank-5 | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| 3 | 96 | 168 | 0 | 0 | 264 |
| 4 | 96 | 13,608 | 20,160 | 0 | 33,864 |
| 5 | 0 | 268,800 | 8,890,560 | 9,999,360 | 19,158,720 |

The totals agree with OEIS A181230 and A088310. Finite tests do not replace the arbitrary-size proof.

## Relationship to prior work
Classical formal-concept clarification collapses duplicate object intents and attribute extents without changing the concept lattice; Cordero, Enciso, López-Rodríguez, and Mora describe it explicitly and give software implementations. Felde, Hanika, and Stumme investigate random incidence contexts, including the coin-toss model, but not the joint clarification dimensions *conditioned on field rank*. The preexisting array OEIS A181230 gives **unranked** numbers of binary matrices having no duplicate rows or columns, and is recovered by summing this finding over ranks. A 2016 MathOverflow discussion explicitly asks about rank-restricted counts of these matrices; its follow-up specifies **real** rank, which differs from rank over \(\mathbb F_2\). The work of Beniamini, Etgar, and Kirkpatrick concerns \(\mathbb F_2\)-rank extremality for **symmetric, zero-diagonal** adjacency matrices, not the rectangular joint enumeration above. Published work on rank versus **nonnegative** rank (including a 5-by-5 census) studies another invariant and does not imply (1).

The ordinary factorization and subspace-Möbius tools are standard. The claimed contribution is their exact combination into a **simultaneous** profile of clarification sizes and finite-field incidence rank, including the uniform random-context law, exact feasibility boundary, and trivariate generating function. No claim is made that the unrefined counts, factorization lemma, or Gaussian-binomial inversion are themselves new.

## Limitations
This result counts labelled incidence matrices over finite fields, not contexts up to arbitrary row/column permutations. It treats equality-based clarification, **not** implication-based reduction, and does not determine the distribution of concept-lattice sizes or pseudo-intents. The field-rank spectrum is not a distribution of real rank, Boolean rectangle-cover rank, or nonnegative rank. The finite-field derivation is exact; any originality assessment remains conditional on discoverability of relevant equivalent formulations. Source searches cannot prove mathematical novelty, and no independent review is asserted.

## References
1. Felde, Hanika, Stumme, *Null Models for Formal Contexts*, Information 11(3), 135 (2020), first public 28 February 2020, https://doi.org/10.3390/info11030135 (primary MSC 03G10).
2. Cordero, Enciso, López-Rodríguez, Mora, *fcaR, Formal Concept Analysis with R*, The R Journal (21 June 2022), https://journal.r-project.org/articles/RJ-2022-014/ (clarification and preservation of conceptual knowledge).
3. Beniamini, Etgar, Kirkpatrick, *The \(\mathbb F_2\)-Rank and Size of Graphs*, arXiv:2206.11625 (23 June 2022), https://arxiv.org/abs/2206.11625 (different symmetric extremal rank problem).
4. OEIS A181230, https://oeis.org/A181230 (Hardin 2010; unrefined row/column-distinct matrix enumeration).
5. MathOverflow, *Number of \(\{0,1\}\) matrices with distinct rows and distinct columns* (28 December 2016), https://mathoverflow.net/questions/258258/.
6. Public mathematical census, *Certified census of the binary 5x5 rank-3 stratum: 713 classes with nonnegative rank 3, 6 with nonnegative rank 4, none with 5*, https://github.com/published-finding corpus/2026/tree/main/2026/9/7/SCOPE008 (distinct real and nonnegative ranks).
