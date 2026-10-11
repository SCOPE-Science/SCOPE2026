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

# Verification and scope

The formal statement is the integral homotopy equivalence for every **odd** integer \(n\ge3\) in `RESULT.md`. The complete proof comprises (i) uniqueness of a maximal open neighborhood for every simplex with at least three vertices, (ii) an explicit free-face collapsing order to dimension two, (iii) simple connectivity using the antipodal double covering of the cube's square complex together with Matsushita's fundamental-group theorem, and (iv) the exact face-count Euler characteristic and the homology Whitehead theorem.

To reproduce finite checks, run `python verify.py` and `python crosscheck.py` from the directory containing these two standalone scripts (Python standard library only). Both scripts were executed successfully before packaging; the numerical checks are summarized in the present file. In dimensions \(3,5,7,9\), the first script enumerates respectively \(14,352,7072,124160\) nonempty faces and finds sphere multiplicities \(1,31,351,2815\). It explicitly checks elementary collapses in dimensions \(3,5,7\), with respectively \(0,80,2688\) collapse pairs. The second implementation constructs the antipodal quotient cube graph independently for \(n=3,5,7\), checking degrees, common-neighbor distributions, and embedded square counts.

These finite calculations are corroborating evidence, not a substitute for the mathematical argument covering infinitely many odd dimensions. The group computation uses the cited published Theorems 1.1 and 3.1; it is not independently reproduced by the finite scripts. No claim is made for even dimensions, and independent audit has not been performed.
