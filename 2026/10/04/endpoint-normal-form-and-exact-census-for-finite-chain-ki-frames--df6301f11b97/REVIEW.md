# Review

## Correctness

PASS. The \(\Box\)-p condition is equivalent on a finite chain to nondecreasing row minima with the empty-row sentinel \(n\): a lower row's minimum is the universal witness required below every successor of an upper row. Dually, \(\Diamond\)-p is equivalent to nondecreasing row maxima with sentinel \(-1\). If both conditions hold, any one nonempty row forces all lower rows nonempty by \(\Box\)-p and all upper rows nonempty by \(\Diamond\)-p, so either every row is nonempty or the relation is empty.

For fixed nondecreasing finite endpoint sequences, no additional cross-row condition remains. Each row contains its two endpoints and independently chooses its strictly intermediate points, giving the stated power-of-two weight. Direct exhaustive checks through four worlds agree exactly with the endpoint criterion and with the independent weighted dynamic program.

## Originality

PASS. Sato's 2026 paper introduces \(\mathbf{KI}\), gives the two confluence conditions, and proves completeness over their intersection, but does not specialize the frame class to finite chains or enumerate it. The 2024 LIK paper uses the same two confluence conditions and studies proof systems and countermodel extraction, but the checked full text contains no chain endpoint normal form or census.

Targeted searches used the aliases downward confluence, forward confluence, local intuitionistic modal frames, stable relations, row minima/maxima, and finite-chain accessibility relations. No equivalent classification or the initial sequence was located. A residual risk remains that the same relation class has been studied combinatorially under terminology detached from intuitionistic modal logic.

## Value

PASS. The frame class is exactly the semantic class used in the completeness theorem for a new modal logic, and linearly ordered intuitionistic worlds are a canonical finite test bed. The result turns two quantified relational conditions into two monotone integer sequences, isolates the unique empty exception, and gives a complete independent-bit representation of every remaining relation. This directly supports exact finite frame generation and semantic experimentation rather than providing an arbitrary small census.

## Closest literature and limitations

Sato (2026), Definition 3.6 and Theorem C.14, are the direct recent source. Balbiani--Gao--Gencer--Olivetti (2024), Definition 2 and Lemma 1, are the closest earlier source because the same forward/downward confluence pair is used for LIK.

The theorem is chain-specific and does not provide a finite-model theorem or an asymptotic estimate.

Same-model review: passed. Independent audit: not yet performed.
