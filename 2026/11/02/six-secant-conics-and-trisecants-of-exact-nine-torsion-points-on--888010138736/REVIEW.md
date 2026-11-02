# Scientific review: six-secant conics of type-nine points

## Correctness — PASS

The quantifiers concern **every** smooth complex plane cubic and six **distinct** points of exact order nine relative to a flex. The equivalence of six-secant conics with zero-sum six-subsets follows from Abel's theorem, degree-zero Riemann–Roch, the exact restriction sequence for a cubic plane curve, and Bézout. The group-character coefficient calculation is explicitly reconstructed in `RESULT.md`; its 1, 8 and 72 character contributions give the total 1,928,772. The pointwise 30-trisecant and 632-disjoint-partner arguments give 227,520 reducible conics and 1,701,252 smooth conics. The standalone verifier independently checks all finite arithmetic and the noncollision of reducible supports. No finite sample is used as an infinite proof.

## Originality — PASS (qualified by priority risk)

Gattazzo (1979, *Punti di tipo 9 di una cubica ellittica*) characterized 72 type-nine points and a third-intersection collinearity property. Szemberg–Szpond (arXiv:2211.00494, 2022) counted 8,244 six-secant conics through the **different 27-point sextactic set**, with 5,976 smooth. Merta–Zięba (arXiv:2406.13802, 2024) determined type-nine coordinates and counted 324 conics of contact type \(3P+3Q\). Merta's 2026 doctoral dissertation (Chapter 2, §2.2) additionally displays three 24-line type-nine subarrangements and (§2.4) the same special bitangent conics. These descriptions do not imply the full six-distinct-point census or 720-trisecant incidence configuration. Relevant primary sections were inspected and equivalent, broader, table, and implication comparisons were recorded in `AUDIT.json`.

An earlier unindexed or generically formulated torsion-subset enumeration may exist; a negative search does not establish absolute priority. This risk is not an identified covering theorem.

## Mathematical value — PASS

The complete, moduli-independent type-nine six-secant count extends a specifically motivated study of geometric conic arrangements at the next special torsion level, rather than enumerating an arbitrary coefficient slice. Separating smooth from reducible members, deriving all 720 trisecants and 30-through-each-point incidence, and obtaining exact point-conic statistics supplies a natural closed enumerative classification not present in the inspected motivating work. No stronger downstream theorem is assumed.

## Limits and verification status

The result does not address isomorphism classes of conics, the global intersection lattice of all six-secant conics, positive-characteristic versions, or Hilbert-scheme multiplicities. Reproducibility is by `verify_sixsecants.py`. No independent external mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
