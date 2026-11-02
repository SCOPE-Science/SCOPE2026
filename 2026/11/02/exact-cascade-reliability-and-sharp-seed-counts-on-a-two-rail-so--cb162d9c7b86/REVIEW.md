# Self-review

## Correctness — PASS

The terminal vacant-state criterion is equivalent to the fixed point of irreversible two-neighbor adoption: the only stable vacant obstructions are end-rung pairs, adjacent full-rung squares, or left-to-right vacant paths. The explicitly defined seven-state transfer eliminates all three, and exact polynomial inversion yields the displayed rational function. Coefficientwise asymptotic scaling gives the exact minimum seed counts and coefficients; an isolated dominant pole at \(y=1\) yields the total-count asymptotic. Reproduction from `artifacts/check.py` exhaustively compares 349,520 concrete configurations, checks each coefficient through nine rungs, and symbolically verifies the rational identity. All integer ranges, endpoint degrees, and the deterministic update convention are specified.

## Originality — PASS within inspected evidence, provisional

Searches for a two-by-\(n\) ladder, threshold-two bootstrap percolation, spanning/contagious seed-set enumerators, exact probabilities, reliability polynomials and equivalent vacancy obstructions did not identify the full two-variable rational formula or its minimum-set coefficients. The primary text of Wang et al. (2015) studies nonredundant contagion on large random networks, Marcilon and Sampaio (2015) study maximum infection time and algorithmic complexity on grids, and Balogh and Pittel (2007) study random-regular graph thresholds. Those results motivate and contextualize the dynamics but do not imply the exact census on the labeled two-rail ladder. Published related results on complete multipartite conversion sets and ladder spanning trees concern different structures and do not cover the claim. General transfer-state techniques are well established; the particular exact rational expression and extracted laws are the assessed contribution. An earlier counting formula under an alternate name remains possible.

## Value — PASS

The two-rail social network is the simplest spatial network featuring both triangles-free loops and distinct boundary/interior susceptibility under the two-neighbor rule. A single exact enumerator quantifies every seeding budget, provides exact random-seed success probabilities, counts all minimum interventions and gives an exponential large-population failure rate. These are substantively stronger outputs than one minimum size or a short finite computation and supply interpretable baseline results for threshold-adoption studies. Their utility is mathematical/model-based rather than a demonstrated empirical social policy.

## Limitations and remaining risks

No extension beyond a width-two rectangular strip, fixed absolute threshold two, permanent adoption or independent initial seeding is claimed. Closed-form equality does not determine process completion time. Extensive searching is not proof of worldwide historical novelty. The general methods and associated graph-family transfer constructions may have older equivalent formulations. The external literature comparisons are self-review and are not independent certification.

Self-review: passed. Independent audit: not yet performed.
