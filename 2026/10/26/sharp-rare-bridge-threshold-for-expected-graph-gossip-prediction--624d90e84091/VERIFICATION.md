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

Under a once-sampled Bernoulli shortcut and two fixed boundary agents, expected gossip converges (in expectation) to a grounded weighted-harmonic solution. Series/parallel effective resistance gives a(t)=(L/H+Lt)/(1+2L/H+2Lt), and linearity of the rest of the path follows from harmonicity. Direct subtraction yields the strictly positive rational Jensen gap. Summing the absolute coordinatewise differences on both short arms and the H+1 central vertices, avoiding double counting endpoints, yields the exact parity-dependent B_H coefficient. When H/L->infinity, p->0, Lp->c including infinity, normalized discrepancy tends to phi(c)/2, and convergence in probability holds because the realized shortcut is absent with probability 1-p->1. Independently solved 175 exact rational grounded Laplacian systems across lengths and shortcut conductances, plus 35 exact discrepancy checks. No assertion of almost-sure convergence of instantaneous gossip states is made.

## originality

PASS

Acemoğlu–Como–Fagnani–Ozdaglar established the harmonic representation of stubborn-agent expected gossip, so the electric-network method is established. Xing–Johansson concentration bounds compare random-graph gossip to expected-graph averages under substantial graph density/anchoring hypotheses not met by the long low-degree path with one rare bridge. The sharp scale p~1/L, exact all-vertex discrepancy and supercritical limit 1/4 within this family are not consequences of their concentration statement. The theorem is a motivated sharp counterexample delineating the hypotheses, not claiming to refute those results.

## value

PASS

The explicit threshold determines where expected-graph predictions break down despite a vanishing edge-presence probability, and the all-population error has a rigorous sharp limit. This is a motivated model warning tied to existing random-graph approximation hypotheses, not a generic Jensen assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
