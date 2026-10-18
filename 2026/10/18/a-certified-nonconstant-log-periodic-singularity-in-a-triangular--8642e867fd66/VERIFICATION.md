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

# Verification record

The analytical proof establishes the full-orbit assertion, local analytic linearization, exact phase invariance, and two-term asymptotic. The computational component is used only for the delicate nonconstancy assertion: it **encloses** two infinite-product values with explicit tail bounds and shows their intervals do not intersect.

Run `python verify.py` using Python 3 with `mpmath`. The script uses `mpmath.iv` at 145 decimal digits, 170-decimal-digit root centers, and 1000 steps in each direction at the rational inputs \(9/20\) and \(1/2\). Every cubic inverse is bracketed against the previous interval using the exact monotonic derivative inequality \(F'(v)\ge2/3\) on \([0,1]\). Tail estimates are \(L\le L_Ne^{5w_N}\), \(B\ge B_N(1-3z_N)\), and \(h\le h_Ne^{z_N^2}\). At completion the script prints `VERIFY_OK` only after confirming a strict positive difference between the two phase-value enclosures.

The enclosing values imply \(A(1/2)-A(9/20)>1.2\times10^{-24}\). Direct floating-point trajectory plots are insufficient to distinguish such a small oscillation and are not used as proof. The certification assumes the stated outward-rounding behavior of the interval library; it has not been validated by independent software or a separate reviewer.
