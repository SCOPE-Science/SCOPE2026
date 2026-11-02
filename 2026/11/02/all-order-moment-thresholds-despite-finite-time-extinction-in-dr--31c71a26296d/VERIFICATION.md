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

The proof is self-contained in `RESULT.md`. An independent finite-case replay of the exact moment matrix is implemented in `verify_moments.py` using rational arithmetic. It checks every Bernoulli history at short horizons for several parameters and moment orders, plus exact determinant identities and waiting-time recursion. Those finite checks establish no independent proof of uniqueness or priority. The all-order claims depend on the binomial identity, strict primitive Perron monotonicity, and a retained-run lower bound given in the proof. No independent mathematical audit has been performed.
