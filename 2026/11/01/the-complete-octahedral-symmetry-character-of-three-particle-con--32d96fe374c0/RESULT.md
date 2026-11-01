# The complete octahedral symmetry character of three-particle configuration homology

## Finding

Let \(O=K_{2,2,2}\) and \(X=\operatorname{UConf}_3(|O|)\). The full graph automorphism group is \(W\cong S_4\times C_2\), where the central involution reverses each of the three opposite vertex pairs. Write \(S^\lambda\) for the rational irreducible representation of \(S_4\) indexed by a partition of four, and write a superscript \(+\) or \(-\) for the eigenvalue of the central involution.

The complete positive-degree rational homology representations are

\[
H_1(X;\mathbb Q)\cong \mathbf1^-\oplus(S^{(1,1,1,1)})^+\oplus(S^{(3,1)})^-\oplus(S^{(2,1,1)})^+,
\]

\[
\begin{aligned}
H_2(X;\mathbb Q)\cong{}&(S^{(1,1,1,1)})^+\oplus2(S^{(1,1,1,1)})^-\\
&\oplus3(S^{(3,1)})^+\oplus2(S^{(3,1)})^-\\
&\oplus3(S^{(2,1,1)})^+\oplus4(S^{(2,1,1)})^-\\
&\oplus2(S^{(2,2)})^+\oplus2(S^{(2,2)})^-.
\end{aligned}
\]

The dimensions are respectively \(8\) and \(47\), while \(H_0(X;\mathbb Q)=\mathbb Q\) and \(H_i(X;\mathbb Q)=0\) for \(i\geq3\). Neither positive-degree representation contains a trivial \(W\)-summand; finite-group rational transfer therefore gives \(\widetilde H_i(X/W;\mathbb Q)=0\) for all \(i\). The central antipodal involution splits second homology into eigenspaces of dimensions \(23\) and \(24\).

## Assumptions and scope

The unoriented geometric realization of the simple octahedral graph has three opposite vertex pairs and one edge between every two vertices from distinct pairs. Configuration particles are pairwise distinct points, unordered; \(\operatorname{UConf}_3\) is topological (not a graph matching complex or discretized graph metric Rips complex). The action is induced by graph automorphisms.

Identify the six vertices as \(0,1,2,3,4,5\), with opposite pairs \(\{0,1\},\{2,3\},\{4,5\}\). There are twelve unordered edges, one between vertices with different integer quotients upon division by two. All homology statements concern ordinary singular homology of the continuous unordered three-point configuration space, with rational coefficients. No assertion of integral torsion-freeness is made.

For an automorphism of \((C_2)^3\rtimes S_3\), a *signed coordinate cycle* of length \(j\) receives a sign from the parity of coordinate flips along that cycle. The ten rational character rows are:

| Signed coordinate cycles | Number | \(\chi_{H_1}\) | \(\chi_{H_2}\) |
|---|---:|---:|---:|
| \((-1),(-1),(-1)\) | 1 | 0 | -1 |
| \((-1),(-1),(+1)\) | 3 | 0 | -1 |
| \((-1),(+1),(+1)\) | 3 | 0 | -1 |
| \((-1),(-2)\) | 6 | 0 | -1 |
| \((-1),(+2)\) | 6 | 0 | -5 |
| \((+1),(+1),(+1)\) | 1 | 8 | 47 |
| \((+1),(-2)\) | 6 | 0 | -1 |
| \((+1),(+2)\) | 6 | -4 | 3 |
| \((-3)\) | 8 | 0 | -1 |
| \((+3)\) | 8 | 2 | -1 |

## Proof

**Chain model and rational Betti dimensions.** Use the standard weight-three reduced Świątkowski chain model for graph configuration homology (the homology of this model agrees with that of \(X\)). For each vertex fix its least-indexed incident edge \(e_0\), introduce degree-one local differences \(h_{v,e}-h_{v,e_0}\) for the other three incident edges, and work over the polynomial ring on twelve edges. Give polynomial edges weight one, and assign weight one to each local generator. Differentials send the local difference to \(e-e_0\), and the differential is extended with alternating Koszul signs. This fixes the normalization, incidence ordering, and all coefficients.

The chain dimensions in degrees \(0,1,2,3\) are \((364,1404,1620,540)\). Exact composition checks give \(\partial^2=0\). Deterministic sparse elimination modulo \(32003\) gives the differential ranks \((363,1033,540)\). Modular ranks give lower bounds on rational ranks, not automatic equalities. The graph is connected, so the rational rank of the first differential is at most \(364-1=363\); the last differential has at most \(540\) columns. The graph is simple, planar, and three-connected, with cycle rank \(12-6+1=7\). Ko and Park's planar three-connected first-homology theorem gives \(\dim_\mathbb Q H_1(X;\mathbb Q)=7+1=8\). Hence the middle differential has rational rank exactly \(1404-363-8=1033\). Therefore the modular bounds on all three differential ranks are exact over \(\mathbb Q\). The resulting rational Betti vector is \((1,8,47,0)\).

