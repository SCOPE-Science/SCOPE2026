# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The theorem reduces the full cyclotomic value to an exact rational
Möbius fingerprint.  After cancellation of a nonempty recovered initial
segment, the remaining quotient has an even number of negative signs and a
unique smallest omitted subset product.  This gives the exact congruence
\[
H_a(P)/H_a(Q_j)\equiv1+2^{a p_{j+1}}
\pmod{2^{a p_{j+1}+1}},
\]
which is precisely the recursive valuation formula.

The startup cases were checked separately because orientation is not known at
the beginning.  For nonsquarefree indices, the true and false valuations are
\(ap_1\) and \(a+1\), which are strictly separated.  For squarefree odd
startup they are \(p_2\) and \(p_1+1\).  When the least prime is \(2\), the
only additional boundary is the presence of \(3\); using \(Q=\{2\}\) when
\(3\nmid n\) and \(Q=\{2,3\}\) when \(3\mid n\) leaves false-orientation
valuation \(3\), strictly below the next missing prime.  The cases \(n=2\)
and \(n=6\) stop before an ambiguous orientation is needed.

The exact-arithmetic artifact checks every index \(2\le n\le1199\) and 100
fixed pseudorandom indices in \([1200,5000]\), comparing the recovered support
with integer factorization.  All tests pass.  This computation supports but
does not replace the proof.

## Originality

**PASS, to the best of our knowledge.** The full text of Shunia's
arXiv:2609.18480v1 was inspected.  It gives paired local valuation identities,
then states local factor stripping by repeatedly applying the squarefree plus
identity to quotient indices.  Its complete single-value reconstruction is
instead developed in Section 5 using \(\log_2\Phi_n(2)\), real fingerprints,
and rounding.  The concluding remarks retain this local-versus-real
distinction.  The inspected text does not state the exact rational residual
formula proved here or a local single-value all-prime-support decoder.

Pomerance--Rubinstein-Salzedo's *Cyclotomic Coincidences* was also inspected at
the radical-reduction, Archimedean inequality, and first-gap statements cited
by the motivating paper.  Those results control cyclotomic size and ordering;
they do not give the 2-adic recursive residuals here.  Shunia's earlier
*Prime-Interval Algebras* recovers interval primes by a different quotient-ring
construction.

Searches for `single cyclotomic value`, `2-adic peeling`, `Phi_n(2) prime
factors`, `Möbius product 2-adic`, and synonymous factor-stripping formulations
did not identify prior coverage beyond the motivating preprint's least-prime
local extractor.  No inaccessible source was identified whose title or indexed
statement specifically suggests the same single-value 2-adic recursion.  The
motivating preprint is only days old, so contemporaneous unindexed work remains
the principal residual originality risk.

## Value

**PASS.** The result fills a clean gap between the two reconstruction modes in
the motivating paper.  The local theory there extracts the radical quotient
and one least prime at a time; the real theory obtains complete peeling from a
single value at the cost of exponentially small real residuals.  Here complete
peeling is recovered locally and exactly from the same integer by rational
2-adic residuals.  The factorial specialization turns the paper's one-real-
value prime decoder into a one-integer-value local decoder, and the interval
specialization recovers every prime in an interval from one cyclotomic value.

The result is structural rather than algorithmic: direct fingerprints can have
exponential subset complexity and the input cyclotomic integer can be enormous.

## Limitations

The index \(n\) is part of the input.  No efficient factorization claim is
made.  Approximate or truncated cyclotomic values are not treated.  The review
does not establish independent validation, formal verification, or exhaustive
literature coverage.
