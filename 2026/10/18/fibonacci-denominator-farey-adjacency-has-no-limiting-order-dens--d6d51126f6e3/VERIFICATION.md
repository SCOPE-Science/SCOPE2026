---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For coprime ordered denominators u,v≤N, the determinant-one equation gives a unique ordered pair of fractions in [0,1], including the endpoint cases. If a/u<h/k<c/v is strictly between such fractions then k=v(uh−ak)+u(ck−vh)≥u+v, so the sum condition is exact, not just a mediant test in one direction. On F_k≤N<F_{k+1}, k≥6, no distinct pair omitting F_k has sum above N, and (1,1), the only coprime diagonal pair, is excluded by its sum. Both (F_k,F_{k−1}) and (F_k,F_{k−2}) are coprime by the Fibonacci gcd identity. Their largest and second-largest sums force the event C(N)=2 exactly on the stated terminal block interval. For N=1,…,7 the denominator rule gives C(N)=1,2,4,2,6,4,2. The terminal blocks have F_{k−3} orders, giving E(F_k−1)=F_{k−2} by induction and the stated maximum formula. E(N)/N decreases up to F_k+F_{k−2}−1 then increases. That minimum converges to 1/(φ²+1), and both ends converge to φ⁻². The supplied full-Farey regression through 450 and denominator-pair regression through 15000 were inspected as recorded finite checks, not executed or used as proof.

## originality

PASS

The distinct result is the exact interval criterion and order-frequency law for adjacency in the full Farey sequence. The run starts are a known Lucas-type sequence, and no novelty is assigned to those integers as a sequence, the Farey criterion, or Fibonacci strong divisibility.

## value

PASS

The full-Farey statistic asks at what orders a natural sparse denominator set leaves exactly the two unavoidable ordered adjacencies. The complete block criterion resolves this at every order and gives sharp bounds on the persistent oscillation, not just examples or an isolated computation of known Lucas numbers. The result is narrow and uses elementary inputs, but identifies a concrete obstruction to assigning a single long-run order frequency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
