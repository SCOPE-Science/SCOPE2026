---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The automorphism coordinates (A,f) have A in GL(V), f:V→Λ²V, and W-action Λ²A. The equation (A,f)^2=I gives A²=I and fA+(Λ²A)f=0. Since char q odd, V=U⊕T with eigensigns + and −, W+=Λ²U⊕Λ²T (dim a) and W−=U∧T (dim b). Thus f(U)⊆W−, f(T)⊆W+ and exactly q^(rb+ta) solutions per A. A central shear h=−(1/2)fA conjugates f to 0; quotient involutions with identical r are GL-conjugate. For the model (A,0), P centralizes A iff P preserves both eigenspaces; central g must obey gA=(Λ²A)g, so g(U)⊆W+,g(T)⊆W−; centralizer |GL_r||GL_t|q^(ra+tb). Independently orbit-stabilizer gives same class size using |Aut|=|GL_n|q^(n binom(n,2)). For r=0, I=q^(n binom(n,2)); Gaussian upper estimate [n choose r]_q<=K_q q^(rt) and exact exponent difference bound the total other classes by K_q q^(−n²/4)/(1−q^(−n²/4)) for n>=20. Independent exact integer tests for q=3,5,7 and n=3..35 verified orbit-centralizer identities and the n>=20 upper bound; the small n<20 were NEVER used to claim the asymptotic bound.

## originality

PASS

The familiar free nilpotent Lie automorphism semidirect-product and Λ²V model are published ingredients. The inspected gradings/representation papers do not determine actual odd finite-field involution conjugacy and centralizer cardinalities or their asymptotic distribution. A general semidirect-product involution lemma and H¹ vanishing could shorten the proof but does not provide the explicit all-rank exterior-square count without specialization; possible earlier explicit specialization remains a risk.

## value

PASS

Conjugacy class multiplicities, centralizer sizes and an asymptotic dominant class form a complete natural structural profile of the unbounded free class-two nilpotent Lie algebra automorphism groups. The exterior-square eigenspace arithmetic makes the actual sizes far from a renaming of matrix involution counts, and the large-n concentration law is a useful qualitative transition. General linear-algebra tools are inputs but the exact closed census for the family is a motivated classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
