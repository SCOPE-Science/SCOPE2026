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
# Reproducible finite verification

Run `python verify_landau_disk.py` with `mpmath`. The checker integrates the diagonal Gaussian energy for small mode indices, checks the elementary closed eigenvalue formula and adjacent-gap factorization for many radii, verifies the integer triple ties and strict gamma half-mass inequality for integer indices, and independently maximizes the first 75 eigenvalues for 33 fixed/deterministically generated radii. At 60-digit working precision, the actual replay reported **PASS: 1648 deterministic checks**.

This finite test does not prove a global maximum over infinitely many modes or infinitely many radii. The proof in RESULT.md supplies the infinite argument using exact sign diagrams, strict gamma median inequality, and an explicit tail cutoff comparison. Exact identities were symbolically reconstructed independently of the numerical output. There is no independent external review or certification.
