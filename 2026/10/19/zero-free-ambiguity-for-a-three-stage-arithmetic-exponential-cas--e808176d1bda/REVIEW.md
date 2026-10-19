# Scientific review

## Correctness — PASS
For arbitrary positive offset and increment, the convolution identity is obtained by Laplace partial fractions. A direct Euler-beta calculation produces the rational ambiguity formula with correct phase and normalization, including the zero-delay case. Shifting the numerator polynomial by three gives a quadratic with strictly positive coefficients, hence every numerator root lies in the strict half-plane \(\Re s<-3\). The discriminant gives one exact double-root threshold, and checking all five pole factors establishes the full continuation census. Direct-integral checks for seven parameter combinations, exact symbolic discriminant identities, and roots on both sides of the threshold all passed. The numerical checks are supplementary; the proof applies to every real delay and frequency.

## Originality — PASS (qualified)
The closest inspected primary work is Gröchenig–Jaming–Malinnikova (arXiv:1811.03937v1), whose Lemma 3.1 covers only two distinct exponential factors and whose Section 4 covers repeated identical rates. It explicitly defers higher distinct-rate convolutions. Kloos–Stöckler (arXiv:1311.7359v1) develops the same class of totally positive windows but investigates Zak transforms, not their full self-ambiguity zero geometry. Searches for the exponential-cascade, beta-polynomial, Hurwitz and higher-convolution formulations in indexed mathematical results yielded no equivalent claim. The arithmetic-progression three-rate case with sharp complex-Doppler transition is not directly implied by those inspected sources. Literature coverage is not exhaustive: older unindexed special-function or signal-processing arguments could imply this result, so publication priority is unresolved.

## Mathematical value — PASS
This is a directly motivated first higher-convolution case singled out as requiring analysis in an established study of zero-free ambiguity functions. It supplies a parameter-uniform global nonvanishing theorem for an unbounded two-parameter family of **three distinct** rates, plus the exact location and multiplicity change of all analytically continued complex-frequency zeros. The calculation is an explicit instance of Hurwitz stability arising from total positivity and goes beyond merely restating the two-rate or coincident-rate examples. It does not claim the complete arbitrary-three-rate problem.

## Limitations and closest literature
The results are restricted to rates in exact arithmetic progression; the zeros beyond real frequencies belong only to a meromorphic continuation. The earlier full-text literature does not certify uniqueness of the result across all historical research. Quantitative integral tests cannot replace the full algebraic proof. No independent external mathematical validation is asserted.

Self-review: passed. Independent audit: not yet performed.
