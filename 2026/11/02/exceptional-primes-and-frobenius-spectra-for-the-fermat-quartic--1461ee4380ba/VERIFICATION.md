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

# Verification of the arithmetic incidence classification

Execute `python3 verify.py` with Python 3.9 or later; it uses the standard library only. The source defines the 28 bitangent coefficient vectors in \(\mathbb Z[t]/(t^4+1)\), their 378 pair intersections, and all 3276 triple determinants. It multiplies four conjugates to compute exact integer norms, checks the full nonzero-norm histogram, and proves that no odd prime other than 3, 5 or 17 can introduce new concurrence. Direct exhaustive pair-incidence calculations at each exceptional odd prime give the complete crossing multiplicities and q-Frobenius cycles; repeating Frobenius on labels verifies the two-degree splitting bound. Successful actual execution is recorded in `verify_output.txt`, ending `VERIFY_OK`.

The universal statement about all odd primes relies on the norm-divisibility lemma coupled with exhaustive determinant coverage; it is not an inference from a finite sample of primes. The published complex 288-double/15-quadruple counts and completeness of 28 odd-characteristic bitangents are externally sourced and not represented as new. Only reduced geometric crossing loci are classified; local nilpotent structure of their Jacobian schemes is not verified. The scientific and priority assessment has not received an independent audit.
