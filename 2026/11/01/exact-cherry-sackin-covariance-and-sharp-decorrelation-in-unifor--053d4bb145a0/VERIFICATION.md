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

The supplied `verify.py` uses only Python standard-library modules. Running `python verify.py` checks exact enumeration of all ordered full binary trees with 2 through 11 leaves, independent bottom-up recurrences for total number of trees, cherry count, Sackin sum, their mixed moment and cherry factorial second moment through 120 leaves, the covariance sign through 200 leaves, and four large-size checks against the proved covariance asymptotic. The completed invocation reported: `PASS: 868 independent finite exact and asymptotic checks`.

The enumeration and bottom-up moment calculations are finite cross-checks, not infinite proofs. The manuscript derives the all-size identities through formal generating functions, proves the sign comparison using exact adjacent ratios, and cites an independent published Sackin variance asymptotic for the sharp correlation constant. An independent external audit has not been performed.
