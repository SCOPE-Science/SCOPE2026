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

Execute `python verify.py` using Python 3.9 or later. The program ran successfully with exact rational arithmetic. Its checks reconstruct both inverse branches, their affine transfer formula, the closed Poisson matrix, and the diffusion identity for \(2\le M\le30\), with the direct branch test for \(2\le M\le9\). The proof in `RESULT.md`, not the finite tests, verifies every integer \(M\ge2\). The standard stationary reverse-martingale central limit theorem is invoked once the bounded corrector has been established; the test program does not attempt to certify that probabilistic theorem. Independent audit has not been performed.
