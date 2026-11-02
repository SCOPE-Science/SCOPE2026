# Scientific review

## Correctness — PASS

The claim is for every integer length \(n\ge6\) and weight \(0\le w\le n\), where overlaps of lengths one through three are forbidden in ordered pairs including self-pairs. A nonempty code has uniform opposite endpoint bits. Fixing the orientation gives exactly four admissible three-bit prefixes with nested sets of compatible suffixes. The occurring largest prefix determines one of four containing complete Cartesian boundary templates. Because the two boundary blocks are disjoint, every middle string is available; coefficients of the four exact boundary weight polynomials establish the optimum, and bit complement exhausts the other orientation. Direct binomial-ratio limits and exact polynomial comparisons give the three crossover densities. The verifier recomputed all 255 nonempty prefix subsets, the complete boundary-weight counts for 475 length/weight pairs, literal nonoverlap for 1,260 template strings, and 24 independent exhaustive literal-code maxima. The proof, not the experiments, establishes all-length correctness.

## Originality — PASS, with qualifications

Blackburn, Nasr Esfahani, Kreher and Stinson, *Constructions and bounds for codes with restricted overlaps* (arXiv:2211.10309, full public HTML), provide the original restricted-overlap framework and the known unweighted optimum via a boundary incompatibility graph (especially Theorems 7 and 8 and the table for three-letter boundaries). This is a substantial precursor: the present endpoint and template method is a specialization of their graph perspective, **not** an independently invented restricted-overlap framework. Their unrestricted cardinality result does not specify the maximum in every constant-Hamming-weight layer, the four coefficient formulas, or the golden-ratio template crossovers. Their global size optimum retains only the middle templates, while low and high weights require different optimizers.

Wang and Wang (arXiv:2108.06934, full public HTML) address classical full non-overlap and variable lengths, so their generating-function results do not imply the restriction to overlap lengths one through three with an exact constant-weight optimum. Stanovnik (DOI:10.1007/s12190-025-02441-z, full open-access HTML, 2025) studies expandability and bounds for restricted overlaps but no equivalent fixed-weight formula was identified in its inspected material. Comparable public research records focused on unrestricted and variable-length nonoverlap; they were compared by statements, not by titles alone.

**Residual risk:** a weighted specialization of the 2022 incompatibility graph might already be present in an unlocated source, or an equivalent fixed-composition optimization might be known under different terminology. The searched sources are not an exhaustive independent literature review.

## Mathematical value — PASS

At prescribed Hamming weight, forbidden short overlaps define a natural constrained synchronization-code problem. A maximum-cardinality unweighted code need not maximize the size of any particular constant-weight layer, so this is not just extracting coefficients from the known unweighted optimum. The theorem gives a complete closed-form answer for infinitely many block lengths and weights, four explicit attaining families, and three density-driven structural switches including two conjugate golden-ratio thresholds. These changes identify when optimal code designs must depart from the previously preferred maximum-cardinality construction. No general-noise performance or broader alphabet claim is made.

Self-review: passed. Independent audit: not yet performed.
