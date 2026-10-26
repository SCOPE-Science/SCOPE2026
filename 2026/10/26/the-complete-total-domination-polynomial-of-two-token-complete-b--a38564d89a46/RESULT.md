# The complete total-domination polynomial of two-token complete bicliques

## Finding

Let \(m,n\ge 2\), and let \(H_{m,n}=F_2(K_{m,n})\) be the two-token graph of the complete bipartite graph. Define the total-domination polynomial
\[
D_t(H_{m,n};z)=\sum_{T\subseteq V(H_{m,n}):\,N_{H_{m,n}}(T)=V(H_{m,n})}z^{|T|},
\]
where \(N(T)\) denotes the **open** neighborhood union, so selected vertices must also have a selected neighbor.

For integers \(a,b\ge 1\), put
\[
E_a(z)=\sum_{i=0}^{a}(-1)^i\binom ai(1+z)^{\binom{a-i}{2}},\qquad
R_{a,b}(z)=\sum_{i=0}^{a}\sum_{j=0}^{b}(-1)^{i+j}\binom ai\binom bj(1+z)^{(a-i)(b-j)}.
\]
Define
\[
U_{m,n}(z)=E_m(z)(1+z)^{\binom n2}+E_n(z)(1+z)^{\binom m2}-E_m(z)E_n(z)
\]
and
\[
V_{m,n}(z)=R_{m,n}(z)+mR_{m-1,n}(z)+nR_{m,n-1}(z)+mnR_{m-1,n-1}(z).
\]
**Theorem.** For every pair of integers \(m,n\ge2\), the exact cardinality enumerator of all total dominating sets is
\[
\boxed{D_t(H_{m,n};z)=U_{m,n}(z)V_{m,n}(z).}
\]
In particular, letting \(s=\max\{m,n\}\) and \(t=\min\{m,n\}\),
\[
\boxed{\gamma_t(H_{m,n})=s-1+\left\lceil\frac t2\right\rceil.}
\]
The complete number of minimum total dominating sets is also explicit. Let \(S(a,b)\) be the Stirling number of the second kind, with \(S(a,b)=0\) when \(b<0\) or \(b>a\), and put
\[
B_{s,t}=s\sum_{j=t-1}^{t}\binom tj j!\,S(s-1,j),
\]
\[
e_q=\begin{cases}
\dfrac{q!}{2^{q/2}(q/2)!},&q\text{ even},\\[3pt]
\dfrac{q!}{2^{(q-1)/2}((q-3)/2)!},&q\text{ odd},
\end{cases}\qquad(q\ge2).
\]
Writing \(h=\lceil t/2\rceil\) and \(\mathbf1_{P}\) for the indicator of proposition \(P\), that number is
\[
\boxed{
B_{s,t}\left(\mathbf1_{\lceil m/2\rceil=h}e_m+\mathbf1_{\lceil n/2\rceil=h}e_n\right).
}
\]
Both same-size sides contribute separately when \(m=n\); the two classes of selected pure-pair vertices are disjoint.

Combining the theorem with the known ordinary-domination formula of Chinman, Cortijo, Pedroni, Seong and Stenger gives, for \(2\le m\le n\),
\[
\gamma_t(H_{m,n})-\gamma(H_{m,n})
=\begin{cases}
1,&m=3,\\
1,&m\ge5\text{ odd and }n=m+1,\\
0,&\text{otherwise}.
\end{cases}
\]
This last comparison is a corollary combining the present theorem and an existing ordinary-domination result, not a separately claimed discovery of that ordinary result.

## Assumptions and scope

Graphs are finite, undirected, simple and labelled. The two vertex classes of \(K_{m,n}\) are \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_n\}\). A vertex of \(H_{m,n}\) is a two-element subset of \(A\cup B\). Two vertices of \(H_{m,n}\) are adjacent if their symmetric difference is precisely one edge of \(K_{m,n}\). The parameters satisfy \(m,n\ge2\); no assertion about a token graph of a general host graph or larger token count is made. Every coefficient of \(D_t\) counts selected vertex *sets*, not orbits modulo automorphisms.

## Proof