**First-homology character, verified directly.** The action on the reduced basis is the signed action on local halfedge differences: an image of a difference is reexpressed relative to the distinguished incident halfedge at its target vertex. Elimination of \(\operatorname{im}\partial_2\) inside \(\ker\partial_1\) over \(\mathbb F_{32003}\) produces an eight-dimensional quotient. The standalone implementation explicitly acts on eight basis cycles and checks the resulting trace for all \(48\) automorphisms. These traces agree with \(\chi_{H_1}(g)=\operatorname{tr}(g\mid C_1(O;\mathbb Q))-\operatorname{tr}(g\mid C_0(O;\mathbb Q))+1+\det_{\mathbb R^3}(g)\), and have values bounded in absolute value by eight. Because the characteristic is coprime to the group order and exceeds twice that bound, the modular computations uniquely determine the integer-valued rational traces. The displayed first-homology decomposition follows by character inner products.

**Second-homology character and irreducibles.** For an automorphism \(g\), let \(\mathcal V(g)\) and \(\mathcal E(g)\) be its orbits on vertices and edges, respectively. Let \(F_C\) count incident halfedges at a selected vertex of vertex orbit \(C\) fixed by the corresponding power \(g^{|C|}\). The alternating full-chain trace at weight three, obtained by multiplying local exterior-degree supertraces and symmetric edge polynomial traces, is

\[
E_g=[t^3]\prod_{C\in\mathcal V(g)}(1+(1-F_C)t^{|C|})
\prod_{D\in\mathcal E(g)}(1-t^{|D|})^{-1}.
\]

There are no rational homology degrees above two, so the equivariant Euler identity implies \(\chi_{H_2}(g)=E_g-1+\chi_{H_1}(g)\). Direct enumeration of all \(9704\) weight-three full-chain basis states for each of the \(48\) automorphisms independently reproduces every Euler trace. The ten conjugacy-class characters in the table are recovered, and their exact inner products with the ten irreducibles of \(S_4\times C_2\) give the claimed nonnegative integral multiplicities. This determines the complete rational graded representation, not only dimensions or invariants.

**Quotient.** Exact inner products with the constant character are zero for both positive degrees. Since \(W\) is finite and the action cellular on an equivariant model, rational homology of the orbit space identifies with the invariant homology. This proves the rational acyclicity of the full-symmetry quotient.

## Verification

Run the standalone programs with Python and NumPy installed in the same directory: `python oct.py`, `python characters.py`, `python verify_equiv.py`, and `python independent_trace.py`. The companion `octchars.json` contains all ten class values and decompositions. The four corresponding `.out` files record exact successful execution. The first program reconstructs boundary matrices and checks their compositions and modular ranks; the second derives all class Euler traces and decompositions; the third independently computes all first-homology actions on actual quotient cycles; the fourth directly enumerates the \(9704\) full-chain basis states to check the Euler traces. The two character routes independently agree for all \(48\) automorphisms. These finite, exhaustive computations are exact for the finite chain model. The topological identification of that chain model with configuration homology and the first-homology theorem are cited theoretical inputs, not consequences of finite enumeration.

## Relationship to prior work

Ko and Park's 2011 first-homology theorem establishes the first Betti number, but not the second-degree full automorphism representation. The reduced Świątkowski model underlies existing computations; Maciążek and Sawicki study graph configuration homology and special graph families but do not state the octahedral three-particle character in their inspected full article. An and Knudsen's theorem that second homology of any planar graph configuration space is generated by toric and theta classes is significantly broader at the generator level, but does not determine this particular equivariant quotient, character table, or decomposition; the present statement does not claim general torus/theta generation as new. Public mathematical records for the ordinary octahedral matching complex, for the two-particle cuboctahedral space, and for three-particle Heawood/Pappus spaces concern mathematically different complexes or graph/particle inputs; none of their recovered claims implies the present \(48\)-element character. These comparisons do not prove absence of equivalent unindexed or unpublished calculations.

## Limitations

The computation concerns rational homology and full linear automorphism actions only. It neither determines integral torsion nor a homotopy-equivalent wedge model nor a presentation of the graph braid group. The modular rank certificates become proofs of rational rank only in conjunction with the cited first-homology theorem and connectedness. Mathematical correctness and publication priority have not been independently audited, and unindexed or inaccessible literature could contain equivalent symmetry calculations.

## References

1. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, original public preprint dated 2011-01-13, https://arxiv.org/abs/1101.2648 (Lemma 3.15 and Theorem 3.16).
2. J. Świątkowski, *Estimates for homological dimension of configuration spaces of graphs*, Colloquium Mathematicum 89 (2001), https://doi.org/10.4064/cm89-1-11 (historical chain method; complete text not inspected).
3. T. Maciążek and A. Sawicki, *Non-abelian quantum statistics on graphs*, Communications in Mathematical Physics (2019), https://doi.org/10.1007/s00220-019-03583-5 (full article sections on graph-configuration homology and the reduced chain complex inspected).
4. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, original public preprint dated 2020-08-24, https://arxiv.org/abs/2008.10371 (main theorem and accompanying sections inspected).
