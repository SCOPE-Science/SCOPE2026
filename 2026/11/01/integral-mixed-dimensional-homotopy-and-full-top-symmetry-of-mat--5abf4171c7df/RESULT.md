# Integral mixed-dimensional homotopy and full top symmetry of \(\mathcal N(T_7)\)

## Finding
Let \(T_7=L(K_7)\) be the triangular graph on the 21 edges of the labeled complete graph \(K_7\). Its ordinary open-neighborhood complex \(X=\mathcal N(T_7)\) has integral homotopy type
\[
X\simeq\bigvee^{246}S^3\vee\bigvee^{7}S^4.
\]
In particular, its only nonzero reduced integral homology groups are \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{246}\) and \(\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^7\), without torsion.

The natural permutation group \(S_7\) acts on the integral fourth-homology lattice by
\[
\widetilde H_4(X;\mathbb Z)\cong \operatorname{sgn}_{S_7}\otimes\mathbb Z^7_{\mathrm{perm}},
\qquad \operatorname{tr}(g\mid\widetilde H_4(X;\mathbb Q))=
\operatorname{sgn}(g)\,|\operatorname{Fix}_{[7]}(g)|.
\]
The representation is an **integral lattice identification**, not merely an agreement of rational characters. It implies that the fourth reduced rational homology of the full-symmetry quotient vanishes, whereas the corresponding alternating-group quotient has fourth reduced rational Betti number one. No claim is made about degree-three quotient invariants.

## Assumptions and scope
An edge of \(K_7\) is a two-element subset \(\{a,b\}\subset[7]\). Two vertices of \(T_7\) are adjacent precisely when their corresponding distinct two-subsets intersect. A simplex in the **open** neighborhood complex is a nonempty collection of such two-subsets all adjacent to some single, distinct two-subset. In particular the common neighbor itself is never included by self-adjacency.

The statement concerns this exact finite abstract simplicial complex and its canonical label-permutation action, with integral homology and ordinary homotopy equivalence. It is not about the clique complex, closed-neighborhood complex, or the independence/matching complex of \(T_7\).

## Proof
Enumerate the 21 graph vertices by lexicographically ordered pairs \((a,b)\) with \(0\le a<b\le6\). Encode a simplex as a nonzero 21-bit mask. For each edge \(e\) of \(K_7\), its open \(T_7\)-neighborhood consists of the ten other edges sharing one endpoint with \(e\). Taking every nonempty submask of those 21 ten-element neighborhoods yields **exactly** 18,494 distinct nonempty faces. The face numbers by dimension zero through nine are
\[
(21,210,1190,3780,5187,4410,2520,945,210,21).
\]
This construction is exhaustive because the existence of a common neighbor is exactly the definition of a face.

The supplied executable constructs an acyclic discrete-Morse matching using sequential element toggles, in the fixed order of the 21 vertices. An unmatched face \(F\) not containing the next vertex \(e\) is paired with \(F\cup\{e\}\) if both are currently unmatched; paired faces are removed before the next toggle. The algorithm produces **9,120 matched face pairs**, leaving one critical zero-dimensional face, 246 critical three-dimensional faces, and seven critical four-dimensional faces. It independently verifies acyclicity by orienting every cover relation of the nonempty face poset downward, except matched relations which are reversed. A complete topological sort visits all 18,494 faces across the **98,805** cover incidences, so no closed gradient path exists.

The nontrivial integral Morse differential can only map degree-four critical cells to degree-three critical cells. For each of the seven critical four-cells, the verifier computes its oriented simplicial boundary and recursively eliminates matched degree-three faces by the signed, unit-pivot relations of their paired degree-four cofaces. The resulting **entire 246-by-7 integral Morse boundary matrix is zero**, not only zero after reduction modulo a prime. The verifier also produces seven genuine oriented simplicial four-cycles, with supports of sizes \(6,36,36,36,36,36,36\), checking every integral third-face coefficient cancels. The matching therefore yields a CW complex with a single zero-cell, 246 three-cells, seven four-cells, no other cells, and zero cellular differential.

