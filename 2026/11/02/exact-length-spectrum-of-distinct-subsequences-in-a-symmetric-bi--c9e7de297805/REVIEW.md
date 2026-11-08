# Independent mathematical audit

## correctness

PASS

For deterministic append bit c, F_c becomes t(1+F_0+F_1) and other final-letter subsequence count remains fixed; uniqueness of subsequence strings is preserved. Complement symmetry and stationary Markov conditioning yield U_(n+1)=t(1/2+U_n+V_n), V_(n+1)=r U_n+(1-r)V_n. Matrix inverse gives exactly rational tz[1-(1-2r)z]/[(1-z)(1-(1-r+t)z+t(1-2r)z²)]. Perron root for t=1 is 1-r/2 + sqrt(r(r+4))/2 for r>0 (matrix primitive including r=1); r=0 deterministic string has count n. Independent enumeration of all binary strings for r=0,1/4,1/2,3/4,1 and n<=9 matched the length coefficients; finite check does not prove formal identity.

## originality

PASS

Biers-Ariel, Godbole, Kelley 2018 Section 3.2 computes total expected distinct subsequences from general Markov chains by larger state recursion; Collins treats i.i.d. fair source; Flaxman et al treat alternating extremal strings. The present two-variable length-marked rational function for symmetric binary Markov interpolation and exact growth rate adds a nontrivial refined invariant beyond an unmarked expectation, not merely a title variation.

## value

PASS

A natural correlated binary word source has an exact entire scattered-subsequence length spectrum, interpolating constant, iid and alternating extremes. The two-variable rational function allows every length and host size expectation and is more informative than total counts alone; it can be used as a benchmark in correlated sequence complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
