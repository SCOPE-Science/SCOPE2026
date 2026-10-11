# Scientific review

## Correctness — PASS

The proof reduces the entire complex \(2\times2\) Schatten-four norm to a real, balanced two-coordinate optimization without assuming Hermitian inputs at the outset. The phase bound, monotonicity in the off-diagonal squared-sum, strict convexity of the denominator, and uniqueness of the positive cubic root establish the exact constant. Pattern compression and rectangular-block averaging extend the result to every bounded zero-one Schur idempotent on finite/countable complex Schatten-four spaces. The same-source algebraic identities and a separate standard-library checker support the proof; finite experiments are not used as an infinite-space certification.

## Originality — PASS

Banks–Harcharras (2004), pp.2121–2124, prove the qualitative sharp-gap reduction and explicitly leave the exact triangle-mask norm for finite \(p>2\) undetermined. The present single new claim supplies that missing exact value at \(p=4\). Doust–Gillespie (2005), Section 2, establish contraction of rectangular block masks and broad boundedness results but not the cubic constant. Levene (2013) addresses bounded-operator, rather than Schatten-four, norm gaps. Targeted searches and related published records did not establish a dominating prior result. An older equivalent formula remains possible, and Doust's 2001 contribution was not available in full.

## Value — PASS

The exact threshold solves a mathematically motivated quantitative gap for all complex Schatten-four zero-one projections. It identifies a sharp universal jump of approximately \(0.037541\) above the contractive norm and an explicit smallest-dimensional extremizer. The sharp value is not supplied by the existing qualitative characterization.

## Scope and residual risks

The statement is restricted to the ordinary induced Schatten-four norm and to finite/countable matrices. No exact formula for other exponents or complete boundedness is asserted. The 2001 short proceedings source could only be evaluated from its abstract; a differently titled later derivation cannot be excluded solely by search.

Same-model review: passed. Independent audit: not yet performed.
