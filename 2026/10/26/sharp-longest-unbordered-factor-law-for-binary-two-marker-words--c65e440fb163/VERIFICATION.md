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

# Reproduction and limits

Place `verify.py` alongside this document and run `python3 verify.py` using Python 3.9 or newer. It requires only the standard library and prints `CHECKS_OK` after all assertions pass.

The direct check enumerates every two-one word of lengths 2 through 23 and every nonempty factor, testing borders independently of the proposed gap formula. The coefficient check generates the bivariate rational formal series from six denominator products through degree 48, then compares with an independent gap enumeration. A second coefficient check verifies the rational first-moment series. An asymptotic sanity check uses every two-one word of length 500 to compare selected empirical CDF values and the normalized mean against the proposed limit.

The universal formula for all lengths, the rational generating functions, weak convergence and the exact limiting mean rely on the detailed mathematical proof in `RESULT.md`; no finite test proves a universal statement or an asymptotic theorem. An independent audit has not been performed.
