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

# Verification

Run `python verify.py` with Python 3 standard library from the directory containing the extracted files. Its direct convolution count sums \(r_c(s,y)^2\) over every target encountered; zero-representation targets contribute zero. The separate closed-form computation builds the finite-field quadratic character from nonzero squares and calculates \(C_c\), \(H_c\), and \(J_c\). For \(c\ne0\), it independently counts rational points on \(w^2=P_c(v)\) and verifies the trace sign. For \(c=0\), it checks the singular specialization and corresponding character values.

The verified cases are every one of the \(155\) parameters in the nine prime fields of orders \(5,7,11,13,17,19,23,29,31\), plus six distinct parameters in each quadratic extension of orders \(25,49,121,169\), giving \(179\) exact comparisons. Field extensions are implemented with a square root of a nonsquare in the prime field; no external field package is needed. Separately, exact symbolic polynomial expansion was used to validate the collision shift factorization; its outcome is recorded in `verification_output.txt`.

These are finite consistency checks. The general all-field proof is the character-sum argument in `RESULT.md`. They do not prove bibliographic novelty, guarantee third-party verification, or establish the sharp bilinear norm for nonconstant weights.
