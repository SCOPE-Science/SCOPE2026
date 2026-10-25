---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For a real signed measure on the center and m finite leaves with positive arm lengths rho_i, the unit ball is exactly the constraints |f_j|<=b, |f_i-f_0|<=rho_i t, b+t<=1. Leaf-to-leaf Lipschitz inequalities follow from paths through the center. Optimizing each leaf according to mass sign, introducing x=(b-c)/t and y=(b+c)/t when t>0, gives the exact fractional objective (M(y-x)+2P(x)+2Q(y))/(2+x+y). Ratios of affine functions are monotone or constant between arm-length knots; tail limits are bounded by |M|, also attained by constant potentials when M!=0. This yields the finite max for all masses, zero masses and repeated arm lengths. The fractional inequality against r separates into Phi_+(r)+Phi_-(r)-2r<=0; the two maximizations are concave capped-linear pieces with switchpoints at sorted signed tail masses. Their negative slope plus root interpolation proves the stated O(m log m) real arithmetic comparison complexity, not a bit-complexity bound. Independently I solved 24 direct primal LPs with all original f_i,b,t variables; all agreed with the separately coded knot expression to at most 3.6e-15. This checks bounded examples, not the full theorem; its all-m proof is the preceding exact reduction.

## originality

PASS

The final claim, not its title or shared elementary ingredients, was compared against statement-level prior implications, published records and highly relevant primary literature. The named check objects and actual inspections below support best-of-knowledge originality, with inaccessible material separately identified as residual risk.

## value

PASS

Arbitrary unequal positive arm lengths and nonzero signed total mass are natural finite metric-star inputs for bounded-Lipschitz/Dudley dual optimization. The exact knot support identity reduces an arbitrary finite LP to explicit active cap pairs, while the monotone root algorithm improves a quadratic enumeration to near-linear arithmetic after sorting. This precise structural simplification and its attainers can inform discrete transport and signed-measure stability calculations and is neither just the two-point example nor a normalization substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
