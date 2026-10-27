# Scientific review: shortest five-letter crucial Abelian-square-free words

## Correctness — PASS
The claim is restricted to the complete finite domain of length-13 five-letter words, with shortestness supplied by the known general theorem of Evdokimov and Kitaev [1, Theorem 5]. The proof establishes a bijection between alphabet-permutation classes and first-appearance canonical words. At every extension step, rejecting a new suffix Abelian square eliminates precisely the prefixes that have just become forbidden. Thus exhaustive traversal of the stated canonical recursion has no omitted or duplicate canonical candidates. Exact integer Parikh-prefix comparisons determine all append witnesses, and all 14 outputs have one witness per appended symbol. Independently written direct-difference C++ code reproduces the 14 representatives and all four forcing signatures. The reproducible search also checks the values 297,588 visited canonical prefixes, 205,424 length-13 five-symbol square-free prefixes, and 14 right-crucial survivors.

## Originality — PASS, with historical-priority risk
The sharp minimum-length formula and known letter-composition restrictions are due to Evdokimov and Kitaev [1] and are not claimed as new. The relevant theorem, proof, and constructed examples in [1] were compared with the exact new statement: they do not specify all minimizers or their append-forcing half-lengths. Glen, Halldórsson and Kitaev [2] provide a general construction in the broader Abelian-power context, without the full five-letter minimizer census. Avgustinovich and collaborators [3] sharpen general lower bounds for higher powers, not the 14-class finite classification. Searches for right-crucial, minimal, maximal-on-the-right and Abelian-square-free variants, including the proposed counts and parameters, revealed no directly covering record. These searches do not demonstrate historical uniqueness. An unindexed earlier equivalent enumeration is the main remaining scientific priority risk. The related bicrucial problem imposes both-side nonextendability and is not equivalent to the present one.

## Value — PASS
The complete classification answers the natural question of how many structurally different extremizers attain a historically established sharp lower bound. Beyond the count 1,680, it determines **every** shortest example up to symbol renaming and shows that all five appended letters have unique obstruction lengths, with exactly four different joint forcing regimes. This structural information is not supplied by a construction of one extremal word or by the length bound. The result is a bounded but exhaustive fact about a motivated extremal family, not an arbitrary parameter restriction or a sample of long words.

## Limits and references
The result is restricted to five-letter words of shortest length 13. No classification for larger alphabets, longer right-crucial words or bicrucial words follows. The finite search is mathematically exhaustive under the supplied bijection, but an external audit of the proof and a definitive historical-priority assessment have not been performed.

[1] A. Evdokimov and S. Kitaev, *Crucial Words and the Complexity of Some Extremal Problems for Sets of Prohibited Words*, arXiv:math/0205217v1 (2002), Theorem 5.

[2] A. Glen, B. V. Halldórsson and S. Kitaev, *Crucial Words for Abelian Powers*, arXiv:0812.4730v1 (2008).

[3] S. Avgustinovich, A. Glen, B. V. Halldórsson and S. Kitaev, *On Shortest Crucial Words Avoiding Abelian Powers*, *Discrete Applied Mathematics* 158 (2010), 605–607.

Self-review: passed. Independent audit: not yet performed.
