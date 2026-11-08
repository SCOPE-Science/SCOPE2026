---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For simple C_3 □ C_n, n>=3, four distinct neighbors exclude the vertex itself. With pair states (a,b), 0/1 transfer edges (a,b)->(b,c) encode each vertex having at least two same-colour neighbors; closed length-n paths count labelled synchronous MM fixed points exactly once. Independent 64-state integer characteristic polynomial agrees with the stated 8-factor decomposition; the sole eigenvalue of modulus 3 is 3 by direct coefficient bounds/Rouche on each remaining factor, proving A_n~3^n. In RMM a minority vertex in any mixed three-vertex column has two disagreeing vertical neighbors, making strict 3-of-4 agreement impossible, so absorbing columns are monochromatic; the no-isolated-letter cyclic-word transfer has spectrum roots of z²-z±1, yielding B_n=phi^n+phihat^n+2cos(n pi/3)~phi^n. Exact independent direct enumeration n=3,4,5 confirms A_n=32,94,218 and B_n=2,6,12. This does not classify non-singleton recurrent classes.

## originality

PASS

The pre-existing one-dimensional majority/circular no-isolated-symbol enumeration is acknowledged and not claimed original. The surviving claim is the explicit width-three torus 64-state spectrum, forced column monochromaticity for strict random ties, and distinct entropy exponents (3 versus golden ratio). Searches of Resultary and primary majority literature did not establish an implication of this exact toroidal spectrum; an equivalent Ising-strip enumeration remains a historical risk.

## value

PASS

A natural comparison of two established update rules on the first four-regular toroidal strip determines exact and sharply different exponential counts. The RMM phase changes from only two singleton configurations on the ordinary cycle to exponentially many on C3 □ Cn, a structural width/boundary phenomenon that can be used in stability and statistical-mechanics models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
