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

# Reproduction and boundaries

Execute `python3 verify.py` with Python 3 and its standard library. The program implements the integral arithmetic of \(\mathbb Z[\omega,\sqrt{13}]\) where \(\omega^2+\omega+1=0\), constructs twelve projective candidate nodes, verifies distinctness and conic membership, enumerates the biquadratic Galois action and fixed-point counts, and checks singular-point counts of the integral sextic via explicit Jacobian evaluations over 20 prime fields from \(5\) through \(89\) (excluding \(7,13\)). Expected output begins `VERIFY_OK`.

The full-field singularity computations sample twenty primes; **they do not prove any all-prime assertion**. Those assertions rest on the displayed subtraction factorization of the conics, the smooth conic determinants, the precise four-intersection calculation, and third-conic norms with prime support \(3,7,13\). Field minimality follows from explicit node-coordinate ratios; prime-density statements follow from the two independent quadratic Frobenius characters and Chebotarev. The result excludes characteristics \(2,3\), and does not classify all singularity types of the exceptional reductions at \(7\) and \(13\).

No independent verification or audit has been performed.
