# Review

**Independent audit on 2026-09-29 UTC: correctness passed; provenance/originality repaired.**

## Correctness

The modal sequence is the Jefferson--D'Hondt allocation. Under rational independence, Janson's random-house-size theorem gives the Cesàro limiting law of the bounded displacement vector, hence convergence of every polynomial moment. The Bernoulli-polynomial generating function and the centered-uniform moment generating function reduce the relevant one-coordinate expectation to
\[
e^w((e^w-1)/w)^{n-2},
\]
and coefficient extraction gives the displayed Stirling-number constant. Independent symbolic checks reproduce the stated low-order values.

## Originality and provenance correction

The original standalone novelty framing is not sustainable against repository chronology. The broader record
`2026/09/18/multinomial-mode-cesaro-universality--a66b1067c370`
was first committed at 2026-09-18T20:07:58Z and already proves the polynomial transfer law and the all-order universal log-coefficient means. The record
`2026/09/19/multinomial-mode-cesaro-log-coefficients--69879bbdb548`,
first committed at 2026-09-19T08:07:59Z, already states the same Bernoulli--Stirling formula. The present record was first committed at 2026-09-19T20:31:49Z.

It is therefore retained as an alternate derivation and verification package, not as a separate discovery.

## Scientific value

Useful for reproducibility and for presenting the cancellation in a compact form. Its scientific value is corroborative relative to the earlier SCOPE records.

## Limitations

The theorem assumes fixed dimension and rationally independent probabilities, gives Cesàro rather than pointwise convergence, and supplies no convergence rate. No separate originality claim is made.
