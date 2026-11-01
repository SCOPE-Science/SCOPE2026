# All-weight symmetric-group homology characters of Johnson graph clique complexes

## Finding
For all integers \(n\ge6\) and \(3\le k\le n-3\), write \(K_{n,k}=\operatorname{Cl}(J(n,k))\). Here \(J(n,k)\) has the \(k\)-subsets of \([n]\) as vertices, and two vertices are adjacent when their intersection has size \(k-1\). Thus \(K_{n,k}\) is the inclusive scale-one, shortest-path Vietoris–Rips complex of the Johnson graph. The full symmetric group \(S_n\) acts by permuting \([n]\).

Let \(P_r=\mathbb Q\bigl[\binom{[n]}r\bigr]\) be the \(r\)-set permutation module; let \(I_-\) be the permutation module on flags \((A,U)\) with \(|A|=k-1\), \(|U|=k\), \(A\subset U\); let \(I_+\) be the permutation module on flags \((U,B)\) with \(|U|=k\), \(|B|=k+1\), \(U\subset B\). Finally let \(E\) be the signed oriented-edge module of \(J(n,k)\): for each unoriented graph edge there is one basis direction, and an automorphism reversing its endpoints negates that basis vector. In particular,
\[
E\cong\operatorname{Ind}_{S_{k-1}\times S_2\times S_{n-k-1}}^{S_n}(\mathbf1\boxtimes\operatorname{sgn}\boxtimes\mathbf1).
\]

The only nonzero reduced rational homology group is in degree two, and its **entire \(S_n\)-character** satisfies the following exact identity in the rational representation ring:
\[
\boxed{[\widetilde H_2(K_{n,k};\mathbb Q)]
=[P_{k-1}]+[P_k]+[P_{k+1}]+[E]-[I_-]-[I_+]-[\mathbf1].}
\]
This is a virtual-module expression for an actual semisimple rational representation, not a claimed decomposition into summands with negative multiplicities. It determines its character on *every* permutation and thus the rational isomorphism class. Its dimension is
\[
\beta(n,k)=\binom nk-1-\frac{k(n-k)}2\binom nk
+\binom n{k-1}\binom{n-k}{2}+\binom n{k+1}\binom k2.
\]
Moreover neither the trivial nor the full sign representation occurs in \(\widetilde H_2(K_{n,k};\mathbb Q)\). Consequently both ordinary symmetry quotients are **rationally acyclic**:
\[
\boxed{\widetilde H_*(|K_{n,k}|/S_n;\mathbb Q)
=\widetilde H_*(|K_{n,k}|/A_n;\mathbb Q)=0.}
\]
These are claims about *rational homology* of the quotient spaces, not contractibility or integral homology. The weight-three character was previously obtained independently; the general all-weight formula, including every \(k\ge4\) in the displayed range, and its uniform alternating-group quotient consequence are the claimed extension.

## Assumptions and scope
All graphs are finite simple graphs; a clique is a set of mutually adjacent vertices. Reduced homology is simplicial homology, and quotient means the topological orbit space of the geometric realization. The indices \(n\ge6\) and \(3\le k\le n-3\) ensure both star and top facets have at least four vertices. The \(S_n\)-action is the coordinate permutation action; \(A_n\) is the alternating subgroup. A character identity in the Grothendieck group of rational \(S_n\)-representations uniquely identifies a rational representation because this category is semisimple.

