# Octahedral two-point configuration homology under signed-permutation symmetry

## Finding
Let \(G=K_{2,2,2}\) be the six-vertex octahedral graph. Let \(X=\operatorname{UConf}_2(|G|)\) be the space of **unordered pairs of distinct points of the geometric realization** of \(G\). The full automorphism group is the 48-element signed-permutation group \(B_3=C_2^3\rtimes S_3\). Let \(W=\mathbb Q^3\) be its defining signed-coordinate module, \(\eta(g)\) be the product of the three coordinate signs, \(\delta(g)=\det(W(g))\), and \(P=\mathbb Q[\{\pm1\}^3]\) be the permutation module on the eight triangular faces of the octahedron, equivalently the eight sign vectors. Then, as rational \(B_3\)-representations,
\[
H_0(X;\mathbb Q)\cong\mathbf1,\qquad
H_1(X;\mathbb Q)\cong\delta\otimes P,\qquad
H_2(X;\mathbb Q)\cong W\oplus\eta,\qquad
H_i(X;\mathbb Q)=0\ (i>2).
\]
In particular, the Betti numbers are \((1,8,4)\). The full-automorphism quotient has no positive-degree rational homology, while the orientation-preserving quotient has precisely one degree-one rational class:
\[
\bigl(\dim_{\mathbb Q}H_i(X/B_3;\mathbb Q)\bigr)_{i\ge0}=(1,0,0,\ldots),
\qquad
\bigl(\dim_{\mathbb Q}H_i(X/B_3^+;\mathbb Q)\bigr)_{i\ge0}=(1,1,0,\ldots),
\]
where \(B_3^+=\ker\delta\) is the 24-element rotational subgroup. These assertions concern **ordinary singular rational homology**, not Borel--Moore homology and not homotopy equivalences of the quotient spaces.

## Assumptions and scope
Enumerate the vertices as \(v_{i,u}\) for \(i=0,1,2\) and \(u=0,1\). Vertices are adjacent precisely when their first coordinates differ, giving \(12\) edges. An automorphism \(g=(\sigma,b)\), with \(\sigma\in S_3\) and \(b\in\{0,1\}^3\), sends \(v_{i,u}\mapsto v_{\sigma(i),u\oplus b_i}\). It acts on \(W\) by the signed permutation \(e_i\mapsto(-1)^{b_i}e_{\sigma(i)}\), hence \(\eta(g)=(-1)^{b_0+b_1+b_2}\), \(\delta(g)=\operatorname{sgn}(\sigma)\eta(g)\). On sign vectors, the signs undergo the same signed permutation.

For every group element \(g=(\sigma,b)\), the complete positive-degree character is equivalently
\[
\chi_{H_1}(g)=\delta(g)\,\#\{s\in\{\pm1\}^3:g(s)=s\},\qquad
\chi_{H_2}(g)=\eta(g)+\sum_{i:\sigma(i)=i}(-1)^{b_i}.
\]
The first fixed-point factor is \(2^{c(\sigma)}\) if the parity of \(b\) around each cycle of \(\sigma\) is even, and zero otherwise.

For two particles the octahedral graph satisfies the sufficient-subdivision conditions of the finite Abrams model, sharpened by Prue--Scrimshaw: distinct essential vertices are separated by at least one edge, and every nontrivial embedded cycle has at least three edges. Thus the unordered two-particle cubical complex is homotopy equivalent to \(X\). The action of each graph automorphism on this model is cellular and agrees with its action on configuration-space homology.

## Proof
**Cubical model and integral boundaries.** Use one \(0\)-cell for each unordered pair of different graph vertices, one \(1\)-cell for each oriented graph edge and a nonincident stationary vertex, and one \(2\)-cell for each unordered pair of disjoint edges. The cellular counts are exactly \((c_0,c_1,c_2)=(15,48,30)\). Orient a graph edge from its smaller vertex index to its larger index; orient a \(2\)-cube by its two edge coordinates in increasing graph-edge index. With these conventions, the explicit boundary of \(e\times f\) is \((\partial e)\times f-e\times(\partial f)\), with the signs implemented in `CHECKER.py`. The one-skeleton of the complex is connected (the checker verifies a complete graph traversal), hence \(\operatorname{rank}\partial_1=14\).

The independent integer certificate `CERTIFICATE.json` lists \(26\) row indices and \(26\) column indices for an integral minor of \(\partial_2\) with exact determinant \(-1\), so \(\operatorname{rank}_{\mathbb Q}\partial_2\ge26\). It also provides four explicit integral \(30\)-coordinate vectors in \(\ker\partial_2\). Their coordinates on columns \(26,27,28,29\) form the \(4\)-by-\(4\) identity, so they are independent, implying \(\operatorname{rank}_{\mathbb Q}\partial_2\le26\). The four vectors are therefore a \(\mathbb Q\)-basis for \(H_2=\ker\partial_2\), because the complex has no \(3\)-cells. Consequently \(\dim H_2=4\) and \(\dim H_1=48-14-26=8\).

