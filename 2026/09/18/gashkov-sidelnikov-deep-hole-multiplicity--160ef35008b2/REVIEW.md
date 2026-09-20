# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The proof reduces nearest-neighbor multiplicity to a marked first-summand count. A minimum weight-three error corresponds to an unordered torus triple. The two-term decomposition theorem is unique up to order, so marking one of the three summands gives the exact identity \(|V(S)|=3M(S)\).

For the search-to-leader comparison, every admissible base-field parameter has two norm-conic lifts and hence gives two distinct marked first summands. Conversely, a valid marked first summand determines the branch parameter. Outside the branch exceptional set, the existence of the required two-term remainder forces the same discriminant/square condition used by the construction. Each exceptional set has size at most six and each parameter has at most two lifts, giving \(2A(S)\le |V(S)|\le2A(S)+12\).

The source's displayed complete character sums give both sides of the parameter estimate: its stated lower bound is \((q-3\sqrt q-28)/4\), while the absolute-value estimates in the same expansion give the upper bound \((q+3\sqrt q+4)/4\). Combining these inequalities yields the stated bound on \(M(S)\).

The norm-class invariance is exact: equal nonzero syndrome norms differ by multiplication by an element of the norm-one torus, which bijects all three-term representations.

The included \(q=9\) exhaustive verification enumerates all error vectors, reproduces the published coset-weight distribution, finds two leaders in every deep coset, and checks six marked first summands for each deep syndrome.

## Originality

PASS, qualified to the best of our knowledge.

The motivating paper arXiv:2609.20402 was inspected through its torus model, two-term uniqueness theorem, all four three-term search branches, character-sum estimates, and the remark quantifying the density of admissible first parameters. Its stated results determine coset weights and construct a leader; they do not state a uniform count of all minimum leaders. The present theorem uses the source's search-density calculation but adds the marked-leader identity and the two-sided comparison needed to convert it into a nearest-neighbor multiplicity estimate.

The 1986 Gashkov--Sidel'nikov paper was inspected through its quasi-perfectness argument and ordinary weight-spectrum theorem. Those statements concern existence of short representations and the weight distribution of codewords, not the per-coset multiplicity asserted here.

Searches for Gashkov--Sidel'nikov coset-leader multiplicity, deep-hole multiplicity, nearest-codeword counts, equivalent torus formulations, and the source paper did not identify a prior statement of this theorem. The current SCOPE archive likewise showed no matching record by source paper, object, or claim family.

Two older sources remain material access risks. S. B. Gashkov and V. M. Sidel'nikov, *Codes, Connected With a Fraction Linear Functions Group and Their Decoding* (FCT 1987), was confirmed bibliographically but its theorem text was not inspected; because it concerns decoding of the same code family, it could contain an equivalent multiplicity observation. A 1992 algebraic-decoding paper for Zetterberg codes was also identified only at bibliographic level and is a lower but nonzero risk because the Zetterberg family is closely related. In addition, arXiv:2609.20402 is extremely recent, so near-simultaneous work or a later revision may overlap.

Coset-leader multiplicity itself is not claimed as a new research question. For comparison, Charpin, Helleseth and Zinoviev studied exact leader counts for weight-four cosets of a binary BCH code. The novelty claim is restricted to the uniform \(q/6+O(\sqrt q)\) deep-hole multiplicity theorem and norm-orbit consequence for these ternary Gashkov--Sidel'nikov families.

## Value

PASS.

The result strengthens an existence-oriented decoding theorem into a quantitative statement about the entire farthest syndrome layer. It shows that every deep hole, not merely an average one, has approximately \(q/6\) nearest codewords, with square-root-scale discrepancy. The norm-orbit invariance also reduces any future exact multiplicity classification from individual syndromes to norm classes.

## Limitations

The constants are not optimized, and no exact norm-by-norm multiplicity formula is obtained. The statement is specific to the two Gashkov--Sidel'nikov families treated in the motivating paper and their branch structure. It does not prove complete regularity. The two older decoding sources described above were not inspected at theorem level. No independent audit has been performed.