## Proof
**1. Unique maximal facet above every edge triangle.** For adjacent \(k\)-sets \(U=A\cup\{a\}\) and \(V=A\cup\{b\}\), where \(|A|=k-1\), a common neighbor is either \(A\cup\{c\}\), or \((A\setminus\{x\})\cup\{a,b\}\). A vertex of the first kind and one of the second kind cannot be adjacent: they intersect in \(k-2\) elements. Hence every clique of at least three vertices belongs to exactly one of two kinds of maximal simplex. A *star* \(F_A\), indexed by \(|A|=k-1\), consists of all \(A\cup\{c\}\) and has \(n-k+1\) vertices; a *top* \(T_B\), indexed by \(|B|=k+1\), consists of the \(B\setminus\{b\}\) and has \(k+1\) vertices. Distinct stars or distinct tops meet in at most one vertex. A star and a top meet in either zero or two vertices; they meet in two exactly when \(A\subset B\). Each graph edge belongs to exactly one star and exactly one top. These assertions follow directly from the set descriptions, independently of any numerical calculation.

**2. Homology is concentrated in degree two.** Choose a vertex \(v_F\) separately in each maximal simplex \(F\). Within each facet, process all subsets \(\tau\subset F\setminus\{v_F\}\) of cardinality at least three in descending cardinality, deleting the elementary pair \((\tau,\tau\cup\{v_F\})\). This is valid because every face of size at least three lies in exactly one facet; every other coface of \(\tau\) has already been deleted in the descending order. All remaining simplices have dimension at most two, so reduced homology above degree two vanishes. The choice of \(v_F\) need not be equivariant, and no equivariant collapse is asserted.

The convex hypersimplex \(\{x\in[0,1]^n:\sum_i x_i=k\}\) has the Johnson graph as its one-skeleton. Its two-dimensional faces are all triangles coming from fixed coordinates with three varying entries, and each such triangle is either a star triangle or a top triangle in \(K_{n,k}\). Because the hypersimplex has dimension \(n-1\ge5\), its boundary is simply connected and so is its cellular two-skeleton. That two-skeleton is contained in \(K_{n,k}\) and has the same one-skeleton. Therefore \(K_{n,k}\) is simply connected. It is connected, has no homology above two, and its integral second homology is free (a subgroup of a free two-chain group of the collapsed complex). In particular the reduced rational homology is concentrated in degree two. This also recovers the known sphere-wedge homotopy classification, without claiming it as new.

**3. Signed equivariant Euler calculation.** Regard rational oriented simplicial chains as \(S_n\)-modules, with the sign of the induced permutation on each simplex. Write \(C_j(F)\) for the chains of a simplex \(F\). Contractibility of a simplex, applied equivariantly to the entire permutation orbit of that facet, gives
\[
\sum_F\sum_{j\ge2}(-1)^j[C_j(F)]
=[P_{k-1}]+[P_{k+1}]-\sum_F[C_0(F)]+\sum_F[C_1(F)].
\]
Every \(j\)-simplex for \(j\ge2\) belongs to a unique maximal facet. The sum of facet vertex modules is exactly \([I_-]+[I_+]\), since each occurrence records an incident star or top. The sum of facet oriented-edge modules is \(2[E]\), because each edge occurs in exactly one facet of each kind and the induced edge orientation action is the same. Finally \(C_0(K_{n,k})=P_k\) and \(C_1(K_{n,k})=E\). Therefore the reduced equivariant Euler identity and the homology concentration from Step 2 give
\[
[\mathbf1]+[\widetilde H_2(K_{n,k})]
=[P_k]-[E]+[P_{k-1}]+[P_{k+1}]-[I_-]-[I_+]+2[E],
\]
which rearranges to the displayed character formula. Taking dimensions gives \(\beta(n,k)\), since \(\dim I_- = k\binom nk\), \(\dim I_+=(n-k)\binom nk\), and \(\dim E=\tfrac12 k(n-k)\binom nk\). Equivalently, the two-dimensional collapse retains \(\binom n{k-1}\binom{n-k}{2}+\binom n{k+1}\binom k2\) triangles.

