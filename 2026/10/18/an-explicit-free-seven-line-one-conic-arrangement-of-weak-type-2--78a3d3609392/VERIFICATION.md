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

# Exact verification

The accompanying `verify.py` uses only the Python standard library. It computes canonical projective line intersections and checks that all 21 line pairs are represented by six double and five triple points; computes exact membership of the conic in four double and two triple points; checks the Hessian determinant and all seven quadratic discriminants; then checks that these six conic locations consume all 14 line–conic intersection incidences and give final \( (n_2,n_3,n_4)=(2,7,2)\).

It constructs polynomial dictionaries with integer coefficients, differentiates the degree-nine product, checks both quartic Jacobian syzygy identities exactly and verifies the full polynomial equality \(\det((x,y,z),P,Q)=-243F\). These are exhaustive finite algebraic identities for the specified formula, sufficient together with Saito's theorem for the claimed freeness.

The verifier was executed on the packaged script with successful `VERIFIED_OK` output. The proof is over \(\mathbb C\); no modular transfer, exhaustive classification of other realizations, or independent mathematical audit is claimed.
