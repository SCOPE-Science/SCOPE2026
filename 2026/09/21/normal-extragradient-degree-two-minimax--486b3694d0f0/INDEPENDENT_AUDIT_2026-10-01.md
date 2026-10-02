# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260921-486b3694d0f0`

## Correctness — PASS

After scaling \(L=1\), normality reduces the worst Euclidean one-cycle contraction to the scalar sup norm of \(p(z)=1-bz+cz^2\) on the half-disk \(K_\delta=\{|z|\le1,\operatorname{Re}z\ge\delta\}\). For \(p_*(z)=1-(1+\delta)z+z^2\), direct boundary calculation gives modulus at most \(1-\delta\) on both the circular arc and vertical chord, hence on the full set by maximum modulus. The matching lower bound follows from the two active spectral points \(z_0=\delta\) and \(z_1=\delta+i\sqrt{1-\delta^2}\): the maximum of their two squared moduli is convex in the real coefficients, and the stated positive subgradient combination vanishes at \(p_*\). A three-dimensional real-normal matrix carrying those spectral points attains equality. The unequal-step extragradient parameters reproduce \(p_*\) exactly; the common-step endpoint minimax gives the larger closed form.

### Correctness sources

- assigned RESULT.md
- artifacts/verify.py and verification.txt
- Azizian et al. 2020 half-disk framework
- Manteuffel 1982 full primary article

### Correctness risks

- Only one stationary degree-two cycle on real normal affine operators is covered; this is not a long-horizon complexity theorem.

## Originality — PASS

The two most relevant primary lines were inspected at theorem level. Azizian et al. use the same strongly-monotone normal half-disk but derive asymptotic/complexity bounds, not this finite degree-two minimax solution. Manteuffel's complete 1982 paper solves optimal parameters for a two-step second-degree stationary recurrence by an ellipse/Chebyshev asymptotic minimax problem; that is a different iteration polynomial from the one-cycle degree-two map optimized here. Its general ellipse machinery does not print or mechanically imply the constrained half-disk one-cycle optimum, the asymmetric extragradient realization, or the exact common-step gap. Resultary searches found no current covering theorem.

### equivalent_formulations

Searches:
- Resultary query: normal strongly monotone half-disk degree two minimax polynomial extragradient unequal steps
- Azizian et al. PMLR 2020 primary paper
- Manteuffel DOI 10.1137/0719058 complete article

Evidence:
- Azizian's half-disk result gives asymptotic lower bounds and method-rate comparisons rather than the exact degree-two minimizer.
- Manteuffel optimizes the asymptotic spectral radius of a two-step stationary recurrence via enclosing ellipses; its characteristic-root minimax is not \(\min_{p(0)=1,\deg p\le2}\|p\|_{K_\delta}\).

Reasoning:
One-cycle polynomial acceleration, two-step stationary recurrences, Chebyshev semi-iteration, and common-step extragradient were compared as separate formulations rather than conflated by the phrase 'degree two'.

### broader_coverage

Searches:
- Manteuffel 1982 full text
- Manteuffel 1977 Chebyshev framework
- Azizian 2020 normal-operator lower bounds
- current Resultary optimization findings

Evidence:
- The classical literature supplies a broad complex spectral approximation framework but no located theorem specializes to the audited finite half-disk formula and algorithmic separation.

Reasoning:
A general methodology is prior art, but no inspected statement dominates the concrete finite-degree theorem.

### exact_database_or_table

Searches:
- current Resultary degree-two/minimax findings
- older complex second-degree iterative-method literature

Evidence:
- No exact database/table result or stronger half-disk formula was located.

Reasoning:
This is a continuous minimax theorem, not a tabulated numerical optimum.

### claim_vs_prior_implication

Searches:
- direct comparison of the audited polynomial with Manteuffel's recurrence characteristic equation

Evidence:
- Manteuffel's modes satisfy a quadratic equation in the recurrence root whose coefficients depend affinely on the matrix eigenvalue; the audited method applies one quadratic polynomial directly to the eigenvalue in a single cycle.

Reasoning:
The two problems are mathematically related but not implication-equivalent; the classical recurrence theorem does not cover the final claim.

### source_inspections

- **Optimal Parameters for Linear Second-Degree Stationary Iterative Methods** — https://doi.org/10.1137/0719058. Trigger: Principal historical-equivalence risk because of the same 'second-degree' and minimax terminology. Material read: Complete seven-page SIAM article, including the recurrence characteristic equation, ellipse mapping, minimax problem, and Chebyshev asymptotics. Method: Primary full-text formula and implication comparison. Assessment: NOT COVERING the one-cycle half-disk degree-two polynomial theorem. Evidence: The paper optimizes asymptotic roots of a two-step stationary recurrence by enclosing spectral ellipses; it does not solve the audited direct polynomial sup norm or extragradient parameter split.
- **Accelerating Smooth Games by Manipulating Spectral Shapes** — https://proceedings.mlr.press/v108/azizian20a.html. Trigger: Primary modern source using the same normal strongly-monotone spectral half-disk. Material read: Full primary paper around the polynomial framework, half-disk geometry, and asymptotic lower-bound corollary; PDF page was visually inspected. Method: Primary theorem comparison. Assessment: NOT COVERING the exact degree-two formula. Evidence: The source develops general spectral-shape rates and an asymptotic half-disk barrier, without the audited closed-form finite-degree minimizer.
- **Assigned numerical verifier** — artifacts/verify.py. Trigger: Boundary formula, sharp real-normal witness, and common-step benchmark. Material read: Complete source and saved output. Method: Line-by-line inspection. Assessment: Correct corroboration. Evidence: Sampled boundary sup norms, the \(3\times3\) witness, and numerical minimization reproduce the symbolic theorem.

### checked_sources

- Manteuffel 1982 full text
- Azizian et al. 2020 full text
- current Resultary degree-two search
- assigned RESULT.md and verifier

### residual_risks

- Older complex approximation literature may contain an equivalent half-disk special case under different notation; no specific covering statement was located after full inspection of the strongest historical candidate.

## Scientific value — PASS

The theorem gives an exact robust two-evaluation design on a natural operator class, identifies a fixed low-dimensional hard instance, and quantifies precisely what is lost by forcing classical extragradient to reuse one step size. The asymmetric-cycle conclusion is algorithmically interpretable rather than a bare polynomial exercise.

### Value sources

- normal strongly-monotone spectral framework
- assigned exact minimax and common-step comparison

### Value risks

- No claim is made for nonnormal transients, nonlinear operators, or optimal long-run iteration complexity.

## Limitations

- Real normal affine operators and Euclidean norm only.
- One stationary degree-two cycle with known positive \(\mu,L\).
- No nonnormal, nonlinear, projected, adaptive, momentum, or higher-degree theorem.
- Historical equivalence risk remains for older complex approximation literature despite inspection of the strongest located candidate.

## Disposition

**PASSED**
