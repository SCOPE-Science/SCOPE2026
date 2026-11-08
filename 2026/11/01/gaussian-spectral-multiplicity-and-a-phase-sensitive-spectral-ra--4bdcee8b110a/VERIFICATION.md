---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

RESULT.md Section 1 computes W*W on Fock kernels: D=1-4|tau|²=q(2-q), A=1/(2-q), |B|=(1-q)/[2(2-q)]. After rotating the quadratic coefficient, exact Segal-Bargmann integration gives the multiplication model m(x)=q^(-1/2)exp(-(1-q)x²). For 0<q<1, m has essential range [0,q^(-1/2)], two monotone inverse branches, absolutely continuous scalar spectral measures, no positive-measure level sets or norming eigenvector: ordinary/essential norm q^(-1/4). Composition W^n carries quadratic coefficient tau sum_{j<n}a^(2j); direct Gaussian HS criterion ((1-|a|^(2n))²-4|coefficient|²)>0 yields W² Hilbert-Schmidt if a is nonreal, while all powers remain critical if a real. Conjugation by exp(tau z²/(1-a²)) yields the exact nonzero eigenvalues a^n in the nonreal phase and excludes all eigenfunctions at real phases. Gelfand/Calkin-radius formulas and strong dominated convergence from compact W_r complete the proof. Independently rechecked exact strict phase margins for q=1/4 and 3/5 at real, purely imaginary and off-axis complex slopes; finite checks corroborate, not prove, the spectrum.

## originality

PASS

Comparison across equivalence, broader coverage, exact results and claimed implication finds no decisive existing result that covers the final scoped theorem in accessible inspected material; precise covered ingredients and full-text access risks are explicitly recorded. This is a best-knowledge scientific judgment, not an attestation of independence or a guarantee of historical priority.

## value

PASS

A natural exact noncompact endpoint in one-dimensional Fock weighted composition has phase-blind, twofold absolutely continuous squared-modulus spectrum but discontinuously phase-dependent ordinary/essential radii (compact square versus no compact power). The explicit strong-but-not-Calkin-norm compact approximation is a sharp boundary effect, not an arbitrary renaming or known compact singular-value table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
