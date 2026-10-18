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
# Reproduction checks

Run `python verify.py` using Python 3 and SymPy (version 1.12 or newer). This verifies: the exact 16-state generator and stationary null equations; the rational current; polynomial denominator positivity by the proof's coefficient argument; the exact algebraic transformation into a degree-nine polynomial; all ten transformed coefficient sign-variation counts; the unique zero of each of the six low-order coefficients and its rational interval; strict ordering of all six intervals; and the endpoint calculation at maximal contrast. A separately coded rational elimination agrees with the symbolic current at five rational boundary pairs.

`polynomial_certificate.json` lists the full exact coefficients and the order of operations. The calculation uses integer and rational arithmetic; the critical interval is a rational root bracket, not a simulation estimate. The global conclusion additionally uses the mathematical Descartes sign-count theorem, positivity of the stationary-current denominators and the transformation of the physical density interval. No external audit or generalization beyond the stated four-site dynamics is claimed.
