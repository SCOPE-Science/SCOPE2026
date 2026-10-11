# Scientific review: An exact nine-zero seven-point Fourier witness on the parabola over the eleven-element field

## Correctness — PASS
All seven coefficients are explicitly specified in the degree-ten cyclotomic basis and are nonzero. The criterion for Fourier vanishing is exact reduction modulo the minimal polynomial \(1+t+\cdots+t^{10}\); the verifier visits all 121 input frequency pairs and identifies exactly the nine stated zeros. The polynomial representations were also checked using an independent symbolic remainder implementation. This is a finite theorem with an exhaustive proof, not a numeric experiment intended to prove an infinite statement.

## Originality — PASS, subject to stated literature risk
The closest primary source is Li, arXiv:2609.16030v1: Theorem 4.13 supplies an upper bound ten in the seven-point problem, and Remark 4.15 explicitly leaves the exact \(p=11\) maximum undetermined. Its Proposition 4.11 gives a six-zero example at **five** support points, not seven. The revised v2 theorem focuses on the complete-MUB problem and does not present an equivalent nine-zero seven-support witness. Targeted mathematical record, related published result, and prior-claim searches did not identify an equivalent example. A more recently posted or unindexed equivalent may exist; absence of a hit is not a proof of novelty.

## Value — PASS
The natural exact-support seven-point maximum at the first permitted prime is a specific gap highlighted by the originating paper. Exhibiting nine zeros supplies a nontrivial lower bound close to its first-version upper bound ten and considerably more informative than a generic six-equation linear-algebra construction. The incomplete determination is stated plainly, rather than presented as a full classification.

## Limits and residual risk
The upper bound of ten from v1 is not independently validated here, and the October revised manuscript removes that stronger seven-point statement; the new lower-bound witness does not rely on it. There is no claim to global optimality or a complete enumeration. Cross-source bibliographic searches cannot rule out unpublished or unindexed equivalent constructions.

Same-model review: passed. Independent audit: not yet performed.
