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
# Reproducibility and scope

Run `python verify_ramanujan_min.py` using Python 3.10 or later. The verifier uses only standard-library exact integer and rational arithmetic.

Its complete enumeration covers the moduli \(2\) through \(163\) and every nonprincipal real Dirichlet character at each modulus, not just primitive characters. The square-class quotient is computed from units, and all nontrivial dual characters are generated; direct multiplicativity assertions provide an additional consistency check.

The expected certificate reports 433 characters, 173 even and 260 odd; 85 odd characters have \(B_{1,\chi}=0\) and 175 have nonzero \(B_{1,\chi}\). It reports the sole strict failure at 163 and the unique sharp lower-range ratio at 67. All root-location decisions follow from the exact reciprocal-quadratic criterion in the proof, not floating root approximations.

This verifies a finite minimality theorem, not the existence of a universal bound beyond the stated range. The modulus-163 counterexample itself is due to Pathak (2026), not to this work. The work has received no independent audit.
