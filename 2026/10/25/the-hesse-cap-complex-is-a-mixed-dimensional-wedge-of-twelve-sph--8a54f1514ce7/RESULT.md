# The Hesse cap complex is a mixed-dimensional wedge of twelve spheres

## Finding

Let \(P=\mathbb F_3^2\), the nine points of the affine plane of order three. For each pair of distinct points \(a,b\in P\), its line consists of \(a,b,-a-b\). Let \(\mathcal A(P)\) be the simplicial complex of subsets of \(P\) containing no complete affine line. It is the cap-set (or line-hypergraph independence) complex of the Hesse \((9_4,12_3)\) configuration. Its **integral homotopy type** is
\[
\mathcal A(P)\simeq S^2\vee\bigvee^{11}S^3.
\]
Consequently, \(\widetilde H_2(\mathcal A(P);\mathbb Z)\cong\mathbb Z\), \(\widetilde H_3(\mathcal A(P);\mathbb Z)\cong\mathbb Z^{11}\), and every other reduced integral homology group vanishes. In particular, no torsion occurs.

## Assumptions and scope

Number the nine points \(0,1,\dots,8\) in row-major order: vertex \(i\) represents \((\lfloor i/3\rfloor,i\bmod3)\). An affine line is any unordered triple \(\{a,b,c\}\) of distinct points with \(a+b+c=0\) coordinatewise in \(\mathbb F_3^2\). A cap is a subset with no such triple. The theorem concerns the entire finite abstract simplicial complex of caps, not merely maximal caps and not cap complexes in higher-dimensional affine spaces or in the thirteen-point projective plane. The empty set is understood as a simplicial face, but only nonempty faces participate in the discrete-Morse matching.

## Proof

**1. Exact face model.** Every pair of distinct points determines the unique third point \(-a-b\) on its affine line. There are exactly twelve lines; each point belongs to four and each pair belongs to exactly one. For a nonempty subset \(F\subseteq P\), encode it by the integer bitmask \(m(F)=\sum_{i\in F}2^i\). Enumerate every mask from \(1\) through \(511\), retaining it precisely if it contains none of the twelve line masks. Exhaustive integer enumeration gives face vector
\[
(f_0,f_1,f_2,f_3)=(9,36,72,54)
\]
and no faces in dimensions above three. There are thus \(171\) nonempty faces.

**2. A complete acyclic matching.** Process vertices in the fixed order
\[
(5,7,1,3,4,2,8,6,0).
\]
At a step with vertex \(v\), scan remaining faces by (cardinality, numerical mask) and pair every still-available face \(F\) not containing \(v\) with \(F\cup\{v\}\), provided both are still available. Remove both faces and continue. This deterministic prescription gives \(79\) disjoint face-cover pairs. Precisely thirteen faces remain critical: the singleton mask \(32\), the triangle mask \(145\), and the eleven tetrahedron masks
\[
29,78,83,197,269,278,323,325,332,344,393.
\]
To check Forman acyclicity, orient every codimension-one face relation downward unless it is one of the matched pairs, in which case orient it upward. The directed Hasse graph has \(171\) vertices and \(504\) incidences; an exhaustive topological sort visits all \(171\) vertices, proving that it has no directed cycle. Forman's discrete Morse theorem therefore gives a CW complex homotopy equivalent to \(\mathcal A(P)\), with one cell in degree zero, none in degree one, one cell in degree two, and eleven cells in degree three.

