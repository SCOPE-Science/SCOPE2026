# Review

## Scientific claim reviewed

For every integer f >= 5, the strict greedy 2-sumfree sequence S_{f,2f+1} is exactly the set stated in RESULT.md; consequently its first-difference sequence has minimal preperiod f+1 and minimal period f+2.

## Correctness

**PASS.** The proof has two separate obligations and addresses both.

1. **Eligibility of every claimed term.** The finite prefix is checked directly. For the periodic tail, all prefix-plus-tail and tail-plus-tail residue sums modulo M=5f+1 are shown to miss the tail residue set. The distinctness restriction is handled explicitly in the only tight prefix calculation: distinct sums from Q=[2f+1,3f] start at 4f+3, so the candidate term 4f+2 is not accidentally excluded by a doubled summand.
2. **Exclusion of every omitted integer.** The complement after the prescribed seed is partitioned into explicit gap intervals. Each gap is identified as f+Q, the distinct-pair sumset of Q, Q+X_k, Q+Y_k, or Q+Z_{k-1}. All summands are distinct and occur earlier than the excluded integer. This proves the greedy equality, not merely 2-sumfreeness of a candidate set.

The difference block follows directly from the exact set formula. Minimality of the preperiod uses the value f+1, absent from the eventual block; minimality of the period uses the unique occurrence of 2f-2 in each block for f>=5.

A standard-library brute-force verifier agrees with the formula for 5 <= f <= 80 through the first 300 sequence terms in every case. This is supplemental evidence, not a substitute for the proof.

## Originality

**PASS, to the best of our knowledge.** The principal source, van Berkel--Bosma (arXiv:2609.18522), states the general eventual-periodicity conjecture, gives the period-length conjecture, and describes proved families through g<=2f while supplying computational evidence beyond that boundary. For d=f+1, Definition 3 predicts period length f+2, but the paper does not state a proof of the infinite line f>=5. Its worked example f=3,g=7 is therefore not claimed as new here.

Searches covered the exact notation S_{f,2f+1}, the equivalent condition g=2f+1, strict/greedy 2-sumfree terminology, the explicit block endpoints in the theorem, the source-paper title, and recent follow-up references. No source located a proof equivalent to the theorem. The earlier arXiv:2609.16843 is also relevant; the later source explicitly describes its established 2-sumfree range as g<2f and adds the boundary g=2f among confirmed cases.

The main residual originality risk is temporal: arXiv:2609.18522 was submitted on 2026-09-16, so a simultaneous or immediately subsequent proof may not yet be indexed. No specific inaccessible paper was identified as likely to contain this result.

## Value

**PASS.** This is an infinite-family theorem on the first uniform parameter line immediately beyond the currently proved boundary in the source paper. It confirms a nontrivial slice of a newly stated global periodicity program and supplies an exact structural description, including the modular tail and minimal (pre)period lengths, rather than another finite computation.

## Review status

Same-model review: passed. Independent audit: not yet performed.
