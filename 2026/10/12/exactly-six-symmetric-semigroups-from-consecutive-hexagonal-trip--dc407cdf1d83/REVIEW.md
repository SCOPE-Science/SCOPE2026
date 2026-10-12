# Self-review: Exactly six symmetric semigroups from consecutive hexagonal triples

## Correctness — PASS

Definitions and quantifiers: ordinary hexagonal numbers \(H_n=n(2n-1)\), all integers \(n\ge2\); symmetric means the Frobenius-gap complement property. Three exact pair-gcd identities bound the only possible membership cases; for \(n\ge61\), positivity of four explicit polynomials rules out the two gcd-three cases and forces the gcd-\(d\) case to have an impossible fractional coefficient. The finite remainder \(2\le n\le60\) is exhausted with a complete membership loop. \(n=3\) is handled as a two-generator exception. Five exact positive witnesses and an independent 59-case Apéry/Frobenius/genus check support the finite classification. The 29 OEIS Frobenius values were reproduced exactly. The program is not used as proof beyond its finite range.

## Originality — PASS, with risk

Closest direct predecessor: OEIS A069758 lists Frobenius numbers for the same generators (dated April 8, 2002), but no genus or all-index symmetry statement. García-Sánchez–Llena–Moscariello (arXiv:1504.02116, p. 13) states the universal gcd criterion used in the proof; it does not evaluate this infinite hexagonal family. Robles-Pérez–Rosales (arXiv:1706.04378) and Pascadi (arXiv:1712.02522, §5.5) cover consecutive triangular/tetrahedral rather than hexagonal generators. Searches for the hexagonal symmetry list, genus equivalence, complete-intersection aliases and indexed related results found no dominant direct classification. A prior unindexed derivation remains possible; no independent priority confirmation is claimed.

## Value — PASS

The theorem classifies a natural structural invariant (semigroup symmetry, tied to the Gorenstein property) throughout the entire historically tabulated hexagonal-triple family, with a sharp largest positive index \(18\). It contrasts with freely generated triangular triples and supplies an exact boundary relevant to Frobenius/genus/factorization work. This is a natural complete classification, not an arbitrary small numerical window.

## Scientific limitations

No all-index Frobenius-number formula, nonsymmetric genus formula, statement about longer blocks or other figurate families, external independence, or optimal method complexity is claimed. Routine numerical verification and search nonhits would not establish theorem or originality without the analytic obstruction and statement-by-statement source comparison.

Self-review: passed. Independent audit: not yet performed.
