# Independent audit — 2026-09-22

**Assigned source:** `2026/09/08/074`  
**Disposition:** **PASS**

## Correctness — PASS

I independently reconstructed the finite computation from the committed generators rather than relying on the record's earlier audit. For each of all 1,386 census rows I recomputed the Apéry set modulo the multiplicity, Frobenius number, conductor, Kunz coordinates and genus, minimal generators and embedding dimension, left-set size, pseudo-Frobenius set/type, and Wilf number. All stored invariants agreed exactly.

I also independently enumerated the numerical-semigroup tree from genus 0 through 12. The counts were
`1,1,2,4,7,12,23,39,67,118,204,343,592`; at genera 6–12 the generator sets agreed exactly with `artifacts/census.json` (no missing or extra semigroups). The claimed genus counts, minimum Wilf number 0 in every genus, W=0 counts `6,3,4,5,6,2,9`, and unique maximum type `t=g` in each genus all replayed. Finally, all 63 `(g,m)` strata in `artifacts/extremals.json` were recomputed: stratum sizes, maximum types, minimum Wilf numbers, and both stored witnesses were correct.

This is a finite computational certificate for genera 6–12, not a proof of Wilf's conjecture in general.

## Originality — PASS, with limited scope

The broad ingredients are not new. Delgado–Eliahou–Fromentin verify Wilf's conjecture through genus 100, so the Boolean statement `W >= 0` for genera 6–12 is already subsumed. OEIS A007323 gives the genus counts, and OEIS A199711 gives the number of numerical semigroups by genus and multiplicity, so the 63 stratum sizes are also prior data. Standard numerical-semigroup software computes the individual invariants used here, and the maximum-type entries should not be treated as a standalone novelty claim.

The remaining contribution is narrower: an integrated, complete genus-6–12 per-semigroup data set together with exact minimum-Wilf values in every `(g,m)` stratum and explicit witnesses, all linked to a replayable generator-only certificate. The substantive prior sources checked below address higher-genus Wilf verification, counting by genus/multiplicity, general type bounds, or algorithms; they do not provide that exact stratified minimum-Wilf table and witness set. The originality finding applies to this data/certificate layer only, not to the known Wilf verification or counting results.

## Scientific value — PASS, modest/data-level

The complete generator-indexed corpus is a reproducible small-genus benchmark: independent implementations of numerical-semigroup enumeration and Wilf/type invariants can test exact row-level values, completeness, and 63 stratum extrema against it. The minimum-Wilf witnesses provide concrete boundary cases rather than only aggregate counts. This is useful as a certified reference data set, although its value is computational and bounded; it establishes no new general theorem and does not extend the known genus range for Wilf verification.

## Prior literature checked

- M. Delgado, S. Eliahou, J. Fromentin, *A verification of Wilf's conjecture up to genus 100*, Journal of Algebra 664 (2025), 150–163, DOI 10.1016/j.jalgebra.2024.10.028; arXiv:2310.07742.
- OEIS A007323, number of numerical semigroups of genus n.
- OEIS A199711, number of numerical semigroups by genus and multiplicity; references include Blanco–García-Sánchez–Puerto and Kaplan.
- N. Kaplan, *Counting Numerical Semigroups*, arXiv:1707.02551.
- M. F. Marashdeh, *An upper bound for the type of a numerical semigroup, and a reduction of Wilf's conjecture*, arXiv:2608.12531.
- NumericalSgps documentation / numerical-semigroups wiki for standard invariant computation.

## Residual limitations

The certificate is computational rather than formally verified. The independent replay used exact integer arithmetic and a separately written enumeration/reconstruction path, which reduces but does not eliminate implementation risk. The originality finding is deliberately narrow and should not be read as claiming novelty for the known genus counts, the genus/multiplicity counts, or Wilf verification itself.
