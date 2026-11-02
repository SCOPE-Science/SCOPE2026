# Scientific review: paired-population Alabama loss law

## Correctness

**PASS.** The proof reduces the four Hamilton remainders to two equal pairs and the parity of the house size, then explicitly accounts for both the residual-seat transfer and whole-quota increments. The reduction from mandatory pair-total loss to loss under every tie resolution is justified by nesting equal-pair assignments when possible. The closed count is derived from multiplication modulo the primitive period. The independently implemented exact-integer checker enumerates every legal tie allocation in 39,330 house-size comparisons across primitive populations through 40 and compares 1,933 closed count values against direct modular enumeration. These finite checks corroborate but do not prove the universal theorem.

## Originality

**PASS, with a residual priority risk.** The closely relevant work of Varshney (2026, arXiv:2608.02759) proves a universal four-state incompatibility between quota and population monotonicity across house sizes, not a formula for Hamilton's unavoidable consecutive-house losses at a fixed population vector. Saari (2026, DOI:10.1007/s11127-026-01480-9), in the inspected apportionment sections of its open-access article, explains Hamilton paradoxes geometrically but gives neither the parity-dependent modular criterion nor the exact two-pair period count. A related publicly described three-population equal-pair law has a single residue interval; its hypothesis and result do not subsume two equal pairs of four populations. Exact paired-population searches did not identify an equivalent classification. Unindexed or implicitly derivable prior formulas remain a genuine priority risk; this assessment is not an independent literature certification.

## Value

**PASS.** Equal-size pairs are a natural way to test whether an apparently symmetric population profile prevents seat loss. Instead, the theorem exposes a strict even/odd distinction, counts all tie-independent failure opportunities over the chamber-size cycle, and gives the unique smallest primitive population witness and earliest house transition. The exact frequency, including its one-quarter extreme-imbalance limit, is useful when evaluating sensitivity to legislature size rather than merely displaying an isolated paradox.

## Limits

Only fixed positive integer paired populations, Hamilton's largest-remainder rule, consecutive house sizes, and losses that are forced under all possible tie choices are covered. The result does not establish uniqueness against all previously published or unindexed mathematics. Computed test ranges are finite. Independent validation remains to be performed.

Self-review: passed. Independent audit: not yet performed.
