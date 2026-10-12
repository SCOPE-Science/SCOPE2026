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

# Reproducibility and boundaries

Run `python3 verify.py` with Python 3. No external packages are required. The verifier constructs the five-dimensional restriction of every derivation on the basis \((x,y,x^2,xy,y^2)\); the omitted unit is always annihilated. Gaussian elimination over finite fields computes the ranks without using the block-quotient argument of the proof.

Actual checked results:

- Over \(\mathbb F_2\), complete enumeration of \(1024\) derivations gives frequencies \(1,21,250,752\) at ranks zero through three.
- Over \(\mathbb F_3\), complete enumeration of \(59049\) derivations gives frequencies \(1,104,624,7776,28674,21870\) at ranks zero through five.
- Every linear-part coefficient quadruple is checked in fields of orders two, three, four and five, including the characteristic-two scalar exception and the characteristic-odd trace-zero split.
- Selected nonlinear coefficient combinations are checked directly over fields of orders four and five; the field of order four is implemented as \(\mathbb F_2[t]/(t^2+t+1)\).
- Formula coefficients are checked to sum to \(q^{10}\) for \(q=2,3,4,5,7,8,9,11\). Those last tests are integer evaluations, not exhaustive finite-field experiments.

The source code does not claim to certify the statement for all prime powers. That scope is justified by the block-rank bijection and the complete two-by-two linear-part classification proved in `RESULT.md`. Neither the verifier nor this report constitutes an independent mathematical audit.
