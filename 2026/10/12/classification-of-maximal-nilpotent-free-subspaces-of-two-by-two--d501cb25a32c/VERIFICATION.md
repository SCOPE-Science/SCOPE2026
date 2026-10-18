---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For any field every three-dimensional subspace H_C is trace-orthogonal to a projective nonzero C. Any nonzero nilpotent 2×2 N has rank one, N=vφ with φ(v)=0; tr(CN)=φ(Cv), vanishing iff Cv lies in span(v). Thus H_C avoids nilpotents iff C has no eigenvalue over F_q, equivalently irreducible characteristic quadratic. Count (q²−q)/2 irreducible quadratics, q(q−1) matrices per polynomial, and identify q−1 scalar multiples to obtain q²(q−1)/2 hyperplanes. Scalar-similarity orbit arguments give q/2 orbits size q(q−1) for even q; odd q has (q−1)/2 trace-normalized orbits of that size plus one trace-zero orbit size q(q−1)/2. Independent exact F3 exhaustive matrix/hyperplane/G-action enumeration found nine good H, orbits [3,6]. Actual source verifier and proof inspected; finite case not taken as universal proof.

## originality

PASS

Wigderson Conjecture 8 asks existence of a maximal nilpotent-free space; its n=2 solution and the published Resultary Galois-twist result give existence only, without exhaustive parameterization, hyperplane counts, or scalar-conjugacy classes. de Seguins Pazzis Proposition 1.5 classifies [H,H] for M2 hyperplanes, a different invariant; it has no nilpotent-free census. Irreducible-quadratic algebra is classical and the resulting enumeration remains exposed to earlier geometry-of-matrix-spaces literature.

## value

PASS

The complete classification and orbit-size decomposition of extremizers at the n=2 boundary of a current matrix-space conjecture is a natural finite invariant; existence was already solved, but the exact extremal locus and conjugation moduli provide information not implied by the existence construction and useful for checking higher-dimensional analogues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