**3. Integral attaching coefficients.** Orient simplices by increasing vertex index. A face obtained by deleting the vertex in position \(j\) has boundary coefficient \((-1)^j\). Let \(t\) denote the sole critical triangle (mask \(145\)). For any triangle \(f\), define its integral coefficient \(Q(f)\) in the reduced critical triangle as follows. Set \(Q(t)=1\). If \(f\) is paired downward with an edge, set \(Q(f)=0\). If \(f\) is paired upward with a tetrahedron \(g\), let \(\epsilon=[f](\partial g)=\pm1\), and set
\[
Q(f)=-\epsilon^{-1}\sum_{h\ne f}[h](\partial g)Q(h).
\]
The acyclicity verified above makes this recursion finite and unambiguous. Evaluating it with exact integers gives, in the critical tetrahedron order specified above,
\[
\left(\sum_{f\subset g}[f](\partial g)Q(f)\right)_{g}
=(0,0,0,0,0,0,0,0,0,0,0).
\]
For an independent algebraic check, cancel all \(79\) Morse pairs directly in the integral cellular chain complex, always using an available \(\pm1\) boundary pivot, modifying the surviving boundary columns by integral elementary operations. All pairs can be canceled and all surviving differential columns are zero. The supplied dependency-free program carries out both independent reductions.

**4. From the Morse complex to homotopy.** The reduced CW model has one zero-cell, no one-cells, and a single two-cell, so its two-skeleton is \(S^2\). Each of its eleven three-cells is attached by a map \(S^2\to S^2\). Since \(\pi_2(S^2)\cong\mathbb Z\), such a map is determined by its degree, precisely its integral cellular boundary coefficient. All eleven degrees vanish in Step 3, so the attachments are nullhomotopic. The CW complex is therefore \(S^2\vee\bigvee^{11}S^3\), proving the claimed integral homotopy type.

## Verification

Run `python3 verify_hesse_cap.py` in a Python 3 environment with no third-party packages. The program re-enumerates the lines and all \(511\) possible nonempty subsets, checks the face vector and the full directed-Hasse acyclicity, computes the exact integral Morse boundary by gradient paths, and independently performs all \(79\) chain cancellations over \(\mathbb Z\). Its expected transcript is included as `verification_output.txt`. It additionally checks the unreduced boundary ranks over \(\mathbb F_2\): \(8,28,43\). This modular computation is only a cross-check; the integral homotopy theorem rests on the exact acyclic matching and integral chain cancellations, not on modular ranks or a numerical guess.

## Relationship to prior work

The Hesse configuration is classically the nine inflection points and twelve inflection lines of a nonsingular plane cubic. Artebani and Dolgachev (first public preprint 2006-11-19, Section 2) identify these points with \(\mathbb F_3^2\) and the lines with cosets of order-three subgroups. Their investigation concerns the Hesse pencil and its geometry, rather than the cap simplicial complex or its homotopy type. Cameron's 2016 account discusses affine caps and the cap-set bounds, not the integral homotopy of the complex of all small caps. A projective cap-complex calculation for \(\operatorname{PG}(2,3)\) is not a homotopy classification of this nine-point induced affine subcomplex, since homotopy invariants do not generally pass to induced subcomplexes. An affine-plane incidence-graph Vietoris–Rips classification concerns another complex whose simplices are determined by graph-metric cliques, not by forbidden collinear triples. Comparisons with the same underlying Hesse incidence geometry must distinguish these definitions before claiming implication.

## Limitations

The assertion is specific to the affine plane of order three and its twelve lines. It does not prove an all-order classification, nor an equivariant splitting under the affine automorphism group. The proof is a complete exact finite computation with a short independent verifier; it has not received independent scientific audit. Literature discovery cannot exclude all unindexed equivalent results; in particular, searching only for the phrase "Hesse cap complex" is not by itself evidence of novelty.

## References

1. Michela Artebani and Igor Dolgachev, *The Hesse pencil of plane cubic curves*, arXiv:math/0611590 (first public November 19, 2006), Section 2; later published in *L'Enseignement Mathématique* 55 (2009), 235–273, DOI 10.4171/LEM/55-3-3.
2. Peter J. Cameron, *Caps in AG(n,3)*, May 23, 2016, https://cameroncounts.wordpress.com/2016/05/23/caps-in-agn3/ (discussion of cap sets and affine lines).
3. Robin Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145, DOI 10.1006/aima.1997.1650 (discrete-Morse CW theorem).
