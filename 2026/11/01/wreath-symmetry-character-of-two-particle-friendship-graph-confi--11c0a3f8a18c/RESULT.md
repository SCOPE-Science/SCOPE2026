# Wreath-symmetry character of two-particle friendship-graph configurations

## Finding
For each integer \(n\ge2\), join \(n\) triangles at a single common vertex to obtain the *friendship graph* \(F_n\). Put \(X_n=\operatorname{UConf}_2(|F_n|)\). Its automorphism group \(W_n=C_2\wr S_n\) permutes the triangular petals and may independently reverse each petal. Let \(B_n\) be the rational permutation representation on the \(n\) petals, let \(B_n^0=\ker(B_n\to\mathbb Q)\) be its augmentation module, and let \(A_n\) be the signed petal module: a reversal of petal \(i\) negates its \(i\)-th basis vector, while petal permutations permute these vectors. Then

\[
H_1(X_n;\mathbb Q)\cong \bigwedge{}^2 B_n^0\oplus(B_n\otimes A_n)
\]

as rational \(W_n\)-modules. In particular,

\[
H_2(X_n;\mathbb Z)=0,\qquad
H_1(X_n;\mathbb Z)\cong\mathbb Z^{1+3\binom n2}.
\]

For \(g=(\sigma,\varepsilon)\in W_n\), let \(f\) be the number of petals fixed by \(\sigma\), let \(f_2\) be the number fixed by \(\sigma^2\), and let \(t\) be the sum of the signs \(\varepsilon_i\in\{1,-1\}\) over petals fixed by \(\sigma\). The first-homology character is

\[
\chi_{H_1}(g)=\frac{(f-1)^2-(f_2-1)}{2}+ft.
\]

The full orbit space is rationally acyclic, while the orbit space for the petal-permutation subgroup has two rational first-homology generators:

\[
\widetilde H_*(X_n/W_n;\mathbb Q)=0,\qquad
\dim_{\mathbb Q}H_1(X_n/S_n;\mathbb Q)=2.
\]

## Assumptions and scope
The graph is the finite simple \(1\)-dimensional CW complex with center \(h\), leaves \(u_i,v_i\), and edges \(h u_i\), \(h v_i\), \(u_i v_i\), for \(1\le i\le n\). Its edges have unit length. The space consists of **unordered pairs of distinct points**, with collisions forbidden also inside edges. The group action is the geometric one induced by graph automorphisms. A reversal exchanges \(u_i\) and \(v_i\). The subgroup \(S_n\le W_n\) preserves the chosen order \(u_i,v_i\) within each petal. These are ordinary, not homotopy/Borel, orbit spaces. All character statements use rational coefficients.

## Proof
**1. An equivariant finite model.** Every cycle of \(F_n\) has length at least three. The necessary subdivision condition for the two-particle cubical model is automatic, since the other condition asks for at least one edge between distinct essential vertices. The standard two-particle graph configuration deformation moves two points on a common edge apart and moves points on adjacent edges away from their shared endpoint. All edges have equal lengths, and each motion is symmetric in its incident edges and the two particles; therefore this construction commutes with every graph automorphism. Thus the unordered Abrams cubical complex \(D_n\) is an equivariant deformation retract of \(X_n\). This argument uses the two-point version of the discrete-model theorem, rather than merely asserting a nonequivariant equivalence.

**2. Cells and integral boundaries.** Write \(U\) for the signed-free permutation module on the \(2n\) leaves (a graph automorphism permutes leaves). Orient spokes from \(h\) to their leaf and each petal edge from \(u_i\) to \(v_i\). A \(0\)-cell of \(D_n\) is an unordered pair of distinct vertices. The \(1\)-cells are an edge together with a vertex disjoint from its closure. The \(2\)-cells are unordered pairs of edges with disjoint closures. There are no higher cells. Consequently the numbers of cells in degrees \(0,1,2\) are

\[
\binom{2n+1}{2},\qquad3n(2n-1),\qquad\frac{5n(n-1)}2.
\]

The square cells split into \(2n(n-1)\) *spoke–other-petal* squares and \(\binom n2\) *petal–petal* squares. The former use a spoke at petal \(i\) and the outer edge at distinct petal \(j\); the latter use outer edges of two different petals.

**3. Unimodularity, torsion, and homology ranks.** Orient a square with ordered edges \(e=(a,b)\), \(f=(c,d)\) by the product orientation. Its boundary is \((f,b)-(f,a)-(e,d)+(e,c)\). For every spoke–other-petal square consisting of the spoke \(h\to u_i\) or \(h\to v_i\) together with outer petal edge \(u_j\to v_j\), choose the boundary row with that spoke and vertex \(u_j\). This row appears in no other spoke–other-petal square, with coefficient \(\pm1\), and in no petal–petal square. For every petal–petal square indexed by \(i<j\), choose the row with oriented petal edge \(u_i\to v_i\) and vertex \(u_j\). This row appears in no other petal–petal square, again with coefficient \(\pm1\). In the order just given the square-boundary matrix has a lower block-triangular square minor with two signed identity diagonal blocks. It has determinant \(\pm1\), so its columns are independent over the integers and generate a primitive direct summand of the free group of \(1\)-chains. Therefore \(H_2(D_n;\mathbb Z)=0\), and \(H_1(D_n;\mathbb Z)\) is torsion-free. The cubical \(1\)-skeleton is connected: on a connected graph with at least three vertices, two unordered vertex tokens may be successively moved along a spanning tree to a common target pair. Euler characteristic now gives

