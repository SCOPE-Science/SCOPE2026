# Resource-permutation homology of Stirling complexes is tree-shape independent

## Finding
Let \(T\) be any finite tree with \(m\ge2\) vertices and let \(n\ge m\). The Stirling cubical complex \(X=\mathcal{S}tr(T,n)\) carries a canonical action of \(S_n\) that permutes the \(n\) labeled resource coordinates. Write \(c(\sigma)\) for the number of cycles, including singleton cycles, of \(\sigma\in S_n\), and define
\[
F_m(k)=\sum_{a=1}^{m-1}(-1)^{m+a+1}\binom{m}{a+1}a^k.
\]
The complete character of its unique nonzero reduced rational homology representation is
\[
\operatorname{tr}\!\left(\sigma\mid\widetilde H_{n-m}(X;\mathbb Q)\right)
=\operatorname{sgn}(\sigma)F_m(c(\sigma)).
\]
All other reduced rational homology vanishes. In particular, the representation character depends only on \(m\) and \(n\), not on the isomorphism type of \(T\). Moreover the resource-unlabeled quotient is rationally acyclic:
\[
\widetilde H_i\!\left(|X|/S_n;\mathbb Q\right)=0\quad\text{for every integer }i.
\]

## Assumptions and scope
A cube of \(T^n\) is specified by an ordered \(n\)-tuple of vertices or unoriented edges of \(T\). It belongs to \(\mathcal{S}tr(T,n)\) precisely when every vertex of \(T\) appears literally as a vertex entry in that tuple. This is the definition in Kozlov's work. A permutation of the resource coordinates acts cellularly on this cubical complex, although it need not preserve each oriented cell's orientation. We consider finite ordinary trees, integer \(m\ge2\), integer \(n\ge m\), rational coefficients, and the permutation action on resources—not permutations of the tree's vertices. When \(n=m\), \(X\) is a discrete space of \(m!\) points and the homology assertion concerns reduced degree zero.

## Proof
**1. Localization of homology.** Kozlov's sphere-wedge theorem for Stirling complexes (Theorem 2.1 of the cited paper) gives \(X\simeq\bigvee^{F_m(n)}S^{n-m}\) for \(n\ge m\), so the only nonzero reduced rational homology is in degree \(n-m\), with dimension \(F_m(n)\). This theorem is used only nonequivariantly; it does not specify the \(S_n\)-action. For \(n=m\) this statement means \(m!\) isolated points, with reduced zeroth homology dimension \(m!-1\).

**2. Cellular traces for an arbitrary resource permutation.** Fix \(\sigma\in S_n\) with \(c=c(\sigma)\) disjoint cycles. Orient each edge of \(T\) once and order the moving coordinates of every cube increasingly. A cube contributes to the trace of \(\sigma\) on its cellular chain group only if the tuple is constant on each cycle of \(\sigma\). Each of the \(c\) cycles is assigned either one of the \(m\) vertices or one of the \(m-1\) edges. To lie in \(X\), the cycles assigned vertices must collectively hit all \(m\) distinct vertices. If exactly \(j\) cycles are assigned edges, the number of such invariant cubes is
\[
\binom cj(m-1)^j\operatorname{Surj}(c-j,m),
\]
where \(\operatorname{Surj}(b,m)\) counts surjections from a \(b\)-element set to an \(m\)-element set (and is zero for \(b<m\)). The cell has dimension equal to the sum of the lengths of its \(j\) edge cycles. The permutation of its edge-coordinate factors has orientation sign \((-1)^{d-j}\), where \(d\) is that dimension, because a length-\(\ell\) cyclic permutation has sign \((-1)^{\ell-1}\). Its contribution to the cellular Lefschetz number is therefore \((-1)^d(-1)^{d-j}=(-1)^j\). Thus
\[
L(\sigma)=\sum_{j=0}^{c}(-1)^j\binom cj(m-1)^j\operatorname{Surj}(c-j,m).
\]
Inclusion–exclusion for surjections gives the **finite exact identity**
\[
\operatorname{Surj}(b,m)=\sum_{h=0}^{m}(-1)^h\binom mh(m-h)^b,
\]
and applying the binomial theorem yields
\[
L(\sigma)=\sum_{h=0}^{m}(-1)^h\binom mh(1-h)^c.
\]
The term \(h=0\) is one; the term \(h=1\) is zero since \(c\ge1\). Reindexing \(h=a+1\) shows
\[
L(\sigma)-1=(-1)^{c+m}F_m(c).
\]

