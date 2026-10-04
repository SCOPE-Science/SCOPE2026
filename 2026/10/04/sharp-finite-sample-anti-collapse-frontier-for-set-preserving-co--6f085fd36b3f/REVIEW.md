# Same-model scientific review

## Correctness

PASS. Let \(e_j=F(j/N)\) and \(m=\min_j e_j\). Set preservation forces the first \(k=\lfloor\alpha N\rfloor\) values to be at least \(1/\alpha\), while all remaining values are at least \(m\). Exactness therefore forces
\[
N\ge \frac{k}{\alpha}+(N-k)m,
\]
which gives the claimed upper bound. The two-level construction attains equality, and equality in the sum inequality characterizes it uniquely on the grid. The lattice case follows because the threshold block alone exhausts the entire exactness budget.

## Originality

PASS with residual literature risk. The inspected Alami–Zakharia–Ben Taieb paper proves existence of positive smooth set-preserving P2E calibrators in the non-lattice case, discusses the product-collapse problem caused by zeros, proves pointwise domination over the all-or-nothing calibrator, and establishes convergence toward all-or-nothing as \(n\) grows. The inspected material does not state the sharp finite-\(N\) optimization of the minimum grid e-value, its unique two-level optimizer, or the explicit \(O(1/N)\) ceiling.

Targeted published-finding corpus searches for set-preserving conformal p-to-e calibration, worst-case minimum e-value, product-collapse floors, and the lattice boundary returned no equivalent published finding. Web searches for “minimum e-value” and “worst-case e-value” calibrator formulations likewise exposed the motivating calibration literature but no theorem matching this finite-grid maximin statement.

A residual risk remains that the same elementary extremal calculation appears in an unindexed note, appendix, or discussion under different terminology.

## Value

PASS. Strict positivity is presented in the motivating paper as a remedy for the destructive zero values of the all-or-nothing calibrator in product-based evidence accumulation. The new theorem gives the exact finite-sample limit of that remedy: positivity can avoid literal zero off the lattice, but exact set preservation cannot guarantee a worst-rank reserve larger than \(m^*\), and \(m^*\) is at most order \(1/N\). This is a directly interpretable design limitation and supplies a sharp benchmark for any smooth positive calibrator.

Same-model review: passed. Independent audit: not yet performed.
