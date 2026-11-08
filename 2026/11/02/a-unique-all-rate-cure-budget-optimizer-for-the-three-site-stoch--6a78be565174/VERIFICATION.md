---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The full seven-state SIS CTMC transient generator (all nonzero 3-bit states) was independently reconstructed, inverted symbolically, and matched the displayed five-class rational mean. For unequal endpoints u=x+h,v=x-h, exact factor after z=x^2-h^2 has positive coefficients in 55 numerator monomials and 16 denominator monomials (independently reproduced in exact SymPy), proving strict endpoint symmetrization. For equal endpoints, derivative has quintic with signs (+,+,-,-,-,-) and P_r(1/2)<0<P_r(1), so unique t in (1/2,1) is global minimum over all budget allocations; boundary zero cure gives infinite expected time. Independent exact-rational examples r=1/2,1,9/10 agree. No general-graph or alternate-initial-state extension.

## originality

PASS

McFadden-Daly-Shneer (2025) study same cure-budget objective and numerically analyze three-node star with uniformly randomly sampled initial infection, whereas candidate proves global analytic optimum starting fully infected and strict unrestricted endpoint symmetrization; primary full text not accessible, so potential overlap remains material risk. Resultary semantic queries of published records performed with two tailored queries; no exact dominating result located, and this is not proof of priority. The listed primary sources were compared on mathematical implications; inaccessible relevant text retained as risk.

## value

PASS

Expected extinction time under a fixed budget is a natural exact optimization target in heterogeneous SIS control. The all-intensity, all-allocation three-site optimum and disagreement with degree-threshold allocation give a substantive exact small-graph benchmark, rather than an arbitrary sample enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
