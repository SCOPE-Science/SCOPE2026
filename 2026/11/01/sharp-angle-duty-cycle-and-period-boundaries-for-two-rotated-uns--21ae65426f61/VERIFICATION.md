---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The two exponential factors have positive-definite undamped product and half-trace S=c²cosh(pT)+(1-c²)cosh(pΔ), determinant one; the Floquet multiplier radius is exp(-aT+arcosh S). Thus stability is equivalent to S<cosh(aT). At balanced dwell the ratio sinh(aT/2)/sinh(pT/2) is strictly decreasing, giving one cutoff iff 0<c<a/p, with c=0 all-period exception and c>=a/p impossibility. The fixed-duty deficit has even Taylor coefficients p^{2k}[c²+(1-c²)m^{2k}]-a^{2k}; monotonicity of weighted power means makes their signs change only from negative to positive, so F(T)/T^{2K} increases through exactly one zero when the average is Hurwitz. The stated exact Δ*, strict fractional shrinkage, logarithmic c->0 and sqrt(T*-T) limits follow from these identities; c=1 gives no stability. A direct independent 2x2 eigenspectrum/expm check agreed in three nontrivial parameter sets; finite checks are not the proof.

## originality

PASS

Only the sharp simultaneous angle, duty and physical-period classification and its exact edge laws are considered candidate new; Floquet criterion, fast-Hurwitz-average sufficiency and general matrix-product monotonicities are explicitly prior. Closely related mechanical results have a restrictive companion-matrix geometry. Best-of-knowledge pass; older full texts may contain an equivalent derivation.

## value

PASS

The canonical engineering/math design question is exactly how rotation angle, dwell imbalance and switching period stabilize two unstable flows. The theorem gives the complete admissible phase diagram, sharp timing robustness, optimal equal duty and singular c->0 and c->a/p limiting laws; these are not just substituting a special value into the standard Floquet spectral-radius criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
