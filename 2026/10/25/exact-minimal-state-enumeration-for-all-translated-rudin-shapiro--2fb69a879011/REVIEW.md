# Scientific review

## Correctness — PASS

The exact binary concatenation identity covers every prefix and continuation. Non-ultimate-periodicity of Rudin–Shapiro, together with the elementary consequence that distinct shifts cannot differ by a 2-periodic function, distinguishes the proposed residual states for all suffixes. The cutoff at bitlength plus three is proved using the structure of quotient/remainder intervals; it does not rely on finite searches. Direct counting of quotient levels gives the stated dyadic formula. The companion checker builds and minimizes an independent addition-and-carry DFAO over 2,048 offsets, and also tests 15,000 sample outputs and 17 dyadic instances. These tests are corroborative, not proofs of universality.

## Originality — PASS within examined evidence

The most relevant recent paper, Moradi–Rampersad–Shallit (arXiv:2512.10017, HTML v5 inspected), addresses shifted state complexity, primarily for MSD-first Thue–Morse and powers-of-two characteristic sequences, but does not provide this exact LSD-first Rudin–Shapiro classification. The same-sequence Rampersad–Shallit 2023 work addresses summatory automata. Rowland–Yassawi 2015 lists the four unshifted Rudin–Shapiro kernel states; this is precisely the isolated special case at zero shift, not the translated formula. Semantic research-record and web searches considered shifts, binary kernels, reverse-digit automata, equivalent state minimization, and stronger general coverage. No claim implying the result was identified. Unindexed or differently phrased priority remains a risk.

## Mathematical value — PASS

An exact arbitrary-translation minimal-state formula for a classical pattern-counting automatic sequence is a structural invariant of natural interest. The bounded short-interval method avoids construction and minimization of a new DFAO for each offset and proves a precise linear logarithmic law on dyadic offsets. The theorem is a complete classification in its scope, not an unmotivated finite slice or an elementary restatement of the generic automaticity closure theorem.

## Scope and limitations

The theorem concerns fixed nonnegative additive offsets of the classical Rudin–Shapiro binary coefficient sequence with least-significant-digit-first inputs and arbitrary terminal zeros. It does not cover most-significant-digit-first state complexity or general affine subsequences. Historical priority and mathematical correctness have not received independent expert validation.

Self-review: passed. Independent audit: not yet performed.
