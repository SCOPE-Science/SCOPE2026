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

# Verification and reproducibility

Run `python3 verify.py` using a standard Python 3 installation; no third-party packages are required. The script independently builds each finite operation table, checks all nonempty subsets for closure when \((p,f)\) equals \((2,1)\), \((3,1)\), and \((2,2)\), and compares the complete size distributions to the Möbius formula. It additionally checks nonnegative span counts, the affine-support decomposition identity \(\sum_t p^{f-t}{f\brack t}_p a_{t,j}(p)=\binom{p^f}{j}\), and one full-set subquandle at further field parameters. Output ends with `ALL_UNIPOTENT_SUBQUANDLE_CHECKS_PASSED` on success.

The script represents the additive group of \(\mathbb F_{p^f}\) by coordinate vectors in \(\mathbb F_p^f\); field multiplication is irrelevant for this operation. Its exhaustive stage tests \(2^4-1\), \(2^9-1\), and \(2^{16}-1\) nonempty subsets, respectively. The larger cases check identities only, not every subset. These computations corroborate finite instances and cannot themselves certify the infinite-domain theorem; the proof is deductive.
