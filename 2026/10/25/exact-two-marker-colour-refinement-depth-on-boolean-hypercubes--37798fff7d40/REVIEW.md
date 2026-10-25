# Scientific review — exact two-marker colour refinement on Boolean hypercubes

## Correctness — PASS

The proof gives a complete induction that the r-th partition is exactly the pair of distances capped at r+1. Its forward step uses neighbor counts at distance R-1, and its reverse step uses the four coordinate flip multiplicities, with separate cases for capped coordinates. Injectivity thresholds on the full (i,j) orbit grid prove all three exact first stable rounds, including d=1 and t=d. The stabilizer is S_t x S_(d-t), giving the exact (t+1)(d-t+1) class census and binomial cell sizes. Full-graph enumeration in 45 configurations and separately built weighted quotients in 820 configurations reproduce all intermediate partitions and depths; these are corroboration, not the infinite proof.

## Originality — PASS (qualified)

The new theorem is the exact roundwise two-marker capped-distance profile and sharp depth for q=2 at all separations. The general 1-WL and equitable-partition literature, specialized perfect-colouring paper, and earlier mathematical formulas for one-root Q_d, marked q=3/4 Hamming graphs, unmarked path powers and Johnson graphs do not, on their stated claims, entail the binary two-marker depth law. Searches of indexed mathematical research records for aliases, source objects and equivalences did not surface a directly covering result; this does not establish uniqueness. The result could be implicit in broader equitable-partition or distance-regular graph literature.

Closest known results used for implication comparisons include the related one-root statement `d6b37563-f9ee-4c6c-9100-cf47adf59958`, the ternary and quaternary marker claims `963ce3c1-04f1-45eb-a0f8-76d74fd6a7db` and `a5e4bc3a-5970-4d79-8d0f-4238f125698b`, and the primary scholarly references listed in the mathematical result. The first is a one-root result; the others address different alphabets, and none asserts sharp binary two-root rounds. The main unresolved risk is a stronger, unindexed theorem on distance-regular graphs or equitable pair-distance partitions. The publisher abstract of the AAAI paper was read, but its full text was not used to rule out coverage.

## Mathematical value — PASS

The exact number of synchronous refinement rounds after individualization is a natural complexity statistic in graph isomorphism and finite-model-theoretic counting refinement. The theorem determines the entire refinement filtration for a canonical family, proves full pointwise-stabilizer orbit recovery, and gives an all-dimensional sharp three-regime phase diagram in seed separation: no speedup for adjacent roots, one-round saving for intermediate roots, and near-halving for antipodes. These contrasts are not determined by the one-root count and are useful as exact structured benchmarks rather than an arbitrarily chosen numeric slice.

## Scientific limitations

The checker is finite and cannot establish the general theorem by itself. No case with more than two markers or a nonbinary alphabet is claimed. The originality conclusion is based on identifiable comparisons, not a declaration that searching proves novelty. The result is not independently audited or certified.

Self-review: passed. Independent audit: not yet performed.
