# Review

## Correctness

The model, weights, and top-three event are explicit. The probability of every ordered top-three sequence is the Plackett–Luce product formula. Exact rational enumeration checks all 60 sequences, their total mass, both marginals, the joint inclusion probability, and the resulting positive covariance. This proves the stated finite counterexample and nothing broader.

## Originality

The closest sources address negative association for other sampling laws and first-order inclusion-probability comparisons for successive sampling. published-finding corpus queries and accessible prior-ledger claim searches found no equivalent claim or implication covering this exact model and pair of inclusion indicators. A broader literature search could still reveal a specialized prior result; the claim is deliberately limited to a reproducible finite counterexample.

## Value

Negative association is a strong dependence property often used to justify concentration and product-type bounds. Showing that it fails for a concrete weighted successive-sampling design prevents transferring such guarantees from uniform or rejective sampling without proof. The small covariance magnitude does not weaken the qualitative counterexample, because its exact sign violates the defining pairwise condition.

Closest literature: Joag-Dev–Proschan (1983); Yu (2010 preprint / 2012 journal article). Limitations: one exact design only; no universal sign or asymptotic statement.

Self-review: passed. Independent audit: not yet performed.
