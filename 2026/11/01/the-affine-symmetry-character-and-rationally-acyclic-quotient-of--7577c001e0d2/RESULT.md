# The affine symmetry character and rationally acyclic quotient of the nine-point cap complex

## Finding
Let \(V=\mathbb F_3^2\). Write \(K\) for the simplicial complex whose faces are the subsets of \(V\) containing no complete affine line (equivalently, no three distinct collinear points). Its full incidence automorphism group is \(G=\operatorname{AGL}_2(\mathbb F_3)\), of order \(432\). The **new calculation** is the complete rational reduced homology character of the action of \(G\) on \(K\), together with the rational homology of the quotient.

More precisely, the supporting nonequivariant integral homotopy type is
\[
K\simeq S^2\vee\bigvee^{11}S^3.
\]
This nonequivariant classification is **not claimed as new**. For an affine transformation \(g(v)=Av+b\), its action on the integral second homology line is
\[
\operatorname{tr}(g\mid\widetilde H_2(K;\mathbb Z))=\varepsilon(g)
=\begin{cases}1,&\det(A)=1\text{ in }\mathbb F_3,\\-1,&\det(A)=2\text{ in }\mathbb F_3.\end{cases}
\]
Its character on the eleven-dimensional rational third homology is determined for **every** \(g\in G\) by
\[
\chi_3(g)=1+\varepsilon(g)-\sum_{k=0}^{3}(-1)^k\,\operatorname{tr}(g\mid C_k(K;\mathbb Q)),
\]
where the chain trace is the signed number of oriented \(k\)-simplices fixed setwise by \(g\). The exact calculation yields the following ten exhaustive profiles. A profile's four-tuple lists the chain traces in dimensions zero through three; \(m\) is its multiplicity among all affine transformations. The determinant label \(+\) or \(-\) means \(1\) or \(2\) in \(\mathbb F_3\), respectively.

| Determinant | Chain traces \((t_0,t_1,t_2,t_3)\) | \(\chi_3\) | \(m\) |
|---|---|---:|---:|
| \(+\) | \((0,0,0,0)\) | 2 | 8 |
| \(+\) | \((0,0,3,0)\) | -1 | 48 |
| \(+\) | \((1,-4,0,6)\) | 3 | 9 |
| \(+\) | \((1,-1,0,0)\) | 0 | 72 |
| \(+\) | \((1,0,0,-2)\) | -1 | 54 |
| \(+\) | \((3,3,0,0)\) | 2 | 24 |
| \(+\) | \((9,36,72,54)\) | 11 | 1 |
| \(-\) | \((0,0,0,0)\) | 0 | 72 |
| \(-\) | \((1,0,0,0)\) | -1 | 108 |
| \(-\) | \((3,0,-6,0)\) | 3 | 36 |

Both reduced characters have zero group average. Consequently, all reduced rational homology groups of the symmetry quotient vanish:
\[
\boxed{\widetilde H_*(K/G;\mathbb Q)=0.}
\]
The character values, rather than just the multiplicity distribution, specify the full rational representation because the formula applies to each affine map and rational representations of finite groups are semisimple.

## Assumptions and scope
Index the points in lexicographic order: index \(3x+y\) denotes \((x,y)\) for \(x,y\in\{0,1,2\}\). An affine line is the unordered triple \(\{p,p+d,p+2d\}\) for nonzero \(d\in\mathbb F_3^2\), where repeated direction vectors identify the same line. There are twelve distinct lines. The cap complex contains every nonempty subset avoiding these lines and has face vector \((9,36,72,54)\) in simplicial dimensions zero through three; it has no larger faces.

The group acts on simplices by permuting the nine vertices. Chain groups carry their usual ordered orientation signs. The rational quotient refers to the topological realization \(|K|/G\), not to the naive orbit set of unoriented simplices. The homology is reduced integral or rational homology, as indicated.

## Proof
**1. A finite integral topological model.** Apply a staged vertex-toggle matching to all 171 nonempty faces, using vertex order \((5,4,7,2,6,0,8,1,3)\). At each stage pair every then-unmatched face not containing the active vertex with its active-vertex extension, when both remain available. There are exactly 79 disjoint pairs. Orient each unmatched face incidence downward and each paired incidence upward. The resulting directed face Hasse graph has 171 nodes and 504 arcs and is acyclic (the standalone verifier checks an exhaustive topological sort). There remain exactly one critical vertex, one critical two-cell and eleven critical three-cells.

For completeness, the integral two-cycle \(z\), with coefficients on oriented triples given by
\[
 z=-[013]+[016]+[023]-[026]-[123]+[126],
\]
and integral two-cocycle \(c\), with its nonzero values given by
\[
\begin{aligned}
 c={}&[014]^*-[025]^*-[045]^*-[046]^*+[067]^*+[123]^*\\
 &-[134]^*-[136]^*+[167]^*+[235]^*-[256]^*+[267]^*,
\end{aligned}
\]
satisfy \(\partial z=0\), \(\delta c=0\) and \(\langle c,z\rangle=-1\), all by direct exact integer checks on the 54 oriented tetrahedra. Here \([ijk]\) denotes the oriented triangle with the three listed point indices; \([ijk]^*\) is its dual cochain.

By the acyclic matching, \(K\) has the homotopy type of a CW complex with one cell in dimensions \(0,2\) and eleven in dimension \(3\). Its only possibly nonzero Morse boundary is from dimension three to dimension two, a homomorphism \(\mathbb Z^{11}\to\mathbb Z\). The pairing with \(z\) and \(c\) proves that \(H_2(K;\mathbb Z)\) contains a free summand, so that boundary must be the zero map. The two-cell attaches to a point, and each three-cell attaches to \(S^2\) by a map of degree zero. Since \(\pi_2(S^2)\cong\mathbb Z\), all attaching maps are null homotopic. This independently reconstructs the supporting wedge type integrally.

