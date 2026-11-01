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
# Reproducibility and verification

Run `python3 verify_john_hexagon.py` with Python 3 and SymPy installed. This standalone script checks 104,412 deterministic symbolic and numeric statements and prints a PASS line. It constructs each tangent hexagon from its supporting normals, integrates the Euclidean polygon areas independently by the shoelace rule, constructs the polar from the normals, verifies nonnegative John weights, and independently checks the boundary optimization identities and local expansions. All test samples are generated from a fixed pseudorandom seed. The equality example is verified symbolically.

Exact mathematics: the global result uses the reduction to three John-compatible gaps, analytic stationary-point exclusion, and exact boundary optimization. The lower endpoint uses the published Aczél–Fuchs/Florian area-sum inequality. An infinite-dimensional claim is not inferred from testing. The proof does not apply without the assumption that all six facet lines are tangent to the John ellipse.

External mathematical verification: not performed. Historical priority: not definitively established.
