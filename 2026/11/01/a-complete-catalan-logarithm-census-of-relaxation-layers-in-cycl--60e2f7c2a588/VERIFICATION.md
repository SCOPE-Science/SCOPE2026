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

# Reproducible checks and boundaries

Invoke `python3 verify.py` with Python 3. The script independently updates each labelled binary ring state and detects the first time its orbit reaches a repeated state; it does not assume that the first time a block disappears is the first periodic time. It computes Catalan coefficients by exact binomial arithmetic and extracts the formal logarithm by an independent finite sum with rational coefficients. The resulting integer counts are compared in every mass sector for all \(2\le n\le15\) and for every permissible transient cutoff. It also checks the ballot-preimage equivalence locally for lengths \(2\) through \(12\). The reference output is preserved as `verification_output.txt`.

The complete verified instance family contains \(65,532\) initial states, \(308\) exact CDF comparisons, \(78\) maximal-layer comparisons, and \(5,460\) local preimage windows. These finite checks do not establish the theorem for arbitrary ring sizes, and the proof uses the known local-preimage characterization plus the new cyclic atom-decomposition and coefficient count. Independent scientific auditing has not been performed.
