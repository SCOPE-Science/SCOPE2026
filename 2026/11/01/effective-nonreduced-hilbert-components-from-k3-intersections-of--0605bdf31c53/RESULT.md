# Effective nonreduced Hilbert components from K3 intersections of three quadrics

## Finding
For every integer \(m\ge 2\), the Hilbert scheme of smooth connected complex curves in \(\mathbb P^5\) has a generically nonreduced irreducible component whose general curve \(C\) belongs to \(|mD|\) on a smooth complete intersection \(S\subset\mathbb P^5\) of three quadrics containing a line \(E\), where \(D=2h+E\) and \(h=\mathcal O_S(1)\). The component has dimension \(17m^2+54\), its general Zariski tangent space has dimension \(17m^2+57\), and its curves have degree \(17m\) and genus \(17m^2+1\). In particular, \(m=2\) yields degree \(34\), genus \(69\), component dimension \(122\), and tangent dimension \(125\). This supplies an effective range for the higher-dimensional construction that previously assumed an unspecified sufficiently large multiple.

## Assumptions and scope
Work over \(\mathbb C\). Let \(S\subset\mathbb P^5\) be a smooth complete intersection of three quadrics that contains a line \(E\simeq\mathbb P^1\). Such surfaces exist by the general complete-intersection Bertini argument with prescribed smooth line. Let \(h\) denote the hyperplane divisor; then \(S\) is a K3 surface with \(h^2=8\), \(h\cdot E=1\), \(E^2=-2\). Put \(D=2h+E\), so \(D^2=34\), \(D\cdot E=0\), \(h\cdot D=17\). Nasu's contraction lemma [1, Lemma 2.3] says that \(|D|\) is basepoint-free and its morphism contracts precisely \(E\). Thus \(D\) is nef and big. The claim concerns the specified components of the Hilbert scheme, not all components with the same Hilbert polynomial, and does not assert any impossibility for \(m=1\).

## Proof
**Step 1: an effective vanishing package.** Kawamata--Viehweg vanishing on the smooth complex K3 surface, applied to the nef and big divisor \(rD\), yields
\[
H^1(S,\mathcal O_S(rD))=0\qquad(r\ge1).
\]
Serre duality, using \(K_S\simeq\mathcal O_S\), gives the same conclusion for \(-rD\). Since \(4h\) is ample and the sum of an ample and a nef divisor is ample, Kodaira vanishing gives
\[
H^1(S,\mathcal O_S(mD-2E))=0\qquad(m\ge2),
\]
because \(mD-2E=4h+(m-2)D\). The stronger shifted vanishing required for second-order obstructions is
\[
H^1(S,\mathcal O_S((m-1)D-2E))=0\qquad(m\ge2).
\]
For \(m\ge3\), this is Kodaira vanishing for \(4h+(m-3)D\). At the endpoint \(m=2\), the line bundle is \(2h-E\). Its restriction sequence is
\[
0\longrightarrow\mathcal O_S(2h-E)\longrightarrow\mathcal O_S(2h)
\longrightarrow\mathcal O_E(2)\longrightarrow0.
\]
The map on global sections is surjective: the degree-two homogeneous polynomials on \(\mathbb P^5\) restrict onto every quadratic polynomial on the projective line \(E\). Since \(H^1(S,\mathcal O_S(2h))=0\), its long exact sequence gives \(H^1(S,\mathcal O_S(2h-E))=0\). By Serre duality this also proves
\[
H^1(S,\mathcal O_S(2E-(m-1)D))=0\qquad(m\ge2).
\]
These are the explicit low-degree substitutes for the asymptotic Serre vanishings used in [1, Lemma 2.6 and Proposition 4.7].

**Step 2: the unobstructed flag family.** For each \(m\ge2\), \(|mD|\) is basepoint-free. A general member is smooth, misses \(E\), and is connected, the last property following from \(H^1(S,\mathcal O_S(-mD))=0\) and \(H^0(S,\mathcal O_S(-mD))=0\). Moreover \(H^1(S,\mathcal O_S(E))=0\): \(E\) is a rigid \((-2)\)-curve, so \(h^0(\mathcal O_S(E))=1\); Riemann--Roch gives \(\chi(\mathcal O_S(E))=1\), and \(h^2(\mathcal O_S(E))=h^0(\mathcal O_S(-E))=0\). Nasu's Hilbert-flag criterion [1, Lemmas 2.12, 4.1 and 4.3] therefore applies with \(C\sim 2mh+mE\): the flag scheme of \(C\subset S\) is smooth at a general pair. By Riemann--Roch and vanishing, \(\dim |mD|=17m^2+1\). The smooth incidence variety of lines on triple-quadric K3 surfaces has dimension \(53\) [1, Lemma 4.1], so the flag dimension is \(17m^2+54\).

