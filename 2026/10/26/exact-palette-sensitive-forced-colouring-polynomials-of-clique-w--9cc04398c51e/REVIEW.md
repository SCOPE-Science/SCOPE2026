# Review of exact palette-sensitive forcing on clique windmills

## Correctness — PASS

For every integer \(r\ge3\), \(m\ge2\), \(q\ge1\), the proof independently derives the conditions for a seed assignment to complete under the stated local forcing rule. With the chromatic palette, hub-seeded and hub-unseeded cases separate; each blade must contain at least \(r-2\) seeds, and a missing hub succeeds exactly when their collectively seeded leaf colours cover all \(r-1\) non-hub colours. This gives the exact polynomial and the minimum coefficient. For a larger palette, a leaf has degree \(r-1<q-1\) and can never be forced, so all leaves are initial seeds; inclusion-exclusion counts the exact surjective colourings that force the hub. The proof checks the \(q<r\) impossibility, \(q>N\) boundary, and the \(q=r+1\) seed jump. The probability polynomial follows by independent state weights. A separately implemented adjacency-based exhaustive local-rule verifier checked every seed size in 489,479 assignments across 12 instances and returned `VERIFY_OK`; finite enumeration is corroboration, not the all-order proof.

## Originality — PASS, with residual risks

The first public source (Farr, arXiv:2609.17108v1, 15 September 2026) defines the invariant and gives complete-graph cases; that is the \(m=1\) boundary, not the \(m\ge2\) theorem. The earlier Farr–Morgan arXiv:2406.15746v1 develops general graph-polynomial machinery but does not state the uniform windmill closed formula. Fully read published quantitative theorems on complete multipartite and complete bipartite graphs do not imply the windmill result, as \(W_{r,m}\) is not complete multipartite for the stated range. A fully read friendship-graph zero-forcing result concerns a different forcing rule. The older forcing chromatic number counts unique extensions, not local iterative propagation. The relevant literature and published-finding corpus searches did not return the precise all-palette windmill formula, the exact seed polynomial, or the \(m\)-sized chromatic-palette transition. Failed search cannot certify global novelty; unindexed prior work is possible.

## Value — PASS

The finding gives a complete exact domain-size polynomial in a natural, infinite, two-parameter family, **at every palette size**. It identifies a sharp behaviour change upon adding one available colour: the minimum successful seed size grows by exactly the number of clique blades, because local propagation becomes impossible away from the hub. This is an interpretable structural feature of chromatic propagation, not a parameter substitution, and it provides full coefficient counts and probabilities rather than an isolated small instance.

## Closest sources and scientific limits

- G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1 (2026): definition, general identities, complete-graph boundary; not this multi-blade formula.
- G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746v1 (2024): polynomial framework.
- *Forced colourings of complete multipartite graphs at the chromatic palette size* (published-finding corpus): non-overlapping graph class and palette restriction.
- *Forced three-colouring polynomial of complete bipartite graphs* (published-finding corpus): non-overlapping family.
- *Zero forcing polynomial of friendship graphs* (published-finding corpus): different rule.
- F. Harary, W. Slany, O. Verbitsky, *On the Computational Complexity of the Forcing Chromatic Number* (2004): distinct unique-extension notion.

The theorem is restricted to uniform clique windmills, named colours, and the stated iterative forcing process. Independent mathematical assessment and a conclusive historical-priority determination have not been performed.

Self-review: passed. Independent audit: not yet performed.
