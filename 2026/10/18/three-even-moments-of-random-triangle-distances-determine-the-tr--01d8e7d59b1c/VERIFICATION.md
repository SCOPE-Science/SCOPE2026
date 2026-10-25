---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Represent the random points by independent Dirichlet(1,1,1) barycentric coordinates. For squared sides p,q,r, D²=pB²+(p+q−r)BC+qC². Exact moments E[U1^i U2^j]=2i!j!/(i+j+2)! give M1=e1/18, M2=(e1²−2e2)/60, M3=23e1³/4200−31e1e2/2100+e3/210. Independently expanded the Dirichlet double sums symbolically for k=1,2,3, all polynomial differences identically zero. The nonzero e3 coefficient gives unique inversion and side polynomial, with strict triangle inequalities necessary and sufficient. Squared sides {1,4,4} and {2,2,5} share e1=9,e2=24 and area √15/4 yet have distinct e3, proving two moments insufficient. Forward sampling and exact population moments are expressly distinguished.

## originality

PASS

Best-of-knowledge PASS for a sharp low-even-moment inverse and realization test. The first squared-distance moment and full forward random-distance distributions are known, and thus not claimed as original. Having an integrable forward CDF implies moments in principle, but does not itself state an explicit three-moment inverse or minimality.

## value

PASS

Natural unlabeled stochastic-geometry measurement: distance between two area-uniform points. Determining complete triangle shape from exactly three low population moments, with explicit feasibility polynomial and two-moment same-area counterexample, gives a sharp and reusable finite algebraic inverse rather than a mere calculation of another forward moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
