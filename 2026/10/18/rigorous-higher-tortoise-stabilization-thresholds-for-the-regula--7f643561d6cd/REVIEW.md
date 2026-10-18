# Scientific review: higher-tortoise thresholds for paperfolding

## Correctness — PASS

The claim is the four exact eventual thresholds \((13,14,25,26)\) for iterates \(k=2,3,4,5\). The prefix-lifting lemma is proved directly from the factorization of a binary word at its \((k+1)\)-st one. The residue-template lemma proves completeness of the finite factor sets, not just agreement with a long experimental prefix: a length at most \(2^r\) interval contains at most one index divisible by \(2^r\), all other paperfolding bits depend only on the start modulo \(2^{r+1}\), and both possible exceptional bits occur. The exact finite certificate gives collision counts at lengths \(12,13,24,25\) and injectivity at \(13,14,25,26\), respectively. Each injective-length factor has enough ones for lifting to all longer lengths. The standalone program reproduces the certificate. No finite prefix is used as an infinite proof.

## Originality — PASS within examined evidence

Campbell and Rampersad, arXiv:2604.25811v2, Section 5, explicitly state all four numerical values as computational expectations; they do not provide proofs for these higher iterates. Their proved Theorem 3 is restricted to one iteration. Therefore the numerical sequence itself is **not** new, but a complete all-length proof of the four unproved assertions is not implied by that paper. Defant and Kravitz, *Stack-sorting for words* (2020), introduce the map and study sortable multiset words rather than paperfolding factor-complexity thresholds. The relevant prior research-record results concern other infinite sequences, including period doubling and Sturmian words. No equivalent proved covering statement was identified in the actual targeted searches. Residual priority risk: an unindexed independent proof may exist.

## Value — PASS

This establishes four exact infinite-length results that the originating study had only reported computationally, including the first higher iterates beyond its one-pass theorem. The 32- and 64-residue factor templates constitute transparent, small, complete certificates, and the prefix-lifting lemma explains why a finite calculation proves eventual injectivity. It gives a reusable structural verification method for questions about iterated tortoise images of binary automatic sequences, without implying an unsupported law for larger iterate counts.

## Scientific limitations

No general formula for \(s(k)\) at \(k\ge6\) is claimed. The direct finite-prefix cross-check is auxiliary; the proof rests on the exact residue cover. Matching numerical predictions from earlier work are expressly credited. Historical priority beyond inspected accessible sources is not certified. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
