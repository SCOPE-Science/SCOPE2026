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

# Exact reproducibility checks

Run `python3 verify.py` using Python 3.8 or newer. The script implements modular Gaussian elimination, checks the determinant identity for the two tangent quadratic blocks for tested parameter pairs, enumerates all two-coordinate-value patterns over three prime fields, and exhaustively enumerates the projective rational points in the smallest case \((p,r)=(5,1)\) to locate six rational singularities. It prints `VERIFY_OK` upon success.

The tests cover only primes \(5,7,11\) and selected values of \(r\), plus all \(\mathbb F_5\)-rational projective points in the smallest case. They cannot certify that there are no additional geometric points over extension fields, and do not prove the arbitrary-prime statement. Those assertions are proved by the two-value Vandermonde argument, the multiplicity divisibility bound and the nondegenerate quadratic formal normal form in `RESULT.md`.

The formula for the local completed ring and reduced Jacobian singular scheme is a characteristic-not-two mathematical argument, not a finite-check inference. An independent mathematical audit has not been performed.
