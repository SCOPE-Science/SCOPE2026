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

The frozen-prefix decomposition is exact because e_t=X_t-(t+1) satisfies nonnegative e_{t+1}=e_t+u_t+e_{u_t}, so any history with final e_n=r cannot use index j>r after time r. The full later steps then draw from fixed indices 0..r with fixed increment weights j+e_j; expanding (1+B_prefix(z))^(n-r) gives nonnegative integer h_{r,k} coefficients and degree r. The leading h_rr=1 comes from all-zero prefixes, the next coefficient 2(r-1) from exactly one 2-increment or a single early 1-prefix. Comparing to independent inversion codes, feedback requires excess at least four, so all prefixes of excess <=2 agree, while the unique excess-one prefix starting at t=1 invalidates exactly r-2 uses of later index two. Hence the r-2 coefficient difference r-2 and n^2(1-A/M)->r(r-1)(r-2) for fixed r>=3.

## originality

PASS

The Ben-Naim–Krapivsky original 2002 source directly considers this history-dependent process and gives minimum and minimum-plus-one endpoint probabilities; Bonner 2023 centers on moments. The classical Mahonian inversion-code law is the uncorrelated comparison model. These statements neither imply exact fixed-surplus polynomiality for every r nor the universal second-order difference without a nontrivial frozen-prefix combinatorial proof. Complete original full-text related portions and Bonner abstract were inspected; potential unindexed addition-chain results remain a risk.

## value

PASS

Exact rare-left-tail probabilities are natural discrete invariants complementary to typical-value/moment asymptotics, and the sharp 1/n^2 deficit isolates the earliest feedback effect against the canonical inversion-count model. The positive binomial-basis coefficients give an effective finite-prefix algorithm for each fixed surplus and identify structural meaning of the correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
