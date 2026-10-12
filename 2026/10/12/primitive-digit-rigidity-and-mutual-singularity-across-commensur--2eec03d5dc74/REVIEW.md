# Review

## Correctness — PASS

The proof translates both iid expansions to a common base \(b^{mn}\), where their digit laws are explicit finite products. Unequal common-base laws are singular by disjoint strong-law digit-frequency events, while equal common-base laws yield identical measures. Equality of product laws across length-\(m\) and length-\(n\) partitions forces each primitive block to split independently across every internal cut, using coprimality; Chinese remaindering makes every primitive digit identically distributed. Endpoint ambiguities have measure zero because all digit probabilities lie strictly between zero and one. Positive cylinders prove full topological support. The verifier's exact 64-by-12 logarithmic constraint matrix has rank ten, and five complete rational compatibility cases pass; these are diagnostic, not proofs for infinitely many parameters.

## Originality — PASS, with priority risk

Pfeffer, Smith, and Severa, *Induced Distributions from Generalized Unfair Dice* (arXiv:2309.07366), Theorem 3.3, prove the fixed-base singularity test; Question 5.1 specifically raises two dice with different numbers of faces. Once the bases share a power, their theorem supplies a corollary when the induced common-base vectors differ. The new contribution is the necessary-and-sufficient primitive-digit **rigidity** description of when those vectors instead coincide, which is absent from their statements and the inspected fixed-base stationary-digit papers arXiv:2001.08492 and arXiv:2201.01521. Targeted searches across alternative iid block and product formulations found no equivalent published claim; priority under different terminology is not independently certified.

## Value — PASS

This classifies **all** strictly positive iid digit measures for every pair of commensurable, unequal integer bases, a natural complete subclass of the different-base problem posed in the cited paper. Its equality condition is a rigid, uniquely parameterized \((b-1)\)-dimensional family rather than a mere test against a large induced vector, and the complementary measures are mutually singular despite their identical full supports. The conclusion is structural and applies to all admissible bases and probability vectors, not a finite example or an arbitrary numerical refinement.

## Scope and limitations

The result does not classify multiplicatively independent bases or zero-weight alphabets. Known same-base frequency arguments are explicitly credited; full comparability and external priority review remain open.

Self-review: passed. Independent audit: not yet performed.
