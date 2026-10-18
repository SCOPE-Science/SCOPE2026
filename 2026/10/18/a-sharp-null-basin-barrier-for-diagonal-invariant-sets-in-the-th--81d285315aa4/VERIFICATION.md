---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and proof boundaries

Run `python check_transverse.py` using Python 3 and SymPy. The checker reports 4,050 exact symbolic/rational identities in six parameter choices and the four open sign sectors. Specifically, it checks the branch determinant, diagonal block characteristic factorization, exact finite nonlinear center/normal recursions, and rational normal derivative products.

The proof of the measure-zero attraction basin is analytic: (i) any asymptotic approach to a compact diagonal set excluding the origin eventually avoids opposite assigned signs, since infinitely many opposite-sign visits force a subsequence to the origin; (ii) the exact transverse recurrence with \(|a|\ge1\) then forces finite entrance into the diagonal; (iii) piecewise affine invertibility makes its finite preimage union a three-dimensional null set. The checker is supplementary and does not certify that infinite statement by enumeration.

The Lyapunov-spectrum statement is conditional on existence of an ergodic invariant probability supported on the diagonal and charging no derivative switching points. It follows from invariant tangent/normal splitting and the bounded finite-branch derivative cocycle. No physical measure, chaotic attractor, or crossing behavior at the excluded origin has been established. Independent audit has not been performed.
