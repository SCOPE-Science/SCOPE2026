# The \(A_8\)-Specht character of the binary projective cap complex

## Finding
Let \(K\) be the simplicial complex of caps in \(\operatorname{PG}(3,2)\): its 15 vertices are the nonzero vectors of \(\mathbb F_2^4\), and its faces are exactly the subsets containing no triple \(\{a,b,a+b\}\) of distinct nonzero vectors. Its full simplicial automorphism group is \(G=\operatorname{GL}_4(\mathbb F_2)\), of order \(20{,}160\), acting by linear substitutions. Under an exceptional isomorphism \(G\cong A_8\), the complete rational reduced homology representation is

\[
\widetilde H_4(K;\mathbb Q)\cong
\bigl(S^{(7,1)}\oplus S^{(4,3,1)}\bigr)\!\downarrow_{A_8},
\qquad
\widetilde H_i(K;\mathbb Q)=0\quad(i\ne4).
\]

Here the displayed \(S^\lambda\) denote ordinary rational Specht representations of \(S_8\), restricted to \(A_8\). Both restrictions are absolutely irreducible, nonisomorphic, and have dimensions \(7\) and \(70\). In particular the natural action on the previously known \(77\)-dimensional rational homology is multiplicity-free, and its full-symmetry quotient is rationally acyclic:

\[
\widetilde H_i(K/G;\mathbb Q)=0\quad\text{for every }i.
\]

The character is specified completely by the following table. Split \(A_8\)-classes of cycle types \((7,1)\) and \((5,3)\) each appear twice, with equal character values.

| \(A_8\) cycle type | class size | \(\chi_{\widetilde H_4}\) |
|:--|--:|--:|
| \((1^8)\) | 1 | 77 |
| \((2^4)\) | 105 | -3 |
| \((2^2,1^4)\) | 210 | 5 |
| \((4^2)\) | 1,260 | -3 |
| \((3^2,1^2)\) | 1,120 | 2 |
| \((4,2,1^2)\) | 2,520 | 1 |
| \((6,2)\) | 3,360 | 0 |
| \((7,1)\) (each of two classes) | 2,880 | 0 |
| \((3,1^5)\) | 112 | -1 |
| \((3,2^2,1)\) | 1,680 | -1 |
| \((5,3)\) (each of two classes) | 1,344 | -1 |
| \((5,1^3)\) | 1,344 | 2 |

## Assumptions and scope
The vertex labels \(1,\ldots,15\) are interpreted as four-bit vectors, and vector addition is bitwise XOR. The forbidden triples are precisely the 35 lines of \(\operatorname{PG}(3,2)\). The result is about ordinary reduced rational simplicial homology of this finite complex, and about the action of **all** projective collineations in characteristic two; there are no scalar multipliers other than one.

Any simplicial automorphism preserves the minimal nonfaces, which are exactly the projective lines. For distinct nonzero vectors \(a,b\), its vertex permutation \(f\) consequently satisfies \(f(a+b)=f(a)+f(b)\). Extending by \(f(0)=0\) makes \(f\) an invertible linear transformation, proving that the simplicial automorphism group is exactly \(G\).

## Proof
**1. Rational concentration.** Direct face enumeration gives \(3{,}048\) nonempty faces with face vector
\[
(f_0,\ldots,f_7)=(15,105,420,945,1008,420,120,15).
\]
The supplied integral Morse verifier defines a deterministic vertex-toggling matching using the pivot order \((12,14,11,13,7,1,2,9,15,10,6,8,4,3,5)\) in one-based vertex labels. It matches \(1{,}484\) pairs. A topological sort of the entire reversed-matching Hasse graph visits all \(3{,}048\) nodes, so the matching is acyclic. Its critical cells are one vertex, one three-cell and 78 four-cells. The signed integral Morse differential from degree four to degree three has the coefficient histogram \(-2:11,\ 0:39,\ 2:28\), hence rank one over \(\mathbb Q\). Thus reduced rational homology is concentrated in degree four, where it has dimension \(78-1=77\). The integral homotopy type and order-two torsion in degree three had already been established separately and are not new claims.

**2. Fixed-face character.** For \(g\in G\), let its orbits on the 15 nonzero vectors be \(O_1,\ldots,O_r\). Each invariant face must be a union of full orbits. If it contains \(s\) orbits, its contribution to the signed simplicial Lefschetz trace is \((-1)^{s-1}\): the sign of its oriented vertex permutation cancels the parity of the total number of vertices except for the number of orbits. Subtracting the empty-face contribution gives the reduced Lefschetz number
\[
\boxed{\displaystyle
\chi(g)=-\sum_{J\subseteq\{1,\ldots,r\}\atop
\bigcup_{j\in J}O_j\text{ is a cap}}(-1)^{|J|}.}
\]
As reduced rational homology is concentrated in degree four, the reduced Lefschetz number is precisely \(\chi_{\widetilde H_4}(g)\). The packaged verifier enumerates all \(20{,}160\) nonsingular binary matrices, calculates their 14 conjugacy classes by conjugation with the 12 elementary transvections, and evaluates the formula on every element. As a separate cross-check, it sums the signs of all invariant oriented simplices for the 14 class representatives. Both procedures return the table above. The class-size-weighted sum of the character is zero.

