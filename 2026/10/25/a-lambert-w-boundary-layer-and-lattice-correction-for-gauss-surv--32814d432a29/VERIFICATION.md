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

# Verification of the dimension-enclosure theorem

Analytic checks: (1) the inverse branches \(\phi_a(x)=1/(a+x)\) map \([0,1/N]\) into itself, with disjoint interiors and the displayed derivative sandwich; (2) monotone scalar pressure zeroes bracket the true dimension; (3) evaluating the lower scalar sum at the upper root shows a defect no larger than \(2/N^2\); (4) its derivative magnitude exceeds \(\log N\) across the root bracket; (5) Euler--Maclaurin makes the scalar root correction \(W(L)^2/[4NL^2(1+W(L))]\), where \(L=\log N\); (6) bracketing controls the map-specific pressure error by \(O(1/(N^2L))\).

Run the included `checker.py` with Python 3 and `mpmath==1.3.0` to reproduce `checker_output.txt`. The program evaluates Hurwitz-zeta roots by bisection for \(N\in\{20,50,100,300,1000,10000\}\), and its output is a finite numerical cross-check of the rigorous enclosure and the asymptotic prediction. Numerical roots are not certified exact or exhaustive. The argument's use of countable-IFS pressure theory and the universal large-\(N\) asymptotic cannot be replaced by the checker.

Source-inspection scope: the motivating paper's arXiv full HTML main theorems and Sections 4--5 were inspected; the sparse-digit comparison's arXiv HTML abstract, Section 1 and its main-theorem setting were inspected; the quantitative lower-cutoff comparison arXiv:2603.27635v1 was read through its Theorem 1.2, Remarks 1.3--1.4 and relevant Section 1 definitions. Independently published priority validation has not occurred.
