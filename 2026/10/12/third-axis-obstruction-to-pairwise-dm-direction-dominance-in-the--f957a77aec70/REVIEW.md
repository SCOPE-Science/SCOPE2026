# Self-review

## Correctness
**PASS.** Direct substitution into the primary source formulas gives two duplicated Boltzmann/Wootters weights for the \(D_x\) family, forcing \(C_x=0\) for every \(T>0\). For \(D_y\), the numerator reduces to the stated exponential polynomial. Positive rescaling gives a function with strictly positive derivative, so the threshold is unique and the temperature interval is exact. `verify.py` replays the formulas and root bracket.

## Originality
**PASS.** Li and Cao state the pairwise directional dominance that the family disproves, but do not identify the inconsistency with their formulas. Park's later full analytic treatment covers mixed-sign single-axis threshold structure and cites the Li--Cao work, but the inspected sections do not state or repair the \(D_x\)-versus-\(D_y\) ordering. Published-finding, alias, parameter, and web searches found no prior statement of the exact correction. The principal residual risk is that the family is derivable from known formulas and may have been noticed elsewhere under different terminology.

## Value
**PASS.** The claim supplies a structural boundary to a published control heuristic: comparing only \(J_x\) and \(J_y\) is insufficient because \(J_z\) can enforce a degeneracy that kills concurrence in one direction. The reversal persists on an open neighborhood, so it is not a numerically tuned isolated accident.

## Closest literature and limitations
The closest primary source is Li--Cao 2009, which provides the formulas and the overbroad pairwise comparison. Park 2019 provides broader critical-temperature analysis but no inspected statement of this pairwise correction. The finding does not classify the globally optimal DM direction for arbitrary parameters.

Self-review: passed. Independent audit: not yet performed.
