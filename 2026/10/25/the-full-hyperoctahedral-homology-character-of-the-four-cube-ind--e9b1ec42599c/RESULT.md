# The full hyperoctahedral homology character of the four-cube independence complex

## Finding

Write \(Q_4\) for the graph on \(\mathbb F_2^4\) with an edge between binary words differing in one coordinate, and let \(K=\operatorname{Ind}(Q_4)\) be its ordinary independence complex. The full graph automorphism group is \(B_4=\mathbb F_2^4\rtimes S_4\), of order \(384\). Give its elements the convention \(g_{\pi,b}(v)=\pi(v)+b\), with \(b\in\mathbb F_2^4\) and \(\pi\in S_4\).

**Theorem.** The only nonzero reduced rational homology is \(\widetilde H_3(K;\mathbb Q)\cong\mathbb Q^7\). Its complete \(B_4\)-character is

\[
\chi(g_{\pi,b})=\operatorname{sgn}(\pi)\left(|\operatorname{Fix}(\pi)|-1+\sum_{i\in\operatorname{Fix}(\pi)}(-1)^{\sum_{j\ne i}b_j}\right).
\]

Here \(\operatorname{Fix}(\pi)\) means the set of coordinates fixed individually by \(\pi\), and the exponent uses any integer representatives of the bits. More explicitly, as rational \(B_4\)-modules,

\[
\widetilde H_3(K;\mathbb Q)\cong \operatorname{sgn}_{S_4}\otimes\left(\operatorname{Std}_{S_4}\oplus V\right).
\]

The three-dimensional standard module \(\operatorname{Std}_{S_4}\) is inflated from \(S_4\), so translations act trivially. The four-dimensional module \(V\) has basis \(e_1,\ldots,e_4\); translations act on \(e_i\) by \((-1)^{\sum_{j\ne i}b_j}\), while coordinate permutations permute the basis. Thus the translation spectrum consists of three copies of the trivial character and four **distinct weight-three binary characters**, each with multiplicity one.

Consequently the full-group invariant homology vanishes, whereas the translation-invariant top homology has dimension three. The rational orbit-space homology therefore satisfies

\[
\widetilde H_*(K/B_4;\mathbb Q)=0,\qquad
\widetilde H_3(K/\mathbb F_2^4;\mathbb Q)\cong\mathbb Q^3,
\]

and all other reduced rational homology of the translation quotient vanishes.

## Assumptions and scope

All simplices are finite unordered sets of distinct vertices; a simplex of \(K\) is a subset having no adjacent pair in \(Q_4\). Vertex labels \(0,\ldots,15\) encode the four binary coordinates. For a permutation \(\pi\), the bit originally in coordinate \(i\) moves to coordinate \(\pi(i)\). The action on simplicial chains uses ascending vertex order and the induced orientation sign. The theorem concerns rational homology and quotient spaces of this particular sixteen-vertex graph. It asserts neither an integral equivariant splitting nor a formula for larger cubes.

## Proof

**Rational homology degree.** Every subset of the sixteen vertices has one membership mask. Retain exactly those masks containing no adjacent graph pair. There are \(742\) nonempty simplices, with counts by dimensions zero through seven

\[
(16,88,208,228,128,56,16,2).
\]

The signed boundary maps, reduced modulo two, have ranks in dimensions one through seven

\[
(15,73,135,86,42,14,2),
\]

computed by exhaustive Gaussian elimination on their precisely defined columns. Thus the mod-two Betti vector is \((1,0,0,7,0,0,0,0)\). Every rational Betti number is at most the corresponding mod-two Betti number, by the universal coefficient theorem. The face vector gives reduced Euler characteristic \(-7\). Consequently the rational reduced homology is seven-dimensional in degree three and zero elsewhere. The computation does not infer integral torsion-freeness from mod-two ranks.

**A finite complete character certificate.** For any automorphism \(g\), the trace of \(g\) on degree-\(d\) simplicial chains is the sum, over all \(g\)-stable \(d\)-simplices, of the sign of the vertex permutation induced by \(g\) on that simplex. Set \(T(g)\) equal to the alternating sum of these chain traces over nonempty simplices. By the Hopf trace formula and the rational-homology calculation,

\[
T(g)=\operatorname{tr}(g|H_0(K;\mathbb Q))-\operatorname{tr}(g|H_3(K;\mathbb Q))=1-\chi(g).
\]

