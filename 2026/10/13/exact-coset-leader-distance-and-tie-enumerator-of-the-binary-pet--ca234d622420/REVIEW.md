# Scientific review

## Correctness — PASS
The statement uses a fixed binary vertex–edge incidence boundary map on the Petersen graph and counts **all** 512 realizable syndromes, not a sample. A complete 32768-pattern enumeration is checked against an independent breadth-first shortest-path calculation and an explicit 18-orbit certificate under the entire natural 120-element automorphism group. The group action preserves graph edges and therefore leader weights and tie counts; the orbit sum supplies the displayed enumerator. The proof explicitly accounts for all six five-edge deep-syndrome leaders as perfect matchings and for the factor 64 converting coset counts to ambient words. The supplied standard-library verifier reproduces every finite assertion.

## Originality — PASS, residual risk disclosed
The original July 2026 graph-code article was inspected at its full-text Petersen construction (Section 6.2, pages 16–17), and its searchable text contains neither covering-radius nor syndrome enumeration. The Error Correction Zoo identifies the older code; Brouwer gives the *ordinary* codeword weight distribution, which does not imply the number of nearest codewords in each coset. Solé–Zaslavsky's 1993 paper provides the general link to minimum T-joins and covering-radius bounds, so neither the link nor the radius alone is claimed new. A full-text reading of that 1993 paper was not obtainable and might disclose earlier special-case tables. Searches of published results and equivalent-formulation terms did not yield the joint bivariate 512-coset table. The finding is limited to that checked table and 18-orbit certificate.

## Value — PASS
The distance spectrum alone does not measure nearest-codeword ambiguity. The complete joint minimum-distance/tie profile supplies that missing exact decoding statistic for a highly symmetric, finite graph code used as a natural benchmark in the recent graph-code construction; nontrivial multiplicities vary among syndromes of equal weight. It also enumerates all deep-hole leaders and gives an orbit compression of 512 cases to 18 geometric types. This is an exact natural invariant, not an arbitrary sublength sample. The result makes no claim of a general theorem for other graphs.

## Sources and limits
The recent primary source is del Valle–Praeger (arXiv:2607.28016, Section 6.2). Prior sources include Solé–Zaslavsky (Discrete Applied Mathematics 45 (1993), 63–70), the Error Correction Zoo's Petersen entry, and Brouwer's Petersen graph note. Main residual risk: the older cycle-code covering paper was accessible only through its abstract and index rather than its full text; an unindexed equivalent finite-table source may exist.

Self-review: passed. Independent audit: not yet performed.
