# Independent audit — 2026-09-22 campaign

**Record:** SCOPE-20260907-012  
**Source path:** `2026/09/07/012`  
**Audited repository state:** `1182b71328a408a740c274616869ab885009b620`  
**RESULT.md blob:** `6ef9a358f697e66e162e60797574cebd8a4152ab`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean or expert attestation is claimed.

## Claim audited

For nine distinct moduli chosen from `[7,20]`, the maximum attainable density of a union of residue classes is exactly `1817/2772`, attained by the displayed nine-modulus witness. The `[7,60]` statement is only an interval plus a conjecture.

## Correctness — PASS

The exact witness was recomputed from first principles over its full LCM period: for moduli `[7,8,9,10,11,12,14,15,16]`, residues `[0,4,1,1,0,2,1,0,0]`, `LCM=55440`, exactly 36,340 residues are covered, reducing to `1817/2772`. The reciprocal-sum ceiling for any nine distinct moduli at least 7 is attained by `7,...,15` by monotonicity and equals `62575/72072<1`, so the stated no-full-cover observation is valid.

The translation-fixing lemma is a direct CRT symmetry argument. The prime-peeling formula follows by splitting each residue modulo `L0` into its `p` lifts when `p∤L0`; exactly one lift can be captured by the isolated prime class if the base residue was uncovered. The prime-maximum exchange lemma then follows by averaging over the replacement modulus's residue classes. An earlier independent branch-and-bound enumeration in this same audit campaign checked all 2,002 nine-subsets of `[7,20]`; for this retry I verified that the audited RESULT blob is unchanged and rechecked the maximizing witness independently. No correctness issue was found. The record correctly labels the `[7,60]` equality as conjectural rather than proved.

## Originality — PASS, qualified

Searches included `distinct covering systems maximum density finite moduli`, `nine residue classes moduli 7 20 density`, `covering systems bounded moduli optimization`, and the Hough/Balister literature on minimum modulus and uncovered density. Hough (Annals 2015, arXiv:1307.0874) and Balister–Bollobas–Morris–Sahasrabudhe–Tiba (Inventiones 2022) concern structural/global bounds, not this finite exact optimization table. I found no prior source giving the `1817/2772` optimum for this precise stratum. This is a relative priority finding, not an absolute guarantee.

## Scientific value — PASS

The contribution is modest but nontrivial: it closes a finite optimization stratum exactly and supplies a reproducible optimum/witness plus reduction lemmas useful for larger bounded searches. This is more than a single arbitrary numerical sample because it establishes a global maximum over 2,002 modulus choices and all residue assignments. The `[7,60]` conjecture is not counted as a validated result.

## Final disposition

**PASSED.** The exact `[7,20]` theorem is correct, appears original relative to checked sources, and has concrete benchmark/reduction value.