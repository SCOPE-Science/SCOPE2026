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

The general argument is a self-contained paper proof: incidence of first/second occurrences, prefix-set cut equivalence, direct-sum component count, unique periodic exception, ordinary generating function, and permutation decomposability asymptotic.

Reproduce standalone finite checks with `python3 checker.py` from the same directory. The checker exhaustively generates \((2q)!/2^q\) distinct double-occurrence words for \(q=2,3,4,5\), a total of \(116016\). Every candidate rotation is evaluated by greedy complete-alphabet arches; for \(q\le4\), a second direct subsequence enumerator validates the arch test. Every qualifying word is grouped under an explicit minimum-rotation canonicalization. The complete observed labeled and necklace distributions by witness cut-pair count match the permutation-component recurrence exactly. The checker prints `CIRCULAR_PERMUTATION_ARCH_PASS words= 116016` after all checks succeed.

Observed totals: \((L_2,N_2)=(6,2)\), \((L_3,N_3)=(78,14)\), \((L_4,N_4)=(1704,216)\), and \((L_5,N_5)=(55320,5544)\). Larger-size predictions, such as \((L_6,N_6)=(2481840,206880)\), follow from the proven formula but are not exhaustively enumerated here.

Finite tests do not prove all-alphabet results, and no machine-checked or external independent proof certification is asserted. Source-inspection conclusions remain subject to discoveries in other literature.
