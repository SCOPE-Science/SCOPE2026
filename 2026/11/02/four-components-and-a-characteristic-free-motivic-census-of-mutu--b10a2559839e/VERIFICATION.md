---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The quadratic and trace polarizations give xy+yx=tr(x)y+tr(y)x−B(x,y)1 and tr(xy)=tr(x)tr(y)−B(x,y) without division by two. For nonzero norm, L_x is invertible by L_bar(x)L_x=N(x)I, since bar(x) is a linear combination of 1 and x and the algebra is alternative. For zero norm and nonzero trace, the two identities force y proportional to bar(x), which indeed annihilates x in both orders. For a nonzero pure null x, the polar identity forces tr(y)=0 since x and 1 are independent (a nonzero scalar has nonzero norm); then conjugation gives the reverse product from xy=0. The nilpotent L_x has rank at most 4; choosing B(x,z)=1 in L_bar(x)L_z+L_bar(z)L_x=I gives rank at least 4 because bar(x)=−x, also in characteristic two. Trace is nonzero on ker L_x by evaluation at xz, with trace −1. The mutual kernel therefore has dimension 3. The two quadrics are geometrically irreducible by polar ranks at least 8 and 6, and the punctured pure cone is smooth even in characteristic two: zero derivative forces u=v=0 and then its equation forces a=0. The rank-1 and rank-3 kernels over the two null strata are bundles of dimensions 8 and 9 respectively; the closures and two axes are incomparable (test a nonnull coordinate on each axis and nonzero first trace off both axes). This proves the component assertion for the reduced variety. The u=0 versus u≠0 affine-fiber strata give [Q]=L^7+L^4−L^3 and [P]=L^6; in the u=0 pure slice use its reduction a=0, not the nonreduced a²=0 scheme. Summing the four mutually exclusive first-factor strata gives 2L^8−[Q]+L([Q]−[P])+L^3([P]−1), which is the stated polynomial. Counting over extensions and applying the defining zeta exponential gives the stated rational function with the negative coefficients placed in the numerator. The inspected Python field/rank checker and recorded totals 1024, 35073, 426496 corroborate the three stated fields, not the geometry over arbitrary fields. No radicality of the original equations is assumed.

## originality

PASS

The retrieved Guterman–Zhilina original supplies effectively all mutual-annihilator fibers over the reals, not just selected graph examples. The real pointwise rank/fiber classification is therefore prior, as is the real projective pure-null incidence of Baez–Huerta. The supported distinct contribution is the characteristic-free geometric component and motivic classification of the full reduced affine pair variety, with the characteristic-two case and resulting extension counts and zeta formula. The earlier inspected arbitrary-field annihilator work excludes characteristic two and its closest formula has a component-norm hypothesis.

## value

PASS

The full simultaneous zero-product locus is a natural invariant of the split algebra, including beyond its classical pure-null geometry. A uniform decomposition detects a unique larger component and exhibits the distinct nonzero-trace component; characteristic two tests genuinely different algebraic behavior. The motivic class packages all finite-extension counts, with a short field-independent proof not requiring group-orbit analysis. This is a structural result, not a numerical rerun of a real relation graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
