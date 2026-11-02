# Scientific review: exact least-core deficit in a binary plurality-voting ensemble

## Correctness — PASS

The analyzed characteristic function is precisely the source's pointwise binary random-tie accuracy game: coalitions with more correct than incorrect predictors score 1, tied nonempty coalitions score 1/2, and losing coalitions score 0. The theorem uses efficient signed allocations and nonnegative additive epsilon for all nonempty proper coalitions. Every formula and boundary case follows from explicit global lower bounds and feasible payoff witnesses. The first lower bound sums all correct singleton constraints and the all-incorrect coalition; the second averages nearly balanced winning-coalition constraints and uses singleton bounds. The maximum of these is attained by the displayed type-symmetric credits. The four types of coalitional payoff are checked in the proof, including the exceptional small tie cases. Direct exact tests covered 1,088 integer parameter profiles and 312,544 type-count coalition inequalities; an independent full, unsymmetrized linear program covered 54 profiles. These checks support, but do not prove, the infinite statement.

## Originality — PASS with stated uncertainty

The closest relevant primary source is Sarpe, Georgakopoulos, and Gionis, *Exact power indices for plurality-voting ensembles*, arXiv:2610.17980v1 (October 13, 2026). Its Eq. (2) defines the same binary characteristic function, while Theorems 4.1 and 4.2 compute Banzhaf and Shapley values; no additive least-core formula is supplied in the inspected full text. General least-core duality and finite-game solvers are known, but they do not state this game-specific all-parameter four-regime formula. Published simple voting-game power-index records concern a different (monotone) game class and different invariants. Searches for the pointwise majority accuracy least core, two-type signed allocations, ties, the originating paper and nearby published records uncovered no equal or stronger result. This is not a proof of universal priority: unindexed equivalent analyses remain possible.

## Value — PASS

The minimum coalitional violation is a natural stability diagnostic complementary to the Shapley and Banzhaf marginal-credit values proposed for classifier ensembles. Its exact four-regime classification applies to all ensemble sizes and yields explicit efficient signed allocations and matching blocking-coalition certificates. The threshold at \(a=2b+1\) has structural content: it identifies when the decisive coalition changes from the all-incorrect set to a winning set containing every incorrect classifier and just enough correct classifiers. This is neither a generic LP recipe nor an arbitrary fixed-size numerical slice. It is restricted to the pointwise game; dataset averaging need not retain the symmetry.

## Closest literature and remaining limitations

- Sarpe, Georgakopoulos, Gionis, arXiv:2610.17980v1, Sections 3–4 and 6: identical pointwise game, different indices; open-access full-text inspection performed.
- *Weighted nucleoli and dually essential coalitions*, DOI 10.1007/s00182-019-00689-x, Section 3: general least-core theory, no special binary ensemble phase diagram identified.
- TUGLab `leastcore` documentation: finite-game LP computation, not a closed uniform symbolic formula.
- Residual priority risk: poorly indexed or nonpublic analyses. Other restrictions (nonnegative credits, multiclass predictors, test-set averages) remain unproved.

Self-review: passed. Independent audit: not yet performed.
