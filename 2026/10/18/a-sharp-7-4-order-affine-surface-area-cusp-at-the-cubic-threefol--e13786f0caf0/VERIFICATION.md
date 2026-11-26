---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For h=1+εxyz, opposite support values sum to 2. Along an oriented great circle the operator ∇²_S(xyz)+(xyz)I kills mode 1 in the directional quadratic form and multiplies mode 3 by −8. The latter has amplitude (1/4)∏√(1−w_i²), where w is the circle normal; equality in AM–GM requires w_i²=1/3. On the representative plane x+y+z=0 there is no mode 1 by the cyclic permutation symmetry, and critical nonzero extrema of xyz on the unit circle have two coordinates equal (by the multiplier equations). Its three positive maxima there and their sign-transforms on the four planes give exactly the twelve positive-product signed permutations of (2,1,1)/√6. They attain the negative extremal radius derivative, proving the sharp cutoff. Independently, for the ambient Hessian H of xyz, tr(H|u⊥)=−6xyz and det(H|u⊥)=uᵀ adj(H)u=4s−1. Shifting by −2xyz I yields the stated D. The co-radius is 3/4 at a contact. In the supplied orthonormal chart I independently truncated the products defining q and s through degree two, replacing the radial factor by 1−(ξ²+η²)/2; this gives D*=27ξ²/8+9η²/16 and −∂εD=√6/3 at the contact. The cutoff leaves D comparable to δ+ξ²+η² there. Gauss parametrization gives power p=3/4. In F'' the term with D^(p−1) remains integrable; the squared first-variation term, after rescaling by √δ, is dominated by (1+|v|²)^(−5/4). Each contact contributes −pπa^(p+1)/√(BC) times δ^(p−1), with a=√6/3, B=27/8, C=9/16. D^(p−1) also controls endpoint first-derivative convergence, so two integrations give precisely the stated negative term, with magnitude 10.9651623547706914; the divergence precludes a finite endpoint second derivative. The result refers to the one-sided ordinary affine surface area in dimension three. The frozen verification script was read, not executed; an independent exact polynomial calculation corroborated the Hessian and coefficient, while the analytic argument proves the limit.

## originality

PASS

Credit only the one-sided affine-surface-area cusp, its exact coefficient and the corresponding derivative singularity. The family, sharp convexity threshold and contacts have prior coverage. No inspected source states or mechanically implies the exact cusp.

## value

PASS

This explicit constant-width family is independently motivated by its exceptional projection symmetry. The cusp identifies exactly how affine surface area loses regularity at its curvature degeneracy and adds a normalized signed coefficient and blow-up, rather than merely exhibiting endpoint singularity or repeating the known convexity transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
