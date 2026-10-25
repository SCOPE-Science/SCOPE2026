# Review of exact right-to-left paperfolding-tail state counts

## Correctness — PASS

The complete residual family is derived for every shift and every finite low-bit prefix, including the empty prefix. For positive prefix length, division of \(c+x+1\) by a power of two exhausts all cases: a smaller translated paperfolding tail, one of two parity functions, or a constant function. Every counted family is reachable. The non-eventual-periodicity argument separates distinct translated tails from each other and from periodic functions, so the residual count is exactly the minimal DFAO state count. Exhaustive finite checks agree but are not used to prove the infinite range.

## Originality — PASS within inspected evidence

The closest source, Zantema–Bosma (2022), explicitly computes four reversed states for the unshifted paperfolding word and six for its single-step tail; those known points are acknowledged. Moradi–Popoli–Shallit–Vukusic (2026) analyzes shifts of the Fibonacci word in Zeckendorf numeration, not the present sequence in binary. Another automata-subsequence paper provides general results rather than the present exact classification. Semantic searches against mathematical research records, alternative names and accessible earlier claims did not show an all-shift dominating theorem. The residual risk is an unindexed table or alternate formulation.

## Mathematical value — PASS

The theorem completely evaluates minimal right-to-left state complexity for a natural infinite family of shifts of a classical automatic word. It locates every jump sharply at powers of two and explains the structure of the minimal residual family, extending the two previously published initial values. It is not an arbitrary numerical increment or a finite census.

## Scope and risks

The proof is restricted to the explicitly defined regular binary paperfolding sequence and least-significant-first binary input, with redundant zeroes permitted. It does not address other paperfolding variants or most-significant-first automata. Historical priority in unpublished/unindexed work is not excluded, and finite verification does not constitute an infinite proof.

Self-review: passed. Independent audit: not yet performed.
