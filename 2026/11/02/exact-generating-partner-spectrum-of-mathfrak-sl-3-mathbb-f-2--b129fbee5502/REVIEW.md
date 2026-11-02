# Scientific review of the binary rank-three Lie generation spectrum

## Correctness — PASS

The claim concerns one finite, explicitly defined 256-element Lie algebra. Rational canonical forms and unit centralizers give exactly seven similarity classes (sizes 1, 21, 84, 42, 28, 56, 24). For each representative, an exhaustive search over all 256 second generators computes the smallest bracket-closed vector subspace; this is mathematically the generated Lie subalgebra. Orbit-invariance transfers these counts to all 256 first generators. A second implementation in an eight-dimensional basis and a third in a nine-bit matrix encoding independently enumerate every one of the 65,536 ordered pairs, reproducing the counts and full dimension distribution. The finite closure process terminates by rank at most eight. Risks: the certificate depends on accurate execution of the supplied source, not on an external theorem prover or independent human review.

## Originality — PASS, qualified

The closest 2026 random-generation paper proves an asymptotic result rather than a fixed \(\mathbb F_2\) exact conditional census. The 2024 paper on two-generation establishes existence; this cannot imply the distribution of generating partners. Chistopolskaya's 2018 Example 3 proves only non-generation with a **nilpotent** second generator when the first is \(E_{12}\), while the new result tests all traceless partners and also identifies a distinct nonextendable idempotent class. Searches for the complete seven-class profile, numeric count 13,440, generating-graph aliases, and matrix conjugacy reductions did not reveal an equivalent statement. The inaccessible full 2024 text and possible older tables are residual priority risks; absence from search results is not a proof of historical novelty.

## Value — PASS

The exact conditional generating invariant is a natural quantitative refinement of the recent random-generation problem, in the smallest rank-three binary case. It exhibits the precise failure of the one-and-a-half generation property: 49 nonzero elements have no partner, despite the existence of 13,440 generating ordered pairs. The seven-class profile and full dimension distribution are reproducible, and the rank-two idempotent obstruction is different from the previously documented nilpotent-restricted obstruction. The result is deliberately a finite exact classification, not a claim about all finite fields.

Self-review: passed. Independent audit: not yet performed.
