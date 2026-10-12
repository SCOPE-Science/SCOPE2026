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

The analytic proof establishes the claim for every integer \(n\ge3\). The computational check is deliberately finite and is not used to infer the infinite theorem.

`verify_total_bondage_crown.py` performs three independent checks from the definitions:

1. For \(n=3,4,5\), it exhausts every crown-edge deletion set of size strictly below \(2n-3\), discards deletions that create isolated vertices, computes both shore-cover numbers, and confirms that total domination never rises above four.
2. For \(n=3,4,5,6\), it solves the finite weighted pair-cover problem exactly and obtains minima \(3,5,7,9\), matching \(2n-3\).
3. For every \(3\le n\le30\), it constructs the proof witness, verifies exactly \(2n-3\) deletions, checks nonisolation, and computes a total domination number strictly above four.

Replay output:

`ALL CHECKS PASSED; exhaustive_orders=[3,4,5]; deletion_subsets_below_target=61276; lemma_orders=[3,4,5,6]; lemma_minima=[3, 5, 7, 9]; witness_range=3..30`

Unproved by computation: no finite replay is claimed to exhaust orders above five for the lower bound. Those orders are covered only by the written inductive lemma and the analytic reduction.
