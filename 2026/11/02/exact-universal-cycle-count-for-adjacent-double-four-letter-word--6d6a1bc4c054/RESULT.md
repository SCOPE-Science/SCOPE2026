# Exact universal-cycle count for adjacent-double four-letter words

## Finding

Fix a labeled alphabet \(\Sigma\) of size \(q\ge 3\), and let
\[
\mathcal A_q=\{aabc,\;abbc,\;abcc:\ a,b,c\in\Sigma\text{ pairwise distinct}\}.
\]
Thus every permitted word has exactly three distinct symbols and exactly one adjacent equal pair. A universal cycle is an oriented cyclic word of length \(|\mathcal A_q|\) whose cyclic four-letter windows are exactly the members of \(\mathcal A_q\), once each. Cycles are identified under rotation, but neither reversal nor alphabet relabeling.

**Theorem.** No universal cycle exists when \(q=3\). For every \(q\ge4\), universal cycles exist, their length is \(3q(q-1)(q-2)\), and their exact number is
\[
\boxed{U_q=q^{q-2}(q-2)^{3q-2}(q-3)^{q^2-3q+1}(q-1)^{q^2-3q}\bigl((q-3)!\bigr)^{2q(q-1)}.}
\]
In every such cycle, each alphabet symbol occurs precisely \(3(q-1)(q-2)\) times. In particular \(U_4=1{,}327{,}104\), and \(U_5=470{,}561{,}093{,}629{,}261{,}335{,}377{,}215{,}488{,}000\).

## Assumptions and scope

The alphabet consists of \(q\) individually labeled symbols. Distinct cycles are identified only under cyclic shift; reflections, alphabet permutations and coordinate relabelings are not quotiented out. Every length-four factor is counted with its cyclic starting position, including factors crossing the boundary. The empty target family for \(q\le2\) is excluded from the definition; the nonexistence statement refers to the nonempty family at \(q=3\).

## Proof

**1. Overlap graph and connectivity.** Give each permitted four-letter word an arc from its first three symbols to its last three. For pairwise distinct \(a,b,c\), the arcs have exactly the following forms:
\[
X_{ab}=aab\ \longrightarrow\ Z_{abc}=abc\quad (aabc),
\]
\[
Z_{abc}=abc\ \longrightarrow\ Y_{bc}=bcc\quad (abcc),
\]
\[
Y_{ab}=abb\ \longrightarrow\ X_{bc}=bbc\quad (abbc).
\]
There are \(q(q-1)\) vertices of each of the \(X\) and \(Y\) types, and \(q(q-1)(q-2)\) vertices of type \(Z\). Every \(X\) or \(Y\) vertex has indegree and outdegree \(d=q-2\); every \(Z\) vertex has both degrees one. Each of the \(3q(q-1)(q-2)\) arcs is a different word.

Contracting each forced two-step path \(X_{ab}\to Z_{abc}\to Y_{bc}\) leaves a bipartite directed graph \(H_q\) with vertices \(X_{ab},Y_{ab}\) for \(a\ne b\), and arcs
\[
X_{ab}\to Y_{bc},\qquad Y_{ab}\to X_{bc}
\quad\text{for all pairwise distinct }a,b,c.
\]
Its transition matrix has block form \(H=\begin{pmatrix}0&T\\T&0\end{pmatrix}\), where \(T_{(a,b),(b,c)}=1\) precisely when \(a,b,c\) are pairwise distinct. Thus \(T\) is the non-backtracking arc matrix of the complete simple graph \(K_q\).

For \(q=3\), its non-backtracking walks split into the two directed triangular orientations; the full overlap graph splits into two components (each containing nine arcs), so no single Euler tour exists. For \(q\ge4\), the non-backtracking directed graph is strongly connected (any oriented edge can be reached from any other without an immediate reversal). It has directed cycles of lengths three and four, so it is aperiodic. Consequently its bipartite parity lift \(H_q\) is strongly connected; subdividing specified arcs preserves strong connectivity. Since the full overlap graph is balanced, Euler tours, hence universal cycles, exist for every \(q\ge4\).

**2. Exact arborescence count.** Let \(d=q-2\) and \(e=q(q-3)/2\). The Ihara determinant identity for the non-backtracking matrix of \(K_q\), whose ordinary adjacency spectrum is \(q-1\) once and \(-1\) with multiplicity \(q-1\), gives
\[
\det(tI-T)=(t^2-1)^e(t-d)(t-1)(t^2+t+d)^{q-1}.
\]
In particular, the eigenvalue \(d\) is simple; the eigenvalues \(1\) and \(-1\) occur with multiplicities \(e+1\) and \(e\), respectively; and each root \(\alpha,\beta\) of \(t^2+t+d\) occurs \(q-1\) times.

