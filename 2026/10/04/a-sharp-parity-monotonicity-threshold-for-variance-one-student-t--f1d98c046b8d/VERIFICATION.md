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

The exact recurrence from Hu--Song--Tan reduces same-parity ordering to an integral inequality. Its integrand decreases with \(s=y^2\), so the endpoint \(s=3\) suffices; convexity plus Jensen reduces the proof to the explicit positive factor \(B_n\), whose polynomial sign argument is valid for all \(n\ge4\), with \(n=3\) checked separately. Closed forms for \(J_3,J_4\) and the one-turn derivative argument prove the cross-parity ordering. The displayed Stirling expansion was independently spot-checked against the exact density through order \(n^{-2}\); differencing its first correction gives the sign change exactly at \(y=\sqrt3\). The package verifier also checks thousands of finite degrees but is not used for the infinite claim.

## originality

PASS

The closest paper studies exactly the same variance-normalized Student anti-concentration functional. Its Theorem 2.4 gives a smaller-range finite maximization and Remark 2.5 proves same-parity monotonicity only for \(0<y\le1\); it does not state the \(\sqrt3\) endpoint, eventual reversal, or the degree-three envelope on the larger interval.

## value

PASS

The theorem identifies the exact maximal interval on which fixed-variance Student central mass is monotone along both parity chains, proves the endpoint is intrinsic through the first asymptotic correction, and yields a closed unique extremizer. This is a natural sharp phase result in an active anti-concentration problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
