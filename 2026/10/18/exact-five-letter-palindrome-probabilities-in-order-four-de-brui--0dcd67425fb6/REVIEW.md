# Scientific review: five-letter palindromes in order-four de Bruijn cycles

## Correctness — PASS
The proof is an exact all-alphabet argument for uniformly sampled labeled cyclic order-four de Bruijn words. An occurrence of \(abcba\) is a consecutive pair of distinct length-four edges when \(a,b,c\) are not all equal; contracted Euler tours are counted by BEST and directed matrix-tree cofactors. A rank-one row-Laplacian update and the explicit shift-chain group inverse give all equality-type fractions. The exact sum is \(\mathbb E X=q^2-2-2/q\) for every integer \(q\ge2\). Constant palindromes are excluded by the unique-four-mer property. Independently, all 16 binary cycles and the small-alphabet tree cofactors were checked exactly with the attached program. Finite checks supplement the infinite proof.

## Originality — PASS, with documented residual risk
Orenstein's 2018 conference contribution (DOI 10.1007/978-3-319-89929-9_10, first online 18 April 2018) and 2020 journal extension (DOI 10.1089/cmb.2019.0448) optimize *reverse-covering* sequences and derive constraints involving palindrome edges. Orenstein--Shamir (DOI 10.1093/bioinformatics/btt213) uses reverse-complement covering paths. Fici--Gabory (DOI 10.4230/LIPIcs.MFCS.2025.48) analyzes generalized de Bruijn words and transforms. These statements do not supply the present exact motif probabilities under uniformly sampled *ordinary* order-four de Bruijn Euler tours. BEST, the matrix-tree theorem, and deterministic palindrome counts are established tools, not novel claims. Unindexed prior work and the uninspected full 2018 chapter remain priority risks.

## Mathematical value — PASS
The statistic is meaningful because an order-four de Bruijn property fixes all length-four occurrences but does not fix length-five adjacency, even for binary alphabets. The finding gives both a complete equality-pattern probability law and a closed all-alphabet mean, revealing correlations invisible at the defining de Bruijn order. The reversible tagged-edge contraction and explicit finite-memory group-inverse calculation are reusable tools for local motif probabilities.

## Limitations
The ensemble is uniform over labeled cyclic de Bruijn words, not random-traversal heuristics. The result does not give variance, the full distribution, reverse-complement analogues, or higher orders. The full 2018 conference chapter was inaccessible despite lawful retrieval attempts, although its accessible abstract/appendix and related later journal full text were examined.

Self-review: passed. Independent audit: not yet performed.
