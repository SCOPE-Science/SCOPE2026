# Same-model review

## Correctness
PASS. Proposition 10 of Stanovnik–Moškon–Mraz supplies the exact SQN representation of \(S(q,6)\). The proof then performs exhaustive algebraic optimization of every SQN branch after the symmetry \(x\leftrightarrow y\): the fifth and fourth levels are optimized linearly; the third level is handled by concavity; the critical cubic branch is normalized and bounded by an exact stationary-envelope argument; the remaining branch is separated by the strict bound \(1/16<1024/15625\). Integer rounding is handled uniformly by \(c=\lfloor q/5\rfloor\). The universal conclusion does not depend on the finite scan in `verify.py`.

## Originality
PASS. Blackburn's full text poses eventual \(k=n-1\) optimality as a conjecture. The 2024 exact-SQN paper states that the conjecture remains unresolved, gives no simple formula for larger word lengths, and limits its exact multi-alphabet tables to \(q\le6\). Current literature searches through later restricted-overlap work, published-finding corpus searches using formula and alias variants, and the prior ledger found no result implying the full \(q\ge10\), \(n=6\) statement. The closest published-finding corpus item is the analogous length-five theorem; the closest prior length-six ledger item covers only \(q=7,8,9\).

## Value
PASS. This is an infinite-tail exact theorem resolving a named open direction at length six, not a routine extra table row. It supplies a closed maximum formula in a regime for which the published SQN method was computational rather than analytic and isolates a provable large-alphabet dominance mechanism.

## Closest literature and limitations
The closest primary sources are Blackburn's 2013 preprint, which supplies the conjecture and construction, and Stanovnik–Moškon–Mraz (2024), which supplies the exact SQN reduction. The theorem does not enumerate maximum codes, does not classify all equality cases, and does not settle lengths at least seven. A non-indexed duplicate remains a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
