---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Bargetz--Bartoš--Kubiś--Luggin identify 1-homogeneity with vertex-transitivity of the distance-colored complete graph, prove \(\delta(X)\le(n+|S_X|)/2\), give the exact odd case, and construct the even lower bound. Edmonds' Theorem 1.4 bounds the number of odd color valencies by the maximal number of involutions in a group of order \(n\); Theorem 1.2 gives that maximum as \(n/2+n_2/2-1\) for even \(n\). Every positive singleton distance has valency one, so including zero gives \(|S_X|\le n/2+n_2/2\), yielding the claimed upper bound. The source construction with \(n=2^a(2k+1)\) has \(2^{a-1}(3k+2)=(3n+n_2)/4\), so equality follows.

## originality

PASS

The 2024 metric-space paper explicitly leaves remaining even values of \(\Delta_1\) open after proving the odd, power-of-two, and selected low-2-adic cases. Edmonds' older theorem supplies exactly the missing universal odd-valency bound but does not formulate the metric invariant. The audited result is the cross-application that closes the open formula; targeted Resultary searches did not locate a prior publication of the same closed expression.

## value

PASS

The theorem closes an explicit exact-value problem for a natural invariant of finite homogeneous metric spaces in every cardinality. It turns a lower-bound family into a complete formula and reveals the precise dependence on the 2-adic part of \(n\).

The dated certificate retains the supplied scientific assessment, sources and limitations.
