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

The mathematical argument in `RESULT.md` proves the infinite statements. The independent-of-proof arithmetic checks are implemented in `verify.py`, which uses only the Python standard library. Run `python3 verify.py` and compare the resulting JSON with `verification_output.json`.

The recorded run passed **1368 assertions**: positivity and normalization of finitely supported truncated-exponential laws; their factorial moments; exact Charlier generating coefficients for \(2\le m\le10\) and \(1\le n\le20\); and high-precision finite sampling computations for \(m=2,3,4\), \(n=20,40,80\). Each displayed finite value approaches the limit in the theorem. The checker does not prove that a sequence converges for all orders and all sample sizes, and numerical agreement is not treated as an independent proof.

Essential proof checks reconstructed analytically: Poisson–Charlier orthogonality; finite-support Poisson \(L^2\) integrability; the expanding-disk Gaussian majorant and exponentially vanishing complementary tail; strong \(L^2\) convergence of the likelihood ratio; uniform integrability in the KL expansion; and positivity of each truncated exponential probability mass.

No independent mathematical audit or external certification has been performed.
