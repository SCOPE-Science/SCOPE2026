# Scientific review: exact radix–period opacity

## Correctness: PASS

For all integer radices \(b\ge2\) and positive periods \(m\), the underlying minimal residue-state automaton has precisely \(m\) reachable distinguishable states. Its incoming edge labels are determined by prefix values modulo \(b\). The proof establishes the sharp bound \(m\le b^L-b\) for every earliest conflicting path and constructs an attaining path by writing \(m=c(b^{L-1}-1)+t\). Thus transparency and the exact normalized opacity follow from the published Allouche–Yao characterization [1]. The level-count calculation is exact interval arithmetic. A finite checker separately confirmed 400 bounded automata, explicit witnesses, and level counts; it is not substituted for the proof over infinite parameter ranges.

## Originality: PASS, with priority risk

[1] proves the general shortest-path opacity theorem and evaluates the two-periodic sequence, whereas the new claim determines shortest paths uniformly for every radix and all distinct-symbol periods, including exact level multiplicities. The later journal publication [2] visibly has a period-three figure; its full updated version was inaccessible, and it might contain more extensive formulas. Neither small-period examples nor the source's general algorithm are claimed as new; the closed simultaneous arithmetic optimization and infinite period-spectrum formula are the novelty claimed. Search results were not treated as a proof of uniqueness.

## Mathematical value: PASS

Residue clocks are a canonical complete class of maximally distinguished periodic automatic sequences. Their ordinary periodic structure conceals a sharp information-loss pattern: precisely periods divisible by the radix are transparent, and other periods exhibit a strict arithmetic ladder of earliest ambiguity lengths. The exact count \((b-1)^2b^{L-2}\) at each positive normalized opacity level provides a global classification, not an arbitrary finite census. No claim is made for noninjective periodic codings or alternate opacity metrics.

## Sources and limits

[1] J.-P. Allouche and J.-Y. Yao, *Opacity complexity of automatic sequences. The general case*, arXiv:2404.13601v1 (2024), especially Theorems 1–2 and Example 4. https://arxiv.org/pdf/2404.13601

[2] Same authors, *Opacity complexity of automatic sequences: the general case*, *Acta Informatica* 63:7 (2026), DOI:10.1007/s00236-026-00521-6; only publisher abstract/preview and figure descriptions inspected. https://doi.org/10.1007/s00236-026-00521-6

Self-review: passed. Independent audit: not yet performed.
