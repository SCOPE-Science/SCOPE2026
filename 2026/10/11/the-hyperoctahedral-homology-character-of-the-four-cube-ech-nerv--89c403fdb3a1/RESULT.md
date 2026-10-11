# The hyperoctahedral homology character of the four-cube Čech nerve at scale three

## Finding

Let \(Q_4\) be the four-dimensional cube graph, with vertices \(\{0,1\}^4\), unit edges, and the shortest-path metric on its geometric realization. Let \(X=\mathcal N(Q_4,3)\) be the nerve of closed radius-\(3/2\) metric balls centered at its sixteen vertices. The natural action of \(B_4=(C_2)^4\rtimes S_4\), of order \(384\), on reduced rational homology has the following complete decomposition:

\[
\widetilde H_3(X;\mathbb Q)\cong V_{\varnothing,(1,1,1,1)}\cong \det,
\qquad
\widetilde H_4(X;\mathbb Q)\cong
V_{(2),(2)}\oplus V_{(2),(1,1)}\oplus V_{(3),(1)}\oplus V_{(2,1),(1)}.
\]

Here \(V_{\lambda,\mu}\) denotes the rational irreducible representation of the signed permutation group indexed by a bipartition of four, with the first partition assigned trivial coordinate signs and the second partition assigned sign coordinate characters. The summands of fourth homology have respective dimensions \(6,6,4,8\). Every other reduced rational homology group is zero. The one-dimensional third homology transforms by the determinant of the standard signed permutation action; neither positive-degree homology group has nonzero vectors fixed by all cube symmetries.

## Assumptions and scope

All complexes are finite simplicial complexes; balls are taken in the **geometric realization of the graph**, not only among graph vertices and not in ambient Euclidean four-space. The scale parameter is exactly \(3\), meaning radius \(3/2\). The asserted action is on rational simplicial homology. Every element of \(B_4\) acts on binary vertices as \(x\mapsto \sigma(x)\oplus b\), where \(\sigma\in S_4\) permutes four coordinates and \(b\in(C_2)^4\) is a coordinate-flip vector.

For bipartitions \((\lambda,\mu)\) with \(|\lambda|+|\mu|=4\), put \(a=|\lambda|\). The character \(\chi^{\lambda,\mu}\) is induced from the character of \((C_2\wr S_a)\times(C_2\wr S_{4-a})\) which is the Specht character \(S^\lambda\) on the first permutation factor and the tensor product of coordinate signs with \(S^\mu\) on the second. This fixes the representation-label convention completely.

## Proof

**1. The exact nerve.** The midpoint of an edge \(uv\) lies within distance \(3/2\) of precisely the cube vertices in \(N_1[u]\cup N_1[v]\). Every common point of closed radius-\(3/2\) balls is in a vertex or on a graph edge; along an edge, the set of eligible centers is contained in that edge-midpoint set. Consequently the maximal simplices are exactly
\[
F_{uv}=N_1[u]\cup N_1[v]\quad(uv\in E(Q_4)).
\]
The 32 edge sets are distinct and each has eight vertices. Exhaustively closing them under taking nonempty subsets gives \(3944\) faces, with face numbers by dimensions zero through seven
\[
(16,112,448,1016,1264,800,256,32).
\]
There are no other simplices or hidden higher-dimensional faces. The full graph automorphism group is \(B_4\): the image of one vertex has sixteen choices, followed by any of the 24 permutations of its four neighbors, and all these choices are realized by coordinate flips and permutations.

**2. Independent homological bounds.** Exact row elimination over \(\mathbb F_2\) on all eight consecutive simplicial chain groups gives ranks of the boundary operators in degrees one through seven
\[
(15,97,351,664,576,224,32).
\]
Hence reduced mod-two homology is one-dimensional in degree three, 24-dimensional in degree four, and zero otherwise. For any finite integral chain complex, its rational Betti number is at most its mod-two Betti number. It follows that over \(\mathbb Q\) only those two degrees are possible, with degree-three rank at most one. The face vector gives reduced Euler characteristic \(23\), so the two rational Betti numbers satisfy \(\beta_4-\beta_3=23\). Thus the only possibilities are \((\beta_3,\beta_4)=(0,23)\) or \((1,24)\).

**3. Signed Lefschetz traces.** For a simplicial symmetry \(g\), let \(c(g)\) be its reduced Lefschetz number, computed without homology from all invariant nonempty simplices:
\[
c(g)=\sum_{\substack{\varnothing\ne A\in X\\gA=A}}
(-1)^{|A|-1}\operatorname{sgn}(g|_A)-1.
\]
The final subtraction accounts for the augmented zero-dimensional chain. All 384 group elements were explicitly enumerated. The values depend only on the signed cycle type, meaning the lengths of the cycles of \(\sigma\) and the parity of coordinate flips on each cycle. The table below gives the 20 classes. In a type like `2-`, the integer is a cycle length and the final sign records odd parity of flips; `2+` records even parity.

