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

The proof is analytic and valid for every odd integer \(n\ge3\). The finite program is a separate stress test. It builds the crown graph from the rule that \(a_i\) is adjacent to \(b_j\) exactly when \(i\ne j\), then tests every vertex subset directly against the definition of odd independence. It computes \(\alpha_{\mathrm{od}}\) by maximization and computes the minimum number of odd-independent color classes by exact bitmask dynamic programming, without using the theorem's formulas.

For \(n\in\{3,5,7,9\}\), the replay checks: \(\alpha_{\mathrm{od}}=2\); \(\chi_{\mathrm{so}}=n\); exactly \(n\) maximum odd independent sets; and one optimal unlabeled partition, namely the deleted matching pairs.

The computation is finite and does not prove the infinite claim; the universal proof in `RESULT.md` supplies that step.
