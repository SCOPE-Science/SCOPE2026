# Scientific review

## Correctness — PASS

The invariant splitting of the star Laplacian is exact for every allowed \(n\), and the leaf-edge perturbation acts only on the \((n-1)\)-dimensional unit-eigenvalue space. Positive-semidefinite rank and trace, strict Jensen concavity, and the incidence Gram equality conditions prove the global minimum and classify all optimizers. Strong concavity plus the exact squared Gram identity proves the quantitative gap. The accompanying script checked 14,107 instances, including every tested overlap pattern and unequal-weight case. Computation is corroboration only; the infinite claim rests on the analytic proof.

## Originality — PASS with stated search limitations

The closest inspected classical studies split the two design decisions: fixed-weight link selection for network coherence (Summers et al., arXiv:1411.4884) and continuous conductance allocation on a fixed topology (Ghosh, Boyd and Saberi, SIAM Review 2008). Kooij and Achterberg's 2023 NP-hardness theorem covers general unweighted edge augmentation, but does not imply a closed star solution. Bhoite et al.'s 2026 mixed-integer and semidefinite study directly includes joint-budget graph augmentation in general, yet its inspected theoretical claims and methods do not state the exact star matching rule or overlap penalty. Search and access are not exhaustive; stronger specialized or unstated prior coverage remains a risk. The precise novel candidate is the simultaneous exact value, all-minimizer classification and constructive quantitative penalty, not the well-known objective or problem formulation.

## Mathematical value — PASS

The theorem resolves all admissible resource allocations for an infinite natural family under a nonconvex count constraint, allowing general positive continuous weights. It proves that local reinforcement should be distributed across disjoint leaf pairs and quantifies every deviation from that configuration. Both the exact cost curve and stability inequality are relevant to sparse robustness upgrades of hub-and-spoke networks. The count restriction and fixed original spokes are substantive, explicit boundaries.

## Literature and verification limitations

No independent audit or independent validation has been performed. The finite checker is not an infinite proof. Potential coverage by other specialized Kirchhoff-index star-augmentation papers is not excluded, and the 2026 generic numerical optimization manuscript contains a related model, not an inspected sharp star theorem.

Self-review: passed. Independent audit: not yet performed.
