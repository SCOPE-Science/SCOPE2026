# Independent audit — Exact prescribed color-class sizes for graphs of maximum degree two

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/17/prescribed-colorings-max-degree-two--9aaf81e2ad5d`
**Audited tree:** `d8068c714cbe04f17b56f36d5f6893685ea43cb6`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The local path/cycle lemma is correct: a maximum requested multiplicity no larger than the component independence number permits the stated gap construction. The global network-flow reduction is also exact. For a color subset S, the min-cut condition is sum_{i in S} a_i <= sum_j min(L_j, |S| alpha(Q_j)); one color yields alpha(G), two colors lose exactly one vertex on each odd-cycle component, and three or more colors make every component constraint automatic. Integral max flow then gives the desired exact multiplicities. An independent exhaustive check over all path/cycle component multisets through 9 vertices and every integer partition (3,885 cases) matched the criterion.

### Independent checks

- Re-derived the path/cycle local multiplicity criterion and checked endpoint/cyclic boundary cases.
- Re-derived the max-flow/min-cut inequality including the source-edge contribution and verified the reductions for |S|=1,2 and >=3.
- Independently brute-forced every disjoint union of paths/cycles through total order 9 and every integer partition: 189 graph types and 3,885 graph/partition pairs, with no mismatch.
- Checked the r=2 remainder-sensitive corollary using alpha(G)>=ceil(n/3) and o(G)<=floor(n/3).

## Originality

Birken’s arXiv:2609.18629 (submitted 2026-09-16) proves a broad skewed-coloring theorem and leaves a remainder-sensitive strengthening as Conjecture 5; Kuchukova–Perkins–Povill provide the surrounding fixed-class-size problem. The audited theorem gives a complete per-graph profile characterization for all maximum-degree-two graphs and implies Birken’s remainder-sensitive statement for r=2. Fresh searches through 2026-09-29 found no equivalent two-inequality characterization in prescribed-coloring or chromatic-symmetric-function language.

### Literature checked

- https://arxiv.org/abs/2609.18629 — Birken, A Hajnal–Szemerédi Theorem for Skewed Colorings; closest live prescribed-coloring theorem and Conjecture 5.
- https://arxiv.org/abs/2603.08259 — Kuchukova–Perkins–Povill, Sampling Colorings with Fixed Color Class Sizes; fixed-profile coloring context.
- https://arxiv.org/abs/2201.07333 — Matherne–Morales–Selover, Newton-polytope/chromatic-symmetric-function context; does not cover odd-cycle maximum-degree-two graphs in this exact form.

## Scientific value

This is an exact structural classification, not a small instance. It isolates the only global obstructions, determines all stable-partition types for the entire maximum-degree-two class, immediately gives saturated Newton polytope for each finite variable restriction, and settles a live remainder-sensitive conjectural base case.

## Limitations

- The theorem is restricted to finite simple graphs of maximum degree at most two and does not address counting, sampling, or higher maximum degree.
- Originality remains a best-of-knowledge assessment; no concrete prior equivalent characterization was located.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
