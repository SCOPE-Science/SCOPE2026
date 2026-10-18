# Full valency spectrum of the five-dimensional Heisenberg comaximal graph

## Finding
For every prime power \(q\), the comaximal graph of the five-dimensional Heisenberg Lie algebra over \(\mathbb F_q\) has precisely five vertex-degree classes. Its complete degree distribution is

| Vertex type | Number of vertices | Degree |
| --- | ---: | ---: |
| Central line | \(1\) | \(0\) |
| Noncentral lines | \((q+1)(q^3+q^2+q+1)\) | \(q^3\) |
| Nonisotropic projected planes | \(q^2(q^2+1)\) | \(q^5+q^4+q^2\) |
| Isotropic projected planes | \((q+1)(q^2+1)^2\) | \(q^5+q^4+q^3+q^2\) |
| Projected hyperplanes | \(q^3+q^2+q+1\) | \(q^5+3q^4+3q^3+2q^2+q\) |

Here the type of a subalgebra is determined by its image in the four-dimensional symplectic quotient, except for the central-line vertex. All multiplicities are counts of **individual Lie subalgebras**, not counts of projected subspaces.

Consequently, the graph has \(q^5+3q^4+5q^3+6q^2+4q+4\) vertices and
\[
\frac{q(q^2+1)(q^7+3q^6+5q^5+9q^4+12q^3+8q^2+4q+1)}{2}
\]
edges. Its unique isolated vertex is the center; deleting it produces a graph of diameter \(2\). The clique and chromatic numbers both equal \(q^3+q^2+q+1\).

## Assumptions and scope
Let \(q\) be an arbitrary prime power (including powers of \(2\)). Set \(V=\mathbb F_q^4\) and equip it with the nondegenerate alternating form
\[
\omega(v,w)=v_1w_2-v_2w_1+v_3w_4-v_4w_3.
\]
Define \(H=V\oplus\mathbb F_q z\), with Lie bracket \([v+az,w+bz]=\omega(v,w)z\). Let \(\Gamma(H)\) have all proper nonzero Lie subalgebras as vertices, with distinct vertices adjacent precisely when the Lie subalgebra they generate is \(H\). Write \(\pi:H\to V\) for the quotient by the center. A projected plane means a two-dimensional subspace \(U\leq V\); it is isotropic when \(\omega|_U=0\) and nonisotropic otherwise. No restriction on characteristic is imposed.

## Proof
**Reduction to projected subspaces.** For each \(U\leq V\), the unique Lie subalgebra containing \(z\) with image \(U\) is \(U\oplus\mathbb F_q z\). A subalgebra not containing \(z\) and projecting isomorphically to \(U\) is the graph of a linear functional \(f:U\to\mathbb F_q\); it is closed under the Lie bracket exactly when \(U\) is totally isotropic. Therefore, for a proper nonzero projected subspace \(U\), its vertex-fiber size is
\[
m(U)=1+\begin{cases}q^{\dim U},&\omega|_U=0,\\0,&\omega|_U\ne0.\end{cases}
\]
The only vertex projecting to zero is \(\mathbb F_qz\); a subalgebra projecting onto all of \(V\) necessarily contains \(z\) and equals \(H\), so is not a vertex.

For any two proper nonzero subalgebras \(A,B\), the generated algebra equals \(H\) if and only if \(\pi(A)+\pi(B)=V\). The forward direction is immediate. Conversely, their projections span \(V\), and a spanning set cannot be totally isotropic for the nondegenerate form, so a nonzero bracket supplies \(z\); then the generated algebra contains \(z\) and projects onto \(V\), hence is all of \(H\). Thus each fiber is independent and adjacency between distinct fibers is determined solely by whether the two projected subspaces span \(V\).

**Subspace counts.** There are \(N=q^3+q^2+q+1\) lines and likewise \(N\) hyperplanes in \(V\). Every line is isotropic. The number of Lagrangian (totally isotropic) planes is \((q+1)(q^2+1)=N\): every line lies in exactly \(q+1\) Lagrangian planes, and each Lagrangian plane contains \(q+1\) lines. All other planes are nonisotropic; since the total number of planes is \((q^2+1)(q^2+q+1)\), their number is \(q^2(q^2+1)\). A hyperplane is never totally isotropic. The fiber-size rule now gives precisely the multiplicities in the table.

**Line degree.** A line spans \(V\) with a proper projected subspace only when the latter is a hyperplane not containing that line. There are \(N-(q^2+q+1)=q^3\) such hyperplanes, each having fiber size one.

