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

The proof is symbolic and uniform in every prime \(p\) and integer \(\alpha\ge1\). The accompanying `verify_rank.py` is a separate finite exact-arithmetic consistency check, not an infinite certificate.

Run `python3 verify_rank.py` from the directory containing this file and the script. The script independently computes binomial coefficients for bounded row indices, compares with the digit transfer, forms the reachability vectors from prefixes \(\epsilon\), \(0^r\), and \(0^r(p-1)\) for \(1\le r<\alpha\), and forms the observation matrix from suffixes \(\epsilon\), \((p-1)^h\), and \(0(p-1)^h\) for \(1\le h<\alpha\). Exact rational elimination checks the two matrix ranks and direct kernel evaluations. Parameter grid: \(p\in\{2,3,5\}\), \(1\le\alpha\le6\). Expected output ends with `VERIFY_OK exact_rational_full_rank_cases=18 all_cases_passed=True`.

**Unproved limits of computation:** The finite grid does not independently establish the universal rank equality, which follows instead from the general reachability and observability proofs. No independent mathematical audit was conducted.
