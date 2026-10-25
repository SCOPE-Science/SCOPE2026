# Independent mathematical audit

## correctness

PASS

Stable extents are formal concepts (maximal complete bipartite rectangles) by Galois antitone duality. Partition by sizes: min-side ≤1 gives ≤2n+2, both sides ≥3 have expectation O_c(n^{3/2}) since t_{a+1,b}/t_{a,b}≤np³=c³/√n for a,b≥3. Two-object pairs with ≥3 common attributes have Poisson(λ=c²) codegrees; an extra object joins their common attributes with probability ≤np³, yielding E|X−(n²/2)P(Poi λ≥3)|=O(n^{3/2}), and symmetrically Y. Maximal 2×2 rectangles have exact mean binom(n,2)²p⁴(1−p²)^{2(n−2)}. Row-resampling changes only rooted K2,2 and K3,2 configurations; their second moments are O_c(n²) because rooted overlap exponent 2−t+(t−1)s/2≤2 for t=0,1,2 and s=0,1,2. Efron–Stein then gives Var Z=O_c(n³), so L1 error O_c(n^{3/2}), implying E|S/n²−F(c)|=O_c(n^−1/2). Independently enumerated all 1×1,2×2,3×3 incidence matrices and cross-checked the exact mean and maximality correction. These exhaustive finite sizes corroborate but do not prove the asymptotic variance estimate.

## originality

PASS

Best-of-knowledge statement-level novelty: the final quantitative theorem differs from matched antecedents while known foundations are credited. Residual priority risks documented. No inspected prior theorem logically entails an O_c(n^−1/2) L1 rate for c/√n: means alone do not control fluctuations, and constant-density results concern a different limit.

## value

PASS

At the critical sparse scale, the count of formal concepts is dominated by distinct Poisson-codegree shapes. Its explicit quadratic density and quantitative L1 concentration provide a useful null-model benchmark in formal concept analysis, random bipartite graph theory and the corresponding two-sorted modality; unlike a bare exact mean identity, concentration is substantial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
