# Scientific review of the exact self-essential biclique equilibrium spectrum

## Correctness

**PASS.** The fixed-point conditions split into exactly three threshold cases at each vertex: action one if the opposite part has at least its threshold of zeros; action zero if the opposite part has at most its threshold minus two of zeros; and no fixed action in the gap. This proves the exact count-pair criterion and uniqueness. Comparing two equilibria forces a separation of at least two in both opposite zero-count coordinates. The sharp construction realizes each allowed count and handles the zero-equilibrium case. The accompanying direct fixed-point enumerator passed \(19{,}432\) threshold assignments covering \(1{,}111{,}428\) binary configurations, together with \(1{,}010\) larger explicit constructions. There is no extrapolation from the finite tests to arbitrary sizes.

## Originality

**PASS, subject to publication-priority risk.** Qiu et al., arXiv:2301.02889, introduce this self-essential model, prove general bipartite hardness, and give a two-equilibrium homogeneous \(K_{3,3}\) example. Their complete-graph algorithm does not settle biclique maximum multiplicity. Fedrigo's complete-bipartite threshold protocol (2024) is a coordination game with a different update rule. The consulted sources did not establish the exact heterogeneous-threshold criterion, sharp upper bound, or full integer spectrum. Related Boolean-network work was compared at the level of fixed-point claims rather than matching graph terminology. The indexed full journal sections of Xia, McAvoy and Su (2025) and its description of a complete-bipartite appendix were compared: that paper uses open-neighbor payoffs and tie retention, with one threshold per community in the appendix, not arbitrary self-essential thresholds. Its supplemental appendix and some older general theory could not be inspected completely, so global precedence is not guaranteed.

## Value

**PASS.** General self-essential anti-coordination equilibrium existence and counting are hard even on bipartite graphs. Complete bipartite structure yields a sharp and efficiently testable theorem rather than merely a simple construction: its full equilibrium multiplicity spectrum is the consecutive interval from zero to \(1+\lfloor\min(a,b)/2\rfloor\), and balanced even graphs attain the maximum using only nonconstant thresholds. This quantifies the amount of multistability that can survive dense two-community connectivity, complementing the motivating numerical observation that generic networks often have zero or very few fixed points. The result is naturally scoped to this model and is not claimed as a general complexity breakthrough.

## Closest literature and limitations

Primary source: Qiu et al., arXiv:2301.02889 (especially §3, §4 and the appendix, including Lemma 4.4). Related work: Fedrigo (2024), Kuhlman et al. (2011), Aracena et al. (2014), and Xia, McAvoy and Su (2025). The theorem applies to unweighted complete bipartite networks, integer inverted thresholds and fixed states, not arbitrary bipartite topologies or stochastic convergence. Residual literature-priority uncertainty and the absence of independent validation remain.

Self-review: passed. Independent audit: not yet performed.
