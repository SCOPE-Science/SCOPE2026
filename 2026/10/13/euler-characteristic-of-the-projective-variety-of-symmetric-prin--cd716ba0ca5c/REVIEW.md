# Self-review

## Correctness
PASS. The proof uses the exact projective tensor model from the primary literature and the published
\[
(\operatorname{SL}(2)^{\times n})\rtimes\mathfrak S_n
\]
invariance. A powers-of-two diagonal cocharacter separates all tensor-coordinate weights, so its ambient fixed locus consists of exactly
\[
2^n
\]
coordinate points. Every coordinate point belongs to the principal-minor variety, both by the Weyl-group orbit of the empty-subset point and by an explicit diagonal degeneration whose exponent gap is exactly the symmetric-difference size. Algebraic
\[
\mathbb C^*
\]
localization then gives the Euler formula without any smoothness assumption.

The packaged checker independently replays the weight separation and degeneration exponents over broad finite ranges. Those computations are regression evidence only and are not used as an infinite proof.

## Originality
PASS. The archival sources define and characterize the same principal-minor variety and its large symmetry group, but targeted full-text inspection found no Euler, Poincaré, or topology formula. Later literature inspected for the same image likewise does not surface this invariant. Semantic and exact web searches under standard names, notation, and fixed-point formulations found no covering theorem.

The novelty domain begins at
\[
n=4
\]
so that the already-covered
\[
n=3
\]
hyperdeterminant hypersurface is not claimed as new. Residual risk remains because the localization proof is short and may have circulated as folklore or under general
\[
G
\]
-variety terminology.

## Value
PASS. The principal-minor variety is a standard object in algebraic geometry with applications to matrix theory, probability, statistical physics, spectral graph theory, and tensor geometry. The equality
\[
\chi_{\mathrm{top}}(Z_n)=2^n
\]
is structurally notable because
\[
\dim Z_n=\binom{n+1}{2}
\]
while the ambient dimension is
\[
2^n-1.
\]
It also gives the exact vanishing
\[
\chi_c(\mathbb P^{2^n-1}\setminus Z_n)=0.
\]

Self-review: passed. Independent audit: not yet performed.
