# Scientific assessment: exact binary circular subsequence universality

## Correctness — PASS

The fixed-alphabet convention, common cyclic cut, indexed-word counting, and exceptional all-transition cycle are explicit. A binary rich arch contains an adjacent unlike pair, while vertex-disjoint unlike pairs can be ordered by a single cyclic cut and each forms a rich block. Thus the circular index equals a cyclic matching number. Every transition vector has even parity and exactly two binary lifts; a non-all-one vector decomposes uniquely into cyclic zero-anchored runs. The weighted block expression \(B_v=(z+vuz^2)/(1-uz^2)\), cycle pointing operation, two-valued parity projection, and isolated all-ones correction produce the stated rational function. Binomial coefficient extraction yields the claimed exact counts. Boundary lengths one and two and constant words are covered. The independently specified direct universality, matching, and coefficient computations agree on every binary word up to length seventeen (262,142 words); polynomial GF coefficients and total row counts agree through length 256. This is a finite check of the algebra; the lemmas supply the infinite proof.

## Originality — PASS, subject to residual risk

The closest published sources characterize circular universality of a *single* word and provide index algorithms. Their displayed results do not give the all-length indexed binary distribution, a matching reduction phrased for this counting problem, or its bivariate generating function. The publicly indexed linear binary universality distribution counts an ordinary single linear input, not the maximum over its cyclic rotations; the two invariants need not agree. A related unpublished-to-this-record construction where individual targets choose their own cuts is logically stronger as a property but has a different input-observation quantifier and does not state the present exact distribution. Comparison is by quantified claim, not title. Primary texts actually examined are listed in the structured audit; an equivalent cyclic-run enumeration or overlooked table remains an uncertainty.

## Mathematical value — PASS

Circular universality is a natural, established invariant of scattered-subsequence languages. A complete two-parameter enumeration for every binary source length gives exact probabilities and the sharp extremal multiplicities \(2^{k+1}-2\) and \((2k+1)2^k\). The transition-matching equivalence exposes an underlying graph structure that is not visible in a generic one-word algorithm. This is a natural complete enumeration, not an isolated finite table or routine substitution.

## Closest literature and limitations

Barker et al. (2020) establish arch/circular universality basics; Fleischmann et al. (2021) study the arch remainder; Schnoebelen and Veron (2023) give efficient index computation. The result is confined to a fixed binary alphabet and one input-dependent but target-independent rotation, counting indexed words rather than necklaces. No independent outside validation has occurred.

Self-review: passed. Independent audit: not yet performed.
