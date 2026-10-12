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
`artifacts/verify.py` uses only the Python standard library.

For \(m=3\), it reconstructs the eight columns of the recursive generator and enumerates every nonempty server subset. It filters the inclusion-minimal recovery sets for all four information objects and verifies the weighted-capacity certificate on every one.

It then checks explicit feasible allocations for every nonzero vertex of the corrected polytope:
\[
(10/3,0,0,0),
\]
the three axis vertices of value \(4\), and the three mixed vertices \((2,2,0,0)\) up to permutation of the last three coordinates. The allocation loads are checked exactly with rational arithmetic. Together with the two proved facet inequalities and convexity, this certifies the exact \(m=3\) region.

For \(3\le m\le8\), it regenerates the recursive column sets, verifies the constant-row normal form, and checks the counterexample family symbolically with exact fractions. These finite checks illustrate the proof; the all-\(m\) statement follows algebraically and from the cited exact theorem.

Successful replay prints `VERIFY_OK`.
