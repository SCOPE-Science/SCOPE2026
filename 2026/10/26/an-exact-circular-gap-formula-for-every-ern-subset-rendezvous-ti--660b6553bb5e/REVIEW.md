# Self-review

## Correctness — PASS

The proof is valid for every integer \(n\ge2\) and every nonempty subset. The displayed word rotates a chosen state to zero, uses the monotone map induced by \(ba^{n-1}\), and merges all other occupied residues at exactly the stated length. The potential \(F\) decreases by at most one under every letter, with the unique two-state-to-singleton boundary checked separately; it gives a matching global lower bound. Independent reverse-BFS calculations confirmed all \(65{,}518\) nonempty subsets for \(2\le n\le15\). The infinite result rests on the proof, not the finite evidence.

## Originality — PASS, with identified risks

The 2020/2022 Behague–Johnson primary article defines the same individual-subset weight and develops size-wise extremal estimates for the Černý family; its relevant sections do not state a pointwise exact formula for every labeled subset. A prior pair-distance result is a genuine special case but does not imply all larger-subset distances. Szykuła–Zyzik develop general subset-search algorithms, not this closed form. Searches also identified closely related work on rank compression and avoidance, but no stronger statement covering all labeled subset distances. Cardoso's 2014 dissertation is a plausible source that could not be fully inspected; the residual risk is real, and a failed search is not novelty proof.

## Mathematical value — PASS

The finding supplies a structural shortest-path potential, an all-subset exact metric, and an explicit shortest-word construction in the standard slowly synchronizing family. It resolves each prescribed initial-state uncertainty set in time proportional to its ordered size, instead of just the minimum, maximum, or pair cases. These are natural synchronization invariants with direct use for deterministic reset control and benchmark computations; the result is not a routine numerical increment.

## Limits

Applies only to the stated Černý family, does not classify optimal-word multiplicities, and retains the source-access originality risk. Independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
