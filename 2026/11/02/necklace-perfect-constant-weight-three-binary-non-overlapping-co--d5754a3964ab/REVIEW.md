# Scientific review

## Correctness — PASS
Every admissible codeword is unbordered and hence primitive; no two codewords can lie in one cyclic rotation class. For weight three, the only imprimitive words are triple repetitions of one-one blocks, allowing an exact primitive-necklace upper bound. The explicit indexed construction has the same cardinality, and an exhaustive suffix-versus-prefix case split proves non-overlap at every nonempty proper length. The three positive cyclic gap types prove a canonical representative exists uniquely in every primitive class. The standalone verifier independently checks prefixes, suffixes, all weight-three primitive necklace classes, and counts for every length 4 through 40. The finite checks are not substituted for the proof.

## Originality — PASS, qualified
Full-text primary comparisons included Chee–Kiah–Purkayastha–Wang (arXiv:1209.0236), Blackburn (arXiv:1303.1026), and the complete accessible article by Stanovnik–Moškon–Mraz (DOI:10.1007/s40314-024-03055-0). General upper bounds and constructions in these sources do not imply a sharp all-length fixed-weight-three construction. The 2025 paper's primitive-count upper-bound method applies, but supplies no tight weight-three construction theorem. Research-index searches for fixed-weight aliases, necklace saturation, binary sparse frame synchronization, and the displayed formula revealed no dominating theorem. The closest finite code tables and coding-theoretic results concern other parameter regions, models or restrictions. An earlier specialized proof in less indexed literature remains possible; independent historical-priority assessment is pending.

## Value — PASS
Fixed Hamming weight is a standard physically relevant sparsity constraint for synchronization sequences; the exact extremal size under cross-bifix-freedom was not implied by the general unrestricted-code bounds. This result is an exact theorem simultaneously for all blocklengths, constructs a maximal family with a deterministic canonical rephasing rule, and shows zero loss relative to the universal primitive-orbit packing constraint. It also separates an exact low-weight regime from the generally difficult optimization of non-overlapping codes. No claim about noise tolerance or higher weights is made.

## Closest literature and residual limitations
Chee et al. (2012) offer different generic constructions and asymptotic bounds. Blackburn (2013) treats unrestricted alphabets and weights. Stanovnik et al. (2025), Section 3, prove a more general primitive-count *upper* bound but not a construction saturating it at fixed weight three for all lengths. The result is limited to binary weight three; independent review and priority verification have not been performed.

Self-review: passed. Independent audit: not yet performed.
