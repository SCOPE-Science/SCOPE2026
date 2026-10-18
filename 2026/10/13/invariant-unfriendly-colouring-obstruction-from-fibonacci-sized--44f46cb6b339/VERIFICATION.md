---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For first-one rank k, M0=1,M1=3 and M_(k+1)=1+Σ_{j<k}M_j+ε_k are odd and satisfy M_parent>Σ children, including leaf contribution; recurrence M_(k+2)=M_(k+1)+M_k+(-1)^k gives Θ(φ^k). Identical odd-size neighborhoods force monochromatic fibres for any unfriendly colouring, with colors opposite to parent; this induces proper parity colouring of the tail-equivalence first-one tree, impossible measurably on conull invariant set by finite-bit-flip invariance/approximation by cylinders; category version similarly. Counting lift of Bernoulli probability across finitely many sheets is E0-invariant; generating function gives Σ2^(−k−1)(M_k+ε_k)=11/3, hence invariant normalized probability 3η/11. Infinite mean degree follows from ∑2^(−k−2)M_kM_(k+1) diverging since φ²/2>1. Induction proves minimality within explicit odd strict-parent-majority certificate class. Independently checked first 12 weights, parity, rational generating-function normalization and divergence rate; unbounded theorem rests on the proof.

## originality

PASS

The initiating 2026 Borel counterexample is explicitly quasi-invariant and proves no invariant probability exists for its cubic-base fibre multiplicities; its §6 identifies the invariant infinite-average-cost direction as a natural gap. Conley–Tamuz prove existence only for invariant finite-average-degree graphs. The present Fibonacci fibre recurrence is summable against Bernoulli mass, creates invariant probability and infinite degree expectation, and gives an obstruction not covered by either theorem.

## value

PASS

Conley–Tamuz require finite invariant mean degree. This graph supplies an invariant-probability counterexample with no measurable unfriendly 2-colouring on any conull domain, showing that integrability cannot be dropped even for hyperfinite closed one-ended bipartite graphs. Replacing the older cubic-growth fibres by optimal-under-certificate Fibonacci weights crosses the finite-mass threshold while keeping infinite degree expectation. This directly addresses a motivated open boundary, not an incidental Fibonacci coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
