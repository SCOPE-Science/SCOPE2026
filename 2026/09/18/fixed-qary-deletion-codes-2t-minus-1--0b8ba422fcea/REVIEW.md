# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The claimed extension was checked lemma by lemma against the proof of En Gad, arXiv:2609.19493v1.

The two places where the published proof visibly uses the binary alphabet are sufficient to account for the change.

First, Definition 2.5 and Lemma 2.6 write the symbols immediately outside a maximal \(d\)-run as \(1-d\). For an alphabet \(\Sigma_q\), replace this by two symbols \(a,b\ne d\), with no requirement that \(a=b\). In the proof that the longer and shorter de Bruijn paths meet only at their endpoints, the first forbidden internal coincidence compares \(d\) with the right boundary symbol and the second compares \(d\) with the left boundary symbol. Only the inequalities \(a\ne d\) and \(b\ne d\) are used. The remainder of the bubble construction is unchanged.

Second, Lemma 5.1 charges at most one extra bit when a known \(k\)-stretch is transferred across a deletion. Over \(\Sigma_q\) this becomes at most one extra alphabet symbol. Likewise a bubble header has \(q\) possible edited symbols. For fixed \(q\), both changes multiply the description count by at most a constant to the power \(O_t(R)\), which is absorbed into \((LR)^{a_{q,t}R}\). In the large-witness case the factor \(2^R\) used to pay for one additional component is replaced by \(q^R\), using \(n\le q^R\) when \(R>L\ge\log_q n\).

The unique-substring density estimate was rederived for overlapping windows: two distinct length-\(k\) windows of a uniformly random \(q\)-ary word agree with probability exactly \(q^{-k}\), including when they overlap. With \(k=2\lceil\log_q n\rceil+2\), the union bound leaves at least \(7/8\) of all words.

The exceptional-alignment count changes from \(2^d n^{2d}\) records to \(q^d n^{2d}\), which changes only the constant for fixed \(q,t\). The torus-hash lemma, the linear-dependence witness extraction, the component bounds, and the final bipartite selection use integer spectrum vectors and support incidence only and are independent of the alphabet size.

No computational experiment is required for the theorem.

## Originality

The principal source, arXiv:2609.19493v1 (submitted 16 September 2026), states the binary coefficient-\(2t-1\) theorem and, in Section 8, explicitly says that codes over a fixed larger alphabet appear to share the needed properties and asks whether the coefficient \(2t-1\) holds for them. The present result answers exactly that stated question for every fixed \(q\).

Searches were made for exact and synonymous formulations including “q-ary deletion codes”, “fixed larger alphabet”, “2t-1”, “3 log_q n” for two deletions, and “linear hashing” with deletion codes. No source was found that establishes the same fixed-\(q\) existential coefficient \(2t-1\).

Relevant earlier work found in the search includes Liu–Tjuawinata–Xing (arXiv:2306.02868 / IEEE TIT 2024), which gives explicit fixed-\(q\) two-deletion codes with a larger leading redundancy, and Alon–Bourla–Graham–He–Kravitz (arXiv:2209.11882 / IEEE TIT 2024), whose asymptotic improvement is stated for binary deletion codes.

Because the motivating preprint is only days old, simultaneous responses, later versions, or material not yet indexed are a substantial residual originality risk. The originality judgment is therefore only to the best of our knowledge.

## Value

The result closes an open extension question stated in the motivating paper and shows that the one-power-of-\(n\) gain of the new hashing method is not a binary-alphabet phenomenon. In the important case \(t=2\), it gives existential fixed-\(q\) codes with leading redundancy \(3\log_q n\) rather than the classical greedy coefficient \(4\).

The result is limited to fixed alphabets and is existential; it does not solve the explicit-construction question or the sharp-coefficient problem.

## Review status

The proof, literature comparison, and stated limitations support acceptance under the Phase II standard. No independent validation is asserted.
