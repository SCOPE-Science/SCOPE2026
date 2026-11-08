---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Direct local truth-table conversion yields (Fx)_i=x_i xor(d_{i-1} OR d_i). Existing walls persist and each zero-wall gap of length g is invaded from both ends until at most one zero remains, giving T=max floor(g/2). Even cyclic wall parity and 2 binary lifts per wall word give C_n(t)=2+2 sum_even_k (n/k)[z^(n-k)](1+...+z^(2t+1))^k. Two-wall extremizers yield 2n or 4n terminal shell for n>=4; transfer-matrix even projection gives B_n=(L_n+2cos(2pi n/3))/2. Independent disjoint windows in the n-1 freely distributed walls prove logarithmic concentration. Independent dynamics and shell checks n=3..10 agree; finite enumeration does not prove all n.

## originality

PASS

Best-of-knowledge qualified originality: the precise complete claim is not shown to be implied by the inspected primary sources, searched published findings, or general results. Pre-existing components are explicitly credited; inaccessible source material remains as named residual risk.

## value

PASS

The full transient first-entry distribution and worst-versus-typical logarithmic clock are natural dynamic invariants of Rule 178: they refine known eventual two-period behavior and qualitative wall motion, and give an exact reproducible census for every ring length, including odd lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
