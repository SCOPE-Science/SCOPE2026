# Scientific review

## Correctness — PASS
The proposed state machine computes parity of every selected length-three input factor exactly. Reachability filtering and Moore refinement produce the intrinsic minimal automaton; the finite label-profile breadth-first search then exhaustively determines the shortest inhomogeneous path or its absence. The pre-existing general opacity theorem translates the path length into normalized opacity. The supplied verifier checks all 256 masks, their exact exceptional classes, and 524,288 direct factor-count cross-check values, giving a finite certificate for the infinite automatic-sequence statement. The uniqueness assertion has a separate explicit recovery argument.

## Originality — PASS
The original Allouche--Yao paper proves a general method and works examples, but does not contain the exact 256-predicate, seven-exception classification. The inspected all-one-pattern literature does not give the census either. The claim is not a mere singleton-pattern assertion: sums of parity counters are not covered by separate opacity values, since taking minimal quotients can create or eliminate incompatible incoming labels. Targeted semantic and bibliographic comparisons found no covering result. Residual priority risk remains for equivalent unpublished or unindexed enumerations.

## Value — PASS
This is a natural complete classification of the first binary multi-pattern parity family in which all eight three-bit local contexts may independently contribute. It explicitly quantifies the rarity of nonzero opacity and gives the exact exceptional sets, demonstrating nontrivial cancellation/composition behavior under XOR. The classification can serve as a reproducible baseline for longer-window and larger-alphabet problems; such extensions are not asserted.

## Limits
The result is computationally assisted finite case analysis with a proved reduction, not a new general opacity algorithm. Scientific priority has not been independently adjudicated; complete reproduction requires running the included source.

Self-review: passed. Independent audit: not yet performed.
