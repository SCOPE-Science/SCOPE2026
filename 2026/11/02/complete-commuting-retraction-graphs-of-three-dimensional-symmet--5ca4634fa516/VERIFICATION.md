---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The endomorphism matrix is necessarily (A,0; psi,mu) because the commutator ideal is Kz. Bracket preservation is A^T diag(1,lambda) A=mu diag(1,lambda); idempotence gives A^2=A, mu in {0,1}, psi A+mu psi=psi. If mu=1, invertibility forces A=I and psi=0. If mu=0, the image of A is totally isotropic, so anisotropy yields only 0 and I; in the split case the two distinct isotropic lines each contribute q choices of complement/kernel and q central lifts. Distinct rank-one projections on the same isotropic line never commute. Across the two isotropic lines they commute exactly when opposite lines are their kernels, yielding K_(q,q) plus 2q(q-1) isolates. The complete clique, centralizer, maximal-subsemigroup and commuting-probability formulas follow by counting graph vertices/edges. Independent enumeration directly multiplied idempotent matrices at q=3 and q=5, checking 18 and 50 noncentral vertices and q^2 edges respectively; source code also covers prime and F9 fields. The proof, not finite tests, supports arbitrary characteristic not 2 and all odd q.

## originality

PASS

Existing primary classification determines this Leibniz structure and automorphism group, but invertible automorphisms exclude precisely the noninvertible idempotents at issue. The specific two-isotropic-line projection compatibility and full commuting graph with clique, centralizer and probability profiles are not consequences of the inspected automorphism theorems. Originality is qualified by possible unlocated retraction/commuting-graph results for equivalent two-step algebras.

## value

PASS

The splitting of a natural nonassociative algebra's symmetric bracket form controls the entire commuting graph of retractions and its maximal commuting subsemilattices. Exact centralizer profiles and a sharp q-dependent commuting probability are intrinsic structural invariants, not merely normalization or a single small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