**3. Passage from chains to homology.** The cellular Lefschetz trace identity and the nonequivariant sphere-wedge theorem imply
\[
L(\sigma)=1+(-1)^{n-m}\operatorname{tr}\!\left(\sigma\mid\widetilde H_{n-m}(X;\mathbb Q)\right).
\]
This remains valid when \(n=m\), using reduced \(H_0\). Since \(\operatorname{sgn}(\sigma)=(-1)^{n-c}\), substitution yields
\[
\operatorname{tr}\!\left(\sigma\mid\widetilde H_{n-m}(X;\mathbb Q)\right)=\operatorname{sgn}(\sigma)F_m(c),
\]
proving the character formula and independence from the structure of the tree.

**4. Quotient.** After an equivariant barycentric subdivision, a finite group action on a finite cellular complex has rational quotient homology equal to invariant rational homology. Averaging the proved character gives the multiplicity of the trivial representation:
\[
\frac1{n!}\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)F_m(c(\sigma))
=\frac1{n!}\sum_{a=1}^{m-1}(-1)^{m+a+1}\binom m{a+1}\prod_{j=0}^{n-1}(a-j).
\]
Here the standard signed cycle-count identity \(\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)a^{c(\sigma)}=a(a-1)\cdots(a-n+1)\) follows, for example, by inserting a new symbol into existing cycles or adding a new singleton cycle. Because \(1\le a\le m-1<n\), every product contains a zero factor. Hence the degree-\(n-m\) invariant part vanishes; all other reduced rational homology already vanishes. The claimed rational acyclicity of the quotient follows.

## Verification
A self-contained standard-library exact checker, `stirling_resource_character_checker.py`, independently enumerates cells fixed by every resource permutation for \((m,n)=(2,2),(2,3),(2,4),(3,3),(3,4),(3,5),(4,4),(4,5)\). It computes orientation signs on fixed cube chains, checks both the closed character formula and a separate inclusion–exclusion trace expression, verifies \(F_m(m)=m!-1\), and confirms that the average character is zero. These are finite consistency checks, not the proof for all trees and all resource counts; the preceding cellular trace argument supplies that proof.

## Relationship to prior work
D. N. Kozlov, *Stirling complexes*, established the same cubical construction, its nonequivariant wedge-of-spheres theorem, and the dimension formula \(F_m(n)\), published online on 24 September 2022. The character formula here is a strictly finer statement: the value for a permutation depends on its cycle count, while the ordinary Betti number recovers only the identity value. Kozlov's explicit open question concerns the \(S_r\)-action permuting **leaves of a star tree**, not the \(S_n\)-action permuting **resources** considered here, so that question is not claimed to be solved. Closely related homological permutation-character methods for different combinatorial complexes do not cover these resource-reconfiguration cubical complexes.

## Limitations
This theorem establishes the complete rational \(S_n\)-character and rational quotient acyclicity only. It does not determine the integral \(S_n\)-lattice, the quotient's integral torsion or homotopy type, the automorphism-group action on the tree's vertices, nor any equivariant homotopy splitting. It depends on the published nonequivariant sphere-wedge theorem. Prior equivalent unindexed work remains a bibliographic risk; absence from searched indexes does not prove uniqueness.

## References
1. D. N. Kozlov, “Stirling complexes,” *Journal of Applied and Computational Topology* 7 (2023), 57–74; first published online 24 September 2022. DOI: https://doi.org/10.1007/s41468-022-00096-4 ; full open-access text: https://link.springer.com/article/10.1007/s41468-022-00096-4 . In particular Definition 1.1, Theorem 2.1, formula (4.2), and Open Question 1.
2. D. N. Kozlov, “Stirling complexes,” arXiv:2309.17142 (2023), later freely accessible manuscript version: https://arxiv.org/abs/2309.17142 .
