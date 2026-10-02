# Mathematical audit — 2026-10-01

## Final claim assessed

Prime-power odd parts in Erdős–Nicolas initial-divisor sums

## Correctness — PASS

PASS. The \(p\)-adic layer decomposition of an ordered divisor prefix is exact. The prime-odd-part classification follows by solving the two-layer prefix equation; the prime-square exclusion follows from parity of the nonempty layers and the cutoff bound; the large-prime result follows because complete binary blocks precede the next \(p\)-adic block. For higher exponents, reducing the first full block modulo \(p\), tracking the last complete layer through \(v_p(2^{a+1}-1)\), and strict decrease of binary exponents yields the finite bound. An independent small-parameter enumeration reproduced Theorems 1 and 2 with no mismatches; the repository's much larger finite scan is corroborative rather than the proof.

## Originality — PASS

PASS to the best of current knowledge. The relevant final section of the original Erdős--Nicolas 1975 paper was inspected directly: it introduces the divisor-prefix equality, identifies the perfect-number case, and lists nonperfect examples below one million beginning with 24, 2016 and 8190, but it does not give the two-prime-power classification. Resultary searches for \(2^a p^b\), prime-square odd parts and Mersenne specializations returned only the assigned exact theorem. No inspected source supplied the prime-square impossibility or the finite-per-\(a\) higher-exponent reduction.


### equivalent_formulations

Searches: Resultary: Erdős Nicolas numbers two-prime-power \(2^a p^b\) initial divisor sums; web: initial divisor sum \(2^a p\) Mersenne 24

Evidence: No earlier equivalent two-prime-power theorem was found; the original 1975 source uses the same divisor-prefix equality but only lists examples.

Reasoning: The ordered-divisor-prefix and Erdős--Nicolas formulations were both searched.
### broader_coverage

Searches: https://doi.org/10.24033/bsmf.1793; OEIS A064510; OEIS A194472

Evidence: The 1975 paper provides the founding equality and examples; the sequence resources provide data and references.

Reasoning: Neither inspected source gives a theorem mechanically implying the prime-square exclusion or the higher-exponent valuation reduction.
### exact_database_or_table

Searches: OEIS A064510; OEIS A194472; Resultary semantic search for \(2^a p^b\) Erdős--Nicolas

Evidence: Finite example tables include 24 but do not establish the quantified classification.

Reasoning: The theorem's infinite exclusions and finite-per-parameter reduction cannot be certified by a data table.
### claim_vs_prior_implication

Searches: relevant final section of Erdős--Nicolas 1975; assigned layer proof

Evidence: The primary paper states the equality and finite examples but no support-size-two structural theorem.

Reasoning: The assigned \(p\)-adic layer and valuation arguments supply additional implications not present in the inspected prior source.

## Scientific value — PASS

PASS. The theorem gives a structural reduction of a classical divisor-prefix problem on a natural two-prime-support family: it completely closes two exponent slices, isolates 24, proves a global large-prime obstruction, and turns every remaining fixed-\(a\) problem into a finite search. The finite computation is secondary to those infinite statements.

## Source inspections

- **Répartition des nombres superabondants** — https://doi.org/10.24033/bsmf.1793. Material read: Primary PDF, with direct inspection of the relevant final section where the equality, perfect case and nonperfect examples below one million are stated. Assessment: FOUNDATIONAL_PRIOR_NOT_EXACT_COVERAGE. Evidence: The paper lists examples including 24, 2016 and 8190 but does not state the two-prime-power classification.
- **OEIS A064510 and A194472** — https://oeis.org/A194472. Material read: Sequence descriptions, example data and references. Assessment: FINITE_DATA_NOT_COMPLETENESS. Evidence: The entries provide known examples and terminology but no theorem matching the structural reduction.

## Limitations and residual risks

The theorem does not eliminate every case with odd-prime exponent at least three. It gives a finite candidate set for each fixed power of two, and the exact computation exhausts that reduced set only through the stated finite range.

- Older poorly indexed problem literature on partial divisor sums may contain a related support-size-two classification under different terminology.

## Disposition

**passed**
