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
The general statement was checked algebraically from the four published one-braid inequalities. The proof separates the exact feasibility threshold, the low-\(q\) active constraint, the half-sum bound in the high-\(q\) regime, and the parity obstruction when \(q\equiv2\pmod4\).

`artifacts/verify_one_braid_closed_form.py` performs an independent finite replay. It enumerates every feasible integer pair for \(2\le p\le30\) and \(p<q\le150\), compares the true enumerated optimum with the formula, verifies the explicit witnesses, and reproduces the published special cases. The observed output is:

`VERIFY_OK exhaustive_pairs=3886; p<=30; q<=150; source_tables_and_corollaries_match`

The replay is not used as an infinite proof. No independent audit or external validation has been performed.
