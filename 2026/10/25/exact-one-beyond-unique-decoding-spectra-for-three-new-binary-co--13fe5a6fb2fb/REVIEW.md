# Scientific review

**Correctness (PASS).** The binary Hamming-ball lemma, disjoint-error-support argument, and unique majority for every close triangle were checked with their radius and minimum-distance boundary cases. The embedded checker exhaustively calculates all pair, triangle, and four-clique incidence counts from the reproduced codewords, confirms the exact stated spectra and that all successful four-cliques have distinct centers (excluding five-lists), and verifies the original code parameters. Separate full-Hamming-cube accumulation independently reproduced the distributions. No infinite assertion is inferred from finite enumeration.

**Originality (PASS; best-knowledge assessment).** The closest original paper is Ota--Osa--Harada, arXiv:2610.11609, Sections 3--4. It supplies the codebooks and minimum distances but does not publish their one-beyond-unique list multiplicities, graph triangle counts, or four-clique center incidences. Existing binary-code tables give size bounds, not these distributions. Similar published code-spectrum records inspect different code families, with no implication of these exact three profiles. The code lists mathematically determine the census, but deriving exact higher-incidence spectra is distinct from merely asserting a minimum-distance bound. Unindexed prior computations cannot be excluded.

**Value (PASS).** These are canonical new record-sized explicit codes. Their exact ambiguity spectra immediately beyond guaranteed unique correction distinguish a three-list code from two four-list codes; the rare four-list centers (eight and ninety-six) and their absence in the third code quantify finite-block ambiguity rather than simply repeat distance parameters. The proof's majority reduction is reusable for other binary codes of minimum distance \(2r-1\).

Scientific limits: only the specified codebooks/radii; no distributional channel-error conclusion and no general optimality assertion.

Self-review: passed. Independent audit: not yet performed.
