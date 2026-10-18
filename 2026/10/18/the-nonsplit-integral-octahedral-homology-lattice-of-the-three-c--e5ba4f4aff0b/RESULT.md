# The nonsplit integral octahedral homology lattice of the three-cube matching complex

## Finding

Let \(Q_3\) be the cube graph on \(\mathbb F_2^3\), equivalently the four-rung circular ladder \(C_4\mathbin{\square}K_2\), and let \(K=\mathcal M(Q_3)\) be the ordinary matching complex: its vertices are the twelve cube edges, and its faces are sets of pairwise vertex-disjoint cube edges. Every graph automorphism is uniquely \(g_{p,t}:v\mapsto p(v)+t\), with \(p\in S_3\), \(t\in\mathbb F_2^3\); thus \(G=\operatorname{Aut}(Q_3)\) has order \(48\).

Let \(\mathcal D\) be the four long body diagonals, \(\pi_g\in S(\mathcal D)\) the permutation induced by \(g\), and \(\varepsilon(g)=(-1)^{|t|}\), where \(|t|\) denotes Hamming weight. The action on \(\mathcal D\) identifies \(G\cong S_4\times C_2\), where central antipodal inversion \(j(v)=v+(1,1,1)\) generates the second factor, and \(\varepsilon(j)=-1\).

