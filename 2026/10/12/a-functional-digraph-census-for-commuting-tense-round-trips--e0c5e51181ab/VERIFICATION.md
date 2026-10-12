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

Run `python3 verify.py` in the same directory. The checker uses only the Python 3 standard library and produces `VERIFICATION_OK` if all checks pass.

It independently enumerates all endofunctions on one through six labelled vertices: 1, 4, 27, 256, 3,125, and 46,656 functions, totaling 50,069. It checks equivalence between fiber saturation and the homogeneous-sibling condition for every one. The qualifying counts are 1, 2, 12, 108, 1,100, and 13,350. It also checks commutation of the original Boolean event operators for every valuation and all endofunctions through five vertices, covering 104,330 function–event configurations.

An exact-rational, independent power-series recurrence reproduces the coefficients for sizes zero through ten:

\[
1,1,2,12,108,1100,13350,194502,3280424,62480952,1328405130.
\]

The general theorem for infinite sets, the reversible functional-digraph decomposition for every size, and the asymptotic rate follow from the mathematical proof; the finite program does not establish these unlimited statements. The numerical singularity approximations are reported for orientation, not as certificates of analytic continuation or uniqueness.
