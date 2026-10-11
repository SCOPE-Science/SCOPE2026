# Only three branch-component patterns for genus-two fibered knots
## Finding
Let \(K\subset S^3\) be a genus-two fibered knot, let \(M_K\) denote zero surgery on \(K\), and let \(B_K\subset T^2\times S^2\) be the branch multisection in the hyperelliptic double cover
\[
M_K\times S^1\longrightarrow T^2\times S^2.
\]
Then the multiset of degrees of the connected components of \(B_K\) is necessarily
\[
(6),\qquad (5,1),\qquad\text{or}\qquad(3,3).
\]
If \(\Delta_K(t)\) is the symmetrically normalized Alexander polynomial and
\[
\widehat{\Delta}_K(t)=t^2\Delta_K(t),
\]
then, modulo two,
\[
\widehat{\Delta}_K(t)\equiv t^4+t^3+t^2+t+1
\]
if and only if the component degrees are \((5,1)\), whereas
\[
\widehat{\Delta}_K(t)\equiv t^4+t^2+1
\]
for each of the patterns \((6)\) and \((3,3)\). Thus the mod-two Alexander polynomial detects the \((5,1)\) pattern but does not distinguish the remaining two patterns.

## Assumptions and scope
Akhmedov proves that for every genus-two fibered knot the capped monodromy can be represented by a diffeomorphism commuting with the genus-two hyperelliptic involution. The resulting double branched cover has branch locus a degree-six braided multisection, and its connected components are tori indexed by the orbits of the induced permutation of the six Weierstrass points. The statement here concerns only this branch multisection and does not assert that each of the three permitted patterns is realized by a knot.

For a genus-two fibered knot, the action of the capped monodromy on first homology has characteristic polynomial equal, up to the usual Laurent monomial normalization, to the Alexander polynomial. The knot normalization gives \(|\Delta_K(1)|=1\).

## Proof
Let \(\Omega\) be the six Weierstrass points and let \(\sigma\in S_6\) be their permutation under the capped monodromy. Over \(\mathbf F_2\), the homology of the closed genus-two fiber has the standard equivariant description
\[
H_1(\Sigma_2;\mathbf F_2)\cong E/\langle\mathbf 1\rangle,
\qquad
E=\left\{x\in\mathbf F_2^6:\sum_{i=1}^6x_i=0\right\}.
\]
Equivalently, a class is represented by an even subset of \(\Omega\), with a subset identified with its complement. The permutation action on branch points agrees with the induced action on this quotient.

Because \(|\Delta_K(1)|=1\), the determinant of \(I-h_*\) is odd. Hence \(I-\bar h_*\) is invertible on \(H_1(\Sigma_2;\mathbf F_2)\): the mod-two monodromy has no nonzero fixed vector.

Suppose a class represented by \(x\in E\) is fixed. Then \(\sigma x=x\) or \(\sigma x=x+\mathbf1\). In the second case, the coordinates must alternate around every cycle of \(\sigma\), so every cycle has even length. Such an alternating vector has exactly three nonzero coordinates, contradicting \(x\in E\). Thus every fixed class has a representative fixed by \(\sigma\), hence is represented by a union of cycles having even total size, modulo complement.

Therefore the absence of nonzero fixed classes is equivalent to saying that no nonempty proper union of cycles of \(\sigma\) has even cardinality. If \(\sigma\) has one cycle, its type is \((6)\). If it has two cycles, each must have odd length, giving exactly \((5,1)\) or \((3,3)\). If it has at least three cycles, then either one cycle has even length, or two odd cycles have even total length; either case produces a forbidden nonempty proper even union. This proves the three-pattern classification. Akhmedov's orbit-component correspondence then turns these cycle lengths into the degrees of the torus components of \(B_K\).

For the polynomial refinement, let \(P=\mathbf F_2^6\) be the permutation module. A permutation with cycle lengths \(\ell_1,\ldots,\ell_r\) has characteristic polynomial
\[
\prod_{j=1}^r(t^{\ell_j}-1)
\]
on \(P\). Passing first to \(E\) and then to \(E/\langle\mathbf1\rangle\) removes two trivial factors, so the characteristic polynomial on \(H_1(\Sigma_2;\mathbf F_2)\) is
\[
\frac{\prod_j(t^{\ell_j}-1)}{(t-1)^2}.
\]
For \((5,1)\) this is \(t^4+t^3+t^2+t+1\). For \((6)\) it is \(t^4+t^2+1\), and for \((3,3)\) it is \((t^2+t+1)^2=t^4+t^2+1\). This characteristic polynomial is precisely \(\widehat{\Delta}_K(t)\) modulo two.

## Verification
The accompanying verifier enumerates all \(720\) permutations of six points, constructs the induced action on \(E/\langle\mathbf1\rangle\), and checks both the zero-fixed-space condition and the characteristic polynomial. It finds exactly the three cycle types above. The finite computation verifies the group-theoretic classification independently of the symbolic argument; the theorem itself does not rely on extrapolation from finite samples.

Verifier output:

`VERIFY_OK allowed_types=(6),(5,1),(3,3) counts=120,144,40 total=304`

`CHAR_OK (5,1)=t^4+t^3+t^2+t+1; (6),(3,3)=t^4+t^2+1`

## Relationship to prior work
Akhmedov's Theorem 2.1 gives the genus-two branched-cover construction, proves that the branch components correspond to Weierstrass-point orbits, and states that every genus-two fibered knot lies in the hyperelliptic setting. It does not impose a cycle-type restriction on those six-point orbits and does not discuss the Alexander polynomial in this connection.

Melvin and Morton study genus-two fibered knots using mod-two monodromy to obstruct presentation as a plumbing of Hopf bands. Their stated results concern Hopf-plumbing restrictions and particular families; they do not give the branch-multisection component classification above. The present argument instead combines the universal knot condition \(|\Delta_K(1)|=1\) with the six-point hyperelliptic permutation representation.

## Limitations
The theorem classifies only the possible component-degree patterns in this specific hyperelliptic branched-cover construction. It does not prove that all three patterns are realized by genus-two fibered knots, and the mod-two Alexander polynomial does not distinguish \((6)\) from \((3,3)\). No classification of integral monodromy conjugacy classes is claimed.

## References
1. Anar Akhmedov, *Braided Surface and Small Exotic 4-Manifolds*, arXiv:2610.00409v1, 30 September 2026; see Theorem 2.1.
2. P. M. Melvin and H. R. Morton, *Fibred Knots of Genus 2 Formed by Plumbing Hopf Bands*, Journal of the London Mathematical Society, s2-34 (1986), 159-168, DOI:10.1112/jlms/s2-34.1.159.
