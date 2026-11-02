# Independent mathematical audit

## correctness

PASS

The reverse subset construction starts at F and maps each subset by the same involution sigma_a, so it remains a complete deterministic undirected automaton. Its accessible subsets are precisely G·F; transitivity of G on the original reachable state set separates any two different subsets by a word moving a point of symmetric difference to q0, proving the orbit DFA minimal. Consequently sc(L^R)=|G·F|<=binom(n,m). Three explicit involutions u(i)=-i, v(i)=1-i, w=(0 1) generate an n-cycle uv and all adjacent transpositions, hence full S_n; a suitable proper F yields a minimal witness attaining all binomial bounds. For two letters involutions s,t, <st> is cyclic normal of index <=2, and transitive G has |G|<=2n. This excludes n>=6 via central binomial>2n, n=4 via orbit divisor 6 not dividing 4 or 8, and n=5 via D5 reflection fixing any unordered pair so orbit size<=5. At n=3 two reflections generate S3; at n=2 one swap suffices. Independent construction and orbit/minimization checks n=2..8 for all accepting subset sizes confirmed these finite cases. Group argument proves all n.

## originality

PASS

Hospodár–Mlynárčik (2020), Lemma7/Theorems8/11, already prove reversal closure and the central-binomial worst-case bound for arbitrary permutation automata, a larger class. The orbit/minimality formula itself is a natural specialization of their permutation reasoning and is not independently new. Their binary optimal examples involve letters that are full cycles, invalid as single-letter DUFA involutions. Kutrib–Malcher–Schneider (2021) treat DUFA and explicitly note a reversal state-complexity gap for multiple finals; the submitted subgroup constraint and exact ternary-versus-binary alphabet threshold are new compared to the inspected complete primary statements. General permutation theorems must be credited, so the original contribution is the sharp alphabet separation and within-subclass attainability.

## value

PASS

DUFA is a natural constrained regular-language model. The exact minimal alphabet threshold for maximal reversal blowup separates two involutions (dihedral transition groups) from three generators (full S_n), a clear structural mechanism useful in state-complexity classifications. The orbit formula clarifies multi-final-state reversal without asserting a genuinely new general permutation automata theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
