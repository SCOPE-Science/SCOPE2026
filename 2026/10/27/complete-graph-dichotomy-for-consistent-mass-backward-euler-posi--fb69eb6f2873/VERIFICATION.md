---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The local element matrices assemble to M=(ell/6)(2D+A), K=(D-A)/ell; positive definiteness of M and semidefiniteness of K give invertibility, and K1=0 gives P1=1. With h=t/ell^2 the normalized step matrix has adjacency coefficient 1-6h. At h=1/6 the update is (2I+D^{-1}A)/3. For h>1/6 the step matrix is irreducible Stieltjes, giving a strictly positive inverse by the nonnegative Neumann walk series, hence strictly positive P. For 0<h<1/6, let b=1-6h and S=M+tK. The identity bP=I-3ell h S^{-1}D forces S^{-1} to have nonpositive off-diagonals if P has nonnegative off-diagonals. S^{-1} is positive definite and irreducible (a block split would also split S), so its inverse S would be strictly positive, contradicting a missing graph edge. For K_n, the constant and orthogonal subspaces give eigenvalues 1 and (2n-3)/(2n-3+6nh); this proves the remaining signs. At h=0 P=I. An independent exact check assembled local matrices and performed rational elimination at seven normalized steps for all 771 connected labelled graphs on 2–5 vertices: 5,397 checks agreed, including equality, strict signs and row sums (private replay: /workspace/branches/replay/euler.py and euler.txt). The finite checks do not replace the all-graph proof.

## originality

PASS

Supported for the full graph-topology dichotomy and the uniform necessity on every positive subthreshold step of every connected noncomplete graph. The numerical threshold as a sufficient bound, the inverse-positivity lemma, and sharp classifications in prior special families are not independently new.

## value

PASS

For a natural space-time discretization, a practitioner can decide exactly when nonnegative input data are preserved from connectivity and completeness alone, with the sharp physical length scaling. The missing-edge obstruction covers every subthreshold step rather than merely asymptotically small steps, and completes the topology classification beyond the bipartite/cycle cases and mesh-dependent sufficient bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
