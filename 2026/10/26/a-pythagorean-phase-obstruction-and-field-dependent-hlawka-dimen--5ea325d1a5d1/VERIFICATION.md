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

# Verification of the Pythagorean Hornich–Hlawka obstruction

The proof in `RESULT.md` supplies universal symbolic identities and strict monotonicity; no finite test has been used as an infinite-dimensional or all-exponents proof. The constants are exact: \(\sqrt{3^2+4^2}=5\), and \(q\) is the unique root in \((3,4)\) of \(3\,2^{1/p}+(3^p+4^p)^{1/p}=8\).

Run `python3 CHECK.py` from the directory containing the extracted files. The script reconstructs the seven complex-vector norms for selected exponents, compares them against the closed gap expression, tests signs at \(p=3,4\), and estimates \(q\) by bisection. The computed estimate is \(q\approx3.57234633082115\), and the gap at \(p=4\) is approximately \(-0.09853757335868\). These diagnostics are illustrative; the rigorous proof is algebraic, and the only external mathematical input is the classical real-planar Hlawka property, for which a zonoid argument is included.

There has been no independent audit. Historical-priority risk, including potentially equivalent older quadrilateral-space results, remains open. The globally optimal exponent for the complex two-coordinate space is not established here.
