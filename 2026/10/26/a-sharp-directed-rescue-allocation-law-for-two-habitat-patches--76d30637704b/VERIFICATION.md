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
# Verification details

The proof uses a three-equation absorbing continuous-time Markov backward system. Its determinant is \(e_1e_2(C+e_1+e_2)>0\), and differentiation of the exact weighted solution produces a strictly negative second derivative. These exact identities establish the theorem for every parameter in the stated domain.

Run `python3 two_patch_verification.py` using a standard Python 3 installation; no third-party packages are required. Its fixed-seed executable checks 5,000 random parameter sets against a separately implemented 3-by-3 Gaussian elimination, the quadratic regret formula and feasible-interval maxima. It also checks integer-rational benchmark instances using `fractions.Fraction`. The recorded outcome in the newly built package was PASS.

The computational checks are necessarily finite and do not independently prove a universal theorem, establish originality, certify empirical realism, or constitute an independent audit. Scientific limitations and the restricted historical source are described in RESULT.md and REVIEW.md.
