# Independent scientific audit — SCOPE-20260919-4291a5da7308

Audited at: 2026-10-01T14:19:47.879090Z

Disposition: **passed**

## Correctness — PASS

The Hall-product proof reconstructs correctly: the primary power map has one rooted component at the identity, the coprime Hall power map is a permutation, and each cycle carries identical primary rooted trees. Optimizing root selection on each cycle gives the claimed factorization; grouping cycles by element order gives the order-spectrum formula. The cyclic-prime alternating-level matching is valid. The exact verifier independently checks 600 cyclic cases but is not used as the general proof.

## Originality — PASS

Published work supplies the power-map functional-graph structure but no inspected source states the exact nilpotent independent-set factorization or closed cyclic-prime formula. The most plausible 2024 nilpotent power-map paper remained inaccessible in full text after lawful access attempts, so it is a named residual risk rather than novelty evidence.

### Equivalent formulations

No equivalent prior statement was located.

### Broader coverage

The structural theory is broader at graph level but does not, in the material read, compute this independence number.

### Exact database or table

The result is a structural optimization rather than a table lookup.

### Claim versus prior implication

The final theorem is not mechanically implied by the inspected statements.

## Value — PASS

An exact reduction for every finite nilpotent group, together with a closed cyclic-prime formula, is a natural structural result for a newly studied extremal invariant.

## Sources inspected

- Finite groups with large power-avoiding subsets — https://arxiv.org/abs/2609.18513. NOT_COVERING_IN_MATERIAL_READ: The inspected scope concerns large subsets and small defect.
- On the functional graph of the power map over finite groups — https://arxiv.org/abs/2107.00584v2. COVERING_INGREDIENT: Graph decomposition, not independent-set optimization.
- Digraphs of power maps over finite nilpotent groups — https://doi.org/10.1016/j.disc.2024.114000. INACCESSIBLE_PLAUSIBLE_SOURCE: Exact overlap could not be ruled out.

## Residual risks

- Fernandes-Reis (2024) full text remains unverified.
- McVeagh's 2026 thesis was not inspected in full.

## Limitations

- Functional-graph structure is prior art.
- The general nonabelian primary factor remains encoded by rooted-tree statistics.
- The Fernandes-Reis access gap remains an originality risk.
