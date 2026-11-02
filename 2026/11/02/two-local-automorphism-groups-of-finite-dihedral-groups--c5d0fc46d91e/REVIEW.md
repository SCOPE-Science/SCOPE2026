# Mathematical review: two-local automorphisms of finite dihedral groups

## Correctness

**PASS.** For every integer \(n\ge3\), automorphisms of \(D_{2n}\) are exactly \(r\mapsto r^a,\ s\mapsto r^bs\), with \(a\) a unit modulo \(n\). Two-point interpolation on pairs of rotations forces one global multiplier \(u\); pairs of reflections are simultaneously interpolable precisely when the gcd of their index difference with \(n\) is preserved. The necessary unit-multiplier congruence is proved prime-power by prime-power, with the Chinese remainder theorem ensuring the converse. Mixed pairs impose no coupling because a reflection translation parameter remains free. The resulting congruence-preserving reflection permutations split into rooted-tree automorphism groups at each prime power. The number of internal tree nodes gives the complete order formula. The cases \(n=1,2\) are treated separately because the rotation subgroup is not characteristic at \(n=2\). All assertions follow from explicit constructive arguments, not extrapolation.

The checker independently constructs actual dihedral automorphisms and tests every ordered pair for every proposed two-local permutation for \(3\le n\le8\). It also enumerates all underlying-set permutations directly for \(n=1,2,3\). These are corroborations, not substitutes for the proof.

## Originality

**PASS with historical-priority qualification.** Molnár and Šemrl, *Local automorphisms of some classical groups* (arXiv:2604.24299, first public 2026-04-27), define the same two-point group-locality condition but establish results about real and complex matrix groups, not finite dihedral groups. The more traditional equivalent concept is the 2-closure of a permutation group in its given action; treating the word "local" alone as a novelty test would be inadequate. Yu and Pan (2019) address primitive holomorph-type actions, whereas the action here is intransitive and is the natural action of the finite dihedral automorphism group on all group elements. Grech and Kisielewicz (2022) study the 2-closure of abelian permutation groups in general but do not state the present finite-dihedral classification.

Importantly, Klin and Kovács (2010), Theorem 1.1 and Section 6, establish generalized-wreath-product descriptions for automorphism groups of cyclic congruence block structures. The reflection gcd-preserving factor is therefore **not** presented as independently new. The claimed contribution is the exact full-group two-point interpolation classification, the independence of rotation and reflection parameters, and its all-\(n\) index. Searches under "2-local automorphisms", "pair-orbit closure", "dihedral", "gcd distance", and associated finite-permutation formulations found no statement covering those combined assertions. Historical priority against all equivalent coherent-configuration descriptions has not been established by independent audit; another source may imply the formula.

## Mathematical value

**PASS.** The 2026 group-local-automorphism work explicitly motivates determining when local behavior forces global homomorphisms. The theorem completely resolves that question for every ordinary finite dihedral group, not a hand-selected group order: every \(n\ge3\) admits nonglobal two-local maps, and the order and group structure of all such maps are exact. The natural nontrivial arithmetical separation between unit slopes on rotations and congruence isometries of reflections gives a structural mechanism, while the index and rooted-tree factors reveal the extent of nonrigidity. This is a motivated finite-group classification, though no assertion of broad consequences for unrelated group families is made.

## Closest sources and limits

- Molnár–Šemrl (2026), arXiv:2604.24299: identical locality definition, different groups.
- Klin–Kovács (2010), arXiv:1008.0751: strong prior coverage of congruence-block automorphism and generalized-wreath factors; does not state the full dihedral two-local map classification.
- Yu–Pan (2019), DOI:10.1515/math-2019-0063: primitive holomorph-type 2-closures, different permutation action.
- Grech–Kisielewicz (2022), DOI:10.1007/s10801-021-01060-8: criteria for abelian permutation groups, not this generally nonabelian action.

Research limitations: no claim on general finite groups, noncyclic generalized-dihedral kernels, or 1-local maps. Potential implicit earlier coverage through orbital/coherent-configuration language remains a specific historical-priority risk. Independent human validation has not been conducted.

Self-review: passed. Independent audit: not yet performed.
