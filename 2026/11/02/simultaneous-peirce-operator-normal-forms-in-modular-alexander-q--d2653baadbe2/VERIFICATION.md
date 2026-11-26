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

On the group basis, a⋆b=Tα(a)Tβ(b) with both factors ordinary ring endomorphisms, including singular β. If an idempotent has augmentation zero then u∈J and u=Tα(u)Tβ(u) repeatedly doubles the ideal power containing it. The presentation K[s₁,…,s_d]/(s₁ᵖ,…,s_dᵖ) with s_i=[e_i]−1 shows nilpotence of J; hence u=0. Otherwise augmentation is one and u is an ordinary unit. Multiplying the idempotency equation out shows L_u M_u=M_u Tβ and R_u M_u=M_u Tα on the entire space, so these are simultaneous similarities and the operators commute. The images of Tβʲ have bases indexed by βʲV, and the stabilized span at step d supports the invertible permutation part. This proves the rank and zero-block formulas by second differences. The fixed-point counts p^dim ker(γˢ−I) give the periodic cycle counts by Möbius inversion. A permutation cycle is cyclic as a K[z]-module with annihilator z^ℓ−1; splitting it for ℓ=pʰe gives precisely the claimed Jordan blocks, also in the wild case. Independently checked the example count: writing u=Σ f_j(S)Tʲ in the F₃ group algebra for the transvection, augmentation one ensures some f_i(1)≠0. The idempotency equation at that i forces Σ f_j(1)S^(−j)=S^(−i), so only f_i has augmentation one. It has 9 choices, and for j≠i the condition (1−S^(j−i))f_j=0 gives 3 choices per f_j in the line spanned by (S−1)². Hence 3·9·3²=243. The rank sequence and cycle lengths in that example also agree.

## originality

PASS

The supported distinct claim is the shared operator conjugator uniformly at all nonzero idempotents in the modular elementary-abelian setting, with its two-sided Jordan analysis. The group-ring transport identity is established prior work; the cycle and second-difference formulas are standard once the common reduction is established. Related complex eigenvalue results or modular rank and idempotent censuses do not cover the claimed pair of operators up to joint similarity.

## value

PASS

The common change of basis removes all dependence on the idempotent at once and gives a computable normal form for the pair. This is useful precisely in modular parameters where a Peirce eigenvalue list loses information or one side is singular: both the nonsemisimple cyclic blocks and the nilpotent blocks are accounted for without enumerating idempotents. The result links an established Peirce problem to explicit data for a natural broad class of quandles, not an isolated small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