The eigenvalues of \(H\) occur in pairs \(\pm\lambda\) for every eigenvalue \(\lambda\) of \(T\), with algebraic multiplicity. The directed Laplacian of \(H_q\) is \(L=dI-H\), of size \(N=2q(q-1)\). Its zero eigenvalue is simple by strong connectivity. The product of its other eigenvalues is
\[
2d(d^2-1)^{2e+1}
\left((d^2-\alpha^2)(d^2-\beta^2)\right)^{q-1}.
\]
Since \(\alpha+\beta=-1\) and \(\alpha\beta=d\), the factor in parentheses equals \(d^3(d+2)=qd^3\). Therefore the product is
\[
2d(d^2-1)^{q(q-3)+1}(qd^3)^{q-1}.
\]
For a strongly connected balanced directed graph, the directed matrix-tree theorem says its arborescence count toward any fixed root equals the product of nonzero Laplacian eigenvalues divided by \(N\). Contracting each degree-one \(Z\) vertex preserves the directed arborescence cofactor rooted at any \(X\) vertex: in the Laplacian cofactor, eliminating the degree-one \(Z\) row and column replaces the path \(X\to Z\to Y\) by the single arc \(X\to Y\), with determinant factor one. Hence the full overlap graph has
\[
\tau_q=\frac{2d}{2q(q-1)}(d^2-1)^{q(q-3)+1}(qd^3)^{q-1}
=q^{q-2}d^{3q-2}(q-3)^{q^2-3q+1}(q-1)^{q^2-3q}
\]
in-arborescences rooted at a fixed vertex.

**3. Euler-tour count and cyclic normalization.** The BEST theorem counts Euler tours beginning with a specified directed arc as
\[
\tau_q\prod_v(\deg^+(v)-1)!=\tau_q\bigl((d-1)!\bigr)^{2q(q-1)}.
\]
The \(Z\) vertices contribute \(0!=1\). Every Euler tour has exactly one cyclic rotation beginning with the specified arc, since the arc is used exactly once. Arc labels are distinct permitted four-letter words, so this is exactly the number of universal cycles modulo rotation, with no additional division by the cycle length. Substituting \(d=q-2\) gives the displayed formula. Finally, for each fixed alphabet symbol, exactly \(3(q-1)(q-2)\) permitted four-letter words start with it, which proves the symbol-frequency statement.

## Verification

The standalone standard-library program `verify.py` independently constructs the full three-letter overlap graph and its contracted bipartite graph. It computes exact directed Laplacian cofactors using integer-preserving fraction-free elimination for \(q=3,4,5\), comparing both with the closed formula. It checks in/out-degree balance, graph components, and all distinct permitted windows. A separate deterministic Hierholzer construction produces and verifies Euler cycles for \(q=4,5,6,7\); the length-\(72\) example for \(q=4\) is included as `witness_q4.txt`.

Run `python3 verify.py` with a standard Python 3 interpreter; success ends with `VERIFY_OK`. These finite calculations independently corroborate the exact determinant and existence deductions, but the all-alphabet theorem rests on the symbolic graph and spectral proof above.

## Relationship to prior work

Gardner and Godbole (2017, Theorem 21) show existence of universal cycles for unrestricted one-or-two-copy augmented-onto words. At length four on three symbols, the unrestricted repeated-letter family is cyclable, whereas imposing that the unique repeat be adjacent splits the graph and destroys cyclability. Leitner and Godbole (2008) prove Eulerian existence for other restricted word classes, without the present local adjacency restriction or enumeration. Chen, Kitaev and Sun (2019) analyze removal of small sets from full word universes and the binary length-four boundary, rather than the all-\(q\) adjacent-double family. Glover and Kempton (2020) provide the non-backtracking spectral identity, used here as a known tool, rather than the restricted-word Euler-tour count. The classical BEST and directed matrix-tree theorems are likewise used rather than claimed new.

## Limitations

The count does not quotient alphabet permutations or reversal. The result is specific to four-letter windows with exactly three distinct symbols and an adjacent unique repeated pair; it does not assert a formula for all one-repeat words or arbitrary window lengths. The existence proof is not a closed-form listing algorithm, although Euler tours are constructible and the provided verifier exhibits finite examples. Prior-work comparison cannot rule out an unindexed equivalent count derived from non-backtracking Euler tours.

## References

- K. B. Gardner and A. Godbole, *Universal Cycles of Restricted Words*, arXiv:1711.07029, first public 2017-11-19, especially Theorem 21. https://arxiv.org/abs/1711.07029
- A. Leitner and A. Godbole, *Universal Cycles of Classes of Restricted Words*, arXiv:0808.1309, first public 2008-08-08. https://arxiv.org/abs/0808.1309
- H. Z. Q. Chen, S. Kitaev and B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116, first public 2019-08-03. https://arxiv.org/abs/1908.01116
- C. Glover and M. Kempton, *Spectral properties of the non-backtracking matrix of a graph*, arXiv:2011.09385, first public 2020-11-18, Theorem 2.1 and Theorem 2.2. https://arxiv.org/abs/2011.09385
- The classical BEST theorem and the directed matrix-tree theorem (standard graph-theoretic tools).