**3. Irreducible identification.** Under \(\operatorname{GL}_4(2)\cong A_8\), conjugacy classes are matched to even cycle types by their orders and sizes, with two split pairs. The rational \(S_8\) Specht characters are calculated independently by the Jacobi–Trudi alternating sum of invariant ordered-block counts for each cycle type. In the table order, the character rows for \(S^{(7,1)}\) and \(S^{(4,3,1)}\) are respectively
\[
(7,-1,3,-1,1,1,-1,0,0,4,0,-1,-1,2)
\]
and
\[
(70,-2,2,-2,1,0,1,0,0,-5,-1,0,0,0).
\]
Their sum is the calculated \(77\)-dimensional homology character on all 14 classes. Their self-inner products in \(A_8\) are both one, so the restrictions are absolutely irreducible; their dimensions differ, so they are not isomorphic. Semisimplicity in characteristic zero proves the asserted direct-sum decomposition.

**4. Quotient.** The class-size-weighted character sum equals zero, so the invariant subspace of \(\widetilde H_4(K;\mathbb Q)\) is zero. A finite group action on a finite simplicial complex has quotient rational homology equal to the invariant rational homology (e.g. after barycentric subdivision). Since all other reduced rational homology groups vanish, the quotient is rationally acyclic.

## Verification
Run each of the supplied standalone Python 3 scripts (standard library only): `verify_integral_morse.py`, `verify_gl4_character.py`, and `verify_a8_specht.py`. The independent exact checks include the full face vector, the matching acyclicity topological sort, all integral Morse differential coefficients, all \(20{,}160\) linear transformations and their conjugacy-class character values, oriented fixed-face Lefschetz traces, the two Specht character vectors and their exact inner products. `CHECKS.txt` records the corresponding reproducible outputs. These are finite, exhaustive computations for the specific object, not extrapolations to larger projective spaces.

## Relationship to prior work
Forbes, Grannell and Griggs studied independent point sets in Steiner triple systems in 2004, and Grynkiewicz and Lev studied binary projective caps in a preprint first posted in 2008. Lew's 2017 thesis explicitly defines projective cap simplicial complexes and reports topological/spectral examples mostly for projective planes and ternary spaces. Murray established the exceptional group isomorphism \(A_8\cong\operatorname{GL}_4(2)\). An earlier calculation of this exact rank-four binary cap complex establishes its nonequivariant homotopy type \(M(\mathbb Z/2,3)\vee\bigvee^{77}S^4\); that nonequivariant theorem is not claimed as new here. The added theorem is the full collineation-group character and its \(7+70\) Specht decomposition, which none of those cited statements implies. Searches did not identify an earlier equivalent character calculation, but bibliographic incompleteness remains a risk.

## Limitations
The result gives the rational \(G\)-representation, not the integral \(\mathbb Z[G]\)-lattice, quotient integral torsion, an equivariant homotopy equivalence, or a classification for projective dimensions other than three. Rational acyclicity of \(K/G\) does not imply contractibility. Identification under \(A_8\) uses a choice of exceptional isomorphism; the character is invariant under the possible interchange of the two split classes, so the stated decomposition is unaffected. Independent external validation has not been performed.

## References
1. A. D. Forbes, M. J. Grannell, and T. S. Griggs, *Independent sets in Steiner triple systems*, Ars Combinatoria 72 (2004), 161–169. https://combinatorialpress.com/ars-articles/volume-072-ars-articles/independent-sets-in-steiner-triple-systems/.
2. D. J. Grynkiewicz and V. F. Lev, *1-Saturating Sets, Caps and Round Sets in Binary Spaces*, arXiv:0811.1322v1 (2008-11-09). https://arxiv.org/abs/0811.1322.
3. A. Lew, *Spectral gaps of generalized flag complexes*, master's thesis (2017), Section 6.2. https://www.math.cmu.edu/~alanlew/files/theses/msc%20thesis.pdf.
4. J. Murray, *The Alternating Group A8 and the General Linerar Group GL4(2)*, Mathematical Proceedings of the Royal Irish Academy 99A (1999), 123–132. https://mural.maynoothuniversity.ie/id/eprint/2153/.
