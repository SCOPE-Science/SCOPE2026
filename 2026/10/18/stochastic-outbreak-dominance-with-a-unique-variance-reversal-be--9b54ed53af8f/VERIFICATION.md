---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

PASS: A simple cubic graph on 6 vertices has a 2-regular complement, either C6 or two disjoint triangles, yielding precisely the two networks. Exhaustive root-cluster counts for every 2^9 open-edge state and each of six roots were reconstructed independently (6144 rooted states). Differences by open edge cardinality j=3,4,5,6 are k4:(4,9,6,1), k5:(0,5,6,1), k6:(0,0,6,1), yielding exact positive tail differences. Moment tail-sum formulas and full variance polynomial Q were reproduced by integer polynomial arithmetic. Descartes transform (1+t)^12 Q(t/(1+t)) coefficients have exactly one sign change; Q(0)>0>Q(1), so exactly one crossing; numeric root ≈0.479245294778868 agrees.

## originality

PASS

PASS (best-of-knowledge): Bond percolation rooted-component size equals the Reed–Frost final outbreak under independent-edge transmission; this equivalence is standard and credited. Earlier clustered-population epidemic results discuss clustering effects rather than this exact finite stochastic order plus variance crossover. Broader coverage and exact table checks find no known proof of this final specialized classification. Residual priority risks are separately documented; unsuccessful searches do not prove novelty.

## value

PASS

PASS: The first size where distinct connected cubic contact networks occur supplies a canonical controlled finite comparison with equal vertices, edges and degrees. Simultaneous all-transmissibility stochastic dominance and reversal of variance ordering is a mathematically informative counterexample to treating mean and spread as co-monotone network effects; sharp uniqueness is not a routine consequence of expectations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
