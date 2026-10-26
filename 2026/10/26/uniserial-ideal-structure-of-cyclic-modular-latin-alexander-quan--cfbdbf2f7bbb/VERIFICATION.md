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

The complete proof is in RESULT.md. An exact independent finite check within this package is `verify.py`: run `python verify.py` from the extracted directory with standard Python 3. It prints three `CHECK_OK` lines for the cyclic groups of orders 3, 5, 9 and multiplier 2. For order 3 it enumerates all 28 vector subspaces and checks left and right ideal closure; for each example it checks all predicted ideal-chain members and the ranks of every ideal product.

The general result is proved by invertible group-ring transport, reduction of every one-sided ideal to an ordinary group-ring ideal, and classification of ideals of `K[z]/(z^m)`. The finite checks are not an exhaustive proof across all fields or parameters. The source comparison is a self-review only; no independent audit, external certification, or complete literature exhaustiveness is claimed.
