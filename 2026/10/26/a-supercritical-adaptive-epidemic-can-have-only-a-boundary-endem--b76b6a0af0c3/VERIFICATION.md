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

# Verification procedure and boundaries

Run `python verify.py` with Python 3 and SymPy installed. The checker uses exact rational arithmetic and symbolic characteristic polynomials to confirm the following data:

- The basic reproduction number \(\mathcal R_0=(9+\sqrt{65})/8>1\), the smallest row sum \(3/4\), and both equilibrium sign identities.
- The partial-endemic state \((1/2,0,1/2,1/2,0,1/2)\) is an equilibrium and has the Jacobian and complete negative spectrum given in the proof.
- A supplementary strictly positive contact-creation example has a spectral reproduction threshold above one although its smallest row sum is less than one; this illustrates why a Perron-weighted argument is needed.

The program is finite symbolic verification, not an enumeration over all contact-response functions or all networks. The general existence theorem follows from the independently stated Perron–Frobenius/Brouwer argument and continuity hypotheses. The impossibility of a fully endemic equilibrium in the explicit model follows from two sign contradictions covering both possible ranges of its first prevalence coordinate. No independent external audit or comprehensive literature-priority certificate has been performed.
