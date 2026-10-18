---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Reconstructed the monitoring definition: x monitors xy because removal increases d(x,y)=1. For x=a_p and a nonincident edge a_r b_s, every target b_j (j!=p) retains its direct edge, every other a_q has n-2>=2 two-edge geodesics with at most one affected, and b_p has (n-1)(n-2) geodesics a_p-b_j-a_i-b_p with at least one avoiding the edge, including s=p. Thus only incident edges are monitored n>=4; by symmetry every monitoring set is a vertex cover. Independent set classification: subsets of A or B plus n matched pairs {a_i,b_i}; I(z)=2(1+z)^n-1+nz² and D(z)=z^(2n)I(z^-1). Minimum monitoring sets exactly A and B, cardinality n. For n=3 is C6 and its monitoring number is 2, so threshold sharp. Independent edge deletion and shortest-path recomputation for all probes and all vertex subsets checked n=3,4,5, including polynomials.

## originality

PASS

The foundational monitoring theorem only implies that vertex covers monitor, with equality when no probe detects a nonincident edge. The present all-n proof establishes this property for the non-complete crown class and enumerates all sets, n=3 exception. Exact equality may be historically known under vertex-cover language; best-of-knowledge.

## value

PASS

Exact identification of all monitoring sets for the natural crown family, not simply another domination statistic, establishes the threshold n>=4 against C6 and describes the precise change caused by deleting a matching from K_{n,n}. This can serve as a test class for monitoring-vs-vertex-cover and perturbation questions; polynomial coefficients then follow transparently.

The dated certificate retains the supplied scientific assessment, sources and limitations.
