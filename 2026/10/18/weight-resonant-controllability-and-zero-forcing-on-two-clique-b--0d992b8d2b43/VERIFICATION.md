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

## Reproduction

Run `python3 verify.py` with Python 3.9 or later. No external packages are required. The script enumerates every vertex subset in 36 positive integer-weighted two-clique bridge graphs, with each clique size between 3 and 5. It directly forms each weighted Laplacian and the associated Kalman matrix, tests matrix rank using modular Gaussian elimination, independently computes graph zero forcing, and compares the resulting cardinality enumerators with the stated closed form.

## Recorded check

`VERIFY_OK 37704 finite assertions across 36 weighted cases (3<=p,q<=5), using exact prime-field ranks`

The modular computations are corroborative tests, not a real-field symbolic proof and not exhaustive over all clique orders or positive real weights. The proof in `RESULT.md` gives an exact real-field PBH characterization for all specified parameters, including the sole exceptional eigenspace at resonance and independence of positive bridge conductance.

## Scope of unperformed checks

No external independent audit or theorem-prover certification has been performed. Literature comparison is limited to cited, inspected materials and research-record searches. No generalization to heterogeneous weights inside a clique or multiple bridge edges is asserted.
