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

# Verification and limits

The checker file `checker.py` is a standalone Python 3 script requiring no external libraries. Its recorded output is in `checker_output.txt`. Run `python3 checker.py` from the extracted file directory; a successful execution prints `PASS: 219 exact rational and deterministic numerical assertions`.

- Exact rational enumeration of all \(n!\) relative-orderings for \(2\le n\le7\) and all possible conditional prefix lengths \(1\le k\le n\). The three conditional formulas are compared without rounding.
- Full move-history enumeration for \(2\le n\le6\), \(1\le r\le6\); the exact occupancy mixture reproduces the directly enumerated means and covariance and verifies strict positivity.
- Deterministic occupancy Markov recursion at \(n=80,160,320,640\) for \(c=0.5,1,2\); the finite covariance matches the predicted scale with decreasing discrepancy.
- Analytical limits are established in the main proof by independent occupancy fluctuations, finite-population sampling and one-dependent Gaussian triangular arrays. Finite experimentation does not establish asymptotic convergence independently.

No human or independent external audit has been performed, and historical priority remains subject to broader literature comparison.
