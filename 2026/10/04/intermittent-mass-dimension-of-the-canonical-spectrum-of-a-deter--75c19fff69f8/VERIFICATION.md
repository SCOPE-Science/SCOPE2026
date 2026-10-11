---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The mixed-radix argument was reconstructed from the stated canonical spectrum. Digit differences are smaller than their base, so each completed level has exactly \(A_n=\prod_{j\le n}M_j\) points. Its radius satisfies \((4/9)P_n\le R_n<(27/52)P_n\), and the next nonzero cluster spacing \(G_{n+1}=P_nh_{n+1}>2R_n\), so \(C(R_n)=A_n\). Last-scale domination and \(r_n/q_n\to s\) give \(\log A_n/\log P_n\to s\). Immediately before the next cluster enters, the same count \(A_n\) persists to a radius comparable to \(P_nh_{n+1}\), and \(N_{n+1}>P_n^{n+1}\) with \(q_{n+1}-r_{n+1}\) a fixed positive proportion forces the exponent to zero. Between completed stages, a uniform cluster-count bound makes the logarithmic exponent maximal asymptotically at the next completed stage, ruling out limsup above \(s\). The proof is genuinely infinite; no finite experiment is used as a substitute.

## originality

PASS

Best-of-knowledge originality passes. Lai--Shi--Xie's primary record constructs the deterministic Salem spectral measure and an exponential orthonormal basis but does not expose the centered lower/upper mass-dimension pair. The closest published Moran-spectrum papers study Beurling dimension or lower discrete Hausdorff dimension, which are different translated-window invariants. Fresh Resultary search found no competing same-spectrum statement.

## value

PASS

The canonical spectrum is a distinguished object in the first deterministic singular Salem spectral construction. Its centered mass growth reveals a strong intermittency invisible in the common Salem dimension: completed stages realize exponent \(s\) while enormous deterministic gaps force exponent zero. This is a natural exact invariant of the construction and clarifies the geometry of its orthonormal basis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
