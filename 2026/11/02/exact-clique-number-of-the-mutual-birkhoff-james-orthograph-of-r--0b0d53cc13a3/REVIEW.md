# Review of the exact mutual-orthograph clique bound

## Correctness
**PASS.** Formula (1) follows from one-sided norm derivatives at the active coordinates of an arbitrary nonzero real sup-norm vector. Replacing nonactive vector coordinates by zero cannot destroy sign-straddling, so the rounding operation preserves mutual edges and does not identify adjacent projective vertices. Ternary adjacency is exactly incomparability of projective signed-support restrictions. Uniform random maximal chains give each rank-\(k\) object probability \(1/(\binom nk2^{k-1})\); the antichain expectation yields the sharp upper bound, attained by a full rank. The standalone exact-comparison checker corroborates the finite special cases without substituting for the general proof.

## Originality
**PASS with bibliographic limits.** Arambašić et al. (2021) prove a general existence bound and the full-sign lower bound \(2^{n-1}\); the published 2026 ternary-layer work already obtains the precise expression \(\max_k\binom nk2^{k-1}\) **as a lower bound**, explicitly not an equality. That construction and its asymptotics are not claimed as new. The added claim is the **upper bound for every real projective vector**, by a graph retraction to the signed-support poset followed by a Lubell bound. Guterman et al. (2024) study different orthodigraph invariants. An inaccessible 2022 review chapter and possible unindexed formulations leave residual novelty risk.

## Mathematical value
**PASS.** The clique number is a natural invariant of an established orthogonality graph. Completing an explicit published best lower bound to an all-dimensional exact formula via a structural reduction resolves an intrinsic classification, independent of finite experiments. The result does not claim complex scalars or a complete description of equality families.

## Closest literature and limits
- L. Arambašić et al., *Symmetrized Birkhoff–James orthogonality in arbitrary normed spaces*, JMAA 502 (2021), 125203: full primary text inspected, especially Example 3.7 and Theorems 3.5/4.1.
- A. Guterman et al., *Birkhoff–James classification of norm’s properties*, Adv. Operator Theory 9 (2024), article 43: full open-access article inspected, especially Theorems 1.1 and 1.4.
- Published 2026 *Ternary-support cliques of order \(3^n/\sqrt n\)*: full RESULT.md inspected; identical lower expression, no matching upper proved.
- The 2022 orthogonality-graph survey: publisher abstract/references inspected, full chapter inaccessible. The present finding is limited to the real supremum norm, and independent audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
