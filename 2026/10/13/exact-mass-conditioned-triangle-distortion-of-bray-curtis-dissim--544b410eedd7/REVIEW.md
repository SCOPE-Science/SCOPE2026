# Self-review

## Correctness — PASS

The proof uses only the \(\ell^1\) triangle and reverse-triangle inequalities, sharp lower bounds on the two incident distances, and a monotonicity argument in the endpoint distance. It constructs an explicit two-species extremizer for every positive prescribed mass triple. All middle- and upper-branch threshold polynomial factorizations were checked by symbolic algebra; exact integer-enumeration checks are independent supporting evidence. The analytic proof covers every nonnegative real profile in every species dimension at least two. The finite calculations are not offered as a substitute for that proof.

## Originality — PASS, with documented literature risk

The original Bray–Curtis construction, its failure of metricity, and the unrestricted sharp relaxed-triangle constant \(3/2\) are **known**. In particular, Gragera–Suppakitpaisarn (2016, 2018) already establishes that global constant for Sørensen–Dice. The only assessed increment is the **fully sharp prescribed-total three-mass profile and iff mass window**, which is neither implied by knowing only the global worst constant nor supplied in the inspected full ecological article and the accessible abstracts. Searches for conditional cardinalities, fixed \(\ell^1\)-norms, quantitative Sørensen–Dice, and Bray–Curtis size constraints found no equivalent statement. The closest theoretical-computer-science paper could not be inspected in full; it may contain stronger coverage. Thus this is a qualified literature-based originality assessment, not proof of global novelty.

## Value — PASS

Unequal ecological sample totals change the geometry of Bray–Curtis comparisons. The result gives an exact decision rule, from three totals alone, identifying when the triangle inequality is guaranteed and when counterexamples exist. Unlike merely rederiving the universal \(3/2\) constant or showing a counterexample, it classifies the complete parameter region and exhibits worst-case communities for any admissible totals. The exact conditional guarantee can inform when distance-based assumptions are justified for raw rather than normalized abundance surveys. It does not validate any empirical inferential procedure.

## Literature and limitations

The work of Bray–Curtis (1957), Ricotta–Podani (2017), Greenacre (2017), and Gragera–Suppakitpaisarn (2016/2018) is credited. The last source's full text remained inaccessible and is a genuine originality risk. The theorem assumes deterministic nonnegative real abundances, prescribed positive sample totals, and at least two possible species; randomness, measurement noise, and prescribed zero-pattern constraints are not covered.

Self-review: passed. Independent audit: not yet performed.
