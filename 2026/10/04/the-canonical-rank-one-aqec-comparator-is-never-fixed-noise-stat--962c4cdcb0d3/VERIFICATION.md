---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The inspected package derives an exact one-parameter fidelity formula from the source Kraus family. At the canonical angle, the trace factor has zero first derivative, so only the second source term contributes. Its derivative reduces to a positive prefactor times \((1-g)^2-(d-1)^2a^2g\). Independent symbolic reconstruction in this audit simplifies that expression exactly to \(p(d^2-1+p)/(d(d+1)^2)>0\). The package verifier also constructs the full Kraus operators and decoder and numerically checks the scalar formula against direct entanglement-fidelity evaluation for several dimensions and noise strengths. Hence the positive directional derivative is a genuine feasible improvement, sufficient to rule out stationarity and exact pair optimality.

## originality

PASS

Li--Jiang's primary paper proves that unrestricted high-rank encoding is strictly better and develops a canonical feasible rank-one construction that attains the correct quadratic asymptotic coefficient, but it does not give a closed-form fixed-noise rank-one optimum. The source's stated open direction asks whether the constructed rank-one encoder with the partial-trace decoder is exactly optimal for fixed positive \(p\). The audited positive derivative answers that comparator question negatively while correctly leaving the global rank-one optimum open. No checked Resultary or web source supplied this fixed-p nonstationarity calculation.

## value

PASS

The result sharpens the interpretation of a current AQEC construction: the natural comparator used to obtain the correct asymptotic rank-one gap is not even locally optimal at any positive noise strength. This materially changes how the finite-noise rank-one benchmark should be optimized while preserving the paper's global high-rank conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
