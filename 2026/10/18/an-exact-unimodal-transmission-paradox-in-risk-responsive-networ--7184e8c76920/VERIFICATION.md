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

# Verification record

Run `python verify.py` from this directory with Python 3 and SymPy. The checker constructs an independent synchronous SIR state-transition enumerator from the edge list and computes the exact absorption polynomial for the canonical contact graph. It checks that the polynomial equals the analytically derived expression, that the expected case counts at transmission probabilities \(0\), \(4/5\), and \(1\) are correct, and that the derivative transformation has exactly one Descartes sign change. It checks the exact social-mixing wedge at selected rational interior parameters and the connected-family gate inequalities over a large finite sample (not as an infinite proof).

The analytical proof, not a bounded computational search, establishes the family statement for every integer \(m\ge3\). The exact state enumeration is complete for the eight-vertex graph only. This is a same-model reproducibility check. No independent scientific audit has been performed.