\[
\operatorname{rank}H_1=1-\binom{2n+1}{2}+3n(2n-1)-\frac{5n(n-1)}2=1+3\binom n2.
\]

**4. Character decomposition.** Work over \(\mathbb Q\). Set \(Q=\mathbb Q[\{\text{unordered pairs of distinct leaves}\}]\). Set \(D\) equal to the signed module on a petal edge together with a leaf in another petal: reversal of the petal carrying the edge changes sign. We have the following genuine isomorphisms of cellular chain representations:

\[
C_0\cong U\oplus Q,
\quad C_1\cong Q\oplus\bigwedge{}^2U\oplus A_n\oplus D,
\quad C_2\cong D\oplus\bigwedge{}^2 A_n.
\]

Indeed, spoke–leaf \(1\)-cells are ordered *distinct* leaf pairs, whose symmetric and antisymmetric parts yield \(Q\oplus\bigwedge{}^2U\) in characteristic zero. Petal-edge–center \(1\)-cells furnish \(A_n\), and petal-edge–other-leaf \(1\)-cells furnish \(D\). The two types of oriented square cells furnish \(D\) and \(\bigwedge{}^2 A_n\), respectively. Since the complex is connected and has no second homology, the alternating character identity gives

\[
[H_1]=[\mathbf1]-[C_0]+[C_1]-[C_2]
=[\mathbf1]-[U]+[\bigwedge{}^2U]+[A_n]-[\bigwedge{}^2A_n].
\]

The leaf module splits canonically as \(U=B_n\oplus A_n\), and \(B_n=\mathbf1\oplus B_n^0\). Thus

\[
[H_1]=[\bigwedge{}^2B_n^0]+[B_n\otimes A_n].
\]

Maschke semisimplicity upgrades equality of rational characters to an isomorphism. Moreover \(\operatorname{tr}(g\mid B_n^0)=f-1\) and \(\operatorname{tr}(g^2\mid B_n^0)=f_2-1\); the usual exterior-square trace identity, together with \(\operatorname{tr}(g\mid A_n)=t\), gives the displayed character.

**5. Quotient calculations.** The independent petal reversals have no fixed vectors in \(B_n\otimes A_n\), and \(\bigwedge{}^2B_n^0\) has no \(S_n\)-invariant vectors. Hence \(H_1(X_n;\mathbb Q)^{W_n}=0\). After restricting to the \(S_n\) petal-permutation subgroup, \(A_n\) becomes \(B_n\), whose tensor square has exactly two invariant directions, corresponding to diagonal and off-diagonal ordered petal pairs. Thus \(\dim H_1(X_n;\mathbb Q)^{S_n}=2\). Rational transfer for a finite group acting cellularly, after equivariant subdivision, identifies rational homology of each ordinary quotient with these invariant groups. Together with connectedness and the vanishing of higher homology, this proves the assertions.

## Verification
The companion standard-library program `verify_friendship.py` reconstructs the oriented cubical boundary operators for \(n=2,3,4,5\). It tests \(\partial_1\partial_2=0\), all primitive-minor pivot entries and zero conditions, and connectivity. It then enumerates **all** \(2^n n!\) automorphisms at each tested \(n\) and independently computes the cellular Lefschetz character, including square-orientation signs. The program prints `FRIENDSHIP_WREATH_CHARACTER_AND_UNIMODULAR_MINOR_OK`. Its finite checks corroborate, but do not replace, the preceding uniform proof.

## Relationship to prior work
Abrams' discrete graph-configuration model and the sufficient-subdivision analysis of Prue–Scrimshaw underpin the finite model. Barnett–Farber studied two-point configurations on graphs, primarily ordered configurations, and Ko–Park determined general nonequivariant first graph-braid homology, including the rank and planar torsion context. Maciążek–Sawicki treat homology of configurations on one-connected graphs. None of these familiar dimension/homology results is presented as novel here; the claimed refinement is the exact action of all independent petal reversals and petal permutations on ordinary rational first homology, with its character and quotient consequences. Relevant mathematical-record comparisons included analogous matching complexes of Dutch windmill graphs (a different space) and exchange-sign Borel–Moore graph-configuration homology (different theory). No claim of definitive publication priority is made.

## Limitations
The result concerns **exactly two unordered, collision-free particles** on friendship graphs and rational representation decomposition. It does not identify the integral representation lattice, determine higher-particle groups, or give the fundamental groups of the ordinary quotients. Existing nonequivariant rank and torsion results are not new contributions. Equivalent unpublished or unindexed equivariant work remains a possibility; independent validation has not been performed.

## References
1. Kathryn Barnett and Michael Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180v1 (public 2009-03-12).
2. Paul Prue and Travis Scrimshaw, *Abrams's Stable Equivalence for Graph Braid Groups*, arXiv:0909.5511v1 (public 2009-09-30).
3. Ki Hyoung Ko and Hyo Won Park, *Characteristics of Graph Braid Groups*, arXiv:1101.2648v1 (public 2011-01-13); especially Theorem 3.16.
4. Tomasz Maciążek and Adam Sawicki, *Homology Groups for Particles on One-Connected Graphs*, arXiv:1606.03414v1 (public 2016-06-10).
