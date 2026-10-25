# Independent mathematical audit

## correctness

PASS

A perfect numerical semigroup S with Frobenius F omits F and F-1, since retaining F-1 would isolate the final missing gap. Let r be the number of maximal consecutive blocks of S in [0,F], including {0}. For each block [u,v] the two forbidden sums F-s and F-1-s give a distinct forced gap interval [F-v-1,F-u] of length (v-u+2), and no isolated gaps give at least two gaps separating retained blocks; the reflected intervals are disjoint. Thus g>=n+r with n=F+1-g, giving 2g>=F+1+r. The all-gap semigroup handles the small exceptional case, while r>=2 otherwise gives g>=floor(F/2)+2, attained by U_F. For odd F the equality r=2 and reflected endpoints force a=k+1,b=F-2. For even F, r=2 yields U_F and r=3 forces positive blocks [a,k-1], [F+1-a,F-2] with 3a>=F+1 and a<=k-1; conversely exactly these are closed under addition with three gap runs all length >=2. Hence the complete minimizer and count formulas, including F=3 and F=4, follow for every F. Fresh independent brute enumeration checked all subsets for F=3..18, with observed minimizer counts (1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,3) and no lower-genus counterexample.

## originality

PASS

The fixed-Frobenius perfect-semigroup covariety literature defines the same beta(F) as least genus achieved among maximal perfect semigroups; every minimum-genus perfect member is inclusion-maximal, so the invariants agree. Perfect means absence of isolated gaps, not symmetric/pseudosymmetric semigroups. The current theorem provides all genus-equality members, not only the beta algorithm. The 2026 Perfect numerical semigroups of type two paper proves a gap-nongap injection and the relation n=g-i for PTT semigroups. PTT is a restricted perfect type-two class, so its general inequality is an antecedent to the lower bound but not a complete characterization of all minimizers. General fixed-F genus distributions over all semigroups are broader in objects yet do not identify this perfect extremal subclass. A general gap-count inequality permits the bound floor(F/2)+2 but cannot classify equality without analyzing intervals of retained elements and their reflected forbidden blocks. The odd uniqueness and even 1+floor((k-1)/3) count therefore do not follow as an immediate corollary of existing lower bounds.

## value

PASS

The minimum genus beta(F) is an explicit natural invariant singled out by the original perfect-semigroup covariety literature. Turning its algorithm into a closed all-F formula and classifying all equality cases, with an unbounded number of additional even-F minimizers, is a genuinely structural extremal result. This is not an arbitrary finite census or just a known genus lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
