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

The determinant proof reconstructs correctly. Translation reduces to \(K=\{0,a,b\}\) with \(D=(\omega^{a^2}-1)(\omega^{b^2}-1)-(\omega^{ab}-1)^2\). If \(N\mid ab\), vanishing is exactly \(N\mid a^2\) or \(N\mid b^2\). Otherwise the sine-phase identity forces \(N\mid(b-a)^2\); with \(c=b-a\), \(X=\omega^{a^2}\), \(R=\omega^{ac}\), the determinant factors as \(-X(R-1)^2\), so vanishing is exactly \(N\mid a(b-a)\). The order/coset formulation follows by writing \(d=gr\), \(q=N/g\). An independent direct complex-determinant check for every triple and every \(3\le N\le35\) found no discrepancy with the criterion.

## originality

PASS

Best-of-knowledge comparison distinguishes the local iff criterion from the published global square-free theorem. Caragea--Lee state that, for \(N>4\), all principal \(3\times3\) Fourier minors are nonzero iff \(N\) is square-free; this implies existence/nonexistence globally but does not identify which triples are singular for a general nonsquarefree composite modulus. Resultary returned the assigned local criterion as the exact semantic hit and nearby Fourier results address different objects. Complete primary text of Caragea--Lee could not be obtained in this run: open full-text retrieval was unavailable and the permitted institutional retrieval returned an Oxford worker error. That access limitation is retained as a residual priority risk rather than converted into a failure.

## value

PASS

The singular locus of the smallest nontrivial principal Fourier minors is a natural exact invariant. The theorem upgrades a global square-free boundary to a complete local arithmetic classification for every composite modulus and supplies equivalent order/coset and valuation forms. That is a structural classification, not a tiny numerical instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
