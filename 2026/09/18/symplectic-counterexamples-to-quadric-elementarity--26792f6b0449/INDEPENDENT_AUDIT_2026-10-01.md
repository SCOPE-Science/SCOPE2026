# Independent mathematical audit — SCOPE-20260918-26792f6b0449

Final disposition: **PASS**.

## Correctness
**PASS.** The representation-theoretic obstruction was reconstructed. A finite-index subgroup of a connected group has dense closure unless the whole group disconnects into finitely many open cosets; therefore a projective quadratic fixed by finite index is fixed projectively by the full connected symplectic group. The scalar action on that line is a one-dimensional character, which is trivial for a connected semisimple group, so an actual invariant symmetric tensor would exist. The standard symplectic group has none: it acts transitively on nonzero vectors, so an invariant quadratic form is constant on nonzero vectors, while homogeneity under \(v\mapsto2v\) forces that constant to be zero. Duality via the symplectic form handles \(\operatorname{Sym}^2(V)\). Finally \(\operatorname{Sp}(2m)\) is a proper algebraic subgroup of \(\operatorname{SL}(2m)\), with smaller dimension, so its projective image is not ambient-Zariski-dense.

## Originality
**PASS.** Faraco-Rungi's very recent paper establishes the projective-dimension-two equivalence and poses the higher-dimensional quadric question. Resultary searches found the assigned symplectic counterexample but no earlier answer using \(\operatorname{PSp}(2m,\mathbb R)\) or an equivalent alternating-form obstruction. The standard representation-theory facts are classical, but their application supplies a direct answer to the newly posed problem. Full text of the Faraco-Rungi preprint was unavailable through the lawful routes tried, so hidden discussion outside the accessible abstract remains a residual risk.

### Equivalent formulations
The quadric definition was compared through its precise representation-theoretic equivalent formulation.

### Broader coverage
The classical ingredients are broader but do not by themselves state the answer to the newly posed quadric/Zariski-density problem.

### Exact database or table
No finite database/table is intrinsic to this problem; the check targeted prior published answers.

### Claim versus prior implication
The counterexample is a new application to the posed characterization problem rather than a corollary already stated in the inspected source.

## Value
**PASS.** A simple classical family immediately answers a newly posed higher-dimensional characterization problem in the negative, identifies the first possible failure dimension, and explains structurally why quadrics cannot detect all proper algebraic subgroups. The discrete surface-group corollary shows the obstruction persists in the intended representation-theoretic setting. This is a motivated counterexample, not an arbitrary type check.

## Source inspections
- **Branched real projective structures on surfaces and geometrisation of representations** (https://arxiv.org/abs/2609.18436): primary abstract; open-access and authorized full-text retrieval attempts did not yield a verified PDF Assessment: ABSTRACT_ONLY_WITH_RESIDUAL_OVERLAP_RISK. Evidence: The accessible primary record concerns projective surface representations and indicates further higher-dimensional directions; the exact problem statement was checked against the assigned scientific package.
- **Maximal representations in lattices of the symplectic group** (https://arxiv.org/abs/2307.06791): primary abstract Assessment: SUPPORTING_DISCRETE_INPUT. Evidence: The source supplies Zariski-dense surface subgroups in the relevant symplectic lattice setting.

## Residual risks
- The Faraco-Rungi preprint could not be inspected in verified full text during this run, leaving a genuine overlap risk for an internal remark or example.
- The theorem does not classify all higher-dimensional elementary subgroups or settle every even projective dimension.