**Theorem.** The only nonzero reduced integral homology of \(K\) is \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^4\). The full rational homology character is
\[
\chi_2(g)=\operatorname{sgn}(\pi_g)\bigl(\#\operatorname{Fix}_{\mathcal D}(g)-1\bigr)+\varepsilon(g).
\]
Consequently its rational representation, under \(G\cong S_4\times C_2\), is
\[
\widetilde H_2(K;\mathbb Q)\cong
\bigl(\operatorname{sgn}_{S_4}\otimes\operatorname{Std}_3\bigr)\boxtimes\mathbf1
\;\oplus\;\mathbf1\boxtimes\varepsilon,
\]
where \(\operatorname{Std}_3\) is the three-dimensional standard rational representation of \(S_4\). Both summands are absolutely irreducible.

The integral representation **does not split** along these two rational constituents: writing \(L=\widetilde H_2(K;\mathbb Z)\) and \(L^{\pm}=\{x\in L:jx=\pm x\}\), one has
\[
\operatorname{rank}L^+=3,\qquad\operatorname{rank}L^-=1,
\qquad [L:L^++L^-]=2.
\]
The subgroup \(\ker\varepsilon\cong S_4\) fixes the primitive rank-one lattice \(L^-\), whereas \(L^G=0\). Thus the antipodal involution has trace \(2\), not \(\pm4\), and there is a genuinely integral, index-two gluing invisible in the rational character.

## Assumptions and scope

All homology is reduced simplicial homology unless stated otherwise. Edges are ordered lexicographically and represented by binary vertex numbers:
\[
(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7).
\]
Every matching is oriented by increasing edge indices. The action on homology is induced by the actual vertex permutation of the cube, including the orientation sign of each simplicial face. No arbitrary choice of coefficient field is hidden in the integral assertion.

For completeness, the rational character is given on the ten classes of \(S_4\times C_2\), in the order of the indicated \(S_4\) cycle types:

| Cycle type of \(\pi_g\) | \(\varepsilon=+1\) | \(\varepsilon=-1\) | Number per sign |
| --- | ---: | ---: | ---: |
| \(1^4\) | 4 | 2 | 1 |
| \(2,1,1\) | 0 | -2 | 6 |
| \(2,2\) | 0 | -2 | 3 |
| \(3,1\) | 1 | -1 | 8 |
| \(4\) | 2 | 0 | 6 |

## Proof

**1. Integral chain model.** Direct enumeration of all matchings yields nonempty face vector \((12,42,44,9)\). Let \(\partial_d\) be the signed simplicial boundary map in dimensions \(d=1,2,3\). The exact integer matrices satisfy \(\partial_1\partial_2=0\), \(\partial_2\partial_3=0\), and have ranks \((11,31,9)\). These are genuine exact ranks, not reductions modulo a prime.

Here is a compact integral certificate. In the \(42\)-by-\(44\) matrix \(\partial_2\), select zero-based rows
\[
R=(0,1,2,3,4,5,7,8,9,10,11,12,14,15,16,17,18,19,21,22,23,24,26,27,28,29,31,32,33,35,36)
\]
and columns \(C=(0,1,\ldots,29,31)\). Their determinant is \(-1\). The remaining thirteen columns are
\[
F=(30,32,33,34,35,36,37,38,39,40,41,42,43).
\]
For each \(f\in F\), there is therefore a unique integral two-cycle \(k_f\) whose coefficient at \(f\) is \(1\), whose other coefficients on \(F\) are \(0\), and whose coefficients on \(C\) are obtained by solving the selected boundary rows. These thirteen cycles freely generate \(\ker\partial_2\) over \(\mathbb Z\): the selected rows determine the pivot coefficients, and all remaining rows vanish because \(\operatorname{rank}\partial_2=31\).

Express the nine columns of \(\partial_3\) in this cycle basis by their coefficients at \(F\), producing a \(13\)-by-\(9\) matrix \(T\). Its row submatrix at zero-based positions \((0,1,4,5,8,9,10,11,12)\) has determinant \(+1\), proving that \(\operatorname{im}\partial_3\) is primitive in \(\ker\partial_2\). The quotient map \(q:\ker\partial_2\to\mathbb Z^4\) is
\[
q(z)=\bigl(z_{33},\;z_{32}+z_{34},\;z_{37},\;z_{30}+z_{38}\bigr),
\]
where \(z_j\) is the coefficient of the \(j\)-th oriented triangle. The equality \(q(\operatorname{im}\partial_3)=0\) and the unimodular submatrix show that \(\ker q=\operatorname{im}\partial_3\). The cycles \(k_{33},k_{34},k_{37},k_{38}\) project to the four standard basis vectors. Hence \(H_2(K;\mathbb Z)\cong\mathbb Z^4\) canonically in these displayed coordinates. Since \(\partial_1\) has rank \(11\) and \(\partial_2\) has a unit rank-maximal minor, reduced \(H_0\) and \(H_1\) vanish integrally; injectivity of \(\partial_3\) gives \(H_3=0\).

**2. Character.** Every cube automorphism is determined by the image of one vertex and a permutation of its three incident edges, proving \(|G|\le8\cdot6\); the displayed affine maps attain the bound. The body-diagonal permutation has kernel \(\{1,j\}\), whence image \(S_4\). The parity character \(\varepsilon\) is a homomorphism, is \(-1\) on \(j\), and separates the central kernel, proving \(G\cong S_4\times C_2\).

For each of the \(48\) affine maps, orient its images of the matching faces by the sorting sign. Let \(a_d(g)\) be the sum of signs on the \(d\)-faces that are preserved setwise. The reduced Lefschetz identity and the concentration of homology in degree two give
\[
\chi_2(g)=-1+a_0(g)-a_1(g)+a_2(g)-a_3(g).
\]
The attached exhaustive exact verifier evaluates this expression on every one of the \(48\) permutations and obtains the five-row table above. Separately, it computes the induced action on the four integral cycle classes using \(q\) and obtains identical traces on all \(48\) group elements. The table is exactly \(\operatorname{sgn}(\pi_g)(\#\operatorname{Fix}(\pi_g)-1)+\varepsilon(g)\). The first summand is the sign twist of the standard \(S_4\)-character; the second is the central sign character. Rational semisimplicity establishes the claimed irreducible decomposition.

**3. Integral obstruction.** In the basis \(([k_{33}],[k_{34}],[k_{37}],[k_{38}])\), central inversion acts by the exact integral matrix
\[
J=\begin{pmatrix}
0&0&1&0\\
1&1&-1&0\\
1&0&0&0\\
0&0&0&1
\end{pmatrix},\qquad J^2=I.
\]
Its \(+1\)-eigenlattice has basis \((0,1,0,0),(1,0,1,0),(0,0,0,1)\), and its \(-1\)-eigenlattice has primitive basis \((1,-1,-1,0)\). The determinant of the matrix formed from these four columns has absolute value \(2\), giving the index-two claim. Every element with \(\varepsilon=+1\) fixes the displayed negative eigenvector, and every element with \(\varepsilon=-1\) negates it, as the verifier checks directly from the integral action. The positive rational subspace is sign-twisted standard and hence has no \(S_4\)-fixed vector. Therefore the full-group fixed homology is zero.

## Verification

Run `python3 verify.py` using Python 3.10 or newer and SymPy 1.10 or newer. The program constructs all matchings, integer boundary matrices, both unit minors, the exact homology quotient, all forty-eight signed simplicial actions, the induced integral four-dimensional matrices, and the complete character formula. It also checks the central eigenlattice bases and their index. Successful execution prints `VERIFY_OK`. The verifier runs without internet or external data and reconstructs every combinatorial input from definitions.

## Relationship to prior work

Classical matching-complex and grid-complex papers give general constructions and homotopy methods. The published exact cube matching-complex result identifies \(K\simeq\bigvee^4S^2\); its full statement and proof give no action of the cube automorphism group. Homotopy type alone does not determine either the character or the integral index-two gluing.

A published equivariant calculation for the *ordinary three-cut complex* of the same cube concerns a different simplicial complex: its four-dimensional homology representation has central inversion trace \(-4\), while the matching-complex action proved here has central trace \(+2\). It neither implies nor subsumes the present claim. Equivalently, replacing the matching complex by the independence complex of the cuboctahedral graph \(L(Q_3)\) leaves the present object unchanged; papers about the **matching complex** of \(L(Q_3)\) instead study a distinct iterated line-graph construction.

## Limitations

This determines the complete rational representation and an integral central-eigenlattice obstruction for the three-cube only. The displayed coordinate construction allows recovery of each integral automorphism matrix but is not asserted to be an abstract classification of all integral \(S_4\times C_2\)-lattices or a formula for higher-dimensional cubes. Originality is relative to the inspected sources; unpublished or unindexed equivalent equivariant calculations cannot be ruled out.

## References

1. A. Björner, L. Lovász, S. T. Vrećica, and R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, Journal of the London Mathematical Society 49 (1994), 25–39; doi:10.1112/jlms/49.1.25.
2. B. Braun and W. K. Hough, *Matching and Independence Complexes Related to Small Grids*, arXiv:1606.01204v1 (3 June 2016).
3. T. Matsushita, *Matching complexes of small grids*, arXiv:1812.11000v1 (28 December 2018).
4. *The cube matching complex is a wedge of four two-spheres*, public mathematical result (11 October 2026), repository record ending `79d70fe8b67e`.
5. *Automorphism-module structure of the cube three-cut complex*, public mathematical result (11 October 2026), repository record ending `7e5f41a11a8d`.