**4. Trivial and sign multiplicities.** Each of the five permutation modules \(P_{k-1},P_k,P_{k+1},I_-,I_+\) is transitive, hence has precisely one invariant vector. The oriented-edge module \(E\) has no invariant vector because its edge stabilizer contains the involution exchanging the two ends and acting by \(-1\). Thus the invariant multiplicity of the displayed character is \(1+1+1+0-1-1-1=0\). None of the five transitive permutation modules contains the full sign representation: each point stabilizer contains an odd permutation. The induced module \(E\) also has no full sign constituent, by Frobenius reciprocity: its stabilizer includes \(S_{k-1}\) and \(S_{n-k-1}\), both of order at least two, which act trivially in the inducing line but nontrivially in the restriction of the full sign representation. Hence the sign multiplicity is zero. For \(A_n\), Frobenius reciprocity shows \(\dim\widetilde H_2(K_{n,k};\mathbb Q)^{A_n}\) equals the sum of the trivial and sign multiplicities for \(S_n\), so it too is zero. Rational homology of the orbit space of a finite simplicial group action agrees with invariants after barycentric subdivision; this proves both quotient claims.

## Verification
The self-contained file `verify_johnson_character.py` constructs faces directly from the two maximal-facet families. For \((n,k)=(6,3),(7,3),(8,3),(8,4)\), it compares the signed fixed-face Lefschetz trace with the completely separate incidence/edge character formula at every cycle-type representative (respectively 11, 15, 22 and 22, totalling 70). It also computes mod-two boundary ranks directly and checks the predicted homology dimensions and that the averages against the trivial and sign characters vanish. The run prints `JOHNSON_ALL_WEIGHT_SYMMETRY_VERIFY_OK 70`; `verification_output.txt` contains the actual output.

Finite checks do not prove the unbounded statement: Steps 1–4 prove it for all stated \(n,k\). For instance \(\beta(8,4)=181\), while transpositions and three-cycles each have trace \(1\); this case is outside the earlier weight-three character result.

## Relationship to prior work
Adamaszek [1] treats clique complexes of distance powers of graphs and motivates Vietoris–Rips homology from graph metrics; his paper does not compute Johnson-graph symmetry representations. Shuldiner–Oldford [2] prove that Johnson cliques have exactly the two families used in Step 1 (their Theorem 3.4 and Proposition 4.2); they do not compute any homology character. The public result [3] already determines the all-parameter **ordinary homotopy type**, hence also the dimensions \(\beta(n,k)\), and is expressly not extended here in that respect. The public result [4] computes the full character for weight \(k=3\); that special case is already covered and is used only as a comparison and check. Neither [3] nor [4] states the two-parameter \(S_n\)-character, especially for \(k\ge4\), or the uniform \(A_n\)-quotient conclusion. Galetto–Montaño–Wellner [5] study the entire Boolean-cube Rips complex with its larger hyperoctahedral action, not the induced single-weight Johnson clique complex. The whole-space representation is not its weight-layer homology representation; an inaccessible full-text comparison for [5] remains a residual bibliographic risk.

## Limitations
This result concerns scale one, rational representations, and ordinary rational quotient homology. It does not classify integral group-action lattices, higher Rips scales, homotopy types of orbit spaces, or their torsion. The character formula is virtual (although it equals an actual character) and is not a positive irreducible Specht-module decomposition. Its weight-three specialization is known. An equivalent unindexed all-weight result may exist, and independent validation of the new calculation has not been performed.

## References
[1] M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433v1 (first public 2011-04-03), https://arxiv.org/abs/1104.0433 .

[2] P. Shuldiner and R. W. Oldford, *The Clique Structure of Johnson Graphs*, arXiv:2208.12710v1 (first public 2022-08-26), https://arxiv.org/abs/2208.12710 .

[3] *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes*, public result 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sphere-wedge-collapse-of-scale-one-johnson-graph-rips-complexes--c10287ed1518 .

[4] *Symmetric-group homology character of constant-weight-three Hamming Rips complexes*, public result 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-symmetric-group-homology-character-of-constant-weight-three-hamm--11db16b6cb70 .

[5] F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1 (first public 2026-06-18), https://arxiv.org/abs/2606.20784 .
