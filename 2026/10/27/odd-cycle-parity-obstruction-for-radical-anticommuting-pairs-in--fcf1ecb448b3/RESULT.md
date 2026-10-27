# Odd-cycle parity obstruction for radical anticommuting pairs in truncated quiver algebras

## Finding
For any finite quiver \(Q\), including loops and parallel arrows, and any finite field \(k=\mathbb F_q\), let \(A=kQ/J_Q^3\), with arrow radical \(J\subseteq A\). Define the labelled ordered-pair counts
\[
 C_Q(q)=\#\{(x,y)\in J\times J:xy-yx=0\},\qquad
 H_Q(q)=\#\{(x,y)\in J\times J:xy+yx=0\}.
\]
Let \(E=Q_1\) be the arrow set and \(p=\#\{(e,f)\in E^2:t(e)=s(f)\}\) the number of directed paths of length two (counting arrow identities separately, including loops and parallel arrows). Define the *arrow-transition graph* \(G_Q\) with vertex set \(E\): it has an undirected edge between \(e\) and \(f\), with a loop when \(e=f\), if either \(ef\) or \(fe\) is a directed length-two path. For \(S\subseteq E\), write \(c(S)\) for the number of connected components of the induced graph \(G_Q[S]\), including isolated supported vertices. Let \(b(S)\) count its bipartite components and \(o(S)=c(S)-b(S)\) its nonbipartite components; any component with a loop is nonbipartite. The empty graph has all three counts zero.

**Theorem.** For every such \(Q\) and \(q\),
\[
 C_Q(q)=q^{2p}\sum_{S\subseteq E}(q-1)^{|S|}(q+1)^{c(S)}.
\]
For odd \(q\),
\[
 H_Q(q)=q^{2p}\sum_{S\subseteq E}(q-1)^{|S|}(q+1)^{b(S)}2^{o(S)},
\]
whereas \(H_Q(q)=C_Q(q)\) for even \(q\). Consequently, for every odd \(q\),
\[
 H_Q(q)=C_Q(q)\quad\Longleftrightarrow\quad G_Q\text{ is bipartite}.
\]
When \(G_Q\) is bipartite the two affine zero loci in \(J\times J\) are linearly isomorphic over any field. When \(G_Q\) is nonbipartite, the inequality \(H_Q(q)<C_Q(q)\) holds for **every** odd prime power \(q\).

## Assumptions and scope
All quivers are finite directed multigraphs. A path is an ordered sequence of *individual* composable arrows; path concatenations of length two form linearly independent basis vectors modulo \(J_Q^3\). This includes quivers with oriented cycles, self-loops, several arrows with the same endpoints, and quivers with no arrows. The fields are all finite fields, not merely prime fields. Both elements range over the radical \(J\), **not** over all of \(A\) and **not** merely over the ideal \(J^2\).

## Proof
The radical has a basis of arrows and directed length-two paths. Write
\[
 x=\sum_{e\in E}a_e e+u,\qquad y=\sum_{e\in E}b_e e+v,\qquad u,v\in J^2.
\]
Since \(J^3=0\), multiplication of \(x,y\) depends only on the arrow coefficients. The coefficient of the independent length-two path \(ef\) in \(xy\mp yx\) is \(a_e b_f\mp b_e a_f\). Thus the length-two coefficients in \(u,v\) are unrestricted, contributing \(q^{2p}\) choices; and every composable ordered arrow pair imposes exactly its indicated bilinear vanishing condition.

For each arrow set \(w_e=(a_e,b_e)\in k^2\) and define its support \(S=\{e:w_e\ne0\}\). An equation involving a zero vector is automatic. For fixed \(S\), each supported arrow determines a projective line \(L_e=[a_e:b_e]\in\mathbb P^1(k)\), and after choosing the lines there are exactly \((q-1)^{|S|}\) choices of nonzero vectors.

For a commuting pair the vanishing determinant \(a_e b_f-b_e a_f=0\) along each transition edge says \(L_e=L_f\). Every connected component of \(G_Q[S]\) may therefore be labelled by any of the \(q+1\) projective points. This gives its factor \((q+1)^{c(S)}\) and proves the first formula.

For an anticommuting pair define the projective involution \(\tau([a:b])=[a:-b]\). The condition \(a_e b_f+b_e a_f=0\) is exactly \(L_f=\tau(L_e)\). Along a connected bipartite component, choosing one of \(q+1\) lines determines all others by alternating \(\tau\). Along a nonbipartite component, an odd cycle or self-loop forces \(L=\tau(L)\); over odd characteristic exactly two projective lines satisfy this, \([1:0]\) and \([0:1]\), and both give consistent labellings. Multiplying these factors over components, then summing supports, proves the second formula. In characteristic two, \(\tau\) is the identity and the two equations coincide.

If \(G_Q\) is bipartite, choose signs \(\epsilon_e\in\{1,-1\}\) opposite on every edge. The invertible linear coordinate change \(b_e\mapsto\epsilon_e b_e\), leaving the other coordinates unchanged, takes each commuting equation to a nonzero scalar multiple of its anticommuting counterpart. Hence the two **affine zero loci, including their polynomial equations up to scalar multiples**, are linearly isomorphic. Conversely, for odd \(q\), if \(G_Q\) is not bipartite then the summand \(S=E\) contains a nonbipartite component; the factor \((q+1)^{c(S)}\) is strictly greater than \((q+1)^{b(S)}2^{o(S)}\). Every other term in the commuting sum is at least as large as its anticommuting analogue, so \(C_Q(q)>H_Q(q)\).

**Acyclic boundary example.** Use seven arrows in the displayed order
\[
 0\to1,\quad1\to2,\quad2\to4,\quad1\to3,\quad3\to5,\quad5\to4,\quad4\to6.
\]
This directed quiver is acyclic, but the induced arrow-transition graph is a single undirected seven-cycle (in arrow index order \(0,1,2,6,5,4,3,0\)); it has \(p=7\) length-two paths. Every proper induced subgraph of this cycle is bipartite, while the full support is nonbipartite. Thus for every odd \(q\),
\[
 C_Q(q)-H_Q(q)=q^{14}(q-1)^7\bigl((q+1)-2\bigr)=q^{14}(q-1)^8>0.
\]
For the oriented three-cycle, the same argument gives difference \(q^6(q-1)^4\), demonstrating the formula in both cyclic and acyclic settings.

## Verification
The standalone Python 3 script `check_pair_census.py`, requiring no nonstandard libraries, directly enumerates every pair of arrow-coefficient assignments for 22 small quiver/field instances. It constructs the directed two-arrow path equations and evaluates their vanishing independently from the support-component formulas, in both odd and even characteristic and over the nonprime field \(\mathbb F_4\). It also checks the derived odd-cycle deficit identities at field sizes three and five. Execute `python3 check_pair_census.py`. The observed completion marker was `QUIVER_ANTICOMMUTING_PARITY_OK 22 direct exhaustive cases; two algebraic odd-cycle checks`. The code multiplies by the independently known factor \(q^{2p}\) for the unrestricted length-two parts; the infinite-family statements are proved above, not inferred from the finite checks.

## Relationship to prior work
Xu, Han and Jiang (2005) develop path-basis and cohomological methods for truncated quiver algebras, not radical-pair commuting versus anticommuting counts. Gawell and Richey Xantcha (2015), although they use generator graphs and anti-commutativity, study relations **imposed on the defining ideal** and consequences for centers and Hochschild cohomology, rather than the number of element pairs satisfying zero anticommutators in the fixed algebra \(kQ/J_Q^3\). Tittmann, Averbouch and Makowsky (2008) establish the already-known induced-subgraph component polynomial; the commuting formula is an evaluation of that graph polynomial once the new quiver-to-graph identification has been made, so no novelty is claimed for the polynomial itself. The parity-twisted anticommuting count, strict equality criterion and acyclic odd-transition example require additional projective-involution analysis. Nearby existing results on radical-square-zero Kronecker commutator fibers and special linearly oriented radical-cube-zero quivers do not state or imply these general anticommuting results.

## Limitations
These are labelled ordered-pair counts, not conjugacy classes or similarity orbits, and involve the radical rather than the full algebra. The varieties are compared by a linear isomorphism only when the transition graph is bipartite; no classification of irreducible components or potentially nonreduced schemes is asserted in the nonbipartite case. Exhaustive computations cover only the specified finite tests. The source comparison does not establish absolute historical priority, and additional literature or graph-polynomial reformulations may contain overlapping consequences. No independent mathematical audit has been conducted.

## References
1. Y. Xu, Y. Han, W. Jiang, *Hochschild cohomology of truncated quiver algebras*, arXiv:math/0509202v1 (first public 2005-09-09), https://arxiv.org/abs/math/0509202.
2. E. Gawell, Q. Richey Xantcha, *Centers of partly (anti-)commutative quiver algebras and finite generation of the Hochschild cohomology ring*, arXiv:1504.00582v1 (first public 2015-04-02), https://arxiv.org/abs/1504.00582.
3. P. Tittmann, I. Averbouch, J. A. Makowsky, *The enumeration of vertex induced subgraphs with respect to the number of components*, arXiv:0812.4147 (first public 2008-12-22), https://arxiv.org/abs/0812.4147.
