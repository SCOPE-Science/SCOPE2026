# Scientific review: open-packing enumeration on clique–path products

## Correctness

PASS. For \(m\geq3\) a selected column contains at most one vertex. Direct common-neighbor analysis proves that adjacent occupied columns must share their row label and occupied columns two steps apart must have different labels. This yields a necessary-and-sufficient four-state word transfer. The matrix inverse has the stated numerator and denominator. A complete run count treats each residue of \(n\) modulo three, including \(n=1,2,3\). A separately implemented graph-subset checker confirms the bivariate coefficients for 16 small cases, while exact recurrence and maximum-coefficient tests cover 162 parameter pairs. Risk: finite checks do not constitute infinite proof; the word bijection and run classification supply that proof.

## Originality

PASS on inspected literature and available records, not a certificate of priority. Mojdeh–Peterin–Samadi–Yero, arXiv:1901.06813, already imply the scalar maximum \(\lceil2n/3\rceil\); it is credited. Brešar–Samadi–Yero, arXiv:2106.09823, identify the two-step-graph interpretation; Samadi–Soltankhah–Yero, arXiv:2306.01488, investigate product injective coloring. No inspected statement covers the complete bivariate enumerator or the labeled maximum-set multiplicity formulas. Related independent-set polynomials and other graph-product packing results do not imply these exact coefficients without further family-specific enumeration. Residual risk: unindexed or unnoticed equivalent literature.

## Mathematical value

PASS. General bounds for open packing leave unanswered how many near- or fully optimal vertex selections exist. The exact two-statistic generating function determines *every* admissible cardinality and induced-matching-edge count for a two-parameter graph family. The maximum coefficients exhibit a sharp residue-dependent structural classification and explicit polynomial dependence on the clique order; these are directly useful for comparing open packing with injective coloring and total domination. This is a complete natural counting invariant rather than a one-off numerical datum. Limitation: no extension is claimed to the width-two factor, cycles, or general factor graphs.

## Evidence and status

The proof and independent small-graph computations are provided in `RESULT.md` and `verify_open_packing.py`. Bibliographic references are in `RESULT.md`, and source-comparison details are recorded in `AUDIT.json`. No independent scientific review or priority certification is represented.

Self-review: passed. Independent audit: not yet performed.
