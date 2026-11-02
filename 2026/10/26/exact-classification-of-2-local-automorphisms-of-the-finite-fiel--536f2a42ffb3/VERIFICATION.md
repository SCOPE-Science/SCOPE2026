---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

From characteristic derived ideal [L,L]=kf and bracket relation [e,f]=f, the actual automorphisms are exactly alpha_{u,d}(e)=e+u f, alpha_{u,d}(f)=d f, with u in k and d in k^*. The pairwise-witness condition fixes the e-coordinate and forces Phi(lambda v)=lambda Phi(v) even for zero. This defines the slope function sigma and nonzero kappa; for distinct slopes s,t, a common automorphism requires d=(sigma(t)-sigma(s))/(t-s) !=0, so sigma is injective and hence bijective over the finite field. Conversely any permutation yields such a d on any two distinct nonvertical slopes; a vertical/nonvertical pair forces d=kappa; dependent pairs are handled by homogeneity. Distinct parameters give distinct maps. Genuine automorphisms impose affine sigma(s)=u+ds and kappa=d. The characteristic-two q=2 boundary follows because both slope permutations are affine with d=1. Independent definition-level finite-prime-field enumeration checked all 2, 12 and 480 claimed maps at q=2,3,5 against every ordered pair of input vectors and the full ordinary automorphism group, giving genuine counts 2,6,20. Finite testing is not used to prove all prime powers.

## originality

PASS

The inspected 2024 primary results concern linear 2-local maps on characteristic-zero model filiform Lie superalgebras or local maps on nilpotent algebras; the present L is two-dimensional solvable and nonnilpotent, and Phi is not assumed linear. A 2026 same-algebra paper studies relatively-free growth rather than 2-local maps. No matching finite-field permutation-times-scaling classification was located; this is qualified best-of-knowledge priority, not definitive absence.

## value

PASS

Complete classification of a natural local-versus-global automorphism rigidity problem in the minimal nonabelian Lie algebra, with exact factorial counting and sharp q=2 exception. Arbitrary nonlinear maps and finite-field dependence give substantive content beyond ordinary automorphism counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
