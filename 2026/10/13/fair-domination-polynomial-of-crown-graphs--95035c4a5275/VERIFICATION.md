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

The theorem is proved symbolically from the exact selected-neighbor counts
\[
|N(a_i)\cap S|=|J|-\mathbf 1_{i\in J},\qquad
|N(b_i)\cap S|=|I|-\mathbf 1_{i\in I}.
\]
The exhaustive checker is an independent finite regression test of that proof structure. It constructs each crown graph directly for \(3\le n\le9\), enumerates every subset, evaluates the literal fair-domination definition, compares it with the claimed classification, and checks every coefficient of the closed polynomial. It also verifies the minimum value and its multiplicity and the central-trinomial total-count identity. For \(3\le n\le8\) it separately constructs the complement and checks the setwise complement equivalence.

Run command:

`python3 verify.py`

Observed output:

`VERIFY_OK n_range=3..9 subset_checks=349504 fair_sets=7877 classification_checks=349504 coefficient_checks=91 minimum_total_checks=21 complement_checks=87360 max_order=18`

The computation proves only the tested finite range. No finite enumeration is used to infer the all-\(n\) theorem; the infinite claim rests on the proof in `RESULT.md`.
