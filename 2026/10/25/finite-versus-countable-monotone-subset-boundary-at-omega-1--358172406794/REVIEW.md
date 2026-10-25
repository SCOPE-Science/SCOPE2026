# Scientific review: finite-versus-countable monotone-subset boundary

## Correctness — PASS

The finite-family assertion follows by finite iteration of the one-map monotone-subset corollary: each new thinning preserves all previously obtained monotonicities. For the obstruction, the injection \(e:\omega_1\hookrightarrow 2^\omega\) exists in ZFC. At any coordinate where two codes differ, one of the complementary binary maps decreases from \(1\) to \(0\); therefore no pair can be simultaneously nondecreasing for all maps.

## Originality — PASS

The closest primary source is Shen’s Corollary 3.3, which handles a single map. It implies the finite-family positive statement by iteration but does not state the countable-family obstruction. The explicit obstruction is supported by the binary-coordinate proof in RESULT.md. Searches for the exact simultaneous-monotonicity formulation did not surface a matching source; the elementary nature of the construction leaves a folklore-priority risk.

## Value — PASS

The question tests a natural strengthening of a monotone-subset lemma used in a recent choice-free partition argument. The result gives a sharp boundary: finite families always admit a common large subset, whereas a countable family can fail even on every two-point set. This prevents an unjustified countable-iteration extension of the one-map lemma.

## Closest literature and limitations

Guozhen Shen, “A choice-free proof of the Erdős–Dushnik–Miller theorem,” arXiv:2609.02703v1, §3, Theorem 3.2 and Corollary 3.3. The counterexample is in ZFC; CH is unnecessary. The coding argument may be folklore, and the claim is deliberately restricted to the exact finite-versus-countable boundary stated.

Self-review: passed. Independent audit: not yet performed.
