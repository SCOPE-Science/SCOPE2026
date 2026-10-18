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

# Reproduction and verification

Run `python3 check.py` with a standard Python 3 installation. The program constructs each integral Sylvester matrix for the two polynomials \(X^{2^{a-1}}+1\) and \((X+1)^{2^{a-1}}+1\), using only exact integer arithmetic, computes the determinant via the Bareiss algorithm, factors the result by trial division, and reconstructs every monic gcd at each relevant characteristic. The determinant computations have integer-size at most \(16\times16\). The output in `certificate.txt` records all evaluated cases.

It also enumerates the nonsquare nonprimitive elements in \(\mathbb F_{49}\), \(\mathbb F_{125}\), and \(\mathbb F_{4913}\), using explicit polynomial-basis field arithmetic; three prime-field negative tests supplement these. Assertions stop execution if any expected value fails. A separate symbolic-algebra calculation of these four integral resultants and modular gcds gave the same values.

The general classification uses a separate proof: cyclic multiplicative groups identify primitive dyadic roots, and exact \(2\)-adic valuations and integer factorization restrict the admissible field orders. Finite test fields do not establish a universal theorem. In particular the proof asserts no primality or existence of untested higher-exponent cofactors. The full text of the later arXiv:2607.17267 source was unavailable, so a residual overlap risk remains.
