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

# Verification notes

Execute `python3 checker.py` from the directory containing this document. The Python standard library suffices. The exact checker derives the 24 source masks, tests every one of 8192 states in the free eight-element sign-symmetry quotient, and evaluates both the autocorrelation and polynomial-square Parseval identities on every tested state. It confirms a minimum moment of 304, precisely four quotient winners, a moment gap to 336, and two disjoint 16-element orbits in the original 65,536-state binary domain. It also checks the orbit cardinalities under all enumerated rotations/reflections and sign modulations.

An inspection of the two displayed representative arrays separately finds their magnitude-three autocorrelation displacement pairs to be \((1,3),(3,-1)\) and \((1,-3),(1,3)\), with absolute dot products zero and eight. The complete proof is finite and does not rely on approximate floating-point checks. The previously published sharp scalar merit factor is not assigned novelty; specialized prior optimizer censuses may exist in historical sources not completely accessible here.

This record reflects same-model review only. No independent audit or external verification is asserted.
