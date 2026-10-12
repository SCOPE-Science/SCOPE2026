# Scientific review

## Correctness — PASS

The result concerns stationary Gaussian AR(1) samples with \(n\ge2\), \(\sigma^2>0\), \(-1<\rho<1\). Gaussian integration by parts and the projection \(P\) yield the exact normalized covariance polynomial. Its cancellation form gives strict positivity near \(\rho=1\); a finite geometric sum plus rational evaluations at the three boundary orders proves negativity at \(\rho=1/2\) for \(n\ge7\). Exact integer summation determines the near-unit coefficients \(2(n^2-1)/3\) and \((n^2-1)(3n^2-5n+8)/30\). Uniform expansions give the two boundary layers and the intermediate-value argument gives root sequences. An executable standard-library program rechecks the exact algebra. Finite experiments are corroboration, not proof of universal signs or limits.

## Originality — PASS, with material uncertainty

The *finite mixed covariance itself is covered* by combining previously obtained zero-crossing/raw-energy and zero-crossing/squared-sample-sum identities. No novelty is attributed to the Gaussian identity, Price's theorem, or this algebraic subtraction. The reviewed contribution is the distinct nonuniform sign theorems: two positive-correlation zeros for each \(n\ge7\), and sharp scales \(1/n\) and \(1/n^2\) with constants \(1\) and \(20/3\). The geometric-distance cancellations and near-perfect-correlation singular limit are not contained in the inspected existing statements. Sinn–Keller addresses crossing-crossing covariances; Lindgren considers crossing and derivative-square estimators in continuous time. A complete historical survey has not established priority, especially because the full Lindgren text was inaccessible. General Gaussian moment identities may allow alternative derivations, so independent verification of priority is needed.

## Value — PASS

Crossing counts and centered sample variance are standard complementary discrete time-series statistics (sign oscillation versus amplitude dispersion). Their covariance exhibits two sharply different positive-dependence reversal scales. The near-one constant \(20/3\) arises from a nontrivial fourth-order projected-distance moment, rather than a routine renaming of the raw-energy statistic. The exact finite cutoff \(n\ge7\), the bulk negative asymptotics, and the two boundary laws give a coherent dependence-phase description useful in interpreting crossing- and variance-based estimators. No stronger nonlinear prediction or uniqueness claim is made.

## Closest literature and boundaries

Lindgren, *Biometrika* 61 (1974) 401–418, published 1974-08-01, is the earliest dated scientific source; only its abstract was accessible. Sinn–Keller (2010/2011) and Vladimirov (2014) were inspected for crossing moments and Gaussian identities, respectively. The two pre-existing finite AR(1) mixed moments cover the exact algebraic identity but not the double-boundary phase theorem asserted here. The possibility that an earlier broad formula renders this analysis implicit remains a residual priority risk. No independent audit or validation is represented.

Self-review: passed. Independent audit: not yet performed.
