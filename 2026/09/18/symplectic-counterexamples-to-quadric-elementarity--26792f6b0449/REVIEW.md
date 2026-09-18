# Review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

The proof was checked against the finite-index formulation in Faraco--Rungi's Definition B.1, not merely against literal setwise preservation by the full group.

For a connected group, the ordinary closure of any finite-index subgroup is again finite index and therefore open; connectedness forces the closure to be the whole group. Hence a projective quadratic form fixed after passing to finite index would also be fixed projectively by the entire connected symplectic group. For a connected semisimple group, a fixed projective line in a linear representation defines a continuous one-dimensional character. Its differential vanishes on the semisimple Lie algebra, and connectedness makes the character trivial. Thus a projectively fixed quadratic form would have to be genuinely invariant.

For the standard symplectic module, no nonzero invariant quadratic form exists. Sp(2m,R) is transitive on nonzero vectors, so an invariant quadratic form would be constant on V minus the origin; comparing v with 2v and using quadratic homogeneity forces that constant to vanish. The symplectic form identifies V equivariantly with V*, so the dual-quadric case is identical. This covers degenerate as well as nondegenerate forms because Faraco--Rungi formulate elementarity equivalently as fixing a point of the projectivised symmetric-square representation.

The ambient non-density claim is also direct: Sp(2m,R) is an algebraic subgroup defined before projectivisation by g^T J g=J, and for m at least two its dimension m(2m+1) is strictly below 4m^2-1, the dimension of PSL(2m,R). Thus its projective image is a proper algebraic subgroup and cannot be ambient-Zariski-dense.

The surface-group corollary uses Audibert's theorem that Sp(4,Z) contains Zariski-dense surface subgroups. A finite-index subgroup of such a surface subgroup has the same connected Zariski closure PSp(4,R); therefore any invariant projective quadratic form would extend to PSp(4,R), contradicting the main theorem.

## Originality

Faraco--Rungi's arXiv:2609.18436 was inspected at Definition B.1, Theorem B.2 and Problem 1.6. The paper proves the quadric/Zariski-density equivalence in PSL(3,R) and explicitly asks whether the same characterisation extends to PSL(n+1,R) for every n at least two. The source was submitted on 16 September 2026.

Searches covered the exact paper title together with symplectic/PSp terminology, the phrases non-elementary iff Zariski-dense, preservation of quadrics by PSp(4,R), symplectic groups and invariant quadratic forms, and synonymous formulations involving projective symmetric-square fixed points. No source was found that answers Faraco--Rungi's Problem 1.6 by the standard projective symplectic subgroup or states the sharp first failure in projective dimension three. The current SCOPE repository was also searched by the source identifier, problem terminology, symplectic group, quadric preservation and Zariski-density formulations; no overlapping record was found.

The classical facts about symplectic and semisimple representations are not claimed as new. Audibert's existence theorem for Zariski-dense surface subgroups is likewise prior work. The originality claim is limited to applying these ingredients to the newly posed higher-dimensional elementarity problem, isolating the general symmetric-tensor obstruction, proving failure for every odd projective dimension at least three, and observing the discrete surface-group consequence in dimension three.

No inaccessible source was identified whose title or available metadata specifically suggests this same answer. Because the motivating problem is only days old, unindexed or unpublished parallel work remains a residual originality risk.

## Value

The result gives a complete negative answer to the proposed equivalence part of Problem 1.6, identifies the first dimension in which the dimension-two theorem can fail, and supplies an infinite family of counterexamples. More importantly, it explains the structural reason for failure: a quadric-based definition only sees symmetric degree-two invariants, whereas proper irreducible algebraic subgroups can instead be defined by tensors of another symmetry type. The surface-group corollary shows that the obstruction is relevant to the representation-theoretic setting motivating the source paper, rather than being only a Lie-group-level pathology.

## Limitations

The result does not classify higher-dimensional elementary subgroups and does not determine the status of the proposed equivalence separately in every even projective dimension. It gives an obstruction to quadric-based characterisation rather than a complete replacement definition. The surface-group corollary in projective dimension three relies on known existence of Zariski-dense surface subgroups in Sp(4,R); no claim is made that every natural family of surface representations exhibits the same phenomenon.
