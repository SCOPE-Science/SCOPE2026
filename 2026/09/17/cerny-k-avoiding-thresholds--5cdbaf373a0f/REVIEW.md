# Review — Exact k-avoiding thresholds of the Černý automata

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof is based on the exact inverse actions of the two Černý letters.  The
critical normalization step is sound: in a shortest inverse path from a target
set to the empty set, a `b^{-1}` step that fixes the current set can be removed,
and a `b^{-1}` step that enlarges it can also be removed because all subsequent
preimage maps are inclusion-preserving.  Therefore every `b^{-1}` in a shortest
path deletes exactly one state.

For the upper bound, every nonempty proper cyclic subset has an occupied state
whose successor is absent.  At most n-1 inverse rotations align that boundary
with n-1→0, after which one inverse b-step deletes a state.  Repetition gives kn.

For the lower bound, the proposed hard set B_k={n-k-1,…,n-2} is a single block
whose unique occupied-to-empty boundary is n-2→n-1.  It takes exactly n-1 inverse
rotations to align this boundary with n-1→0; the deletion then leaves B_{k-1}.
Induction yields kn, and (ba^{n-1})^k attains it.  The uniqueness argument is
also valid: every other k-set has an exposed boundary alignable in at most n-2
rotations, giving total length at most kn-1.

Exhaustive image-subset BFS for all n≤11 and all 1≤k<n agrees with the theorem
and with uniqueness of the maximizer.

## Originality

PASS, qualified to the best of our knowledge.

The 2021 MFCS paper by Ferens, Szykuła and Vorel defines k-avoiding thresholds
and explicitly records the n=4 Černý values 4, 8, 12.  Its inspected text treats
that as an example and develops general extremal bounds; no all-n Černý formula
was located.  Szykuła's 2026 open-problems survey explicitly records the k=1
Černý threshold n.  These cases are excluded from the novelty claim.

Ferens and Szykuła's 2026 complete-reachability paper states that the Černý
automata meet Don's reaching bound by subset cardinality.  This does not imply
the lower bound here, because avoidance allows the final image to be a proper
subset of the complement; the new inverse-boundary argument is what excludes
that shortcut for the hard targets.

Searches using avoiding, k-avoiding, totally extending, preimage, included
reachability, subset reachability, and Černý terminology did not locate the
general statement at_k(C_n)=kn or the unique-maximizer refinement.  The main
residual coverage risk is older work on circular or 1-contracting automata in
which the same fact could be phrased as a total-extension or included-reachability
result rather than as an avoiding threshold.

## Value

PASS.

The result gives a closed exact formula across the full two-parameter Černý
family, not a fixed small parameter case.  It also supplies a canonical exact
benchmark for the proposed O(kn) behavior of k-avoiding thresholds in
synchronizing automata: the best-known extremal reset family itself has threshold
exactly kn for every k.  The unique-hard-target statement adds structural content
and makes clear why ordinary reaching bounds alone are insufficient.

## Scientific limitations

The result concerns the standard Černý automata, not arbitrary synchronizing or
completely reachable automata.  It does not prove the general O(kn) conjecture.
The exhaustive computation is finite-case corroboration only; correctness for
all n,k rests on the proof.  No independent validation or independent audit is
asserted.
