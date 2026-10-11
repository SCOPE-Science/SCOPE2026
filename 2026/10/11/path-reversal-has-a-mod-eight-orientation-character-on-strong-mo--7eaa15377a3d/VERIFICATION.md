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

# Reproducible checks and limits

Run `python3 verify.py` with Python 3 and its standard library; no external dependencies are required. The script checks the downward closure of full direction strings against the local forbidden-subword model for path lengths \(1\) through \(11\), the action of path reversal and the direct signed augmented simplicial Lefschetz trace for those eleven complexes, exact reduced mod-two homology via boundary-matrix elimination for path lengths \(1\) through \(10\), half-word signed counts through length corresponding to \(n=24\), and the closed recurrence for \(1\le n\le300\). Expected output begins `VERIFY_OK` and prints the number of cases by category.

These finite tests do not certify the full infinite theorem. The infinite step is the algebraically derived recurrence \(S_{h+1}=-S_{h-1}\), with base values \(S_0=1\), \(S_1=0\), combined with the published nonequivariant homotopy classification. The quotient-space assertion uses rational transfer for finite simplicial group actions.

The mathematical result was reviewed for correctness, originality, and value at the same-model level. Independent validation and independent audit have not been performed.
