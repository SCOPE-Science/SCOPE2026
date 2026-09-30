# Independent audit — 2026-09-30

Record: `2026/09/19/szeged-wiener-equality-near-complete-graphs--a6c30db346eb`  
Assigned and audited source tree: `9c64e339627d616f7d1b9751b9e7bd08e6f2bd89`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `e34557a29888cb7311ae1a062a61655e7b23b1ad`  
Disposition: **repaired**

## Correctness

**independently_reproduced**. The formulas and equality classification are correct. The record's convention differs only by labels from the earlier theorem: its C is the common-neighbor class and D is the neither-neighbor class, whereas the 18 September record uses the reverse convention. Substitution converts all three formulas exactly. Independent definition-level enumeration and the symbolic integer case split reproduce the Zhang–Li family plus the unique n=10 exception and no other high-clique equality case.

## Originality

**requires_provenance_repair**. The broader SCOPE record `2026/09/18/szeged-wiener-equality-clique-n-minus-two--a84aa8e708f8` predates this record by more than a day and already proves the same theorem. It was committed at 2026-09-18 03:47:31 UTC; this record first appeared at 2026-09-19 20:49:32 UTC. The present record is therefore a later rederivation/reproducibility package rather than an independent discovery. No dependence inference beyond the repository chronology is made.

## Scientific value

**useful_corroborating_rederivation**. The alternative derivation, parameterization, and verification remain useful evidence for the correctness of the high-clique classification. Its scientific role is corroboration and reproducibility, not a separate advance beyond the earlier SCOPE theorem.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/commit/c0fc87c28df975025d87707c9327bc68127a1d1c
- https://arxiv.org/abs/2609.20025
- https://doi.org/10.1016/j.amc.2017.05.047
## Limitations

- No separate originality claim remains relative to the earlier SCOPE record.
- The classification is only a partial solution of the global equality problem.
- Finite exhaustive checking is supporting evidence, not the proof.
- Very recent parallel external work remains possible.
