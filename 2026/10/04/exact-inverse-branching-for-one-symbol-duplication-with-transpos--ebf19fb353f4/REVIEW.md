# Review

## Correctness
**PASS.** Reversing the operation is exactly deletion of a non-first occurrence of a symbol. The deletion-collision lemma identifies equal deletion parents precisely with positions in one constant run, giving the pointwise formula. The maximum follows from a run-length budget, and the edge count follows by summing run boundaries and singleton first runs. The verifier independently rebuilds both channel directions on finite parameter ranges.

## Originality
**PASS.** The closest inspected source, Polyanskii–Vorobyev, defines the same duplication-with-transposition graph and parent/child relation but uses indegree only to define roots and studies root distance for arbitrary duplicated blocks. Its inspected main-results material does not state a one-symbol inverse-degree formula, an extremizer classification, or an edge count. Searches under several equivalent parent/preimage/indegree/run formulations did not locate a covering statement. A residual risk remains that the elementary length-one specialization has appeared in an unindexed note, thesis, or differently phrased derivation.

## Value
**PASS.** Inverse degree is the exact one-step list ambiguity of the mutation graph. The theorem turns that ambiguity into a transparent run statistic, gives the sharp worst case for every alphabet and block length, and supplies the exact global edge count. This is a complete structural invariant for the atomic length-one case rather than a finite parameter census.

## Closest literature and limitations
The primary paper studies the broader operation but a different invariant: asymptotic distance to roots. The present theorem does not extend to longer duplicated blocks or repeated/noisy operations, where deletion collisions can have more complicated overlap geometry.

Same-model review: passed. Independent audit: not yet performed.
