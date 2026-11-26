---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The nonzero cycle weights make the target squares a basis. Since images of distinct natural-basis elements multiply to zero, their supports are disjoint. Invertibility then forces one nonzero coordinate per image. Comparing squares forces the resulting permutation to commute with the directed successor, hence it is a rotation r. Starting with λ₀, the scalar recurrence c_i λ_{i+1}=λ_i² b_{i+r} closes iff λ₀^(2^n−1)=Δ(c)/Δ_r(b). One step of rotation replaces Δ(b) by Δ(b)²/b₀^(2^n−1), so the diagonal quotient of size d=gcd(2^n−1,q−1) has rotation action by doubling. A representative with all but the last weight 1 and last weight Δ(c) therefore always works. The fixed subgroup of the r-th doubling iterate has size gcd(d,2^r−1), including d at r=0, yielding Burnside's sum also for d=1. For automorphisms the rotation homomorphism hits exactly the stabilizer and the diagonal kernel is parametrized multiplicatively by the d roots for λ₀. The exact sequence makes no splitting claim. For an idempotent, one zero coordinate forces all to vanish; the recurrence x_{i+1}=c_i x_i² gives x₀^(2^n−1)=Δ(c)^−1 for nonzero solutions. It yields d of them exactly in the trivial orbit. Independent checks included an F7 length-two direct test of invertible linear maps against all basis multiplications and full idempotent coordinates, giving class sizes 12 and 24, automorphism orders 6 and 3, and idempotent counts 4 and 1; separate exponent checks cover F4 and F8 length-three classifications and reproduce the F16 length-four five-orbit example.

## originality

PASS

The exact contribution supported here is the one-cycle reduction to the power quotient with residual doubling action and its explicit coupled finite-field classification, class count and stabilizers, with the idempotent boundary as a consequence of the same invariant. General monomial isomorphism, the graph exact-sequence framework, Burnside's method and the idempotent coordinate equation are prior ingredients. The strongest overlapping indexed item, e8db04aa8932, really gives the same core mathematics plus a distribution; that later-dated entry is evidence of equivalent catalogue content, not evidence establishing earlier availability or independent derivation. The inspected primary publications do not already give the complete arithmetic reduction.

## value

PASS

The directed cycle is a basic connected permutation support and a motivated case where algebra structure, automorphisms and solutions of x²=x can be studied together over finite fields. The reduction replaces a large space of structure matrices and change-of-basis choices with an explicit small cyclic orbit problem for any n and q. In particular, among the many possible arithmetic isomorphism classes exactly one has a nonzero idempotent, and the same orbit invariant gives all rational stabilizer sizes. This is useful exact structure, not a table of small cases or a formal relabeling of the general orbit equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
