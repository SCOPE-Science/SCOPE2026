# Independent audit — 2026-09-29

Record: `2026/09/18/symplectic-counterexamples-to-quadric-elementarity--26792f6b0449`  
Assigned and audited source tree: `2793be6a86516fa8b7dd7f2587cff320199fe346`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The symplectic counterexample is correct. A finite-index subgroup of a connected Lie group has dense closure; a projective quadratic line fixed by it is therefore fixed by the whole group. For a connected semisimple group, the scalar action on that line is a continuous one-dimensional character with zero differential, hence trivial. The standard Sp(2m,R)-module has no nonzero invariant quadratic form: Sp acts transitively on nonzero vectors, while homogeneity would require q(2v)=4q(v) for two vectors in the same orbit, forcing q=0. The symplectic form identifies V with V*, so the dual symmetric square is also excluded. PSp(2m,R) is a proper algebraic subgroup of PSL(2m,R) for m≥2 by its defining equations and dimension. Audibert's theorem supplies Zariski-dense surface subgroups in Sp(4,Z), so the discrete surface-group corollary follows as well.

## Originality

**qualified_source_specific_resolution**. Faraco–Rungi's September 2026 paper poses the higher-dimensional quadric-based characterization problem, while the symplectic representation-theoretic ingredients are classical. Current searches did not locate this direct PSp counterexample applied to that newly posed problem. Originality is therefore accepted only for the application/resolution and its first-failure observation in projective dimension three, not for the classical facts about symplectic representations or semisimple characters.

## Scientific value

**meaningful_negative_resolution**. The construction gives an infinite family showing that quadrics cannot detect all proper algebraic subgroups in higher projective dimension and supplies discrete surface-group examples in the first failure dimension. This directly changes the answer to the proposed generalization while also indicating why a higher-dimensional notion of elementarity must use richer invariants.

## Evidence and literature checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/symplectic-counterexamples-to-quadric-elementarity--26792f6b0449
- https://arxiv.org/abs/2609.18436
- https://arxiv.org/abs/2307.06791

## Limitations

- The result refutes the quadric/Zariski-density equivalence but does not classify higher-dimensional elementary subgroups.
- The projective-dimension-three counterexample uses classical symplectic structure; novelty is the application to a very recent problem.
- No complete substitute invariant for higher dimensions is proposed.
