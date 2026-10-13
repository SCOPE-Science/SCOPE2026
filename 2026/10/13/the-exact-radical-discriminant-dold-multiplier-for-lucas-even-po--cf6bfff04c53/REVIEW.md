# Scientific review: exact radical-discriminant Dold multiplier

## Correctness — PASS

The theorem is reconstructed for arbitrary integer recurrence parameters \(P,Q\), each positive even index exponent \(2s\), and every positive integer multiplier \(M\). The companion matrix represents the Lucas sequence exactly, even at repeated characteristic roots. For primes not dividing \(\Delta=P^2-4Q\), separable Frobenius gives the full \(p^r\) local congruence. For primes dividing \(\Delta\), the nilpotent part of the matrix dies modulo \(p\), and a commuting-matrix lifting lemma supplies the necessary \(p^{r-1}\) congruence at every higher level. A single factor of each bad prime completes the Möbius divisibility condition. At the prime index itself, \(U_{p^{2s}}-U_1\equiv-1\pmod p\), forcing that factor in every possible multiplier. The same obstruction for every prime proves the \(\Delta=0\) boundary. The proof handles \(p=2\) explicitly and requires no nondegeneracy or coprimality assumption.

The standalone exact-integer tests pass 18,700 square-index Möbius sums, 14,268 higher-even-power sums, and 104 degenerate-discriminant prime obstructions. These are finite sanity checks, not a substitute for the unrestricted proof. No unproved number-theoretic lemma or external numerical certificate is needed.

## Originality — PASS relative to checked literature

Moss–Ward (arXiv:2011.13068v1, especially Corollary 3) prove the minimal Fibonacci multiplier \(5\) along even powers; this is one member of the new parameter classification. Luca–Ward (arXiv:2204.02711v2, *Journal of Integer Sequences* 26, Article 23.4.6, Theorems 1 and 5, and the proof at pp. 9–10) already prove the general discriminant-scaled square-index Dold statement and a smaller sufficient multiplier \(|P|\) for \(Q=0\). This theorem does **not** re-claim either published result. They do not state the all-parameter necessary-and-sufficient multiplier \(\operatorname{rad}(|\Delta|)\); their sufficient results alone cannot be divided by discarded prime powers, so the new sharp classification is not an implication of the stated conclusions.

The Byszewski–Graff–Ward survey (DOI:10.1112/blms.12531) describes general Dold congruences and trace sequences, not the exact sharp multiplier for the nonlinear index map. Available published mathematical-search results on local Dold properties of companion Lucas sequences address \(V_n\) rather than \(U_{n^{2s}}\). A mathematically equivalent but unindexed result remains a bibliographic risk; the originality assessment is not an independent priority certification.

## Value — PASS

Finding the **least** factor that repairs the divisibility congruences is a natural arithmetic question left quantitative in the sufficient-multiplier results. The theorem classifies every positive multiplier for the complete two-parameter first-kind Lucas family, uniformly over all even powers, and shows that only the prime support—not the multiplicities—of the discriminant matters. The improvement can be arbitrarily large in nondegenerate examples, while \(\Delta=0\) supplies a sharp impossibility boundary. The result is not a numerical increment or an arbitrary parameter slice; it determines a natural exact invariant attached to the published Dold-repair problem.

## Remaining limitations

The proof does not establish the nonnegative sign condition for dynamical realizability. Odd index powers are excluded. An equivalent result outside inspected and searchable literature remains possible, and no independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
