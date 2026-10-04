# Review

## Correctness

PASS. The source's Theorem 5.2 gives a finite-world witness bound controlled by the single-negation subformula closure and modal depth. With formula length \(n\), these parameters are at most \(2n\) and \(n\), so \((4n)^{n+1}\) safely bounds the number of worlds. Lemma 5.1 preserves the epistemic world set when moving to standard arithmetic. Theorem 5.6 then compresses relevant constant values to at most \((|C_\varphi||W|+1)(B+1)\); explicit successor syntax gives \(|C_\varphi|,B\le n\).

A full model description has \(2^{O(n\log n)}\) bits. Equivalence checking and direct bottom-up semantic evaluation, including the pairwise test for knowing-value formulas, are polynomial in that certificate size. Hence nondeterministic \(2^{O(n\log n)}\) time is sufficient.

## Originality

PASS. Wang states finite model property and decidability but does not give a standard complexity-class upper bound. Candidate-specific published-finding and literature searches for the exact source together with NEXPTIME, exponential certificates, and satisfiability complexity did not locate this consequence. Earlier knowing-value complexity results concern logics without the successor-arithmetic extension and therefore do not imply the stated upper bound for \(\mathrm{ELKvSA}^r\).

## Value

PASS. The primary paper explicitly motivates its logic as balancing arithmetic expressiveness with computational tractability, but its final decision result is only qualitative. Converting the quantitative finite-model proof into a standard nondeterministic time bound gives a reusable complexity baseline for the new logic and sharply constrains future exact-complexity work.

## Closest literature and limitations

Wang (2026), especially Lemma 5.1, Theorem 5.2, and Theorem 5.6, is the direct source. Ding (2016) gives PSPACE-completeness for a related conditional knowing-what logic without successor arithmetic.

The upper bound is not claimed optimal and excludes public-announcement reduction blow-up and succinctly coded successor exponents.

Same-model review: passed. Independent audit: not yet performed.
