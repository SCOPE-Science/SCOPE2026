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

# Verification protocol and scope

Execute `python3 verify.py` in the directory containing this document and the companion script. It uses only Python's standard library; no external files are required.

The deterministic script checks 72 exponent/weight parameter pairs, 15,840 random positive vector upper bounds for the alternating configuration, 66 algebraic lower-gap identities for non-Hilbert exponents, and 660 Hilbert-case tests. The numerical optimizer is a golden-section search in the logarithm of the positive ratio, followed by explicit evaluation of the trial-vector identities. The check reports:

`PASS | cases=72 alt_random_bounds=15840 constructive_gap=66 Hilbert_bounds=660`

For \(p=4\), \(a=3\), \(b=1\) the estimated alternating optimum is \(2.079009579543\) and the constructive adjacent lower bound is \(2.191604738458\). At \(p=2\) the grouped value is \(\sqrt5\) and the alternating value is \(2\). The script exercises a finite set of cases only; these tests cannot establish uniqueness, infinite-dimensional claims, or the global all-parameter inequality without the preceding analytic proof. The exact nonlinear adjacent radius is not computed.
