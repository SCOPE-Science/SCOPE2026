# Scientific review: exact scattered-subsequence universality of Rudin–Shapiro prefixes

## Correctness (C): PASS
The claim fixes the binary Rudin–Shapiro coding, zero-based indexing, scattered rather than contiguous subsequences, and every integer \(N\ge1\). The greedy-arch equivalence is justified by a constructive embedding of all \(k\)-words and an explicit absent word of length \(k+1\). The morphism is derived from the pair (binary-\(11\) parity, final digit); the level-four profiles and eight even/odd symbolic composition identities provide an infinite induction. Aligned binary-block decomposition gives the all-prefix error bound. The supplied standalone program checks the symbolic induction as affine identities and independently scans finite prefixes; its scans are corroboration, not the infinite proof. The argument makes no statement about arbitrary shifted factors.

## Originality (O): PASS
Barker et al. (arXiv:2003.04629) provide the scattered-universality framework. Schnoebelen and Veron (arXiv:2304.11932, Algorithm 5.2, Theorem 6.1) provide generic compositional signatures and algorithms for any SLP-compressed word. These inputs are credited; an algorithm computing an individual index is not a published exact parity-dependent formula or a proved \(5/16\) limit for this named automatic word. Adamson et al. (arXiv:2407.18599, Sections 2–6) bound absent-subsequence counts *given* the index. Rampersad and Shallit (arXiv:2302.00405) study numerical signed Rudin–Shapiro prefix sums, not arch counts. The checked related indexed results about string attractors address contiguous factors. The remaining risk is an unindexed derivation of the same fixed-point specialization, not a known covering statement.

## Value (V): PASS
The limit \(5/16\), its exact parity correction at every dyadic prefix, and its explicit logarithmic discrepancy at arbitrary lengths constitute a motivated complete asymptotic characterization of a natural canonical word statistic. They complement general absent-subsequence theorems by specifying the index parameter for a highly structured infinite family, rather than being merely a computational restatement of a generic algorithm.

## Limits and reproducibility
The theorem is about fixed-point prefixes, not arbitrary factors; the \(s_2(N)\) error is not proved pointwise optimal. Run `python3 verify.py` with Python 3.9+ to check the algebraic proof identities and finite-prefix consistency, without third-party packages. Scientific novelty comparisons cannot exclude unavailable or unindexed literature.

Self-review: passed. Independent audit: not yet performed.
