# Independent mathematical audit

## correctness

PASS

For total weight W and part sum s_i, the exact closed-neighborhood sum at a vertex v of part i is f(v)+W-s_i. When W<=1 every positive-sum part yields a contradiction from its smallest positive label or from a -1 vertex, and all nonpositive parts contradict the sum; hence W>=2. If all parts have >=3 vertices, assuming W=2 similarly makes positive-sum part impossible, so W>=3. The displayed label blocks sum to 0 outside a marked two-vertex part for W=2, or to 1 in three marked parts for W=3; every -1 sees sufficient positive weight outside its part. Independent brute enumeration on K_(2,2,2), K_(2,2,3), K_(2,3,3), K_(3,3,3) matched 2,2,2,3. Analytic proof covers all r and n_i, not the bounded test.

## originality

PASS

The initiating 2023 definition and published examples are chiefly trees/cycles/Petersen and do not give this multipartite threshold. Previous Resultary/SCOPE exact domination results for multipartite graphs concern 3,2-domination, signed domination, quasi-total double Roman, perfect Italian, or other nonidentical constraints; their formulas and role of negative labels do not imply this value.

## value

PASS

Complete multipartite graphs are canonical test classes for signed/Italian domination. The exact two-regime threshold for arbitrarily many parts and sizes reveals that one two-vertex class controls the optimum; the simultaneous closed-neighborhood and defender-subset requirements make it a genuine structural classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
