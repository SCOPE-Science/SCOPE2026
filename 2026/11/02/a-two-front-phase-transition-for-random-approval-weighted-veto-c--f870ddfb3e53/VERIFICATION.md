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

The analytical proof treats all integer candidate counts \(m\ge2\) and all fixed probabilities \(0<p,q<1\). Its steps are an exact coalition-to-subset equivalence, finitely many strong-law limits, strict convexity, and one- or two-dimensional central limit theorems. The Gaussian correlation and strict/non-strict boundary conventions are computed explicitly.

Run `python3 PROOF_CHECK.py` in the directory containing this file. The checker includes direct enumeration of all 40,960 binary approval profiles over three finite parameter sizes and confirms equivalence of the literal blocking definition with the exact reduced test. It also checks 5,771 parameter grid cases for the endpoint maximum, and optionally runs seeded 30,000-draw multinomial simulations at three double-critical configurations using NumPy. Simulation is a diagnostic, not a proof of a limit.

The mathematical law is not an assertion about correlated approvals, heterogeneous rival acceptance rates or the composition of the veto core with another selection rule. No independent scientific audit has been performed.