**Exact group action.** All \(3!\,2^3=48\) maps above preserve the graph. For each of the 48 automorphisms, the checker explicitly constructs its signed permutation actions on all oriented \(0\)-, \(1\)- and \(2\)-cells. It acts on each of the four certified kernel vectors, reads its four coefficients using the distinguished coordinates, and checks agreement with the full transformed \(30\)-coordinate cycle; thus the \(H_2\) action and trace are exact. The \(H_1\)-trace is then forced by the equivariant cellular Euler identity
\[
1-\chi_{H_1}(g)+\chi_{H_2}(g)=\operatorname{tr}(g\mid C_0)-\operatorname{tr}(g\mid C_1)+\operatorname{tr}(g\mid C_2).
\]
The exhaustive integer calculations give the two character formulas in the scope statement for **every** group element, not merely a sample or approximate numerical comparison.

**Module identification.** The character of \(\delta\otimes P\) is \(\delta(g)\) times the number of fixed sign vectors, and the character of \(W\oplus\eta\) is \(\sum_{\sigma(i)=i}(-1)^{b_i}+\eta(g)\). The computed characters coincide with these characters on every element of the finite group. By semisimplicity of rational representations of finite groups and rational character uniqueness, the displayed module isomorphisms follow.

**Quotients.** Rational homology of a finite-group quotient equals the invariants of rational homology of its domain. The group-average of \(\chi_{H_1},\chi_{H_2}\) over \(B_3\) is \((0,0)\). Over \(B_3^+\) it is \((1,0)\). Since both groups act on connected \(X\), the displayed rational quotient Betti numbers follow.

## Verification
The portable, standard-library-only script `CHECKER.py`, together with `CERTIFICATE.json`, reconstructs all cells and integer boundaries, verifies the \(26\)-by-\(26\) minor using fraction-free Bareiss elimination, and verifies the four integral kernel cycles and their normalized coordinates. It enumerates all 48 graph automorphisms, computes the oriented cellular traces and their exact action on the four \(2\)-cycles, and verifies the 10 signed-cycle-type character rows and invariant averages. Run `python3 CHECKER.py CERTIFICATE.json`; the expected success line is `OCTAHEDRAL_TWO_POINT_EQUIVARIANT_CERTIFICATE_OK`. No mathematical assertion in this result depends on reusing a calculation outside these two packaged files.

## Relationship to prior work
An and Knudsen establish structural generators for degree-two homology of configuration spaces of planar graphs in arXiv:2008.10371, first posted 2020-08-24, primary MSC 55R80. Their theorem does not identify the present octahedral automorphism representations or the rational homology of symmetry quotients. Prue and Scrimshaw justify the small subdivision threshold for the cubical model. Related explicit symmetry computations for two-point configurations on the cuboctahedral and dodecahedral graphs concern **different spaces and groups**. A further two-point graph result concerns the **exchange-sign Borel--Moore local system**, which is not the ordinary homology considered here. A result on the octahedral **matching complex** concerns a different complex and does not cover two-point graph configurations. These distinctions were checked by comparing the mathematical statements, not by matching titles or numerical parameters.

## Limitations
This calculation is restricted to two **unordered** collision-free particles, the geometric octahedral graph, and **rational** homology representations. The exact integral minor establishes rational ranks and an integral top-kernel basis, but no claim about possible torsion in \(H_1(X;\mathbb Z)\) or an integral representation decomposition is made. It does not classify more particles or other polyhedral graphs. The quotient statements concern rational homology, not simple connectivity or homotopy equivalence to a point or a circle. Indexed-source and accessible historical-record comparisons do not rule out unindexed or unpublished equivalent calculations. Independent external verification has not been performed.

## References
1. Byung Hee An and Ben Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371 (first public 2020-08-24), Journal of Topology 15 (2022), 666--691. https://arxiv.org/abs/2008.10371 ; https://doi.org/10.1112/topo.12228.
2. Paul Prue and Travis Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511 (2009), Theorem 3.2. https://arxiv.org/abs/0909.5511.
3. Byung Hee An and Tomasz Maciazek, *Geometric Presentations of Braid Groups for Particles on a Graph*, Communications in Mathematical Physics 384 (2021), 1109--1140. https://doi.org/10.1007/s00220-021-04095-x.
