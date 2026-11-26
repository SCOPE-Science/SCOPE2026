# Independent mathematical audit

## correctness

PASS

The original identification with Belardinelli–Zhang contraction is false: Definition 4.1 gates the addition of the falsifiers of θ at sources satisfying Box θ, not θ. The repaired theorem concerns exactly the original displayed truth-gated dynamics, not that contraction. Unchanged truth sets force the next update to be unchanged. A shrinking inner Box p set gives the one-step existential-outer bound and the two-step universal-outer bound; an increasing inner Diamond p set gives a growing nonempty proper truth set in the double-diamond case and must grow at every nonterminal strict update in the Box Diamond case. Explicit witnesses realize all bounds. The original double-diamond cycle wrongly claimed an empty terminal false set: induction gives D={k+1,…,n−1}, T={k,…,n−2} at the stage k=n−2−t, and the last strict addition saturates the true rows against the still-false vertex n−1. Independent replay at n=3 through 8 matches this endpoint and the n−1 lifetime (branches/dd49d72a-8016-44f9-8b8d-bc93b3fe274c/cycle-terminal-replay.md). The nar­row n=2 bound also follows symbolically: a strict second edge would have to go from the initially inactive vertex to the active vertex, but if missing, the inactive vertex cannot see the first changed row and so remains inactive. The supplied checker was inspected, not executed; the replacement maintains the finite test ranges and adds the cycle endpoint assertion.

## originality

PASS

For the repaired truth-gated rule, no covering statement for the four exact lifetimes was established from the inspected evidence. The strongest indexed comparison uses the same row formula Box Diamond p and a path with the same n-step lifetime, but genuinely different target predicates, with different updated relations already at the initial path step. The defining paper's result for the different belief-gated operator cannot be claimed as context for an identical rule.

## value

PASS

The repaired rule is a natural single-formula directed closure: connect every currently satisfying source to every currently falsifying target, then reevaluate on the enlarged relation. A complete classification of the four length-two modal words shows that interchanging outer and inner modalities can change the sharp lifetime from constant to linear. The two linear bounds differ by one for a structural reason and require different cycling and propagation witnesses. This is a result about the exact rule used, not a claim to resolve lifetimes for the established contraction rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
