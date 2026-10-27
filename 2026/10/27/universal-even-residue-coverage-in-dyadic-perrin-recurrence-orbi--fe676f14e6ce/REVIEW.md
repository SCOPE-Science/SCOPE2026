# Review: universal even-residue coverage in dyadic Perrin recurrences

## Correctness

PASS. The integer identities for the seventh and fourteenth companion-matrix powers were independently recomputed; the three mod-two columns form a basis for every nonzero initial parity triple, and the seven successive first-coordinate rows traverse all nonzero linear forms. The unique resulting index has a first-coordinate value zero mod two and unit normalized increments at both the first and every later doubling scale. A binary-lifting induction proves an exact bijection with all even residues for every modulus, not merely a finite sample. The scale-factor argument correctly covers nonprimitive initial states.

## Originality

PASS, subject to the literature risk below. Brent (1994), Lemma 2 and Theorem 3, proves the maximal period of primitive trinomial recurrences; this *covers* the standard modular period and straightforward cycle census, so neither is attributed to this finding. The non-implied assertion here is the exact even-value bijection along a selected modulo-seven subsequence for **every initial triple**. Sedaghat (2014) investigates zero avoidance for second-order Fibonacci over prime fields; OEIS A104217 tabulates periods for one Perrin initial state; Bravo--Irmak (2024) evaluates valuations for particular Padovan/Perrin sequences. Those inspected results do not state the all-initial-state value-permutation property. Klaška's (2008) arbitrary-initial-state Tribonacci study uses a different characteristic polynomial and its abstract does not establish this result. No proof of uniqueness in the literature is asserted; a related distribution theorem may remain unlocated.

## Mathematical value

PASS. A single-index arithmetic subsequence visiting **every** even residue exactly once is a substantive uniform distribution statement over an unbounded family of nonfield rings; it gives the complete answer (zero zero-avoiding trajectories, including nonprimitive ones) to a natural zero-avoidance problem motivated by earlier recurrence literature. The result is not a restatement of primitive-trinomial maximal periods: an exact first-coordinate value distribution requires extra dyadic derivative and finite-field basis structure. The theorem is specific to a naturally named cubic recurrence and does not claim a general theory of all recurrence polynomials.

## Closest literature, risks, and limitations

The closest decisive source is Brent's 1994 general maximal-period theorem (open preprint arXiv:1004.5439), carefully excluded from the novelty claim. Sedaghat's 2014 zero-avoidance paper is motivation, not direct coverage. Bravo and Irmak's 2024 explicit Perrin valuation theorem concerns particular initial values. Morgan's 1998 *The distribution of second order linear recurrence sequences mod 2^m* treats second rather than third order; full text access was unsuccessful, so potential methodological overlap is a residual risk. General pseudorandom-generator distribution literature may contain an equivalent result under different vocabulary.

The verifier checks all primitive states through modulus sixteen and selected states at modulus thirty-two, but these finite checks are not the proof. The theorem does not address odd prime-power moduli, other cubic recurrences, or exact frequencies of all odd residues.

Self-review: passed. Independent audit: not yet performed.
