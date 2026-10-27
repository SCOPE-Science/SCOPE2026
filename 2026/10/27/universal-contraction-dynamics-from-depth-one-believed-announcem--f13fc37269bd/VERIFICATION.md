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

# Reproducibility and scope

Execute \(\texttt{python3 checker.py}\) using an ordinary Python 3 interpreter and the bundled file. It implements independent Kripke evaluations for the fixed valuation/type family and checks semantic outputs against finite truth tables, positive-map counts and explicit sharp-orbit witnesses. The observed output is \(\texttt{ALL\_CHECKS\_OK 7280}\).

The check includes all \(16\) contracting maps on a two-type carrier, sampled contracting maps for four types, exhaustive monotonicity enumeration on at most three type coordinates, Dedekind counts through three inputs and direct sharp-orbit simulations through sixteen types. Finite exhaustive enumeration does not prove the infinite-parameter theorem: the proof rests on the support-test normal form, coordinatewise monotonicity and the explicit orbit construction in RESULT.md.

No separate human or independent scientific audit is represented by these checks. The authoring review is solely self-reviewed; correctness and priority require any future independent assessment to be treated separately.
