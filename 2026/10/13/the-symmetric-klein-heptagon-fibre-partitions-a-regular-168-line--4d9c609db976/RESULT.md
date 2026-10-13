# The symmetric Klein-heptagon fibre partitions a regular \(168\)-line orbit

## Finding
Let \(C: x^3y+y^3z+z^3x=0\) be the Klein quartic and let \(\eta_{\mathrm{sym}}\) be its unique \(\operatorname{Aut}(C)\)-invariant even theta characteristic. Agostini--Plaumann--Sinn--Wesner determine the fibre of the heptagon adjoint map over \((C,\eta_{\mathrm{sym}})\): after quotienting labels by \(D_7\), it consists of \(24\) heptagons and is one orbit under \(G=\operatorname{Aut}(C)\cong\operatorname{PSL}(2,7)\).

The constituent lines have a stronger orbit property. Across all \(24\) heptagons there are exactly \(168\) distinct projective lines, and \(G\) acts freely and transitively on this set. Equivalently, every constituent line has trivial stabilizer in \(G\). If \(H\cong C_7\) is the stabilizer of one heptagon, then under the regular identification \(G\to G\cdot\ell\), \(g\mapsto g\ell\), the seven lines of each heptagon are one left coset of \(H\); hence the \(24\) heptagons partition the regular \(168\)-element \(G\)-set into \(24\) septuples.

## Assumptions and scope
The statement is over \(\mathbf C\) and concerns the distinguished symmetric-theta fibre for the Klein quartic, with heptagons identified under the standard dihedral relabelling action. The source proves that this fibre contains \(336=14\cdot24\) labelled heptagons and that an order-seven automorphism cyclically rotates the seven sides of the constructed heptagon. The additional assertion proved here is line-level: no constituent line is reused by two distinct heptagons in the \(D_7\)-quotient fibre.

## Proof
Choose a primitive seventh root \(\zeta\), put \(b=\zeta^3+\zeta^4\), and choose \(a\) with
\[
a^7=-\frac{b+1}{b^3}.
\]
The source's explicit construction may be written with
\[
R_i=[b(a\zeta^i)^3:a\zeta^i:1],\qquad i\in\mathbf Z/7\mathbf Z,
\]
and sides \(L_i=\overline{R_{i-2}R_i}\). Exact substitution verifies that the \(R_i\) lie on \(C\), that the seven \(L_i\) are distinct with no three concurrent, and that their \(14\) nonconsecutive pairwise intersections lie on \(C\). Thus they give the required heptagon.

The automorphism
\[
\phi=[\zeta^4x:\zeta^2y:\zeta z]
\]
has order \(7\) and sends \(R_i\) to \(R_{i+1}\), hence cyclically permutes the seven sides. Let \(H=\langle\phi\rangle\). The source's orbit calculation gives \(|G|=168\) and identifies \(H\) as the stabilizer of the heptagon class, so the \(24\) heptagons are the cosets \(G/H\).

It remains to prove that the passage from heptagons to their sides introduces no identifications. Using exact matrices for \(G\), the attached verification closes the projective matrix group and obtains exactly \(168\) elements. It then applies all of them to one side, say \(L_0\), by the dual action and checks the projective stabilizer exactly. The stabilizer contains only the identity. Therefore \(|G\cdot L_0|=168\).

Since \(H\) cyclically permutes the seven sides of the base heptagon, its side set is \(H\cdot L_0\). For two cosets \(g_1H\) and \(g_2H\), an equality \(g_1h_1L_0=g_2h_2L_0\) would give a nonidentity stabilizer of \(L_0\) unless \(g_1H=g_2H\). Hence the side sets belonging to distinct heptagons are disjoint. Their union has \(24\cdot7=168\) lines and equals the regular orbit \(G\cdot L_0\).

## Verification
The standalone verifier uses exact arithmetic in the degree-\(42\) extension \(\mathbf Q(\zeta,a)\): it first proves that \(T^7+(b+1)/b^3\) is irreducible over \(\mathbf Q(\zeta)\), reconstructs the heptagon and all \(14\) residual quartic points, closes the explicit projective automorphism generators to a group of order \(168\), checks that \(\phi\) cycles the seven sides, enumerates the \(24\) cosets of \(H\), and computes the stabilizer of one line to have order \(1\). A fresh replay with SymPy 1.14.0 returned:

`VERIFY_OK field_degree=42 group=168 residual_points=14 line_stabilizer=1 line_orbit=168 heptagon_partition=24x7`

All computations are exact; no floating-point sampling or finite-field specialization is used as proof.

## Relationship to prior work
Agostini--Plaumann--Sinn--Wesner construct the symmetric Klein heptagon, prove the automorphism-orbit structure of its labelled fibre, and obtain the sharp count of \(336\) labelled heptagons over a quartic with a fixed even theta characteristic. Their result therefore supplies the \(24\) heptagon classes and the cyclic order-seven side rotation. The inspected source does not state that the constituent lines across those classes are pairwise distinct, nor that they form a regular \(168\)-line orbit.

The distinction is substantive: freeness of the action on heptagons does not imply freeness on a single constituent line, because an automorphism could stabilize a line while moving its containing heptagon. The exact line-stabilizer computation rules out precisely this possibility. Semantic database searches and targeted public searches for the line-orbit, stabilizer, and \(168\)-line formulations found no covering statement.

## Limitations
The result concerns the symmetric-theta fibre of the Klein quartic and does not assert an analogous regular line orbit for a generic quartic or for the other theta-characteristic fibres of the Klein quartic. The originality assessment is bounded by the inspected literature and database searches; a classical treatment under different language for Klein configurations could conceivably contain an equivalent line-level statement. Independent audit has not been performed.

## References
1. D. Agostini, D. Plaumann, R. Sinn, J. L. Wesner, *Plane quartics and heptagons*, arXiv:2408.15759v1, first public 2024-08-28.
2. Magma Handbook, *Automorphisms of plane quartics*, example `CrvG3_auts-ex (H136E4)`, giving explicit projective generators for the Klein quartic automorphism group of order \(168\).
