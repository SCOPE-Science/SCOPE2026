---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For any 2n-support, complementary n-subset pairs produce a cross-polytope boundary ∂C_d, d=binom(2n,n)/2, p=d−1. The witness facet replaces two special n-subsets of [2n−1] by their complements, with full union S and no additional n-subset meeting all face vertices, so its integral cochain is a cocycle taking value ±1 on exactly its own sphere; dual evaluations produce a split, primitive lattice in global H_p. Under a transposition, permutation determinant on all n-subsets is +1, while determinant on complementary-pair sums is (-1)^{binom(2n−2,n−1)/2}; v2 of central binomial equals binary digit sum of n−1, so the sign exponent is 1 iff n−1 a power of two. Induction from support stabilizer gives the integral induced module. A finite-group rational averaging argument gives nonzero quotient homology when eps=0, while published beta9=binom(m,6) yields complete rational triple module. Direct determinant and facet checks corroborated but do not replace all-n proof.

## originality

PASS

Feng–Wang 2024 already supply cross-polytopal spheres and rank lower bound; Feng 2026 determines rational triple Betti numbers, not characters. The new narrow conclusion is the all-n orientation parity, the primitive integral induced-module structure with correct stabilizer sign, and resulting invariant/character statements. The claimed orbit lattice is not all homology for n>=4, and the integral splitting is explicitly not equivariant.

## value

PASS

The sign-vs-trivial orientation law detects an arithmetic power-of-two transition invisible in homology ranks, gives a concrete primitive integral symmetry module, and yields nontrivial rational homology of quotients in the trivial-sign regime. This is a motivated representation refinement of a canonical Kneser complex construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