**Step 1: Exact neighborhoods.** Partition the two-token configurations into three disjoint classes:
\[
\mathcal A=\binom A2,\qquad\mathcal M=\{\{a_i,b_j\}:1\le i\le m,\ 1\le j\le n\},\qquad\mathcal B=\binom B2.
\]
Every token move exchanges an \(A\)-vertex and a \(B\)-vertex. Thus the only token-graph edges run between \(\mathcal M\) and \(\mathcal A\cup\mathcal B\); in particular, the token graph is bipartite with these two sides. Directly from the definition,
\[
N(\{a_i,a_k\})=\{\{a_i,b_j\},\{a_k,b_j\}:1\le j\le n\},
\]
\[
N(\{b_j,b_\ell\})=\{\{a_i,b_j\},\{a_i,b_\ell\}:1\le i\le m\},
\]
and
\[
N(\{a_i,b_j\})=\{\{a_i,a_k\}:k\ne i\}\cup\{\{b_j,b_\ell\}:\ell\ne j\}.
\]

**Step 2: Two independent tests for total domination.** For a chosen set \(T\), write \(X=T\cap(\mathcal A\cup\mathcal B)\) and \(Y=T\cap\mathcal M\). The bipartition implies \(T\) is total dominating if and only if every mixed vertex has a neighbor in \(X\) **and** every pure-pair vertex has a neighbor in \(Y\). No selected-vertex exception is allowed.

Regard \(Y\) as the occupied cells of an \(m\)-by-\(n\) binary matrix. All \(A\)-pure pair vertices have neighbors in \(Y\) precisely when at most one row is wholly empty; otherwise the pair of two empty rows has no neighbor. Likewise, all \(B\)-pure pair vertices have neighbors in \(Y\) precisely when at most one column is wholly empty. Therefore the admissible \(Y\)'s are exactly the matrices having at most one empty row and at most one empty column.

Regard \(X\cap\mathcal A\) as an edge set of a labelled \(K_m\), and \(X\cap\mathcal B\) as an edge set of a labelled \(K_n\). A mixed vertex \(\{a_i,b_j\}\) is dominated by \(X\) if and only if vertex \(a_i\) belongs to one of the selected \(K_m\)-edges or vertex \(b_j\) belongs to one of the selected \(K_n\)-edges. If neither chosen edge set covers its entire underlying vertex class, an uncovered row \(i\) and an uncovered column \(j\) together produce an undominated mixed vertex. Conversely, covering either entire class suffices. Thus admissible \(X\)'s are exactly pairs of edge sets in which at least one side is an edge cover.

**Step 3: Exact polynomial enumeration.** Inclusion-exclusion over vertices left uncovered by an edge set of \(K_a\) gives \(E_a(z)\): after forbidding \(i\) vertices as endpoints, one may choose any of the \(\binom{a-i}{2}\) remaining edges. Inclusion-exclusion for the union of the two edge-cover conditions gives the displayed \(U_{m,n}\).

Similarly, inclusion-exclusion over \(i\) all-zero rows and \(j\) all-zero columns of an \(a\)-by-\(b\) binary matrix yields \(R_{a,b}(z)\), the cardinality enumerator of matrices with no all-zero row and no all-zero column. Choosing exactly zero or one empty row and exactly zero or one empty column, then demanding all remaining rows and columns nonempty, gives precisely the four terms of \(V_{m,n}\). The two admissibility tests concern disjoint vertices of the token graph, so their cardinality generating polynomials multiply. This proves the full identity.

**Step 4: Minimum degree and exact optimizer counts.** An edge cover of \(K_q\) requires at least \(\lceil q/2\rceil\) edges and attains that size: for even \(q\), choose a perfect matching; for odd \(q\), choose a three-vertex path together with a perfect matching on the other \(q-3\) vertices. Hence the smallest admissible \(X\) has size \(\min\{\lceil m/2\rceil,\lceil n/2\rceil\}=\lceil t/2\rceil\). The number of ways to choose this minimal \(X\) is exactly the indicator-weighted sum of \(e_m,e_n\) in the theorem. For even \(q\), the formula for \(e_q\) counts perfect matchings. For odd \(q\), it chooses the center and its two neighbors of the unique three-vertex path, and matches the remaining vertices, giving \(q!/[2^{(q-1)/2}((q-3)/2)!]\).

