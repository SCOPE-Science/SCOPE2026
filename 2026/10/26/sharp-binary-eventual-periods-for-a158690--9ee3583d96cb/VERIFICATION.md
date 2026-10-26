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

# Verification of the dyadic period theorem

The executable `VERIFY.py` uses only the Python standard library and exact integer arithmetic. It independently expands the product defining A158690 for indices \(0\le n\le8\), recovering the coefficients \(a(6)=1431665\) and \(a(8)=6646603073\). It also constructs the integral formal series \(H(y)\) modulo powers of two, converts its coefficients to the truncated Stirling power-sum weights, and checks these independently against the direct coefficients.

It checks the eventual period for moduli \(2^r\), \(2\le r\le16\), for twelve indices at each exponent, checks the exact residue \(2^{r-1}\) of half-period differences at six even indices for each \(5\le r\le16\), and verifies the base coefficient invariant \(B\equiv2\pmod4\) at those exponents. The recorded execution result was `VERIFY_OK 393`.

The code does not enumerate all natural indices or all exponents. The infinite statement rests on the binomial-divisibility argument and the exact coefficient computations documented in `RESULT.md`. No external independent validation has occurred.
