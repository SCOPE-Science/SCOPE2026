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

# Reproducibility and verification

The program `verify_sunlet.py` uses only Python's standard library. Running `python3 verify_sunlet.py` produces the checks captured in `verify_sunlet_output.txt`.

The direct finite-state implementation updates every core vertex by bitwise majority of its two cyclic neighbors and its private leaf, and copies every core state to its leaf. Every state is tested for fixedness and two-step return independently of the symbolic double-cover enumeration. All \(2^{2n}\) configurations are exhausted for each \(3\le n\le10\), totaling \(1{,}398{,}080\) configurations.

A separate four-state transfer-matrix calculation verifies its exact polynomial identity and traces through power 40. Direct cyclic-word enumeration checks the no-singleton condition for \(3\le m\le16\), totaling \(131{,}064\) words. All computed counts agree with the stated formulas. The mathematical argument establishing the parity split and transfer identity for arbitrary \(n\) is contained in `RESULT.md`; no inference from finite enumeration to an infinite claim is made.

No independent audit has been performed.
