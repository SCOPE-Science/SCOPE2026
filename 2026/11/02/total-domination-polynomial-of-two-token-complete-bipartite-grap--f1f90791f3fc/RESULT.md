# Total-domination polynomial of two-token complete-bipartite graphs

## Finding

Let \(2\le m\le n\), and let \(T_{m,n}=F_2(K_{m,n})\) be the two-token graph of the labelled complete bipartite graph. Its vertices are the two-element subsets of the underlying \(m+n\) vertices. Two such subsets are adjacent precisely when one token moves along an edge of \(K_{m,n}\) to a vacant vertex. A subset \(D\) of vertices of \(T_{m,n}\) is *total dominating* if **every** vertex of \(T_{m,n}\), including those in \(D\), has a neighbor in \(D\).

Write \(\mathcal D_t(T_{m,n};z)=\sum_{D\text{ total dominating}}z^{|D|}\). For a nonnegative integer \(s\), define the complete-graph edge-cover polynomial
\[
 C_s(z)=\sum_{j=0}^{s}(-1)^j\binom{s}{j}(1+z)^{\binom{s-j}{2}}.
\]
For nonnegative \(a,b\), define
\[
 Q_{a,b}(z)=\sum_{i=0}^{a}\sum_{j=0}^{b}(-1)^{i+j}\binom{a}{i}\binom{b}{j}(1+z)^{(a-i)(b-j)},
\]
and, for \(m,n\ge2\), put
\[
 R_{m,n}(z)=\sum_{a=m-1}^{m}\sum_{b=n-1}^{n}\binom{m}{a}\binom{n}{b} Q_{a,b}(z),
\]
\[
 E_{m,n}(z)=C_m(z)(1+z)^{\binom n2}+C_n(z)(1+z)^{\binom m2}-C_m(z)C_n(z).
\]
Then the **entire total-domination polynomial** has the exact factorization
\[
 \boxed{\mathcal D_t(T_{m,n};z)=R_{m,n}(z)E_{m,n}(z).}
\]
In particular,
\[
 \boxed{\gamma_t(T_{m,n})=n-1+\left\lceil m/2\right\rceil.}
\]

The coefficient at this least exponent, i.e. the **number of labelled minimum total-dominating sets**, also has a closed form. Let \(S(p,q)\) be the Stirling number of the second kind, with \(S(p,q)=0\) if \(q>p\). Define
\[
 e_{2r}=\frac{(2r)!}{2^r r!}\quad(r\ge1),\qquad
 e_{2r+1}=\frac{(2r+1)!}{2^r(r-1)!}\quad(r\ge1).
\]
Then
\[
 \boxed{[z^{\gamma_t(T_{m,n})}]\mathcal D_t(T_{m,n};z)
 =n\,m!\bigl(S(n-1,m-1)+S(n-1,m)\bigr)
 \left(e_m+\mathbf 1_{\{\lceil n/2\rceil=\lceil m/2\rceil\}}e_n\right).}
\]
For example, \(T_{3,4}\) has total domination number \(5\) and exactly \(576\) minimum total-dominating sets. The complete formula determines every cardinality coefficient, not just the minimum.

## Assumptions and scope

All graphs are finite and simple. The two bipartition classes of \(K_{m,n}\) are labelled \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_n\}\), with \(2\le m\le n\). The variable \(z\) records the size of a *vertex subset of the token graph*, not the size of a subset of the original host graph. Empty total-dominating sets are not counted. The total-domination condition is open-neighborhood domination, so a selected token-graph vertex cannot dominate itself.

Define \(X=\{\{a_i,b_j\}:1\le i\le m,\ 1\le j\le n\}\) and \(Y=\binom{A}{2}\cup\binom{B}{2}\). The two sets are the sides of the natural bipartition of \(T_{m,n}\). For \(D\subseteq V(T_{m,n})\), write \(D_X=D\cap X\), \(D_A=D\cap\binom{A}{2}\), and \(D_B=D\cap\binom{B}{2}\).

## Proof

**1. The complete feasibility criterion.** For a vertex \(\{a_i,a_j\}\in\binom{A}{2}\), its neighbors are the mixed pairs \(\{a_i,b\}\) and \(\{a_j,b\}\) for \(b\in B\). Thus every vertex of \(\binom{A}{2}\) is adjacent to \(D_X\) if and only if at most one row of the \(m\times n\) incidence matrix of \(D_X\) is empty. Symmetrically, every vertex of \(\binom{B}{2}\) is adjacent to \(D_X\) if and only if at most one column is empty.

A mixed vertex \(\{a_i,b_j\}\) is adjacent to \(D_A\cup D_B\) if and only if \(a_i\) is incident to a chosen pair of \(D_A\) or \(b_j\) is incident to a chosen pair of \(D_B\). Every mixed vertex is therefore adjacent to \(D_A\cup D_B\) if and only if **all vertices of \(A\) are covered by \(D_A\), or all vertices of \(B\) are covered by \(D_B\)**. The two conditions are independent because all token-graph edges join \(X\) to \(Y\). Consequently, \(D\) is total dominating exactly when its \(X\)-part has at least \(m-1\) nonempty rows and at least \(n-1\) nonempty columns, and its pure-pair part fully covers one host-side vertex class.

