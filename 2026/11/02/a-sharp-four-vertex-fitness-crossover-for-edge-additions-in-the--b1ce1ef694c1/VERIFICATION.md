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

# Reproducibility and limits

Run `python verify.py` using Python 3 and SymPy. The certificate reconstructs all transient birth–death fixation equations from the adjacency lists; checks all six resulting exact rational functions; enumerates every connected graph and missing-edge addition on two through four vertices up to permutation isomorphism; and factors every single-edge difference. Each denominator is shown positive for fitness above one by the positivity of its shifted integer-polynomial factors. Exact rational evaluations at \(4887/1000\) and \(4888/1000\), together with the one coefficient sign change of the ninth-degree polynomial, establish a unique crossing. The three-vertex identity is also rederived and verified.

The embedded program executed successfully and printed five `PASS` lines. The mathematical universal claims follow from the displayed harmonic equations, exact factorization identities, positivity, Descartes' rule and exhaustive graph-class enumeration, not from floating-point tests. No computation about graphs with more than four vertices is claimed. The earliest supporting public source is the 2005 graph-evolution paper; the 2009 paper already documented the qualitative reversal. A full historical originality certification and independent audit have not been performed.