**2. The full affine automorphism group.** Every map \(v\mapsto Av+b\) with \(A\in\operatorname{GL}_2(\mathbb F_3)\) and \(b\in\mathbb F_3^2\) preserves the twelve lines. There are \(48\cdot9=432\) such distinct maps. Conversely, any incidence automorphism is determined by the image of an ordered noncollinear triple: every remaining point is constructed from the triple using the unique third point on a line and affine-line intersections. There are \(9\cdot8\cdot6=432\) ordered noncollinear triples, proving equality with the full incidence automorphism group.

**3. The degree-two sign.** The unimodular pairing \(\langle c,z\rangle=-1\) shows that \([z]\) is a primitive generator of the rank-one integral second homology. For every one of the 432 affine permutations, calculate the integer
\[
 \varepsilon(g)=\frac{\langle c,gz\rangle}{\langle c,z\rangle}.
\]
The complete finite enumeration in `verify_hesse.py` checks that this is exactly \(+1\) for determinant one and \(-1\) for determinant two. This determines the full integral degree-two action without using character theory over a field.

**4. The degree-three character.** For a permutation of vertices acting on a simplicial complex, the trace on oriented chain degree \(k\) is the signed number of \(k\)-simplices fixed as sets. The simplicial Lefschetz identity, with ordinary degree-zero homology of trace one, gives
\[
 \sum_{k=0}^3(-1)^k\operatorname{tr}(g\mid C_k)
 =1+\varepsilon(g)-\chi_3(g).
\]
Enumerating the four chain traces for every affine permutation yields exactly the ten displayed profiles, with total multiplicity \(432\). In particular, the identity has third-homology trace eleven.

**5. The rational quotient.** Maschke averaging implies that the dimension of the \(G\)-invariant part of a rational representation equals the average character value. The table gives
\[
 \frac1{432}\sum_{g\in G}\varepsilon(g)=0,
 \qquad \frac1{432}\sum_{g\in G}\chi_3(g)=0.
\]
After barycentric subdivision the finite simplicial action has no inversions. Its quotient cellular chain complex over \(\mathbb Q\) computes the coinvariant chains, and averaging identifies rational quotient homology with the invariant part of rational homology. Both reduced invariant spaces therefore vanish.

## Verification
`verify_hesse.py` is standalone Python 3 code using only the standard library. It constructs the affine lines and all faces from coordinates; checks that the face vector is exactly \((9,36,72,54)\); generates the 79 pairs from the stated order; checks disjointness and exhaustive acyclicity of the directed Hasse graph; verifies the cycle, cocycle and unit pairing over the integers; enumerates 432 distinct affine permutations and verifies preservation of all lines; compares all 432 degree-two signs with determinants; recomputes signed chain traces, the ten character profiles and both group averages. The checked execution ends with `VERIFY_OK`, and the recorded output is in `verification_output.txt`.

The proof concerns a finite complex and a finite group, so the specified exhaustive checks are complete over the stated domain. No floating-point arithmetic, finite-to-infinite extrapolation or unsupported rank inference is used.

## Relationship to prior work
Merino, Ramírez-Ibáñez and Rodríguez-Sánchez (first available 2012-10-04) discuss the nine-point affine-plane Steiner system and its matroid Tutte polynomial. The rank-three **matroid independence complex** excludes four-element sets, whereas \(K\) has 54 tetrahedral faces; its Tutte polynomial does not specify the present character. Lew's 2017 spectral-gap preprint explicitly obtains nonzero real second cohomology for this exact forbidden-line complex; the supporting nonequivariant homology is therefore not new. Lew's 2020 representability-and-boxicity paper explicitly names the same complex \(X_{2,9}\) and asks whether its representability is at most five. That question is **not** resolved here. A separate earlier homotopy computation already establishes the nonequivariant sphere wedge; this manuscript's contribution is exclusively the full affine homology action and the resulting quotient statement.

Searches also compared aliases `Hesse configuration`, `nine-point cap complex`, `affine Steiner triple system`, `forbidden-line complex`, and `X_{2,9}` with relevant published topological computations. No reviewed source identified the 432-element character profile or the rational quotient conclusion. Absence from indexed records is not proof of publication priority.

## Limitations
The rational representation character is determined, but an explicit irreducible decomposition and the full integral degree-three lattice are not supplied. Rational acyclicity of \(K/G\) does not imply integral acyclicity or contractibility. The result does not establish a convex-nerve representation bound, and in particular does not settle the representability question of Lew. An unindexed equivalent character computation may exist. The finite calculations are reproducible, but independent mathematical evaluation has not been performed.

## References
1. C. Merino, M. Ramírez-Ibáñez and G. Rodríguez-Sánchez, *The Tutte Polynomial of Some Matroids*, International Journal of Combinatorics (first published 2012-10-04), DOI: `10.1155/2012/430859`, https://doi.org/10.1155/2012/430859 ; Section 3.1 treats \(\operatorname{AG}(2,3)\).
2. A. Lew, *Spectral gaps of simplicial complexes without large missing faces*, arXiv:1706.00358v1 (2017-06-01), https://arxiv.org/abs/1706.00358 ; page 2 discusses the exact forbidden-line complex and its real second cohomology.
3. A. Lew, *Representability and boxicity of simplicial complexes*, arXiv:2008.09997v1 (2020-08-23), https://arxiv.org/abs/2008.09997 ; Conjecture 20 defines the exact complex \(X_{2,9}\).
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145; used for the standard acyclic-matching implication.
