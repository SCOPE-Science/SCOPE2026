# Scientific review: exact rare bipartiteness in randomly twisted hypercubes

## Correctness — PASS

Every recursively constructed graph is connected and regular. A bipartite regular child has equal color classes and a unique bipartition up to sign, so exactly \(2((m/2)!)^2\) out of \(m!\) uniform cross-matchings preserve two-colorability. This count depends only on the child size, not its random graph shape; its independent-child and duplicated-child recurrences, conditional laws, and finite product identities follow without an exchangeability assumption. Stirling's formula gives the stated two different leading exponential scales, the independent convergent constant, and the duplicube quadratic correction with summably bounded error. All displayed quantifiers, initial dimensions, normalizations, and Markov spectral equivalences are accounted for. The standalone checker reproduced finite exact enumerations and symbolic recurrences.

## Originality — PASS, with specific priority limits

Baran–Šarković (arXiv:2610.21976v1, October 15, 2026) study walk mixing, cover times, chromatic number, and typical nonbipartiteness, but the relevant inspected text does not give the exact bipartiteness probability, a comparison of independent and duplicated cases, or the conditional law of accepted matchings. Benjamini–Dikstein–Gross–Zhukovskii (arXiv:2211.06988) introduce both models and note rare bipartiteness qualitatively in their chromatic-number question; they do not state the products or these asymptotics. Exact event statements were also compared against relevant published research records and accessible earlier claims. The closest prior observations suggest the first combinatorial count, so novelty is asserted for the integrated exact two-model probabilities, rare-event entropy separation, and conditioned sampling statement, not for balanced bipartition counting in isolation. Residual risk: a prior unpublished or unlocated work might have already evaluated the same products; no search certifies priority conclusively.

## Mathematical value — PASS

The absence of bipartiteness controls whether the *non-lazy* walk is aperiodic and whether the extreme adjacency eigenvalue \(-n\) is present. The exceptional probability is a natural, exactly specified random-graph invariant, not a selected artificial parameter slice. The two canonical couplings have similar high-probability diameter and expansion properties, yet exhibit fundamentally different probabilities of the same global spectral obstruction, differing by a full factor of dimension in the leading logarithmic scale. The conditional matching law additionally identifies the precise exceptional random-graph ensemble and makes it available for subsequent study of rare-event geometry and conditional walk behavior. This is more than a qualitative high-probability nonbipartiteness assertion or a numerical finite table.

## Limits

The proof does not characterize conditional spectral gaps, other chromatic numbers, or general dependent child couplings; no independence is imputed to duplicated child graphs. Originality is based on inspected available literature and research records rather than a proof of priority. All finite checks supplement, rather than replace, the analytic argument.

Self-review: passed. Independent audit: not yet performed.
