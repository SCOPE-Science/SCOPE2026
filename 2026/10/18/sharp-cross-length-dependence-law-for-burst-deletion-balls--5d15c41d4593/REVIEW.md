# Scientific review: cross-length burst-deletion-ball dependence

## Correctness — PASS

The theorem follows from a complete comparison of outputs at two deletion starts, giving the exact one-length mismatch identity; a residue-class cycle decomposition of the union of two distance graphs; and centered edge-indicator expectations. Pairwise zero covariance is valid even for overlapping edges. The sharp independence boundary is not inferred from covariance: independent graph edges provide the positive direction, while the simultaneous minimum-ball event and its exact cycle-rank ratio disprove independence beyond the threshold. The three-way formula enumerates only triangular edge triples, each contributing \(-(q-1)/q^3\). The proof treats all finite alphabets of size \(q\ge2\), all allowed lengths and boundary cases. An independent exhaustive checker enumerates actual deletion outputs and confirms the claims in 19 complete alphabet/length cases, but these computations are not the infinite proof.

## Originality — PASS (self-review)

The 2016 paper of Schoeny, Wachter-Zeh, Gabrys and Yaakobi explicitly reproduces Levenshtein's **one-length** ball-size identity and its **binary marginal** size distribution (Equation (2), Appendix A, Lemma 8). Neither statement supplies the joint probability law: different joint distributions can have identical binomial marginals. Song and Cai's 2022 preprint develops nonbinary deletion and burst-code constructions, not cross-length dependence identities; its introduction, definitions, relevant construction statements and appendix were inspected. Related 2023 literature on pseudorandom sequence correlation concerns extrema over shifts, not the uniform-word burst-ball pair. Searches with burst-ball, lag mismatch, autocorrelation, gcd-cycle and third-moment equivalents, together with comparison against accessible earlier scientific claims, found no theorem that implies the exact independence cutoff together with the additive third-moment rule. The mathematical comparison, not failure of a text search, supports this assessment.

Residual risk: a prior result phrased as a chromatic-polynomial law, random coloring of a two-distance graph, or lag-dependent autocorrelation could imply these statements without mentioning deletion channels. The binary one-length enumerator and all standard forest-coloring facts are acknowledged prior knowledge. Independent literature certification has not occurred.

## Mathematical value — PASS

This is a structural, non-marginal theorem for two competing burst lengths under one random source word. It gives a complete sharp independence/dependence phase boundary involving \(\gcd(a,b)\), an exact likelihood-ratio witness of dependence, and the first nonzero mixed interaction for three lengths, characterized by additive relations. It prevents erroneous multiplication of marginal sphere-volume probabilities in simultaneous burst models, even though each pair has zero covariance. Its content is not an incremental one-length count or a code-capacity claim; the novelty and value reside in the joint dependence geometry. The result is limited to uniformly random inputs, linear words, exact consecutive deletions, and distinct lengths.

## Closest scientific sources and limits

- C. Schoeny, A. Wachter-Zeh, R. Gabrys, E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820v2 (2016), §IV and Appendix A.
- W. Song, K. Cai, *Non-binary Two-Deletion Correcting Codes and Burst-Deletion Correcting Codes*, arXiv:2210.14006v1 (2022), introductory burst model and §§IV–V.
- A. Winterhof, *Pseudorandom binary sequences: quality measures and number-theoretic constructions*, arXiv:2305.11486 (2023), §4 on correlation measures, as a distinct related area.

Self-review: passed. Independent audit: not yet performed.
