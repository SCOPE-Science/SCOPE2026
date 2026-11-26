# Independent mathematical audit

## correctness

PASS

The repaired RESULT distinguishes convergence of the expected iterates from L1 convergence and independence of epoch innovations from stage independence. The frozen 'converge in mean' is false in its conventional L1 sense: for v nonzero the trajectories are uniformly bounded by norm contraction and both stationary second moments are strictly positive. The two RR signs inside a pair are dependent. The exact risk theorem itself survives. Inserting the extrapolated state into the same signed field gives M=I-eta J+kappa eta^2 J^2 and d=-eta(I-kappa eta J)v. The two epoch innovations are M d times one sign plus d times another, independent for IID and opposite for RR. Squared norm difference is -2< Md,d >, which in each plane is 2(kappa t^2-1)||d_j||^2. Orthogonal planes and independent centered epoch innovations give the geometric factors; an isolated active violating plane proves necessity at every epoch and at stationarity, but mixtures can favor either method. A convergent past-innovation series and forgetting of initial states justify the stationary laws. An independent exact rational computation re-evaluating both SEG stages gave per-epoch innovations with squared norms in expectation 1476891/390625 and 2313441/390625; the common squared epoch contraction is 119716/390625. Thus the stationary fractions and their ratio 1521/971 are correct. The repaired upper-limit factorization is positive since (kappa-1)(2kappa-1)/kappa^2<2. The supplied checker was inspected, not executed.

## originality

PASS

For the repaired claim the distinct result is the sharp SEG frequency threshold and modal risk on stable skew-affine games, not the general anti-correlation identity or the idea of reshuffling overshoot. The common-Hessian SGD result is a close mechanistic antecedent and is now acknowledged. Its real scalar update eigenvalues do not cover the complex SEG rotation modes, and the SEG sources do not identify this stable-noise regime or its numerical penalty.

## value

PASS

The threshold separates an all-offset noise reduction guarantee from a parameter interval in which reshuffling increases exact stationary and finite-horizon error even though every stage contracts. The distinction matters for step choice in a standard SEG model with persistent residual offsets; the source ratio admits a concrete penalty of roughly 57 percent. The value is the sharp stable SEG boundary and risk quantification, not a generic covariance identity or a renaming of the SGD overshoot theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
