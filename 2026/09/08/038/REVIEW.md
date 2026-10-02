# Review status

Independent audit date: 2026-09-30 UTC.

Disposition: **passed**.

Correctness: PASS. A fresh construction of PSL(2,7) in its degree-8 projective-line permutation model gives 168 elements and the expected class sizes. Direct product-one enumeration gives 4032 tuples for each of the 12 class-position patterns, 48384 total. A fresh braid-generator BFS on these tuples is one orbit of size 48384. One tuple generates the whole group, and Hurwitz moves preserve the generated subgroup, so generation is automatic throughout that orbit. Because the group is centerless, simultaneous conjugation acts freely on generating tuples, giving 48384 divided by 168 = 288 reduced classes, again one component.

Originality: PASS. General Hurwitz-space sources describe braid-orbit/component machinery and asymptotic component counts, but the inspected literature does not tabulate this four-point PSL(2,7) Nielsen class or imply that its 48384 ordered tuples form one orbit. LMFDB supplies group structure, not this braid dynamics. Resultary searches found this exact component census as the matching record and different Hurwitz classes as nearby work.

Scientific value: PASS. Connectedness is the basic global invariant of a Hurwitz space, and this is a natural small simple-group Nielsen class built from the classical 2,3,7 structure. The exact orbit size, reduced degree, and explicit braid witness are reusable data for inverse-Galois and Hurwitz-space computations. The non-invariance of the chosen lift sign also records a useful boundary on a common component-separation heuristic.

Evidence: `INDEPENDENT_AUDIT_2026-09-30.md` and `INDEPENDENT_AUDIT_2026-09-30.json`.
