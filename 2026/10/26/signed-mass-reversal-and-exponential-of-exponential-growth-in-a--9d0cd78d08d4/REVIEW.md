# Scientific review

## Correctness (C): PASS

Equations (3), (5)–(8) and (10) of Pezzella's defining source reduce at Gauss–Lobatto nodes \(0,1\), with one sweep, to the componentwise exponential trapezoidal formula written in RESULT.md. The explicit predictor ratio and both corrected values follow by substitution. The exact conservative two-compartment solution is computed by diagonalizing the exchange generator. Strict Jensen convexity proves the predictor mass surplus. Direct series expansion through cubic order gives the signed correction coefficient, and comparison of the two explicit log-endpoints gives the large-step limit. The accompanying verifier confirms stage identities and Taylor coefficients symbolically and runs finite arithmetic diagnostics; the general statements are not inferred from those finite tests.

## Originality (O): PASS (self-review only)

The closest source is Pezzella, arXiv:2606.29523 (Sections 2–6), whose positive SPIDeC stages and diagonal linear stability are established, but whose results do not give the specific two-state conservative exchange mass law. Öffner–Torlo, arXiv:1905.09237, establishes *mass-conserving* modified-Patankar deferred correction, a different flux-weighted update. Torlo–Öffner–Ranocha, arXiv:2108.07347, uses a related two-state exchange example but analyzes different Patankar integrators. Öffner–Redle–Torlo, arXiv:2610.21857, likewise employs modified-Patankar correction. Searches for the precise source, one-sweep exponential trapezoidal map, Markov exchange, mass drift, and exponential-of-exponential amplification returned no exact implication match. This is a scoped originality judgment, not proof that a specialized equivalent cannot exist.

## Mathematical value (V): PASS

The invariant \(u+v\) is essential in mass-transfer and population compartments, not an arbitrary diagnostic. The theorem quantifies a structurally meaningful separation: unconditional stage positivity and exact scalar/diagonal semigroup integration coexist with signed mass reversal and exceptionally severe large-step mass inflation in the smallest coupled conservative system. The explicit small-step coefficient, leading large-step constant, and existence of a mass-error crossing provide a stress benchmark and explain why separately enforcing conservation is material.

## Scientific limits and residual risk

Only the two-node Gauss–Lobatto, one-correction, exact-arithmetic scheme on the symmetric two-compartment exchange generator is assessed. The source's unconditional positivity theorem is not contradicted. Its nonlinear contractivity conclusions require additional hypotheses not established for this system. No numerical threshold uniqueness, multi-sweep extension, or broad method-level failure is claimed. Earlier specialized coverage is possible; independent review has not occurred.

Self-review: passed. Independent audit: not yet performed.
