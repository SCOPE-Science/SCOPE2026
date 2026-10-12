# Self-review

## Correctness
**PASS.** The normalization identity is exact, including endpoint values of \(\sigma\). The minimax statement is proved by a sharp lower bound and attainment at independent one-dimensional minimizers. The complete minimizing set and the boundary-equality criterion follow directly. The practical ratio calculation is exact decimal/rational arithmetic and is reproduced by `verify.py`.

## Originality
**PASS.** The motivating full text was inspected at the allocation definition, Eq. (16)-(20), Theorem 5, Appendix B.2, the practical-data section, and the conclusions. Targeted published-finding searches used the exact source title/authors and the aliases “feasible set”, “simplex”, “square”, “conditional split”, and “separable minimax”; no covering published finding was returned. The closest broader epidemic-allocation papers use genuine top-level budget shares and do not imply this source-specific correction. A residual risk remains that an uncatalogued commentary could have noticed the same inconsistency.

## Value
**PASS.** The issue changes the admissible control set, can change the instantaneous optimum, and yields a simpler exact solution. It also resolves an internal mismatch between the paper's formal feasible set and its own reported practical conditional ratios. The claim is limited to the source's instantaneous algebra, so it does not overstate consequences for the full dynamic control problem.

## Closest literature and limitations
The closest inspected source is the motivating article itself, which defines the hierarchical fractions but later imposes the incompatible simplex. Related treatment- and vaccine-allocation literature formulates actual top-level budget shares rather than two conditional splits. The main limitation is the source's inconsistent notation: a differently intended model would need to be specified and re-derived.

Self-review: passed. Independent audit: not yet performed.
