# Scientific review — Exact gap-sumsets of the minimal-multiplicity non-Weierstrass family

## Correctness — PASS

The gap set splits exactly as
\[
G_g=\{3\}\sqcup\{\alpha,\alpha+3,\ldots,g-3\}\sqcup\{\beta,\beta+3,\ldots,2g-3\},
\]
where \(\alpha\) and \(\beta\) represent the nonzero residue classes of \(g\) and \(2g\) modulo three. From the classwise progressions in \(2G_g\), induction shows every later residue piece is a complete step-three interval. The three exact maximal sums are \(hF\), \(hF-g\), and \(hF-(2g-6)\); their omitted tails yield exactly \(g-3\) holes in \([h,hF]\), for every \(h\ge1\). This reconstructs the exact cardinality formula and all-order Buchweitz deficits. A standalone exact-integer enumeration checked \(864\) admissible parameter pairs, but the infinite result rests on the proof.

## Originality — PASS, with residual historical risk

Eisenbud–Schreyer, arXiv:2603.00780v1, Example 3.2, already establishes non-Weierstrass status for precisely this family. That is not presented as a new theorem. Their inspected original text does not state any all-order gap-sumset formula. Eliahou–García-García–Marín-Aragón–Vigneron-Tenorio, *The Buchweitz Set of a Numerical Semigroup*, establishes general eventual linearity and finite Buchweitz sets, but not this exact all-parameter, all-order count or omitted locations. García-García–Marín-Aragón–Torres–Vigneron-Tenorio, *On reducible non-Weierstrass semigroups*, provides other generator families whose statements do not dominate this one. The same-generator, equivalent-function, broader-theorem, and known-table comparisons found no direct coverage. Full comparison with a later revision and all older literature is incomplete, so priority is provisional.

## Value — PASS

The first multiplicity-six non-Weierstrass family has a complete failure of Buchweitz detection even though each sumset is close to the obstruction threshold: at order \(h\ge2\) the shortfall is exactly \(2h-3\). The theorem determines the full sumsets by two missing arithmetic progressions and counts exactly \(g-3\) holes at every order, establishing a quantitative structural boundary of a classical test rather than a routine isolated numerical check.

## Verification scope and limitations

The self-contained Python 3 checker regenerated the semigroup gaps by dynamic membership and tested equality of every enumerated sumset with the explicit set formula for all integers \(g\) between \(13\) and \(120\) not divisible by three, and all \(h\) from \(1\) through \(12\), a total of \(864\) parameter pairs. It returned `VERIFY_OK`. The computation does not prove arbitrary parameters and does not reprove the earlier non-Weierstrass syzygy theorem. The later version of the motivating paper could not be exhaustively compared; independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
