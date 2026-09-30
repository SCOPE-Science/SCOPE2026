# Independent Audit — 2026/09/19/anisotropy-moore-penrose-triple-transfer-adjoint-rings--135669e67f0d

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `8e228d93af1e92b961bf369a29c49714847d5407`
- Disposition: **PASSED**

## Correctness

**PASS** — If h is anisotropic, every subspace is nondegenerate, so for T the decompositions V=ker(T) direct-sum ker(T)^perp and V=im(T) direct-sum im(T)^perp make T|_{ker(T)^perp}->im(T) an isomorphism. Extending its inverse by zero gives all four Moore-Penrose equations, hence every element is MP-invertible and both triple conditions hold. Conversely an isotropic vector u supports a rank-one obstruction. With theta_{p,q}(v)=p h(q,v), the stated choices give ABC=0 but ACB=theta_{u,y} nonzero. If theta_{u,y} had an MP inverse, TT^dagger would be a self-adjoint idempotent onto the totally isotropic line uD; images of self-adjoint idempotents are nondegenerate, a contradiction. Since 0 is MP-invertible, (MP) implies (Z), completing the equivalence. The transpose finite-field specialization is also correct: n=2 is anisotropic exactly for odd q with -1 nonsquare, and every quadratic form in n>=3 variables over a finite field has a nontrivial zero. The submitted F_5 matrices were independently multiplied: ABC=0 and ACB=A with isotropic image.

## Originality

**PASS** — Chen-Wang-Zou introduced the relevant transposed triple conditions in September 2026 and explicitly leave the implication from their zero-product MP condition to the general MP condition as an open question. Classical generalized-inverse literature over fields and semisimple Artinian rings supplies background on existence and proper involutions, but predates these triple-product conditions. The audited theorem solves the new question on the natural class of simple Artinian adjoint *-rings by an explicit rank-one isotropy obstruction and gives the finite-field classification. No pre-existing statement can literally answer the new condition, and targeted searches found no equivalent matrix reformulation covering the same theorem.

## Scientific value

**PASS** — The result identifies a clean geometric invariant—anisotropy of the underlying form—that exactly controls two apparently ring-theoretic MP transfer conditions. It supplies both a positive structural theorem and explicit negative witnesses, and turns the new source question into a complete classification for adjoint endomorphism rings and ordinary transpose matrices over finite fields.

## Sources

- Transposed Triple Products and Pro-Symmetric Rings in *-Rings (Huaxi Chen; Long Wang; Honglin Zou): https://arxiv.org/abs/2609.20084 — Primary 2026 source introducing the triple-product conditions and the open implication addressed by the record.
- The Moore-Penrose inverse of a matrix over a semi-simple artinian ring with respect to an involution (D. Huylebrouck; R. Puystjens; J. Van Geel): https://doi.org/10.1080/03081088808817878 — Classical MP-inverse background for semisimple Artinian rings with involution.
- Generalized inverses of matrices with entries taken from an arbitrary field (M. H. Pearl): https://doi.org/10.1016/0024-3795(68)90028-1 — Classical generalized-inverse background over arbitrary fields.

## Limitations

- The theorem does not resolve the source question for arbitrary *-rings outside finite-dimensional adjoint endomorphism rings.
- The old generalized-inverse literature can overlap with the anisotropy/MP-existence ingredient, but not with the newly introduced triple-transfer question itself.
- Skew-Hermitian forms in exceptional characteristics require the usual nondegeneracy/anisotropy conventions; no broader form-theoretic classification is claimed.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "rank_one_composition_checked": true,
  "finite_field_F5_example_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked before considering institutional retrieval.
