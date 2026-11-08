---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the precise tournaplex F_t={nonempty 11-vertex masks with at most t cyclic triples}. Independently enumerated all 165 triples, found 55 cyclic, 2,047 nonempty faces and exactly 17 threshold values 0,1,2,3,4,5,6,7,8,11,12,13,18,19,28,40,55. Fresh signed finite-field reductions of all 2,047 filtration columns independently matched complete supplied F2 barcode (727 positive-length intervals, 20 types) and F3 barcode (726 intervals, 18 types), both with 1,023 finite simplex pairs, all bars finite after reduced H0. Fresh sparse integral unit-pivot Smith reductions for every degree at all 17 thresholds checked all rank-one residual 2×2 minors and gcd invariant; the only nonunit factors are 2 in ∂3 at level 0 and 2 in ∂6 at level 12. All free ranks, mod-2 UCT and F3 ranks agree with the three exact CSV files. The independent replay code `/mnt/data/test_scope_3.py` exited with both PALEY11_INDEPENDENT_PERSISTENCE_CHECK_OK and PALEY11_INDEPENDENT_INTEGRAL_SMITH_CHECK_OK. This is exhaustive for 11 vertices; no integral interval decomposition or family generalization.

## originality

PASS

Best-of-knowledge PASS for complete levelwise integral homology and full F2/F3 motif persistence after the already known level-zero Moore-space result. Govc–Levi–Smith defined the motif-count filtration but did not tabulate Paley-11; Govc 2020 already contains the 11-vertex doubly regular tournament zero-stage Z/2 in H2 (and Z10 free), explicitly not novel. Neither source implies the later second torsion event at level 12 nor the complete inclusion-map barcodes.

## value

PASS

The precise recurrence and disappearance/reappearance of integral 2-torsion in a canonical doubly regular tournament distinguishes filtration stages invisible in its previously classified unweighted directed flag complex. A complete reproducible pair of coefficient-dependent barcodes and all integral stage invariants provide a natural finite benchmark for directionality persistence, including UCT-driven crosschecks; intrinsically useful exact finite classification, not arbitrary slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
