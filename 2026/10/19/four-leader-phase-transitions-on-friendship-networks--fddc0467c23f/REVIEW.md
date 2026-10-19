# Review: four-leader phase transitions on friendship networks

## Correctness — PASS

The claim is an all-size, all-positive-gain global optimization over exactly four vertices of \(F_m\). Positive definiteness permits a hub Schur complement. The five occupancy profiles for \(m\ge4\), four for \(m=3\), and two for \(m=2\) are exhaustive. Each explicit rational difference is independently rederived and symbolically matched in `verify.py`; its denominator is positive in the claim domain. Three strict clustering penalties eliminate all noncanonical profiles for \(m\ge4\). A quadratic in \(\kappa\) then yields precisely two transitions for \(m=6,7\), and no other transitions in that size range. The small cases are separately controlled by strictly signed rational differences and one quartic with a single positive root. Exact full-matrix inverses for all four-leader subsets on \(F_2\) through \(F_5\) at four gains confirm the formulas. The finite checks alone are not the proof.

## Originality — PASS, with specific residual risk

The complete source-level formulations in Lin–Fardad–Jovanović (arXiv:1302.0450v2) and Fitch–Leonard (arXiv:1407.1569v2) contain the general inverse-trace optimization objective and centrality relations, but neither states this all-size, four-leader friendship-network phase diagram or the reciprocal two-transition gain law. Targeted published-finding corpus comparisons found no equivalent published claim; the nearest returned results concern unrelated graph combinatorics such as generalized windmill general-position polynomials and multipartite power-domination selection. The closest directly overlapping graph literature is Sun–Li–Liu (Chaos, 2020, DOI:10.1063/5.0020696). Its abstract describes freely assigned leaders and windmill coherence, but the inaccessible full paper leaves a material historical-coverage risk. This is not treated as a complete negative full-text comparison. Mathematical proof is independent of any earlier general formulas, and the specialized phase classification is not an automatic stated corollary of the inspected texts.

## Value — PASS

The friendship family is a canonical clustered hub-and-spoke graph. Exact leader placements allow a clear comparison between relying on its central hub and spreading sensing across triangles. The global four-leader classification reveals a nonmonotone design reversal in precisely two network sizes and exact algebraic thresholds with common product \(9/4\). This distinction matters for finite-gain network design; it is not a selected numerical example, a parameter renaming, or a recomputation of the generic inverse-trace formula.

## Limitations

Four equal positive finite feedback gains, unit edges, independent isotropic forcing, exactly one hub shared by disjoint triangles. The claim neither establishes historical priority beyond inspected material nor extends to generic clique bouquets, unequal-gain leaders, or higher leader budgets. The 2020 windmill paper's full text warrants independent literature review.

Self-review: passed. Independent audit: not yet performed.
