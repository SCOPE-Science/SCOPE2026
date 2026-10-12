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
# Reproduction and bounds of verification

Run `python3 verify.py` with Python 3.9 or later. The script requires no third-party libraries. In the performed check, it printed:

`VERIFY_OK 509 exact arithmetic checks`

It compares exact rational values from direct energy-shell state enumeration through nine bath qubits against the independent closed binomial and Catalan expressions, checks all six rational Boltzmann factors \(0,1/5,1/2,2/3,4/5,1\) through thirteen qubits, checks parity and incremental Catalan identities through twenty pairs, checks raw numerator coefficient identities through twenty-four, and compares exact central-binomial endpoint expressions. It separately verifies the five-qubit first-activation example at \(q=2/3\).

The script's loops test finitely many dimensions and rational factors. They cannot establish the all-size formula, uniqueness and monotonicity of thermal thresholds, the infinite-bath bound, or the sharp asymptotic; these conclusions follow from the exact energy-sector eigenvalue bound, Pascal identities, the Catalan generating function and the uniform Stirling tail in `RESULT.md`. No third-party certificate or independent audit is asserted.
