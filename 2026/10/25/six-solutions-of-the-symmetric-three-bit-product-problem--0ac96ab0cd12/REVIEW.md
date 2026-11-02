# Independent mathematical audit

## correctness

PASS

The explicitly cited Kaneko–Stoll Theorem 2.2 gives ab<2^(-13+4*3*3)=2^23 for positive odd factor weights (3,3) and product weight 3. Therefore each factor and product is one of exactly 231 odd three-bit integers 1+2^i+2^j, 1<=i<j<=22. The package implements both complete factor-pair search under the strict product bound and independent product-divisor search. Fresh independent integer enumeration reproduced all six pairs, the 231 product candidates, and eleven ordered solutions, with direct bitcount checks. The external infinite bound, not the finite enumeration alone, proves exhaustion over all positive odd integers; it was verified against the cited theorem statement. No inference is made for negative/even factors or other weights.

## originality

PASS

The broad finiteness bound and binary-weight product problem are already Kaneko–Stoll; the 2026 published Resultary asymmetric (3,2,3) census is a different parameter slice. Kaneko–Stoll primary theorem/proof do not exhibit the six (3,3,3) solutions in inspected statements. The new content is complete finite classification of the natural first symmetric weight-three case under the established bound, with qualified priority against unindexed small-weight tables.

## value

PASS

The symmetric first nontrivial binary digit-weight product slice has a natural finite answer not supplied by the global exponent bound; six exact sporadic solutions and the proof of exhaustiveness answer a concrete arithmetic classification problem. It is a self-contained exact classification despite reliance on a published reduction, not a claim to improve general digit bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
