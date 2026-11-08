# Independent mathematical audit

## correctness

PASS

For A=diag(a,b,...,b), m>=2,a>b>0 and single iid sparse-sign probe, let B indicate active spike and K~Bin(m,p). When B=1,K=j, projection residual has squared spectral norm b^2+delta_j and squared Frobenius mb^2+delta_j with delta_j=b^2 j(a^2-b^2)/(a^2+b^2j); B=0 produces distinct missed-spike and all-zero atoms. The probability of tolerances between adjacent j-levels is p Pr[Bin(m,p)<=k]; derivative sign has one change in t=p/(1-p), proving unique maximizer with special p_{m,0}=1/(m+1) and p_{m,m-1}=(m+1)^(-1/m). Fixed-k optimizer Poisson convergence follows from uniform polynomial limits. Independently formed all 27 sparse-sign outcomes at m=2,a=3,b=1 and checked residual singular/Frobenius norms against support formulas and zero atom. This is one-column exact arithmetic, not universal isotropic-sketch optimality.

## originality

PASS

The sparse Rademacher sketch family and randomized range-finder error estimates are established by Saibaba–Międlar and Halko–Martinsson–Tropp, but the inspected general large-sample inequalities do not specify the exact discrete joint error law of a single one-spike sketch or its target-tolerance optimizer. Related expectation comparisons do not imply this conditional tail probability. Priority to an existing one-probe toy example remains possible.

## value

PASS

This natural simplest anisotropic range-finder model supplies a sharp design frontier: sparsity beats a dense probe at strict high-accuracy thresholds, while dense sampling dominates at its own error. The atom at zero and Poisson rare-event scaling quantify restart costs and qualify generic expected-error heuristics; a precise nontrivial benchmark for randomized linear algebra despite its restricted singular basis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
