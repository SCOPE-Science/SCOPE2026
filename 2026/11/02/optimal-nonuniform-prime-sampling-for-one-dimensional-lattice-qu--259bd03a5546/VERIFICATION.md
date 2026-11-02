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

Run `python3 verify.py` with Python 3.10 or newer. No external dependencies are required.

The verifier uses exact rational arithmetic for every normalized kernel entry and sampling weight at each integer \(2\le n\le100\) and every integer \(s\in\{2,3,4,5\}\). It tests the exact quadratic identity, positivity, normalization, strict monotonicity for nontrivial prime sets, uniform-vs-optimal separation, direct least-common-multiple arithmetic and sampled competitor laws. It also checks Fourier partial-sum inequalities at two designs and three truncation levels, and the exact \(\sqrt{7/6}\) and \(\sqrt{217/120}\) constants.

The complete executable reports `PASS 402 exact finite-design groups plus finite-Fourier and asymptotic checks`. These checks independently catch arithmetic or transcription errors but do not exhaust the infinitely many \(n\) or all real \(\alpha>1/2\). Those quantifiers are justified by the analytic argument in `RESULT.md`. The prime number theorem is used as a standard analytic input and is not re-proved or computationally certified here. External independent audit has not been performed.