Every admissible \(Y\) must use at least \(s-1\) cells, since at least \(s-1\) lines parallel to the short direction must be nonempty. The bound is achieved by placing exactly one cell in each of \(s-1\) distinct long-coordinate positions, making at least \(t-1\) short-coordinate positions occupied. To count all such minima, choose the unique missing long position in \(s\) ways, choose the \(j\) occupied short positions in \(\binom tj\) ways, and assign the \(s-1\) distinct long positions surjectively onto these \(j\) short positions, in \(j!S(s-1,j)\) ways. Only \(j=t-1\) or \(j=t\) can occur. This proves the formula for \(B_{s,t}\). Multiplying the independent minimum choices proves the minimum total domination number and the complete minimum-set census.

**Step 5: Comparison with ordinary domination.** For \(m\le n\), Theorem 1.1 of Chinman et al. gives ordinary domination \(n-1+m/2\) for even \(m\), \(n\) for \(m=3\), \(n-1+(m-1)/2\) for odd \(m\ge5,n=m+1\), and \(n+(m-1)/2\) in the remaining odd cases. Subtracting from \(n-1+\lceil m/2\rceil\) proves the displayed zero-or-one gap, with no further premise.

## Verification

A complete standalone stdlib Python checker, `verify.py`, is included. It implements the two inclusion-exclusion polynomials arithmetically, independently constructs all token-graph adjacency lists from symmetric differences, enumerates the open-neighborhood total domination conditions, and compares **all coefficients**. In a second pathway it directly exhausts all selected vertex subsets for five small labelled host graphs; the independent bipartition-based enumerator checks nine parameter pairs. Minimum coefficients and the closed Stirling-number formulas are cross-checked. The completed run returned `VERIFY_OK symbolic_actual=9 exhaustive=5`. Examples: for \((m,n)=(2,2)\), \(D_t=8z^2+16z^3+14z^4+6z^5+z^6\); for \((m,n)=(3,3)\), the minimum size is \(4\) and its coefficient is \(108\). These finite checks verify the implementation but do not replace the infinite proof above.

To replay: execute `python3 verify.py` with Python 3.9 or later from the directory containing the package files. No network, additional datasets, or third-party packages are required.

## Relationship to prior work

Fabila-Monroy and Gómez-Galicia's September 19, 2025 preprint, *Domination number of Token Graphs* (arXiv:2509.16448), studies ordinary domination of two-token stars and complete graphs, giving the natural token-graph domination context. Chinman, Cortijo, Pedroni, Seong and Stenger's October 20, 2026 preprint (arXiv:2610.28936) determines the **ordinary** domination number of two-token complete bipartite graphs and gives bounds for higher token numbers. Its displayed partition into pure and mixed token types is structurally compatible with the partition used here, but ordinary domination permits self-coverage of selected vertices and therefore does not imply the present all-size **open-neighborhood total-domination** polynomial. The comparison with its ordinary parameter is expressly a corollary and not a priority claim.

The general concept of total domination polynomials predates this work: see Chaluvaraju and Chaitra (2014), *Total Domination Polynomial of A Graph*, DOI:10.26713/jims.v6i2.256, and Hu et al. (2016), arXiv:1607.00400. Their general reductions are not an explicit result for \(F_2(K_{m,n})\). Targeted literature and mathematical-record comparisons did not identify a previously published formula for the displayed factorization or complete optimal-set count. This is not a proof of historical uniqueness; independent priority checking remains needed.

## Limitations

The theorem assumes two tokens and a complete bipartite host with both parts of size at least two. It makes no statement for higher token counts, general bipartite hosts, or variants of total domination where selected vertices need not be adjacent to a selected vertex. The count distinguishes labelled configurations. The correctness argument is self-contained, but no independent mathematical audit has been performed. Historical priority and obscure equivalent presentations remain possible.

## References

1. R. Fabila-Monroy and S. G. Gómez-Galicia, *Domination number of Token Graphs*, arXiv:2509.16448 (first submitted September 19, 2025). https://arxiv.org/abs/2509.16448
2. N. Chinman, A. Cortijo, B. Pedroni, I. Seong, and L. Stenger, *The domination number of the k-token graph of the complete bipartite graph K_{m,n}*, arXiv:2610.28936v1 (October 20, 2026). https://arxiv.org/html/2610.28936v1
3. B. Chaluvaraju and V. Chaitra, *Total Domination Polynomial of A Graph*, Journal of Informatics and Mathematical Sciences 6 (2014), 416–435. DOI:10.26713/jims.v6i2.256.
4. J. Hu, E. Shan, S. Wang, C. Wang, and B. Wei, *Total domination polynomials of graphs*, arXiv:1607.00400 (2016). https://arxiv.org/abs/1607.00400
