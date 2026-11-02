# Scientific review: exactly seven nonunimodal complete-bipartite general-position polynomials

## Correctness — PASS

The statement covers every positive unordered part-size pair and explicitly includes the single-edge boundary. The proof begins with the original geodesic definition and rederives the previously published cardinality formula; it then establishes log-concavity of the entire auxiliary binomial-row sum via a factored convolution and a justified Toeplitz-minor lemma. This limits any possible coefficient valley to the transition from cardinality two through four. A sharp parameter partition, using inequalities for largest parts at most seven, at least ten, and exhaustive exact integer checks for largest part eight or nine, yields precisely the seven stated exceptions. The \(m\ge10\) argument includes both the \(n\ge9\) inequality and the monotone finite-difference argument for \(n\le8\). The independently programmed graph-distance verifier exhausts 530604 vertex subsets across 36 boards; a separate exact-arithmetic sweep tests 11325 parameter pairs. Both returned `VERIFY_OK`. Finite checks are supplementary, not proof of the infinite statement.

## Originality — PASS, subject to publication-priority risk

The first primary article [1] already supplies the complete-bipartite coefficient formula and two nonunimodal examples, \(K_{8,4}\) and \(K_{9,7}\). The 2026 multipartite paper [2] rederives the coefficient formula and exhibits \(K_{8,8}\), but does not give the seven-case classification for arbitrary two part sizes. The August 2026 survey [3] describes the examples and balanced-part thresholds without this universal exception list. The actual mathematical addition is an all-parameter *if and only if* statement, supported by a log-concavity reduction and an exact exclusion proof; it is not a claim to the source polynomial formula or the known examples. Searches with complete-bipartite, unimodality, coefficient-valley, and binomial-row synonyms and the accessible mathematical-record summaries did not identify a stronger result implying the classification. A search absence is not a novelty certificate; inaccessible and unindexed writings remain a residual risk.

## Mathematical value — PASS

The originating paper singles out complete bipartite counterexamples to unimodality, and later literature adds further examples. The theorem closes the natural question *which complete bipartite graphs exhibit the phenomenon*: only seven isomorphism types, with no others regardless of part size. The proof also identifies an invariant mechanism—log-concavity of the binomial-row tail—that rules out any larger-cardinality valleys and explains why all failure is confined to the degree-three boundary. This is a complete classification with a sharp infinite exclusion argument, not a recomputation of a known coefficient or an arbitrary finite range.

## Closest sources and limits

[1] V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General position polynomials*, arXiv:2401.05696v1, Proposition 2.1(v) and Section 4, https://arxiv.org/html/2401.05696v1 (first posted 2024-01-11).

[2] B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930v1, Sections 3–4, https://arxiv.org/abs/2603.06930 (2026-03-06).

[3] U. Chandran S. V., S. Klavžar, J. Tuite, *The General Position Problem: A Survey*, arXiv:2501.19385v5, Section 2.3.4, https://arxiv.org/html/2501.19385v5 (2026-08-16 version).

Scope excludes multipartite graphs with three or more parts and excludes full-polynomial log-concavity, which is strictly stronger than unimodality. Full priority determination cannot be guaranteed by the sources inspected. Independent mathematical review has not occurred.

Self-review: passed. Independent audit: not yet performed.
