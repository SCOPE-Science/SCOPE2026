---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The substitution yields s_n=(-1)^nu2(n+1). Periodic truncation modulo 2^K differs only on at most three exceptional residue classes, so ordinary-time limits equal Haar averages on Z2. For three positions the ultrametric valuations are necessarily (m,m,t); splitting Haar U by nu2(U)<m and the two residue classes mod 2^(m+1) reduces the triple to a mean 1/3 and a pair moment at valuation t-m-1, giving 1/3-4(-1)^m/(3*2^t). Walsh expansion gives all probabilities, while t>=m+1 yields exact zero/min/max classes. Independently generated 2^15 substitution signs from recursion and checked ten triple averages against analytic values with strict finite-modulus error ≤6/32768; the infinite claim is supported by the Haar case proof.

## originality

PASS

Baake-Grimm derive the same substitution, 2-adic internal space and exact two-point autocorrelations; those are credited, not claimed new. Deng-Moody general model-set Haar-intersection theory and Polakova exact arbitrary contiguous-cylinder probabilities can in principle evaluate every fixed sparse triple; the statement here is the explicitly uniform two-valuation formula for arbitrary unbounded lags and sharp global classifications, not existence of computable frequencies. The earlier broad results are genuine coverage of existence and fixed-lag computability, and an equivalent uniform specialization remains a substantive originality risk.

## value

PASS

An exact closed all-lag third-order invariant of a classical substitution system, its complete three-site word law and sharp attainable range can distinguish higher-order structure not supplied by two-point diffraction, and serves as a reusable concise sparse-cylinder benchmark rather than arbitrary one-off arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
