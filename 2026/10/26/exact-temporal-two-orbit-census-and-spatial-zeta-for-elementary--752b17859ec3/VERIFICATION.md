---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Local rule f=1 precisely for triples 001,100. Two updates depend on five bits, and F²x=x imposes exactly 20 allowed five-blocks. A 16-state de Bruijn transfer graph with allowed edges has trace M^n exactly equal to # n-periodic configurations of Fix(F²), including repeated coordinates n<5 by the cyclic-edge condition. Direct exact directed-cycle determinant yields det(I−zM)=(1−z)(1−z⁴−2z⁵−z⁶), a finite complete certificate governing all lengths, not an extrapolation. The only F-fixed ring configuration is all zero because a rule-18 output one implies central input zero. Thus b_n/2 temporal two-orbits. The recurrence/seed gives b_n>0 except n=1,2,3,7, and unique Perron eigenvalue rho of λ³−λ−1 yields entropy and O(1.30^n) error. Fresh independent 20-block enumeration, symbolic determinant and direct all 2^n words for n≤12 agreed.

## originality

PASS

Zhu–Richard 2026 finite-ring Koopman spectra, Stricker 2023 longest cycle classifications, and Sabrié–Törmä 2023 rule-18 limit dynamics and a period-two example concern overlapping dynamics, but the inspected results do not give the all-n temporal-two orbit count and exact spatial zeta. The 4-cycle existence already known is explicitly not novel; contribution is exact complete census.

## value

PASS

Rule 18 is a standard elementary cellular automaton with nontrivial nonlinear dynamics. The precise rational zeta, exact orbit counts for every ring length and characterization of the exceptional length seven provide a natural finite-type invariant and quantitative entropy of temporal-two points, not just isolated computational examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