The bundled standard-library program `verify.py` reconstructs every independent set, every group element \((\pi,b)\), and every fixed simplex with its integer orientation sign. It compares \(1-T(g)\) against the displayed character formula for **all \(24\cdot16=384\) automorphisms**, not a sample. Exact integer assertions succeed in all cases; the full algorithm and output are provided. Hence the character formula holds on the entire finite group.

**Representation identification.** On \(\operatorname{Std}_{S_4}\), the trace of \(\pi\) is \(|\operatorname{Fix}(\pi)|-1\); on \(V\), the trace of \((\pi,b)\) is \(\sum_{i\in\operatorname{Fix}(\pi)}(-1)^{\sum_{j\ne i}b_j}\). Tensoring both by \(\operatorname{sgn}_{S_4}\) yields exactly the certified homology character. Semisimplicity of rational representations of finite groups and character uniqueness establish the rational module isomorphism. Restricting to \(\mathbb F_2^4\), Fourier inversion yields multiplicity three for the trivial character, one for each weight-three character, and zero for all other binary characters. Averaging the full character over all \(384\) elements gives zero, so the full-group invariant dimension is zero. After barycentric subdivision the finite action is simplicial without inversions; rational transfer identifies quotient rational homology with invariant homology, proving the final assertions.

## Verification

Run `python3 verify.py` with Python 3.10 or newer; no external packages or external datasets are required. The script checks the eight simplex counts, all seven mod-two boundary ranks, the reduced Euler value, all \(384\) signed Lefschetz equalities, all sixteen translation characters, Fourier inversion, and the full-character average. The exact output is included as `verification_output.txt`; its terminal marker is `VERIFY_OK_Q4_INDEPENDENCE_FULL_HYPEROCTAHEDRAL_CHARACTER`. The signed simplex enumerator is exhaustive because all \(2^{16}-1\) nonempty vertex subsets are explicitly tested, and every \((\pi,b)\) is iterated.

## Relationship to prior work

The original grid-independence analysis of Bousquet-Mélou, Linusson, and Nevo [1] computes homotopy types for open and cylindrical lattices and discusses toroidal alternating counts, not the full four-cube automorphism action. Huijse and Schoutens [2] connect independent-set homology with supersymmetric lattice fermions, including special periodic grids, but their stated tiling theorem has period-index divisible by three, unlike this \(4\)-by-\(4\) torus of period-index sixteen. Adamaszek [3] develops nontrivial independence-complex cycles for lattices rather than the present full equivariant character.

A separately published, exactly matching **nonequivariant** calculation establishes \(\operatorname{Ind}(Q_4)\simeq\bigvee^7S^3\) [4]. Its full result text was compared directly; it explicitly does not determine a canonical equivariant decomposition. Therefore the seven-dimensional Betti number and homotopy type are acknowledged as known, and the only proposed contribution is the complete signed-permutation homology representation and the two rational quotient consequences. Calculations of other hypercube complexes, notably metric Vietoris–Rips or Čech complexes, concern different simplices and do not imply the independence-complex character. Nonidentity trace data are necessary: the nonequivariant wedge type by itself does not determine a group representation.

## Limitations

The conclusion is an exact, finite, rational equivariant calculation for one canonical graph, not a family-wide classification. Its computation is exhaustive but depends on faithfully executing and reviewing the included small integer algorithm; no independent review is claimed. Rational characters do not determine the integral module up to isomorphism, and rational transfer does not establish integral orbit-space homology. Coverage by unindexed equivalent work, including older symmetry-resolved hard-core lattice calculations, cannot be excluded.

## References

[1] M. Bousquet-Mélou, S. Linusson, E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, first public posting 2007-01-30. https://arxiv.org/abs/math/0701890

[2] L. Huijse, K. Schoutens, *Supersymmetry, lattice fermions, independence complexes and cohomology theory*, arXiv:0903.0784, first public posting 2009-03-04. https://arxiv.org/abs/0903.0784

[3] M. Adamaszek, *Special cycles in independence complexes and superfrustration in some lattices*, arXiv:1109.4914, first public posting 2011-09-22. https://arxiv.org/abs/1109.4914

[4] *The four-cube independence complex is a wedge of seven three-spheres*, publicly indexed note (2026), full primary text: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-four-cube-independence-complex-is-a-wedge-of-seven-three-sph--9947aaad144c/RESULT.md
