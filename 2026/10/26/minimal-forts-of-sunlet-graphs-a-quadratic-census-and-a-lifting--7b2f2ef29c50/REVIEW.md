# Scientific review

## Correctness

PASS. The original fort predicate forces each selected rim vertex to carry its leaf. An unselected rim position forces its leaf exactly when it has one selected rim neighbor; the only optional leaf is removable and cannot occur in an inclusion-minimal fort. All smaller forts correspond to nonempty proper subsets of rim support respecting equality constraints across each absent rim vertex with two selected neighbors. These are precisely unions of components of the distance-two support graph. The even and odd cycle counts follow from exhaustive classifications of connected intervals in respectively two parity cycles and one step-two cycle. The six-cycle obstruction is checked directly, and the standalone verifier independently exhausts all sunlet subsets through nine rim vertices. The proof does not extrapolate from that finite sample.

## Originality

PASS at best-knowledge priority standard, with documented material risks. Becker et al., arXiv:2404.05963v1 (9 April 2024), Section 5.2, discuss the same sunlet and give only an exponential lower bound rather than the exact count; the asserted lifting proposition is contradicted by the explicit six-cycle construction. The full relevant preprint corona section and proof were read, not just the abstract. An equivalent characterization of maximal failed zero forcing sets would cover the finding, but targeted searches did not locate one. The 2025 journal full text and unindexed work remain priority risks; the statement comparing the older paper is limited explicitly to the inspected preprint version.

## Value

PASS. This closes a named graph-family census left as a lower bound in primary literature and corrects a mathematically consequential structural assumption. The exact count is quadratic in cycle order, versus a published claimed exponential lower bound, and the classification is a complete description of every minimal fort rather than a single counterexample. Since minimal forts form the obstruction constraints in zero-forcing fort-cover formulations, their actual number and structure matter directly.

## Closest literature and scope

Becker et al. (2024), Sections 2, 4 and 5.2; Gomez et al. (2021), failed-zero-forcing terminology. Claims apply to standard inclusion-minimal forts on named one-leaf sunlets. Journal-version wording remains uninspected, and no claim of an independent audit is made.

Self-review: passed. Independent audit: not yet performed.
