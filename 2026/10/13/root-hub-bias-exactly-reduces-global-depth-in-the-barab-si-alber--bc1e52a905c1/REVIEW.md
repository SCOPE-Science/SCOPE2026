# Review

## Correctness

PASS. The proof starts from the exact growth coupling. The deterministic identity
\[
\sum_v\deg(v)d(v)=2P_n-(n-1)
\]
converts degree-proportional attachment into an exact conditional mean for the chosen parent's depth. The root-selection indicator has zero product with that depth, because the root depth is zero. These facts give the covariance recurrence without approximation.

The mean root degree and mean total depth are solved independently from their one-step recurrences. Dividing the covariance recurrence by the root-degree mean makes it telescope. The resulting positive finite sum establishes the sign and a direct summation-by-parts calculation gives the harmonic closed form.

The standalone checker independently replays every weighted preferential-attachment parent history through \(n=9\) with rational probabilities and verifies the finite formulas exactly. It also checks the recurrence and the equivalence of the two closed forms through \(n=300\).

## Originality

PASS, with a residual bibliographic risk from the size of the older preferential-attachment literature. The strongest same-model full source inspected, Feng--Hu, explicitly motivates an inner connection between large degree and short path length but develops Zagreb and Randić indices rather than a root-degree/path-length covariance. Targeted full-text searches in that paper found no covariance occurrence and no root-degree mixed theorem.

Móri's archive-era paper studies the maximum degree rather than a joint depth law. Katona studies degree distributions across levels rather than the exact covariance of the distinguished root degree with total root depth.

The closest own-ledger preferential-attachment result concerns root degree against leaf count. That statement does not imply the present mixed law: total path length has different growth dynamics, and covariance cannot be transferred through a third statistic. The present proof instead depends on the degree-weighted-depth identity and on a new telescoping recurrence.

## Value

PASS. Root degree is the canonical early-hub statistic in the Barabási–Albert tree, while total root depth is a canonical global search-cost and profile functional. Their interaction directly quantifies the qualitative hub-versus-short-path mechanism emphasized in scale-free-tree literature.

The result is structural rather than a routine marginal recombination: root-degree size bias reduces expected total depth by the explicit amount \(B_n\), asymptotic to \((1-\log2)n\), while the raw covariance has the nontrivial scale \(n^{3/2}\). This gives a finite-size and asymptotic bridge between hub formation and global depth.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK sizes=8 weighted_histories=46233 history_checks=8 finite_formula_checks=30 recurrence_checks=894 asymptotic_checks=3`.
