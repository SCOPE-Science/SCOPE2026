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

The direct mathematical proof is in `RESULT.md` and uses two standard path hitting-probability identities and one conditional edge-exchangeability identity. No computational experiment is used to prove the universal conditional law.

`python verify_exchangeable_cycle.py` completed with the exact output `PASS 187 exact rational consistency assertions; no infinite proof inferred`. It checks direct absorbing-chain linear-system solutions separately from the closed formula, full edge-permutation averages, multisets with repeated values, and the explicit one-defect law, using only standard-library exact fractions.

The verification program tests finitely many integer cycle sizes and rational environments. It does not and cannot certify the full quantifiers, priority over all published literature, any extension to arbitrary nonreversible random walks, or any external independent audit. The 2000 nonuniform weighted-cycle paper was only accessible by abstract; that remains a specific scientific originality limitation.
