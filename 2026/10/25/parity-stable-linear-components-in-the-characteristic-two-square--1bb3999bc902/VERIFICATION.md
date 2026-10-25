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

# Reproducibility
The included `verify_char2_derivations.py` uses only Python standard-library arithmetic. Run `python3 verify_char2_derivations.py` from the folder containing it. It constructs multiplication and derivations of \(k[t]/(t^n)\) directly, computes the complete derivation square on basis monomials, computes matrix ranks by field elimination, and compares against the proposed union of linear components.

The program enumerates both \(n=2m\) and \(n=2m+1\) for \(m=1,2,3,4,5\) over \(\mathbb F_2\) and for \(m=1,2,3\) over \(\mathbb F_4\) (sixteen cases). Observed counts for \(q=2\), \(m=1,2,3,4,5\), are respectively \(2,6,12,32,64\) at **each** parity; for \(q=4\), \(m=1,2,3\), they are \(4,28,112\). Every case checks the pointwise component condition, the predicted differential rank, and (for even length) the acyclic count. The exact success marker is `CHAR2_DERIVATION_SQUARE_ZERO_OK`.

These finite tests are not an infinite-family proof. The general result is obtained in RESULT.md from the necessary-and-sufficient coefficient equations and truncated valuations. All geometric assertions refer to reduced varieties; nonreduced scheme structures were not determined. Independent mathematical audit was not performed.
