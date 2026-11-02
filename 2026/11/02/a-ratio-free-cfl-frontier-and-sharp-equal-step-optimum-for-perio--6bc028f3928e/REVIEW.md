# Scientific review

## Correctness — PASS

The standard variable-coefficient AB2 recurrence is reconstructed from the two-point interpolation formula. Multiplication of the two exact transfer matrices yields \(\operatorname{tr}P=a+d\) and \(\det P=d\). The discriminant factorization proves real positive multipliers throughout the stable domain. The unit-root test \(p(1)=c(1-c/2)\) proves both the precise boundary and instability beyond it. A monotonicity derivative in the single ratio-dependent determinant proves uniqueness of the balanced-step optimum. The factorization of the equal-step polynomial at \(3a/5\) proves the global sharp \(5/3\) penalty. The SPD corollary follows by orthogonal spectral decomposition. The standalone verifier executes the critical algebra from its own file.

## Originality — PASS, qualified

The closest accessible sources concern variable-step AB2 formulas (Verschelde, 2022), general Adams coefficient and implementation strategies (López–Romay, 2010), and zero-stability of interpolation/Nordsieck Adams step changes (Calvo–Montijano–Rández, 2016). The inspected full texts do not establish the necessary-and-sufficient two-periodic negative-real CFL criterion, unique equal-split optimality or sharp universal \(5/3\) spectral penalty. Searches for alternating AB2 Floquet transfer, periodic Adams–Bashforth root conditions and two-step sum thresholds returned no directly dominating claim. A highly relevant 1989 Calvo–Lisbona–Montijano paper was identified but only its abstract was accessible; it is expressly a residual priority risk, not treated as conclusively excluding coverage.

## Value — PASS

The problem is motivated by stability of adaptive multistep solvers when the step-size ratio changes sharply. The theorem supplies the exact stability condition for the simplest nontrivial periodic mesh and, separately, the unique optimal step allocation and a universal sharp price of imbalance. A ratio-free spectral CFL condition coexists with a ratio-unbounded transient norm; the explicit distinction prevents misuse in adaptive error analysis. The bound is a complete all-ratio classification, not a sample-specific numerical threshold or a routine restatement of the constant-step result.

## Closest literature and limits

The work is distinct from general Nordsieck zero-stability and practical adaptive ratio-selection analysis. Only a negative real spectrum and a strictly repeating pair of steps are covered; positivity, nonlinear stability, arbitrary step patterns, and ratio-uniform perturbation bounds remain unproved. The unavailable full 1989 article and potentially uncatalogued textbook discussions leave finite priority risk.

Self-review: passed. Independent audit: not yet performed.