**Step 3: the three excess tangent directions.** The normal bundle of \(S\) in \(\mathbb P^5\) is \(\mathcal O_S(2h)^{\oplus3}\). For \(m\ge2\),
\[
N_{S/\mathbb P^5}(E-C)\simeq\mathcal O_S((1-m)D)^{\oplus3},
\]
whose first and zeroth cohomology vanish by Step 1 and negativity. As \(D\cdot E=0\), the exact sequence
\[
0\to N_{S/\mathbb P^5}(-C)\to N_{S/\mathbb P^5}(E-C)
\to\mathcal O_E^{\oplus3}\to0
\]
implies \(H^0(N_{S/\mathbb P^5}(-C))=0\) and \(H^1(N_{S/\mathbb P^5}(-C))\simeq\mathbb C^3\). The obstruction map for the Hilbert flag is surjective as in [1, Lemma 4.6], because \(\delta_{\mathcal O_S(C)}=m\delta_{\mathcal O_S(E)}\neq0\) in characteristic zero and \(H^1(\mathcal O_S(C))=0\). Consequently the differential from the smooth flag scheme to the Hilbert scheme of curves is injective and has cokernel \(\mathbb C^3\). The ambient Hilbert tangent dimension is \(17m^2+57\).

**Step 4: primary obstructions persist at the endpoint.** Nasu's pole-deformation theorem [1, Theorem 1.2] is independent of \(m\). His argument in [1, Proposition 4.7] shows that every tangent direction outside the flag tangent is obstructed if restriction preserves the nonzero class of a pole deformation. The only additional asymptotic input used there is \(H^1(N_{S/\mathbb P^5}(3E-C))=0\). Indeed,
\[
N_{S/\mathbb P^5}(3E-C)\simeq
\mathcal O_S(2E-(m-1)D)^{\oplus3},
\]
so the vanishing established in Step 1 provides the required injectivity for every \(m\ge2\). Thus the full obstruction argument of [1, Proposition 4.7], not merely its dimension computation, applies throughout this effective range. Its component criterion [1, Lemma 2.11] proves that the image of the smooth flag family is an irreducible component of the reduced Hilbert scheme, generically nonreduced with tangent excess three.

For clarity about the component dimension, quadrics containing \(C\) are precisely the three independent quadrics defining \(S\). Indeed, the extra quadrics would give sections of \(\mathcal O_S(2h-mD)\), which has no sections because its intersection with \(h\) is \(16-17m<0\). Hence \(S\) is uniquely recovered from \(C\). Any line \(E\) on the recovered K3 surface is rigid (normal bundle \(\mathcal O_E(-2)\)) and its projective Fano scheme of lines is finite. Consequently the flag incidence map has generically finite fibres and the image dimension is exactly \(17m^2+54\), agreeing with the obstruction criterion.

**Step 5: numerical invariants.** The intersection equalities \(C\cdot h=17m\) and \(C^2=34m^2\), together with adjunction on a K3, give \(\deg C=17m\) and \(g(C)=17m^2+1\). Substitution \(m=2\) gives \((\deg C,g(C))=(34,69)\), component dimension \(122\), and general Hilbert tangent dimension \(125\).

## Verification
The included `artifacts/verify_target.py` performs reproducible exact integer checks of the intersection pairing, the divisor identities used in the vanishing reductions, the Hilbert-component dimension and degree/genus formulas for the whole range, and the endpoint calculations. Its computations do not replace the algebraic-geometric vanishing theorems or the nonstandard deformation-obstruction theorem explicitly invoked above. The proof of infinite validity is the symbolic argument in Steps 1--5, not finite enumeration.

## Relationship to prior work
Nasu [1, Theorem 1.1] proves generic nonreducedness of these components for **sufficiently large** \(m\), under a characteristic restriction; the proof of [1, Lemmas 4.3, 4.6 and Proposition 4.7] uses eventual vanishings. The result here supplies the missing effective vanishing at \(m=2\) and proves their applicability for all \(m\ge2\) over \(\mathbb C\); it does not claim a new obstruction mechanism. Nasu's earlier del Pezzo-surface construction [2] concerns curves in \(\mathbb P^4\) on intersections of two quadrics and does not imply the claim for K3 surfaces in \(\mathbb P^5\). Earlier general deformation criteria involving K3 surfaces or cubic surfaces likewise do not provide this effective range for the specific triple-quadric family.

## Limitations
The proof is over \(\mathbb C\), not in arbitrary positive characteristic. The bound \(m\ge2\) is the first multiple handled by this argument, not a proof that the case \(m=1\) is generically reduced or impossible. It does not determine scheme-theoretic multiplicities or all components with the same degree and genus. Publication priority beyond the inspected sources has not been independently certified.

## References
[1] H. Nasu, *Obstructions to deforming space curves lying on a complete intersection of quadrics*, arXiv:2610.30962v1 (first public 22 October 2026), §§2.1--2.4 and 4, especially Lemmas 2.3, 2.11--2.12 and 4.1, 4.3, 4.6, Proposition 4.7 and Theorems 1.1--1.2. https://arxiv.org/html/2610.30962v1

[2] H. Nasu, *Obstructions to deforming space curves lying on a del Pezzo surface*, arXiv:2501.15788v1 (2025). https://arxiv.org/abs/2501.15788
