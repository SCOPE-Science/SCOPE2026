# Scientific assessment

## Correctness — PASS

The two-block part follows by subtracting successive suffix-selection marginals, reflecting the forced block-count distributions across the fixed total, and a dimension bound on the image of a finite simplex. The four-party part follows from the forced identity \(b+c-1=p_{23}-p_{14}\), two lower bounds, exact feasible lotteries in both sign chambers, and the equality conditions proving uniqueness. The exact-rational verifier independently enumerates small LP vertices and covers \(1{,}398\) rational profiles; the arbitrary-real and arbitrary-block-size assertions follow from proof, not extrapolation. Potential limits: floor blocks must be distinct, quota and marginal axioms exact, and ties resolved as stated.

## Originality — PASS with residual priority risk

The closest primary literature is La Commare, Tucker-Foltz and Verdugo, *Envy-free Randomized Apportionment* (arXiv:2610.24217v1), particularly Proposition 4.2, Theorem 4.3, and the four-party worked example in Section 4.2. Its general flow and optimization LP cover algorithmic feasibility and numerical minimization, but its inspected statements do not give the general two-block reflection compatibility and measure-zero theorem, nor the unique symbolic optimizer and exact minimum for all four-party two-block instances. Published mathematical-record searches did not reveal an earlier equivalent; this is not proof of unique priority. General LP reduction and unindexed prior symbolic analyses remain material risks.

## Value — PASS

The theorem supplies an exact structural reason why two distinct, repeated floor groups generally cannot achieve zero envy even though randomized rounding is ex-ante fair. It also turns the first nontrivial multiblock optimization cell into an explicit, unique, constant-time lottery and gives a sharp quantitative price for failing the reflection condition. These are motivated by quota rounding and the finite examples of the initiating work, not arbitrary numerical restrictions. The sharp identity simultaneously controls the expected count and the probability of any envy.

## Scope and independence

The theorem is not a universal solution for all floor-block partitions and has not undergone an independent audit.

Self-review: passed. Independent audit: not yet performed.
