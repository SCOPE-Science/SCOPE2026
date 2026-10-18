# Scientific review: Two marked vertices recover Johnson-graph automorphism orbits

## Correctness — PASS

The all-parameter proof identifies distances from the two individually coloured anchors within \(k\) refinement rounds. One additional round exposes two simultaneous distance-transition counts. Their difference has coefficient \(2k-n\) on the otherwise hidden four-zone intersection parameter, hence determines it if \(n>2k\). At \(n=2k\), the remaining quadratic ambiguity consists exactly of one complementation-related involution. Actual coordinate permutations and a balanced complement-permutation map act transitively on the proposed classes, proving refinement cannot split them. A generating-function count, Burnside's lemma and independent class-size formulas finish the proof. Two standalone checks passed 62 directly constructed graphs (20,098 vertex occurrences) and 2,008 arithmetic configurations (268,128 signatures), respectively. These finite computations corroborate but do not establish the infinite statement.

## Originality — PASS, with priority risk

Gavrilyuk–Goryainov (2012, DOI 10.1002/jcd.21327) study perfect two-colour equitable partitions of \(J(v,3)\), not the two-mark refinement orbit partition. Ganesan (2014, arXiv:1412.5055) determines Johnson automorphisms, including balanced complementation, but no refinement-round reconstruction. Arvind–Köbler–Rattan–Verbitsky (2015, arXiv:1502.01255) establish a stronger all-individualizations Tinhofer property for \(J(n,2)\) in their appendix, but do not state the theorem for \(k\ge3\); this theorem deliberately excludes \(k=2\). Arvind and collaborators (2016, DOI 10.4230/LIPIcs.MFCS.2016.13) address the complexity of vertex individualization more broadly. Semantic searches of published mathematical records produced no matching statement, although absence from a search index cannot certify priority. The precise claim is the complete two-anchor orbit profile, class sizes, complement transition and bounded refinement depth over all \(k\ge3\). A specialized prior result under Terwilliger-algebra or coherent-configuration terminology remains a risk.

## Value — PASS

Johnson graphs provide a canonical, highly symmetric family distinct from unrestricted Hamming graphs. Two anchors yield a natural four-zone invariant, but distance data alone do not always distinguish all four-zone possibilities. The explicit transition-count argument proves an exact and uniform remedy, pinpoints a sharp balanced-complementation exception and gives closed class-count and class-size formulas. This supplies an interpretable complete refinement invariant for every pair of landmarks throughout an infinite family, without relying on unsubstantiated downstream applications.

## Limitations and verification status

No assertion is made about three or more marks, full graph identification against arbitrary competitors, or a sharp universal minimum number of rounds. The observed finite checks are not substitutes for a proof. Independent correctness and priority assessments are not available.

Self-review: passed. Independent audit: not yet performed.
