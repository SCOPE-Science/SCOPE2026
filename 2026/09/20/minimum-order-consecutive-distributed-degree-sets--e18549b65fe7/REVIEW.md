# Review: minimum order for consecutive distributed degree sets

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The lower bound follows from two extremal degree-sum inequalities: with `y` vertices realizing `[b]`, the `Y`-sum is at least `S_b+y-b`; with `x` vertices realizing `[a]`, the `X`-sum is at most `ax-a(a-1)/2`. Minimizing the resulting order bound forces `y=b` and gives the stated formula.

Sharpness is supported by an explicit pair of degree sequences. The staircase sequence `(b,b-1,...,1)` is self-conjugate. Its excess over `(a,a-1,...,1)` is redistributed into parts of size at most `a`; the original excess partition majorizes the redistributed partition, and adjoining the common staircase preserves majorization. Gale-Ryser then gives a simple bipartite realization of exactly the lower-bound order.

The connectivity claim is separately justified. Positive bigraphic sequences with `e>=n-1` admit a connected realization by a component-merging 2-switch using a cycle edge from one component and an arbitrary edge from another. For the sharp sequences, the inequality `e>=n-1` holds for every `a>=2`. The family `a=1<b` is genuinely impossible to connect because every vertex on one side has degree one. The boundary case `a=b=1` is `K_2`.

The verification artifact checks the constructive Gale-Ryser conditions for 610 parameter pairs and independently exhausts small multiplicity patterns for both ordinary and connected minima. These computations agree with the theorem.

## Originality

**PASS, to the best of our knowledge.** The directly relevant 2014 Manoussakis-Patil paper treats prescribed distributed degree sets of equal cardinality and explicitly records the different-cardinality minimum-order direction as open. The 2015 Iványi-Pirzada-Dar paper removes the equal-cardinality restriction for existence, but its general construction is explicitly noted to usually produce a larger solution; it also records `{1}` versus `{1,2}` as a positive-set obstruction to connected realization. The inspected later `k`-partite degree-set paper focuses on global degree sets and existence.

Targeted searches were made for the exact formula, consecutive distributed degree sets, prescribed partite degree sets, and synonymous minimum-order formulations. No equivalent exact theorem for `[a]` versus `[b]`, nor the connected-feasibility classification, was located in the checked sources or in current SCOPE records.

Residual risk remains from unindexed literature, theses, or alternate terminology. The theorem is deliberately claimed only for consecutive positive sets; it does not claim to solve the arbitrary unequal-cardinality problem.

## Value

**PASS.** The result gives a closed-form sharp minimum for an infinite two-parameter family that lies directly inside the previously identified unequal-cardinality gap. It also shows that minimum order and connected minimum order coincide throughout the entire feasible range `a>=2`, and isolates the exact infinite obstruction family `[1]` versus `[b]`. The proof supplies both a majorization-based realization and a reusable connected-realization lemma for positive bipartite degree sequences.

## Scientific limitations

- Originality is to the best of our knowledge; differently phrased or unindexed equivalent statements may exist.
- Only consecutive positive distributed degree sets `[a]` and `[b]` are treated.
- The equal-cardinality specialization is consistent with prior work and is not claimed as new.
- The computational artifact is corroborative; the theorem rests on the general proof.