| Signed cycle type | Class size | \(c(g)\) | \(\det(g)\) | \(c(g)+\det(g)\) |
|:--|--:|--:|--:|--:|
| `1+,1+,1+,1+` | 1 | 23 | 1 | 24 |
| `1+,1+,1+,1-` | 4 | 7 | -1 | 6 |
| `1+,1+,1-,1-` | 6 | -5 | 1 | -4 |
| `1+,1+,2+` | 12 | 5 | -1 | 4 |
| `1+,1+,2-` | 12 | 3 | 1 | 4 |
| `1+,1-,1-,1-` | 4 | -5 | -1 | -6 |
| `1+,1-,2+` | 24 | -3 | 1 | -2 |
| `1+,1-,2-` | 24 | -1 | -1 | -2 |
| `1+,3+` | 32 | -1 | 1 | 0 |
| `1+,3-` | 32 | 1 | -1 | 0 |
| `1-,1-,1-,1-` | 1 | -1 | 1 | 0 |
| `1-,1-,2+` | 12 | 1 | -1 | 0 |
| `1-,1-,2-` | 12 | -1 | 1 | 0 |
| `1-,3+` | 32 | 1 | -1 | 0 |
| `1-,3-` | 32 | -1 | 1 | 0 |
| `2+,2+` | 12 | -1 | 1 | 0 |
| `2+,2-` | 24 | 1 | -1 | 0 |
| `2-,2-` | 12 | -1 | 1 | 0 |
| `4+` | 48 | 1 | -1 | 0 |
| `4-` | 48 | -1 | 1 | 0 |

A weighted sum over the class sizes gives the exact character inner products
\[
\langle c,\mathbf1\rangle=0,\quad
\langle c,\operatorname{sgn}(\sigma)\rangle=0,\quad
\langle c,(-1)^{|b|}\rangle=0,\quad
\langle c,\det\rangle=-1.
\]
The reduced Lefschetz identity and the homological bounds imply \(c=\chi_4-\chi_3\). If degree-three rational homology vanished, then \(c=\chi_4\) would be a genuine character, contrary to its negative multiplicity \(-1\) of \(\det\). Therefore its rank is one and the ranks are exactly \(1\) and \(24\). Its character must be one of the four one-dimensional characters listed above; because \(\chi_4=c+\chi_3\) must have nonnegative multiplicities, necessarily \(\chi_3=\det\). Hence \(\chi_4=c+\det\).

**4. Complete decomposition.** For each signed cycle \(C\), let \(\ell(C)\) denote its length and \(\epsilon(C)\in\{0,1\}\) its flip parity. The irreducible character in the convention above is explicitly
\[
\chi^{\lambda,\mu}(g)=
\sum_{\substack{J\subseteq\operatorname{Cyc}(g)\\\sum_{C\in J}\ell(C)=|\lambda|}}
\chi^\lambda_{S_{|\lambda|}}(\{\ell(C):C\in J\})
\chi^\mu_{S_{|\mu|}}(\{\ell(C):C\notin J\})
(-1)^{\sum_{C\notin J}\epsilon(C)}.
\]
These 20 characters form an orthonormal basis of class functions, as checked directly with all 20 class sizes and the symmetric-group character tables of degrees at most four. Inner products of \(c+\det\) against this basis are precisely one for the four bipartitions in the finding, and zero for all remaining sixteen. Their dimensions add to \(24\). This proves the rational representation statement. The four summands all have a nonempty second partition, so none has vectors fixed by the full translation subgroup; the determinant module also has no full-group fixed vectors.

## Verification

Run the included standalone Python 3 script `verify.py` using only the standard library. It builds all 32 edge-neighborhood facets, every face, the boundary matrices over \(\mathbb F_2\), and every signed simplicial trace for all 384 cube symmetries. It checks constancy on each of the 20 signed-cycle classes, the total class sizes, the 20-by-20 character orthogonality relations, the four irreducible multiplicities, and both exact mod-two Betti dimensions. The script terminates with `VERIFY_OK` if and only if its assertions all pass. The tables in this proof are fully reconstructed by that code.

## Relationship to prior work

Adams, Shukla and Singh's *Čech complexes of hypercube graphs*, first publicly available 12 December 2022, defines this same intrinsic graph Čech construction. Its Lemma 3.1 supplies the maximal-simplex description, Table 1 reports already-known integral Betti numbers \(\beta_3=1\) and \(\beta_4=24\) for the present cube, and Theorems 5.9 and 5.13 establish collapsibility and vanishing outside degrees three and four for all larger cubes. Those nonequivariant statements do not determine the induced action of cube automorphisms on either homology group. The present finding is specifically the character and full irreducible decomposition, not a claim to discover those Betti numbers or a nonequivariant homotopy type. Greg Egan's *Hypercube (Technical Notes)* independently records the 384-element four-cube symmetry group's 20 conjugacy classes and character table; it does not discuss homology of this Čech nerve.

## Limitations

The theorem is confined to the four-cube, exactly scale three, and rational representations. It gives no integral lattice classification of the \(B_4\)-modules and does not extend to higher-dimensional cubes or other filtration parameters. Character computations determine representations but do not supply an equivariant homotopy equivalence or an equivariant cell decomposition. Its originality comparison is limited to inspected sources and indexed searches; an unindexed equivalent computation may exist.

## References

1. Henry Adams, Samir Shukla and Anurag Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871 (first public 2022-12-12), especially Lemma 3.1, Table 1 and Section 5. Full open text: https://arxiv.org/html/2212.05871v2 .
2. Greg Egan, *Hypercube (Technical Notes)*, section “The character table for the symmetries of the 4-cube”, https://www.gregegan.net/APPLETS/29/HypercubeNotes.html .
