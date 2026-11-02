# Scientific review: synchronized time-conscious proxy forests

## Correctness

PASS. The theorem fixes one dated action per delegator, a rooted forest with one committed caster per component, and arbitrary integer trust horizons in the stated range. The unique undirected path to the caster forces every chosen delegation to point toward its rooted parent. The recurrence conditions on that parent's actual action time; the child's feasible times are exactly the intervals \([s-h_c(s),s]\). The disjointness of child subtrees proves the additive welfare recursion by induction, while a casting voter's persistent vote is accessible from a child action at any time not before the casting declaration. A heap-based interval stabbing sweep attains the claimed \(O(M+nL\log(L+1))\) operation count and reconstructs a maximizing action set. The explicit four-voter construction has three final-round delegators, separate time-conscious paths and incompatible parent-action times; the at-most-three-voter argument covers both rooted-tree shapes. Exact integer exhaustive comparisons independently checked 3,900 seeded finite instances, with 2,510 feasible and all reconstructed witnesses valid. These computations are corroboration, not proof of the universal statements.

## Originality

PASS under accessible evidence, with residual priority risk. The motivating 2023 temporal delegation paper proves NP-hardness in general and fixed-parameter tractability under retrospective trust; it does not state the exact one-caster forest recurrence, arbitrary-horizon optimization bound, or sharp synchronization obstruction. The 2019 tree delegation result optimizes equilibria of a static guru-preference game, whereas the present theorem optimizes temporal satisfaction with one dated action per delegator. The 2019 restless temporal path work concerns single-path reachability, not simultaneous welfare-optimal choices. The 2023 temporal group-Steiner study has a different objective and temporal feasibility conditions. The checked mathematical-record results address other objects. A more general specialized result not retrieved could nevertheless provide the recurrence as a corollary. The timestamp-synchronized requirement is expressly part of the present object and is not silently attributed to all meanings of the source's confluence axiom.

## Value

PASS. Arbitrary, voter-specific non-retrospective trust horizons are exactly a hard setting for unrestricted temporal delegation. A fixed trust forest with a single caster in each component is a recognizable decentralized organization, and the theorem gives exact utility optimization in time almost linear in the time-expanded input. The four-voter minimal obstruction proves that independently valid proxy paths do not guarantee a simultaneously actionable resolution, even without any cycle in the social support and even when everyone has an approval in the final round. The combination resolves a genuinely motivated structural boundary rather than a numerical sample or a routine scoring restatement.

## Closest literature and limitations

The comparison is with Markakis–Papasotiropoulos (arXiv:2307.12898), Escoffier–Gilbert–Pass-Lanneau (arXiv:1904.05775), Casteigts–Himmel–Molter–Zschoche (arXiv:1909.06437) and Ge et al. (DOI:10.1155/2023/1974161). The claim does not extend to cyclic support, multiple casters in one component, or representations that allow one delegator to use distinct dated actions for different ballots. Originality is bounded by accessible literature. No independent check has been performed.

Self-review: passed. Independent audit: not yet performed.
