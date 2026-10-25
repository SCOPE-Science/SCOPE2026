---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For every prime power q≡1 mod9, s=(q-1)/3, cubic-residue subgroup K of size s and mu3⊂K, the coefficient change a_u=u^k c(u) bijects the three copies of K. The map f_c multiplies each multiplicative fiber by a_u and is always a permutation; f_c+X permutes iff 1+a_u nonzero and image fiber indices i+j_i form a permutation. Three rotations require constant shift j, three transpositions shift triples are permutations of 0,1,2, giving R=sum_j N_j³, T=3∏N_j. The character sum S=sum_{a∈K}χ(1+a)=(J(χ,χ)-2)/3 follows from χ(-1)=1 and mixed Jacobi sum -1, yielding N_j=(q-4+ζ^-j(J-2)+ζ^j(conj J-2))/9. Orthogonality and cubic factorization yield strict R−T=(q-4)|J-2|²/27, |J|=sqrt(q)>2. The q→∞ expansions require retaining ∑d_j² and O(q^3/2) cubic terms and dividing by s³, yielding 2/9−5/(3q)+O(q^-3/2). Independently enumerated prime fields q=19,37,73: N=[2,1,2],[2,5,4],[8,6,9], (R,T)=(17,12),(197,120),(1457,1296), respectively, and Jacobi-norm identity; original verifier also treats characteristic two q=64. These finite tests do not replace the cubic character proof.

## originality

PASS

The exact mathematical conclusions compared to prior results were not identified as an implication of an inspected stronger result; best-of-knowledge, not exhaustive priority certification. Bell 2013 is material inaccessible overlap risk explicitly named, not dismissed.

## value

PASS

Complete permutation polynomials and cyclotomic orthomorphisms are natural algebraic objects with applications to permutation structure. The conditional density and strict rotation/transposition imbalance for a concrete scalar family measure more than isolated existence examples: an exact all-field arithmetic preference with a norm-controlled second-order term. The parameter k independence follows from subgroup action, not mere renaming. The restricted nature is intrinsic to the motivating scalar criterion, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
