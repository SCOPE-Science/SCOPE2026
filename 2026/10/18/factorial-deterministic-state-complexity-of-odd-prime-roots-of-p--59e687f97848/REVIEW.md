# Scientific review

## Correctness — PASS
The complete finite-group upper bound, explicit binary witness, prime-cycle characterization, constructive right-stabilizer lemma, Myhill–Nerode distinguishability, and unary strict inequality are proved in `RESULT.md` for every \(n\ge3\) and odd prime \(3\le p\le n\). The critical two-cycle obstruction is proved in both cases of the lemma. The independent finite group enumeration and DFA partition minimization corroborate all tested instances; no finite test is substituted for the infinite proof.

## Originality — PASS within examined sources
The closest accessible root-complexity literature considers unrestricted square roots, nondeterministic square-root complexity, subword-closed input languages, or other automaton operations; these do not imply the new sharp restricted odd-prime lower bound. A related known square-root permutation result covers exponent two but does not supply the prime-cycle stabilizer lemma. Targeted searches for root/power aliases, group languages, sharp factorial automata bounds, and indexed tables did not locate a covering theorem. General root-and-Boolean-operations work (Caron, Hamel-De le Court, Luque, 2020/2022) remained accessible by abstract only and is an explicit originality risk. Absence from search results is not priority proof.

## Value — PASS
The theorem gives a sharp factorial deterministic state-complexity maximum over infinitely many paired parameters and determines the optimal two-letter alphabet size. The main new structural lemma distinguishes a point-cycle acceptance predicate for every allowed odd prime; this result is mathematically more than a finite census or mechanical change of exponent.

## Limitations and remaining risks
The theorem does not cover composite root exponents or primes larger than the input-state count, does not optimize witness lengths, and does not address NFA state complexity. Unavailable broad prior full text and unindexed earlier variants remain originality risks. Finite computations were replayed, but independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
