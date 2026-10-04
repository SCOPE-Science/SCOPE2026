# Same-model review

## Correctness
PASS. Under the complete null, the published knockoff sign-flip lemma makes the ordered signs iid fair coins conditional on the magnitudes. At \(q=1/r\), the Knockoff+ threshold condition is exactly \(P_k-rN_k\ge r\), hence a first hit of level \(r\) by a skip-free-upward \(+1/-r\) walk. The one-level defective generating function satisfies \(F=z(1+F^{r+1})/2\); strong Markov factorization and Lagrange inversion give the displayed first-passage coefficients and the eventual probability \(f_r^r\). Exact rational replay independently matches the formula to dynamic programming over many levels and horizons and exhaustively checks the threshold/hitting equivalence for short sign strings.

## Originality
PASS with a recorded residual risk. The directly inspected Model-X paper states the iid conditional sign property and the Knockoff+ FDR bound, but not the exact complete-null finite-horizon or limiting FDR. Rajchert and Keich analyze the necessity of the \(+1\) correction and rational threshold arithmetic, not the attained all-null FDR of the original rule. Ren and Barber analyze the stopping-time/e-value representation without the reciprocal-level Fuss-Catalan law. Targeted semantic searches using complete-null, first-passage, random-walk, Fuss-Catalan, reciprocal-level, and golden-ratio formulations found no equivalent record. The residual risk is that an older competition/ballot-theorem treatment states the same specialization under different terminology.

## Value
PASS. The result quantifies a practically important but usually qualitative feature of Knockoff+: strong conservatism under sparse or complete-null regimes. The exact formula shows that at the common nominal level \(0.1\), complete-null FDR is below \(0.001\) even with arbitrarily many features under ideal sign-flip conditions. It also isolates the structural source of that conservatism and supplies an exact finite-\(p\) calibration benchmark for implementations and approximations.

## Closest literature and limitations
The closest foundational source is Candès et al. because its Lemma 3.3 supplies precisely the iid sign property and its Theorem 3.4 supplies the Knockoff+ threshold. Rajchert and Keich are closest on the role of the \(+1\) term; Ren and Barber are closest on stopping-time structure. The theorem is intentionally limited to the complete null, reciprocal integer levels, and distinct nonzero magnitudes.

Same-model review: passed. Independent audit: not yet performed.