The three-skeleton of this Morse CW complex is a wedge of 246 three-spheres. Each four-cell attaches by a map from a three-sphere, whose homotopy class lies in
\[
\pi_3\!\left(\bigvee^{246}S^3\right)\cong\mathbb Z^{246}.
\]
This group is exactly detected by the degree vector in cellular homology. Since every computed degree is zero, every attaching map is nullhomotopic. Attaching the seven four-cells therefore gives the asserted **integral homotopy wedge**, rather than only a homology calculation.

For symmetry, the code projects any oriented simplicial four-chain to its seven critical four-cell coordinates by the same signed unit-pivot elimination. The seven lifted integral four-cycles map to the standard unimodular coordinate basis. Starting from the shortest lifted cycle \(z_0\), define \(w_0=[z_0]\) and \(w_i=-[(0\ i)z_0]\) for \(1\le i\le6\). Their coordinate vectors are seven distinct signed standard basis vectors, hence form an **integral unimodular basis**. On this basis the code verifies each of the six adjacent transpositions \(s_i=(i\ i+1)\) acts by \(s_iw_j=-w_{s_i(j)}\) for every \(0\le j\le6\). Adjacent transpositions generate \(S_7\); the integral module consequently is the stated sign-twisted permutation lattice. For an independent character check, the program evaluates the full 15 conjugacy-class character values and verifies \(\operatorname{tr}(g)=\operatorname{sgn}(g)|\operatorname{Fix}(g)|\).

For a finite group action on a finite complex, rational homology of the topological quotient agrees with the invariant part of rational homology. A transposition acts by negative permutation on the indicated seven-dimensional lattice, giving no full \(S_7\)-invariants, while restricting to \(A_7\) gives the ordinary permutation module, with a one-dimensional invariant line.

## Verification
Execute `python3 verify.py` using Python's standard library. It recomputes the complex, the entire acyclic matching and oriented Hasse graph, the full integer Morse boundary, explicit integral cycles, all six adjacent-generator actions, and all 15 conjugacy-class traces. The exact expected stdout is embedded in `verification_output.txt`. No sampling, floating point, modular-only inference, or external computational packages are used. The result is also reproducible from the definitions and algorithms described above.

## Relationship to prior work
A published calculation titled *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)* establishes the degree-three and degree-four \(\mathbf F_2\)-Betti numbers 246 and 7, explicitly **without** asserting integral homology, homotopy type, attaching maps, or a symmetry representation. The new acyclic Morse certificate, exact integral vanishing differential, and integral \(S_7\)-module supply the additional conclusions; matching mod-two dimensions alone cannot imply them.

Kozlov's 2005 simple-homotopy equivalences between neighborhood and graph-Hom complexes apply generally, but they do not compute this instance. Matsushita's fundamental-group results concern other homotopy data, not these high-dimensional invariants. The Shukla work on graphs of degree at most three and 4-regular circulants excludes the 10-regular \(T_7\). The Fröberg neighborhood-complex computations cover different graph families. In particular, results about the clique or matching complex of a line graph are not statements about its open-neighborhood complex. An earlier calculation of the full natural \(S_6\)-character for \(\mathcal N(T_6)\) concerns a different graph and cannot imply the integral \(S_7\)-lattice here.

## Limitations
This is one finite, natural seven-label case, not a formula for all triangular graphs. It does not determine the integral \(S_7\)-module structure in degree three, the actual action on the entire homotopy type, the higher integral homotopy groups, or integral homology of symmetry quotients. The group-quotient conclusions concern only degree-four rational homology. Published unindexed equivalent results may exist; independently verified publication priority is not asserted.

## References
1. D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613, initial public posting 2005-03-28, https://arxiv.org/abs/math/0503613.
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1, initial public posting 2012-10-10, https://arxiv.org/abs/1210.2803.
3. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v1, https://arxiv.org/abs/1802.04526.
4. R. Fröberg, *Stanley–Reisner rings of neighborhood complexes and linear resolutions*, Journal of Algebraic Combinatorics 63 (2026), article 56, DOI 10.1007/s10801-026-01530-x.
5. *Mixed-dimensional mod-two neighborhood homology first appears at \(T_7\)*, previously published mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-mod-two-neighborhood-homology-first-appears-at--5026f3f1e8ec.
