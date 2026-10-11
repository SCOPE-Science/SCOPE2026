# Independent mathematical audit

## correctness

PASS

Multiplicativity gives the exact equation \(p^a+1=qR_a(p)\). Reducing \(X^a+1\) modulo the monic integer polynomial \(R_a(X)\) gives an integer remainder \(B_a\). For a solution, \(R_a(p)\) divides \(B_a(p)\). The verifier excludes positive integer roots of every nonzero remainder, bounds \(p\) from the degree gap using the coefficient \(\ell_1\)-norm, and then enumerates every prime within the resulting finite bounds. A fresh independent exact replay reproduced 34 divisibility pairs, the maximal coefficient bound \(1082\) at \(a=35\), and exactly the four prime quotients claimed; candidates.tsv supplies explicit factors for all 30 composite quotients.

## originality

PASS

The motivating Trudgian paper materially inspected in full asks whether equality between the unitary and exponential divisor sums occurs infinitely often, reports the five values through one billion, and records the remote example \(2^{49}\cdot4363953127297\). The current OEIS A236474 similarly tabulates examples. Neither source states that the four displayed \(p^a q\) triples exhaust every singleton-cofactor layer through exponent 49. Resultary searches returned the audited finding as the exact hit but no distinct earlier finding that implies its finite-layer completeness.

## value

PASS

The exponent-49 example is specifically highlighted in the primary literature as a remote equality instance. Proving that every singleton-cofactor two-prime layer up to that example is exhausted, and that there is no new layer between 6 and 49, is a meaningful literature-anchored finite cutoff rather than an arbitrary search horizon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
