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

# Verification of the phase-ensemble identity

Run `python3 verify_magic_phase.py` using the Python standard library. The script computes the full fourth Pauli sum for all \(5^N\) choices of fifth-root phases for six probability vectors with \(N\in\{2,4\}\), including boundary support. Averaging over fifth roots is exactly equivalent to averaging independent uniform continuous phases for every fourth-order phase monomial (all nonzero exponents have magnitude at most four); numerical complex arithmetic introduces only floating error. It then tests the independently coded pair-orbit enumeration against the autocorrelation law for 450 fixed-seed probability vectors and eight flat cases. The verified output is:

`VERIFY_OK: 464 ensemble/orbit/flat-dimensional checks; six exhaustive fifth-root phase-grid ensembles`

The universal theorem is proved by the orbit count in `RESULT.md`; the finite checks are not substituted for an infinite-dimensional or all-parameter proof. This package contains no independent audit, no Lean formalization, and no external certification. The threshold bound is one-sided and is not a claim of full concentration.
