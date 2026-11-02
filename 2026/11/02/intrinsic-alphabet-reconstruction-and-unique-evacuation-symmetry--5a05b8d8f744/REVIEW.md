# Assessment of intrinsic rigidity of stylic monoids

## Correctness — PASS

The proof identifies the original generators as the \(\mathcal J\)-coatoms below the unit using support preservation and idempotence. It recovers the direction of the total order from \((ab)^2=ab\) on pairs of distinct coatoms, using two-letter Knuth relations plus the explicit action on the empty column to exclude the reversed case. This immediately constrains all abstract isomorphisms and anti-isomorphisms, and the published presentation and evacuation construction supply existence. The proof treats ranks zero and one separately; no infinite conclusion relies on enumeration. The supplied checker exhaustively enumerates ranks one through five and verifies the anti-multiplication law for all element pairs.

## Originality — PASS (with specified priority risk)

Abram--Reutenauer (arXiv:2106.06556) state the stylic presentation, \(\mathcal J\)-triviality, and existence of one canonical anti-involution. They do not state uniqueness of abstract anti-automorphisms or reconstruct the alphabet and order from the abstract multiplication table. Aird--Ribeiro study the canonical involution but do not classify every monoid automorphism. An analogous rigidity statement **is known** for Kiselman's semigroup (Kudryavtseva--Mazorchuk, Proposition 20 as quoted in Andrenšek); this is a separate presented monoid and its statement does not by itself imply the quotient's rigidity. The new reconstruction argument uses existing ingredients and is short, so prior implicit treatment is a real risk. No published full generalization covering stylic monoids was established by the targeted comparisons.

## Mathematical value — PASS (bounded)

The result completely classifies a natural structural invariant for **every rank**, including anti-isomorphisms and cross-alphabet isomorphisms. The source's canonical Schützenberger involution operates on Bell-number-sized monoids; the new characterization shows it exhausts *all* possible abstract symmetries, without assuming that a symmetry respects letters or tableaux. The recoverability of the linear alphabet order from intrinsic semigroup products is a non-obvious interpretation of the established structure. Value is that of a compact structural rigidity classification, not a new algorithm or a new broad theory; the proof is short and close in method to Kiselman rigidity.

## Closest literature and limits

Abram--Reutenauer 2021 (arXiv:2106.06556), especially Theorems 8.1, 9.1, 11.1, is the strongest comparison. Aird--Ribeiro 2022 (DOI 10.1007/s00233-022-10328-9) examines the same canonical involution. Andrenšek 2025 (DOI 10.1007/s00233-025-10577-4) reports the known automorphism classification for the distinct Kiselman semigroup. Source statements and implications, not titles alone, were compared. Missing earlier records and possible unlocated implicit rigidity corollaries limit publication-priority confidence.

Self-review: passed. Independent audit: not yet performed.
