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
# Reproducibility and limitations

Run `python3 verify.py` with a Python 3 standard-library interpreter. The checker verifies the right Leibniz polynomial identity and zero-product reciprocity on every ordered pair over \(\mathbb F_3^2\), for all possible bilinear laws on that fixed two-dimensional vector space; it selects \(8\) symmetric and \(8\) Lie laws with one-dimensional derived line. It constructs \(364\) central and \(312\) noncentral three-dimensional laws over \(\mathbb F_3\) and checks the polynomial identities and reciprocity for each; they total \(676\). For the explicitly specified derived-dimension-two counterexample it checks all pairs of quotient coordinates over \(\mathbb F_3\), \(\mathbb F_5\) and \(\mathbb F_7\).

The mathematical proof handles arbitrary dimension and any odd finite field; the computer checks cover only the enumerated finite cases. The abstract nonsingularity and similarity classification of finite-field bilinear forms is a classical input and is not computationally certified here. No independent mathematical audit has been performed.