**2. Count all cardinalities.** For a prescribed set of \(a\) active rows and \(b\) active columns, the polynomial \(Q_{a,b}(z)\) counts \(0\)-\(1\) selected-cell patterns in the resulting \(a\times b\) rectangle with no empty row or column. Inclusion–exclusion over empty rows and columns gives the displayed finite sum. Choosing the active row and column sets produces \(R_{m,n}(z)\).

The polynomial \(C_s(z)\) counts edge subsets of the complete graph on \(s\) labelled vertices that cover every vertex; this follows from inclusion–exclusion over isolated vertices. A chosen set of pure token vertices fully covers \(A\), or fully covers \(B\), so inclusion–exclusion over these two events yields \(E_{m,n}(z)\). The independent decomposition \(D=D_X\sqcup D_A\sqcup D_B\) proves \(\mathcal D_t=R_{m,n}E_{m,n}\).

**3. The minimum.** Covering all pure pairs from \(B\) requires at least \(n-1\) nonempty columns, hence at least \(n-1\) mixed token vertices. This bound is attained: choose one mixed vertex in each of \(n-1\) columns so that at least \(m-1\) distinct rows occur. Separately, covering every vertex of \(A\) by chosen pairs requires at least \(\lceil m/2\rceil\) pure vertices; covering \(B\) instead needs at least \(\lceil n/2\rceil\). Choosing a minimum edge cover of the smaller class \(A\) attains \(\lceil m/2\rceil\). The two independent lower bounds sum and are simultaneously attained.

**4. Count the minima.** In any minimum \(D_X\), exactly one of the \(n\) columns is empty and the other \(n-1\) columns each contain one selected cell. Assign a row to each nonempty column. The image must have size \(m\) or \(m-1\). The number of these functions is \(m!S(n-1,m)+m!S(n-1,m-1)\), hence the first factor \(n\,m!\bigl(S(n-1,m)+S(n-1,m-1)\bigr)\).

A minimum pure-pair part of size \(\lceil m/2\rceil\) must be an edge cover lying **entirely** in \(A\), or, only when \(\lceil n/2\rceil=\lceil m/2\rceil\), entirely in \(B\). The two alternatives are disjoint because mixing selected edges between the host sides leaves neither side completely covered at this minimum size. A minimum edge cover of \(K_{2r}\) is a perfect matching, counted by \((2r)!/(2^r r!)\). A minimum edge cover of \(K_{2r+1}\) is one three-vertex path together with \(r-1\) disjoint edges, counted by \((2r+1)!/(2^r(r-1)!)\). Multiplying the two independent minimum counts proves the last box.

## Verification

The standalone script `verify.py` uses two distinct tests of the theorem. First, it builds the token graph from the original symmetric-difference edge definition and exhaustively enumerates all initial vertex subsets for \((m,n)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4)\), checking literal open-neighborhood domination and the **whole** polynomial; these comprise \(4,260,928\) tested subsets. Second, for \((3,5),(4,4),(4,5)\), it separately enumerates mixed and pure selected subsets from the raw incidence conditions and checks their polynomial convolution. It also checks the degree and closed minimum coefficient for \(56\) additional ordered parameter pairs. All reported checks returned `VERIFY_OK`. Finite enumeration is corroboration; the proof above covers every \(2\le m\le n\).

## Relationship to prior work

Chinman, Cortijo, Pedroni, Seong, and Stenger, *The domination number of the \(k\)-token graph of the complete bipartite graph \(K_{m,n}\)* (arXiv:2610.28936v1, publicly submitted 2026-10-20), and Acosta Troncoso, Caldera Caldera, and Rivera, *The domination number of the \(2\)-token graph of the complete bipartite graph* (arXiv:2610.31557v1, publicly submitted 2026-10-22), determine **ordinary** domination numbers. Neither paper's relevant statements address total domination or enumerate the total-dominating vertex sets by cardinality. Their description of the token-graph bipartition and its neighborhoods is credited as prior structural context.

The distinction between the parameters is genuine. In the cases identified by the cited ordinary-domination theorem, \(\gamma_t(T_{m,n})-\gamma(T_{m,n})=1\) precisely when \(m=3\), or when \(m\ge5\) is odd and \(n=m+1\); otherwise the difference is zero. An ordinary dominating set can satisfy its coverage requirement by containing an otherwise undominated vertex, whereas a total dominating set cannot. Earlier general descriptions of domination polynomials and edge-cover polynomials do not themselves give the displayed all-parameter token-graph formula or its minimum-set multiplicities.

## Limitations

The result is restricted to two tokens on complete bipartite host graphs with both parts of size at least two. It does not determine total-domination polynomials for larger token counts or arbitrary host graphs. The displayed formulas are finite exact sums but are not claimed to be the fastest evaluation algorithm. Priority against literature using alternative terminology (such as open-neighborhood covering in symmetric squares) has not been independently certified.

## References

1. N. Chinman, A. Cortijo, B. Pedroni, I. Seong, and L. Stenger, *The domination number of the \(k\)-token graph of the complete bipartite graph \(K_{m,n}\)*, arXiv:2610.28936v1 (2026-10-20), https://arxiv.org/abs/2610.28936.
2. E. Acosta Troncoso, I. Caldera Caldera, and L. M. Rivera, *The domination number of the \(2\)-token graph of the complete bipartite graph*, arXiv:2610.31557v1 (2026-10-22), https://arxiv.org/abs/2610.31557.
3. Standard Stirling-number and complete-graph edge-cover enumeration identities are proved directly where needed, rather than asserted as new facts.
