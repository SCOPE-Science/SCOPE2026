# Scientific review: exact rooted refinement depth of cycle powers

## Correctness — PASS
The proof fixes the synchronous counting convention, identifies exact round-one colours and establishes round-two distance separation for \(n\ge4k+1\). The inductive frontier uses the smallest previously separated distance class adjacent to a newly exposed vertex, which is exactly indexed by \(j-k\). This establishes the complete intermediate partitions and the sharp depth \(\lceil(\lfloor n/2\rfloor-1)/k\rceil\). At \(n=4k\), an explicitly computed second-round collision of the final two distance strata is resolved on round three. The final classes are precisely reflection orbits, hence stable. Two separate executable finite checks passed. Their finite scope is not substituted for the proof.

## Originality — PASS, with priority uncertainty
The closest inspected source is Kluge (2022), Lemma 38, establishing the eventual single-root colour classes for *prime-order* circulants in terms of multiplier stabilizers. It already covers the final prime-order partition and is not treated as a novel special case. It does not provide the parameter-uniform exact intermediate partition evolution, composite-order family, or sharp three-round boundary at \(n=4k\). Kiefer and McKay (2020) address worst-case iteration numbers, and Kersting et al. (2014) address general colour-refinement optimization rather than this exact family. An independently indexed study of rainbow connection on cycle powers concerns edge-colouring, not the claimed counting-refinement invariant, but its complete text was not inspected; it remains a literature-access risk. Targeted mathematical-literature and research-index searches found no direct exact-depth statement. Search absence alone is not proof of priority.

## Value — PASS
The family is the natural consecutive-generator circulant family, and the result gives the exact number of synchronous local aggregation rounds needed to expose every root-stabilizer orbit. The transition at \(n=4k\) is a genuine geometric wrap-around obstruction: the antipodal stratum acquires a second near-neighbour and remains merged with the penultimate distance stratum for an extra round. The unbounded depth for fixed \(k\) is made quantitative. This is a structural finite-model-theoretic classification, not a renamed general bound or isolated table value.

## Closest references and scientific limitations
Arvind et al. (2015), Kluge (2022), Kiefer and McKay (2020), and Kersting et al. (2014) were examined at the material levels described in the structured audit. The prime-order stable-partition conclusion has earlier coverage; no priority is claimed for that subresult. Full external priority verification and the smaller dense regime are outside this result. No independent audit was conducted.

Self-review: passed. Independent audit: not yet performed.
