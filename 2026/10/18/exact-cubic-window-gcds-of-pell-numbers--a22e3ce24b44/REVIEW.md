# Scientific review: cubic Pell-window GCDs

## Correctness — PASS

The precise domain is every positive window length and every nonnegative starting index for the standard Pell recurrence. The proof reconstructs the odd-length prime obstruction, the exact even-length Pell matrix difference, an integer cubic antidifference, and the valuations at the only exceptional primes \(3\) and \(7\). For any odd prime dividing every window sum, the shift differences and Cassini identity force the prime into the half-index factor. Polynomial congruences give the exact valuation of the first window, not merely a lower bound. The characteristic-four recurrence reduces the infinite gcd to its first four windows. The standalone exact-integer checker passes for all lengths through \(480\), but those finite tests are supplemental, not the justification for the universal quantifiers.

## Originality — PASS relative to inspected literature

Mbirika–Schrader–Spilker (2023, arXiv:2301.05758, primary MSC 11B39), the closest exact-object paper, treats first powers and gives a square-power partial result. The relevant full-text sections and the paper's statements were inspected; no cubic Pell-window classification occurs there. Anand et al. (2024, arXiv:2407.12868) study unpowered Pell sums and fixed-multiple identities, not gcds of cubic windows. Mbirika–Spilker (2022, arXiv:2204.12626) addresses squares for a different recurrence. The corresponding Pell term tables in OEIS A000129 and A001333 do not, by themselves, imply a cubic-window gcd classification. Searches for aliases (window GCD, sums of third powers, Pell cubes), parameter-equivalent half-index formulas, and first/square-power implications found no covering statement. This is not a claim that searching proves global uniqueness: equivalent unindexed or independently derived literature remains a residual risk.

## Value — PASS

The result settles a natural exact invariant for every window length, not an arbitrary finite slice. It explains a non-obvious factor \(7\) arising from the cubic antidifference and a distinct factor \(3\) arising only at quarter-period indices; these are exact prime-adic phenomena invisible in the first-power and square-power Pell formulas. The classification distinguishes odd and even lengths and three independent congruence triggers. A usable infinite closed form and a self-contained valuation proof make the determination substantively more informative than a recurrence-specific numerical table.

## Limits and evidence

The result is restricted to classical Pell cubes and does not extend automatically to associated Pell cubes, higher powers, or arbitrary Lucas parameters. The verifier uses exact arithmetic and ordinary Python but is not a substitute for the proof. Relevant primary literature was inspected; the possibility of a prior equivalent theorem outside the indexed sources persists.

Self-review: passed. Independent audit: not yet performed.
