# Independent audit — 2026-09-29 UTC

Record: `2026/09/19/unit-rigidity-pro-star-reversible-rings--021b28e85bd3`  
Assigned and audited source tree: `34f7c2746a42dd2f5fb727ef855330eca20481f5`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `ea2f878af985073bc3eec915efa38671681ee35b`  
Disposition: **repaired**

## Correctness

**independently_supported**. The exact equivalence is sound. Pro-star-reversibility applied to u^{-1}u=1 forces u* u^{-1} to be an invertible projection and hence 1. Conversely, in a star-reversible ring with all units fixed, p=ab is central with ba=p; the q=1-p corner gives qb* a=0 and the inverse corner units pa,pb lift to a unit whose self-adjointness yields pb* a=p. Thus b* a=p. The abelian-unit, local, clean, division, and free-algebra consequences follow.

## Originality

**requires_repository_provenance_repair**. The mathematics is not a separate discovery of this record. The exact unit-group criterion already appeared in the SCOPE record unit-group-criterion-pro-star-reversibility--dcd6bac06405, first committed 2026-09-19T10:47:25Z; this record first appeared at 23:20:48Z. Unit rigidity and local/semiperfect collapse were already in pro-star-reversible-semiperfect-rigidity--8cd8850c47f1, committed 2026-09-18T22:24:59Z. The record should therefore be retained only as an alternate proof/consequence package.

## Scientific value

**useful_corroborating_presentation**. The proof is short and transparent and the corollaries are useful, but scientific value is corroborative/expository relative to the earlier repository results rather than a distinct advance.

## Evidence and literature checked

- https://arxiv.org/abs/2609.20076
- https://doi.org/10.1155/2013/650702
- https://github.com/SCOPE-Science/SCOPE2026/commit/82cb7bf9020615c45f0905c06c4c81e201744a04
- https://github.com/SCOPE-Science/SCOPE2026/commit/b45e8bfcc18c75872054854af54075a940dc29fd
## Limitations

- No separate priority claim survives repository chronology.
- The external pro-star-reversible notion is extremely recent.
- The result concerns unital rings with involution.
