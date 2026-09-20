# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The argument reduces the dimension-two code to a multiset of the q+1 points of PG(1,q), where each projective point P corresponds to q-1 scalar-equivalent nonzero codewords of weight n-m(P). Under n=2d+1, minimum distance d forces a unique maximum multiplicity d+1. A full-weight word forces an empty projective point. The local gap d+1 through d+t forbids multiplicities d through d+1-t, so every remaining point has multiplicity at most d-t. Removing the unique heavy point and one empty point leaves at most q-1 points carrying total multiplicity d, proving d <= (q-1)(d-t). Conversely, any distribution of d among q-1 points under the cap d-t, together with multiplicities d+1 and 0, gives the required code. The dimension inequality is met with equality because k=2 and n=2d+1.

The smallest ternary example was checked directly, and the verification artifact enumerates 280 constructed prime-field parameter cases plus 42 small exhaustive sharpness cases. These checks are supplementary; the proof is field-independent and applies to every prime power q>=3.

Adversarial checks considered zero columns, repeated maximum-multiplicity points, and rank loss. A full-weight codeword rules out zero columns; two points of multiplicity d+1 cannot coexist because their multiplicities would exceed n; and the cap d-t<d prevents all residual multiplicity d from lying on one projective point, so the constructed multiset spans PG(1,q).

## Originality

**PASS, to the best of our knowledge.** The motivating preprint arXiv:2609.20344 proves the mirror band only for binary codes, explains that its disjoint-support proof is binary-specific, and says a q-ary analogue would need extra conditions. Its q-ary discussion points to MDS codes, which do not satisfy the local-gap hypothesis, so it does not provide a counterexample satisfying the binary theorem's hypotheses.

Targeted external searches included combinations of “mirror vanishing band”, “q-ary”, “A_{d+1}”, “A_{2d+1}”, “[2d+1,2,d]”, “dimension-two linear code”, “weight distribution”, “projective line”, and “projective multiset”. The searches found the recent binary mirror-band paper, classical/projective-multiset descriptions of linear codes, and unrelated dimension-two cyclic/few-weight code literature, but no statement of the sharp threshold t <= d-ceil(d/(q-1)) or this counterexample family.

The SCOPE archive was searched by the motivating arXiv identifier, mirror-vanishing terminology, q-ary linear-code terminology, and projective-line/weight-distribution terminology; no overlapping successful record was found. Search indexes can lag, so repository state was also checked directly before publication.

Residual risk: the projective-line representation is classical and makes the proof short, so the result may exist as folklore or as an unstated consequence in classification literature. The motivating preprint is also very recent, creating a near-simultaneous-observation risk. No inaccessible source produced concrete evidence of prior coverage.

## Value

**PASS.** The result fills the exact logical gap in the recent binary paper's q-ary boundary discussion: it supplies codes satisfying the full local-gap and dimension hypotheses while violating the mirrored conclusion. The iff threshold is sharp within the extremal dimension-two/full-weight setting, and it shows the failure is robust rather than sporadic: for fixed q the admissible gap is linear in d, and for q>=d+1 it can extend from d+1 all the way through 2d-1.

## Limitations

The theorem concerns dimension two, length n=2d+1, and violation by a full-weight codeword. It does not characterize arbitrary q-ary mirror-band failures, nonlinear or additive codes, or sufficient additional assumptions that would restore a q-ary mirror theorem.
