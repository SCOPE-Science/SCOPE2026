# Scientific review

## Correctness — PASS

The formal cluster identity is derived by signed overlapping clusters; equation (2) recovers the full unweighted overlap polynomial from the first \(2m\) length coefficients, and differentiation in equation (3) recovers the weighted overlap polynomial from the first-moment coefficients. Each polynomial comparison has degree at most \(m-1\), so agreement through \(2m-1\) is logically sufficient. Explicit witness families prove the cutoff sharp for all \(m\ge4\); the two-factor example proves the structural boundary. Independent integer-program implementations agree on \(630\) forbidden patterns, with \(932\) direct enumeration checks. Infinite statements rest on the formal proof, not these finite counts.

## Originality — PASS (best-knowledge, not certified priority)

The closest paper, Bóna–Maga–Richey (arXiv:2606.06655, Fact 2.9, Corollary 2.11), derives the full bivariate generating function from the weighted border polynomial and the forward implication from equal border polynomials to equal spectra. It does not state that only the first two statistics at lengths through a sharp finite cutoff determine that polynomial. Carrigan–Hollars–Rowland (arXiv:2212.08959) characterize unweighted avoidance equivalence, while Myers (arXiv:0906.3763) gives weighted-count generating-function methods. The new conclusion is an inverse finite-data rigidity theorem with an optimal universal horizon and explicit failure beyond one forbidden factor; it is derived using, and does not claim to supersede, the classical formula. Residual risk: an unindexed equivalent inverse argument or a nonobvious corollary in the broader literature could alter publication priority.

## Value — PASS

The motivating letter-frequency question naturally asks what aggregate statistics retain about a forbidden word. The theorem answers a stronger reconstruction question: a finite first-order statistical jet fixes all higher marked-letter counts, at every future length. The exact cutoff is information-theoretically sharp in every word length at least four and the two-pattern counterexample isolates the mechanism. This is a structural boundary, not a change of notation, an arbitrary sample, or a numerical recomputation.

## Scope and limitations

This is one common marked letter, a single forbidden factor, equal forbidden-factor lengths, finite alphabets, and linear words. It does not classify all conjugacies or construct canonical bijections, and sharpness is asserted only for \(m\ge4\). No independent mathematical audit or exhaustive publication-priority certification has occurred.

Self-review: passed. Independent audit: not yet performed.
