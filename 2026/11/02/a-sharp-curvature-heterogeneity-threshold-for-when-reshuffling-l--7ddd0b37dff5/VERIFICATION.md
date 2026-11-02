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

# Verification

Install the declared SymPy dependency and run `python verify.py` in the directory containing the extracted files. The program proves exact algebraic identities using symbolic polynomial operations, counts real roots by exact Sturm sequences, isolates the two discriminant parameters using rational endpoints, bounds the common double-root location with rational interval arithmetic, and checks the explicitly stated stationary-error examples. The checker terminates with `ALL CERTIFICATES PASS` when all assertions are satisfied.

The mathematical argument in `RESULT.md` establishes the general interval topology by continuity between its exactly isolated singular and boundary events. This inference is analytical; finite numerical tests are illustrative only. There is no proof of any extension outside two scalar positive-curvature quadratics, the individually contractive stepsize range, or fresh independent permutations. No independent audit or external certification has been performed.
