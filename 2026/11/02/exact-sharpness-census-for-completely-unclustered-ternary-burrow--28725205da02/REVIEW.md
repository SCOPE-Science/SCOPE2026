# Scientific review: finite unclustered BWT census

## Correctness — PASS

The standard-permutation criterion and Hamming identity (Kumallagov, Proposition 4.3) identify the exact finite predicate. The enumeration visits precisely all \(3\cdot2^{n-1}\) ternary words without equal adjacent letters at each tested length and retains exactly the one-cycle words at the sharp Hamming threshold. The sole pruning invokes Kumallagov's proved parity necessity. The program was compiled and exercised from its actual included source; the second, independently written bit-decision count agrees for all lengths 13–26 without parity pruning. Eighteen direct inverse-BWT/forward-BWT reconstructions check every claimed positive witness, and an independent short exhaustive loop gives the same four images at length 14. The explicit witness plus the established universal lower bound proves the numeric optimum for all larger alphabets.

## Originality — PASS, with priority risk

The principal 2026 preprint (arXiv:2606.01267v1) provides a conjecture, sharp examples only through length 12, and an arithmetic family that already covers numerical optima at lengths 13, 28 and 29; these prior numbers are explicitly excluded as individually new numerical claims. The 2025 construction paper (arXiv:2508.20879v1) concerns existence of unclustered images, without minimum input run counts. Neither inspected manuscript supplies the exact eighteen ternary optimizer counts, four-word classification at length 14, or finite sharpness over the remaining fifteen new numerical lengths. Searches by both the direct formulation and the equivalent one-cycle/Hamming/Parikh descriptions found no decisive broader coverage. Index recall and implicit coverage elsewhere remain risks.

## Value — PASS

The fully enumerated sharp-image spectrum is a motivated invariant of the central open extremal BWT problem and captures the first eighteen lengths beyond the main published witness table. The finite cutoff through length 30 covers all four residue classes and includes the sparsely realized 14-symbol parameter (exactly four optimizers with the same content). It gives useful benchmark counts and exact test cases for constructing or classifying future infinite sharpness families; it is not a routine one-step extension of an already published table.

## Limits

The result is exact only for the displayed finite interval; image counts are ternary, not counts for every larger alphabet. The theorem leaves the unrestricted conjecture open. Independent review and broader historical priority checking remain necessary.

Self-review: passed. Independent audit: not yet performed.
