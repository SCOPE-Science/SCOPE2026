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

The infinite proof is analytic. The key general implication is checked directly: if fewer than \(\eta(G)\) edges are bichromatic, every color class has size \(1\) or \(N-1\); three classes would force the union of two singleton classes to have at least \(\eta(G)\) bichromatic boundary edges. Thus every nonmonochromatic coloring in this range is exactly a singleton-versus-complement coloring.

For crowns, the proof establishes \(\eta(\operatorname{Cr}_n)=2n-4\) by a direct lower bound on every nontrivial vertex cut and an adjacent-pair witness. This is valid for all \(n\ge4\).

`verify.py` independently performs three finite checks: exhaustive nontrivial subset cuts for \(4\le n\le9\); exhaustive unlabeled color partitions for \(n=4,5\); and arithmetic identity checks through \(n=100\). Its replay output is:

`ALL CHECKS PASSED; restricted_cut_orders=4..9; subset_checks=349272; partition_orders=4,5; set_partitions=120115; symbolic_orders=4..100`

Finite enumeration is corroborative only. It is not used to infer the theorem for unbounded \(n\) or arbitrary graphs. The result does not determine lower \(k\)-defect values below the sharp crown threshold.
