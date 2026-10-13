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

# Verification details
Run `python3 verify.py` in a Python 3 environment. The verifier computes exact integer binomial coefficients and modular powers in the finite test domain, and independently reconstructs the finite-precision p-adic limit and base-\(q\) digit sum. It tests 82 direct small-domain congruences, nine boundary cases, and the exact \(q=31,p=5\) and \(q=19,p=7\) witnesses. The expected output is recorded separately in `verification-output.txt`.

The universal theorem is proved algebraically by (i) the Jacobsthal increment \(p^{3j}\), (ii) the Teichmüller limit, (iii) Legendre's valuation formula, and (iv) the Chinese remainder theorem. This proof is needed: a finite computational grid alone would not verify the infinitely many primes and exponents in the claim. For \(r\le3\) it is enough to compute the unscaled binomial \(B_0\) modulo \(p^r\); for larger \(r\) the verifier uses enough Jacobsthal-dilated terms to control the p-adic tail. No general finiteness of the p-adic tower is claimed.