**Plane degrees.** Fix a plane \(U\). Its neighbors project either to hyperplanes not containing \(U\) (there are \(q^3+q^2\)) or to complementary planes \(W\) with \(V=U\oplus W\). There are \(q^4\) complementary planes, of which the isotropic ones contribute an extra \(q^2\) vertices each. If \(U\) is Lagrangian, choose a complementary Lagrangian plane \(U'\); complementary planes are graphs of linear maps \(U'\to U\), and the isotropy condition corresponds to symmetric bilinear forms on the two-space \(U'\), giving exactly \(q^3\) isotropic complements. If \(U\) is nonisotropic, then \(V=U\perp U^\perp\) with both factors symplectic planes. The complements are graphs of maps \(T:U^\perp\to U\). In symplectic bases their isotropy condition is \(\det T=-1\). Such maps form one determinant fiber of \(\operatorname{GL}_2(\mathbb F_q)\), of cardinality \(q(q^2-1)\), also in characteristic two. Hence
\[
\deg(U)=q^3+q^2+q^4+q^2 c(U),\qquad
c(U)=\begin{cases}q^3,&U\text{ isotropic},\\q(q^2-1),&U\text{ nonisotropic}.\end{cases}
\]
This yields the two plane rows.

**Hyperplane degree.** For any hyperplane \(U\), its neighbors project to (i) the other \(N-1\) hyperplanes, (ii) the \(q^3\) lines outside \(U\), each with fiber size \(q+1\), and (iii) the \(q^2(q^2+q+1)\) planes outside \(U\), with one extra \(q^2\) vertices for each isotropic such plane. The restricted alternating form on \(U\) has a one-dimensional radical. Its totally isotropic planes are exactly the \(q+1\) planes containing that radical. Since \(V\) has \((q+1)(q^2+1)\) isotropic planes, precisely \(q^2(q+1)\) lie outside \(U\). Adding contributions gives
\[
\deg(U)=(N-1)+q^3(q+1)+q^2(q^2+q+1)+q^4(q+1)
=q^5+3q^4+3q^3+2q^2+q.
\]
Finally \(\mathbb F_qz\) projects to zero and is isolated. This proves the complete spectrum.

**Consequences.** Summing the multiplicities and half the multiplicity-weighted degrees gives the asserted vertex and edge counts. All \(N\) hyperplanes are mutually adjacent, showing \(\omega(\Gamma)\ge N\). Conversely, color each noncentral vertex by any projected hyperplane containing its projected proper subspace; adjacent vertices cannot receive the same color. Color the isolated vertex arbitrarily. This proves \(\chi(\Gamma)=\omega(\Gamma)=N\). For any two distinct nonisolated, nonadjacent vertices, choose a projected hyperplane containing neither projection: two proper annihilator subspaces cannot cover the entire four-dimensional dual space. Its associated vertex is adjacent to both, proving diameter at most two; nonadjacent vertices in any line fiber give diameter exactly two.

## Verification
The accompanying standalone `verify.py` enumerates every vector subspace of \(\mathbb F_q^5\) in reduced-row-echelon form for \(q=2\) and \(q=3\), retains exactly the Lie-bracket-closed nonzero proper ones, determines adjacency by the span of their generators and their brackets (rather than assuming the projected-adjacency criterion), and checks every predicted vertex type and degree. The resulting degree distributions are:

- \(q=2\): degree-multiplicity pairs \((0,1),(8,45),(52,20),(60,75),(114,15)\); total \(156\) vertices.
- \(q=3\): degree-multiplicity pairs \((0,1),(27,160),(333,90),(360,400),(588,40)\); total \(691\) vertices.

These are exhaustive **finite cases** corroborating, not replacing, the symbolic proof for all prime powers.

## Relationship to prior work
Towers, Zuleta and Gutierrez introduced comaximal graphs of finite-dimensional Lie algebras and determined the three-dimensional cases in arXiv:2605.09583. Their follow-up arXiv:2608.16575 computes triangle numbers in dimension three, analyzes selected four-dimensional algebras, and gives a general Frattini-quotient blow-up framework in Theorem 6.1. The present five-dimensional degree spectrum is a new **explicit specialization with nonuniform symplectic fiber sizes and two distinct plane valencies**; the blow-up principle and the small-dimensional classifications are prior work and are not claimed anew. Existing subalgebra-commutativity-degree computations concern the different adjacency relation of subalgebra permutability, not Lie generation.

## Limitations
The theorem concerns the five-dimensional, two-step Heisenberg Lie algebra only; it does not classify arbitrary five-dimensional Lie algebras or compute graph spectra of higher-rank Heisenberg algebras. External literature searches cannot exclude an unindexed prior degree-spectrum computation or equivalent finite-geometric result. The finite checks cover prime fields of orders two and three, while the proof covers all prime powers.

## References
1. D. A. Towers, Y. Zuleta, I. Gutierrez, *The comaximal graph of a finite-dimensional Lie algebra* (2026), arXiv:2605.09583, https://arxiv.org/abs/2605.09583.
2. D. Towers, Y. Zuleta, I. Gutierrez, *Comaximal Graphs of finite-dimensional Lie algebras over finite fields: Triangle counts and structural invariants* (2026), arXiv:2608.16575, https://arxiv.org/abs/2608.16575. Author-uploaded open text at https://www.researchgate.net/publication/412293715_COMAXIMAL_GRAPHS_OF_FINITE-DIMENSIONAL_LIE_ALGEBRAS_OVER_FINITE_FIELDS_TRIANGLE_COUNTS_AND_STRUCTURAL_INVARIANTS.
