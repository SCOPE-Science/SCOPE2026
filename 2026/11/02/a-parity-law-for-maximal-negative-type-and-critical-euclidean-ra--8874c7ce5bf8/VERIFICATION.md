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

# Verification record

The standalone program `check_wheel.py` uses only standard Python and deterministic seed 20261026. Running `python check_wheel.py` completed **10,009 checks**. It directly evaluates the powered-distance matrix quadratic form and checks its invariant-subspace formula using exact rational inputs; enumerates all Fourier frequencies for wheel rims from 4 through 200; compares the claimed global minimum against the radial direction; evaluates critical exponents and parity; and computes sharp sine/cosine witness Rayleigh quotients directly from pairwise graph distances.

Finite loops do not establish statements for unbounded dimension or arbitrary real exponents. The universal proof is the block Fourier diagonalization and analytic radial-dominance inequality in RESULT.md. Real-number calculations involving cosines have floating-point tolerance and are only corroborating checks. Source-inspection limitations, especially inaccessible 1990 metric-transform full text, affect originality rather than the reconstructed correctness proof.
