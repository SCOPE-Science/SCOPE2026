# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The upper bound is reduced to three explicit pointwise quadratic certificates on the 20 possible category-count vectors for three p-values. Pairwise independence fixes the expectations of the ten quadratic count features used by those certificates. Their expected values give three analytic bounds whose lower envelope is the stated piecewise formula.

Sharpness is supplied separately in each parameter interval by an explicit exchangeable distribution on category-count multisets. The masses are nonnegative on the stated intervals, sum to one, and have exactly the required ten pair-category moments. Conditional independent uniformization inside the four Simes threshold bins converts the category construction into continuous Uniform(0,1) p-values without changing the rejection event. Exact-rational verification separately checks all certificate inequalities and all moment identities.

Boundary consistency was checked at alpha=3/5 and alpha=3/4; adjacent formulas agree. At alpha=0 and alpha=1 the envelope gives 0 and 1, respectively.

## Originality

PASS, to the best of our knowledge. The starting literature establishes exact Simes size under mutual independence (Simes, 1986), sharp overall-test bounds under arbitrary dependence (Hommel, 1983), and concrete anticonservativeness under dependence (Samuel-Cahn, 1996). Searches for “pairwise independent Simes”, “pairwise independence Simes inequality”, “2-wise independent p-values”, “pairwise independent Benjamini-Hochberg”, and “limited independence multiple testing” did not locate the exact three-p-value envelope or the displayed extremizers.

Ramachandra and Natarajan (2023), which is highly relevant because it studies tight probability bounds under pairwise independence via linear programming, was inspected in full-text form available through arXiv. Searches within that text found no occurrence of “Simes” or “multiple testing”. Its results concern Bernoulli union and threshold probabilities rather than this ordered-p-value event.

The principal residual originality risk is terminology mismatch: the same finite extremal problem might be encoded in older Bonferroni inequalities, copula bounds, or general probability-bounds literature without mentioning Simes or p-values. The inspected Hommel (1983) source exposed the abstract and bibliographic material but not the full theorem text; the abstract states arbitrary-dependence sharp bounds, so uninspected details remain the most plausible older source of equivalent coverage. No concrete evidence of such coverage was found.

## Value

PASS. Pairwise independence is a natural and substantially weaker condition than mutual independence. The theorem gives an exact finite-sample answer, not only a counterexample: it identifies the complete worst-case size curve for three uniform p-values and provides explicit extremizers for every nominal level. The global-null equivalence transfers the result directly to the Benjamini-Hochberg FDR for three hypotheses.

## Scientific limitations

The result is specific to three exactly uniform null p-values. It does not solve the corresponding extremal problem for m>=4, super-uniform non-uniform p-values, mixed null/alternative configurations, or k-wise independence with k>2. The construction is continuous after within-bin randomization, but no claim is made about additional dependence properties such as exchangeable copulas beyond the stated pairwise independence.
