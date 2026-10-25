# Mathematical review

## Correctness — PASS

The discriminant has six distinct roots, while the rational elliptic source has six \(I_1\) fibers and one split \(I_0^*\) fiber at infinity; its Picard number is ten. Shioda–Tate and the tabulated \(D_4^*\) rational-surface lattice give torsion-free rank four. Four displayed sections satisfy the Weierstrass equation and, on every admissible hyperelliptic double cover, have distinct slopes at the point above infinity, no other mutual intersections and no intersection with the zero section. Shioda's height formula then gives \(2I_4\); degree-two height scaling and lattice determinants give exact index two. Finally, elimination of the generic constant coefficient \(c_0\) identifies the universal function field as a purely transcendental extension of \(\mathbb C(t)\), where an elliptic curve acquires no new rational points. These arguments prove the full generic group and lattice. The exact-arithmetic checker passed; it does not substitute for the geometric arguments.

## Originality — PASS, with residual risk

Li and Liu, *Examples of infinitely many \((-1)\)-curves with higher genus on elliptic surfaces*, first posted 27 May 2026, exhibit one non-torsion section and the twelve nodal fibers, but do not classify the Mordell–Weil group or provide an orthogonal rank-four subsystem. Oguiso and Shioda's 1991 Main Theorem, table row 9, classifies the rational elliptic **source** with root lattice \(D_4\), rank four and dual lattice \(D_4^*\): that antecedent is not claimed as new. The new specific conclusion identifies four explicit index-two sections on higher-genus base changes and the full lattice over the universal generic hyperelliptic coefficient field. Directed exact-parameter, model-equivalence and broader-coverage searches found no stated prior consequence for this family; absence of a matching record does not prove uniqueness. A derivation implicit in older elliptic-base-change literature or an unindexed table remains a risk.

## Value — PASS

The Li–Liu surfaces are a motivated newly constructed family, with \(\chi(\mathcal O_X)=1\), genus arbitrarily large, and infinitely many negative curves. An exact rank-four generic Mordell–Weil lattice upgrades existence of one non-torsion section to a precise intrinsic group invariant, exposes four independent generators on **all** admissible complex members, and separates generic rational rank from potential special-fiber jumps. This is a natural complete generic classification for a precisely defined geometric family, not an arbitrary numerical slice or routine recomputation of a known table. The contribution is specific: the general Shioda–Tate framework and rational-source lattice were known.

## Closest literature and limitations

Li–Liu: arXiv:2605.27926v1 (27 May 2026; v2 26 Aug 2026), Sections 2.2–2.3. Oguiso–Shioda: *The Mordell–Weil lattice of a rational elliptic surface* (1991), Main Theorem row 9 and height arguments. The full rank equality does not extend as stated to every complex specialization or to a geometric generic base after extending the coefficients; those ranks may jump. The standalone Python arithmetic test checks exact identities and small lattice arithmetic, not the global theorems.

Self-review: passed. Independent audit: not yet performed.
