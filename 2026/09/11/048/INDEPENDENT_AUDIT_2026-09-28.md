# Independent Audit — 2026/09/11/048

**Audit date:** 2026-09-28 (UTC)  
**Audited tree:** `3a5dc9dd07d38146e62e77b2695378a67303504f`  
**Disposition:** **REPAIRED**

## Correctness

The structural torsion conclusion is sound, but the exact ordered rank 189 is not proved by the supplied certificate. After the lifted collapse, C_3=0, so H_2(F_5;Z)=ker(d_2) is indeed a subgroup of a free abelian group and therefore torsion-free; this alone disproves the requested Z/2 witness. The unordered computation also certifies H_2(B_5;Z)=Z^3 using a rational rank. For the ordered complex, however, the scripts compute rank(d_2)=31731 only over F_2,F_3,F_5,F_7,F_1000003. Modular rank gives rank_Q(d_2) >= 31731, hence rank H_2(F_5;Z) <=189; agreement over several primes is strong evidence but not a proof that the rational rank is exactly 31731. The source's statement that five-modulus agreement 'pins' Z^189 is therefore unjustified.

## Originality

The unordered Z^3/torsion-free theta result overlaps an earlier published SCOPE finding and known theta-graph homology theory, so that portion is not new. The ordered-cover structural conclusion for this exact n=5 target—torsion-free H_2 and therefore no transfer-killed 2-torsion witness—remains a distinct, reproducible consequence of the lifted two-dimensional model. The repaired claim deliberately drops the uncertified exact ordered rank.

## Scientific value

The repaired result still completely answers the target’s existence question: no Z/2 class can occur upstairs at all. It also gives a rigorous rank interval 3 <= rank H_2(F_5;Z) <=189: the lower bound follows from transfer applied to the certified Z^3 downstairs, and the upper bound from the modular rank certificate. This is useful fixed-n information even though the exact ordered rank remains unresolved.

## Limitations

- Exact rank 189 for H_2(F_5;Z) remains unproved by the supplied modular calculations; a rational/integer rank certificate or an independent theorem is required.
- The repaired statement uses only the certified two-dimensional model, exact unordered rank, covering transfer, and modular rank lower bound.
- No integer matrix for p_* is computed; the target is nevertheless refuted because H_2(F_5;Z) is torsion-free.

## Evidence

- [SCOPE042, H_2 of unordered configuration spaces of the theta graph is torsion-free](https://github.com/Resultary/2026/tree/main/2026/9/11/SCOPE042): Already records unordered theta H_2 torsion-freeness and rank 3 at five particles, so the repaired record does not claim novelty for the downstairs computation.
- [Chettih–Lütgehetmann, The homology of configuration spaces of trees with loops](https://doi.org/10.2140/agt.2018.18.2443): Provides torsion-freeness results for ordered configurations in a restricted graph class and general H_1 machinery; it does not directly supply the exact ordered theta n=5 H_2 rank.
- [Wawrykow, Homology Generators and Relations for the Ordered Configuration Space of a Star Graph](https://arxiv.org/abs/2401.13821): Shows the current ordered-configuration literature is sensitive to graph class and particle number; no exact theta n=5 H_2 rank 189 theorem was found here.

Repository evidence was read from `SCOPE-Science/SCOPE2026` at tree `3a5dc9dd07d38146e62e77b2695378a67303504f`; comparison against current `main` found no changes under this record path since the assignment snapshot. No repository writes were made by this audit.
