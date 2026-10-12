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
# Reproducibility and limits

Run `python3 verify.py` from the directory containing this file. The verifier uses only the Python standard library. It explicitly expands the defining sextic, verifies all 24 signed-coordinate permutations preserve the homogeneous degree-nine equation up to nonzero scalar, and computes orbit sizes of the 13 previously known singular points using exact Gaussian-integer coordinates. Its finite matrix tests demonstrate the lower-bound subgroup and orbit partition; the infinite-group upper bound follows from irreducible-component uniqueness and coefficient comparison in RESULT.md. The verification does not replace that proof or independently rederive the singularity basket supplied by the originating full text. No independent mathematical audit has been performed.
