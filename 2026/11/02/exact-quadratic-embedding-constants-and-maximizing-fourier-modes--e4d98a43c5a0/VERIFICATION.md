---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For each unit-edge M_{2n}, n≥3, the shortest-path profile f(k)=min(k,n+1−k) on 0≤k≤n is exact by cycle/opposite-jump parity. Thus D is a real symmetric 2n-circulant. Fourier transforming its discrete second difference at profile corners gives nonpositive even-index eigenvalues and, at odd j, (−1)^((j+1)/2)csc(πj/(2n)) for odd n or the corresponding cotangent for even n. Among positive reflected frequencies, j=3 gives the unique largest eigenvalue (one real dimension at n=3; 2 otherwise). Its strict positivity rules out squared-Hilbert embedding by conditional negative definiteness; Taylor series establish parity tails. Independent BFS-built matrix eigenanalysis corroborated all n=3,…,23; the corner algebra proves all n.

## originality

PASS

Best-of-knowledge PASS for the parity-resolved geodesic-distance QEC plus exact maximizer subspaces and asymptotics. General constant-row-sum QEC/eigenvalue equivalence and known M6=K3,3 case are credited; identified Möbius-ladder matrix paper studies effective resistance, a different metric. Undiscovered classical distance-spectrum coverage remains a genuine risk.

## value

PASS

A complete all-size exact signed-distance embedding obstruction and maximizing eigendirections for a natural cubic graph family identifies sharp non-Euclidean metric behavior; even-vs-odd asymptotic corrections are meaningful structural invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
