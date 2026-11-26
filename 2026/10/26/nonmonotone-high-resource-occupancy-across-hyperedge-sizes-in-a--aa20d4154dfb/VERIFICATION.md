---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The frozen-strategy kernel in Wei et al. gives p=pq+(1−p)q², with the unique solution h(q)=q²/(1−q+q²), including the absorbing boundary cases q=0 and q=1. Uniform subset sampling gives the hypergeometric weights; averaging the stationary marginal needs no independence between edges. For sizes 2 and 3 I checked the closed forms by using h(1/2)=1/3 and h(1/3)=1/7, h(2/3)=4/7. The sign of H(3)−H(2) in the nontrivial range is that of 6m−5n+4. For H(n)−H(2) the sign is that of P=m²+(2n−3)m−2n²+3n. P increases in m, P(n−2)=n²−8n+10 is negative for 3≤n≤6, and at m=n−1 the sign of H(3)−H(2) is positive. An independent bounded replay enumerated all size-g bit masks for g=2,3,n, 3≤n≤7, 1≤m<n, using the first m bits for cooperators and summing k²/(g²−gk+k²) as reduced fractions. The only reversal was (7,5), yielding (31/49,40/63,25/39) in the asserted order. Taking the fixed-g hypergeometric-to-binomial limit before g→∞ gives the Bernstein averages and then h by concentration and bounded continuity. Direct subtraction of the two Bernstein polynomials and h verifies the signs and ties at 1/√2, √3−1 and 5/6. The frozen verify.py and VERIFICATION.md were inspected, not run; their finite grid is not used to prove the continuous diagram. Neither coevolution nor an arbitrary fixed hypergraph is covered.

## originality

PASS

The transition rule, stationary averaging and Bernstein convergence are known ingredients. The supported distinct claims are the minimal strict finite-population reversal for the specified three scales and the exact order of the three density-limit benchmarks. The same kernel in Wei et al. is not itself a result ordering these averages. The closest indexed overlaps located cover only parts of the calculation, and are later-dated; the stronger-looking envelope bounds do not determine the uniform sampling average.

## value

PASS

The smallest exact counterexample to monotone ordering at sizes 2, 3 and the full population is a useful benchmark for the published environmental transition in isolation. It makes the reversal attributable to group composition alone and gives a reproducible test before adding strategy dynamics. The exact density intervals distinguish when the large-group limit merely recovers above size 3 from when it also exceeds size 2. The contribution is modest and conditional, but does not rest on novelty of routine stationarity or approximate simulation plots.

The dated certificate retains the supplied scientific assessment, sources and limitations.
