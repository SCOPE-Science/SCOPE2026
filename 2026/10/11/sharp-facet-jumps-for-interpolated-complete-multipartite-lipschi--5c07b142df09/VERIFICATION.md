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

# Reproducible verification

Run `python3 check_facets.py` with a standard Python installation. The verifier uses `fractions.Fraction` and exact tight-edge graph connectivity, with no third-party dependencies. It covers the four multipartite profiles \((2,1,1)\), \((2,2,1)\), \((2,2,2)\), \((3,1,1)\) and the three parameter values \(t=1\), \(t=3/2\), \(t=2\). All twelve exact cases passed.

The verification grid is exhaustive only in these finite cases: if a vertex has a connected tight graph, values relative to the basepoint are integer combinations of edge lengths, hence half-integers in the tested configurations. Their magnitudes do not exceed \(2\), so the finite enumerator covers all candidate vertices. A connected tight graph provides the required full rank. The all-size and all-real-parameter theorem instead follows from the two-type analytic classification in `RESULT.md`.

A separate small numerical halfspace-vertex computation was also compared for the profiles \((2,1,1)\), \((2,2,1)\), \((2,2,2)\), \((3,1,1)\), \((2,1,1,1)\) at four parameter values, totaling twenty checks; these do not certify the infinite family. The prior graph-metric endpoint is explicitly distinguished from the new interior formula. Independent review is not available.
