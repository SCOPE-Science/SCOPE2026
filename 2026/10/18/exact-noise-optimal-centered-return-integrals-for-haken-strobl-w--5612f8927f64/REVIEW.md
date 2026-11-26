# Independent mathematical audit

## correctness

PASS

With off-diagonal damping at gamma, the traceless generator eigenmodes have strictly negative real part: an imaginary-axis eigenmode would have zero off-diagonal entries by Hilbert–Schmidt dissipation, hence commute with adjacency and be scalar by connectivity. Thus the signed centered integral converges. In the permutation-symmetric equations the integrated imaginary coherences are P=(n−1)/(2bJn) and Q=−1/(2bJn) when the latter orbit exists. The integrated real coherences are U=−(n−2)/(2 gamma n), and V=W=1/(gamma n) for existing orbits. Substitution into the remaining equations and the trace constraint gives nX/(n−1) with the stated K and R coefficients. The a=1 equations give gamma/[2J²(b+1)]+(b−1)/[gamma(b+1)], including b=1. R=2b(b−1) for a=1, b(3b−2) for a=2, and has nonnegative coefficients in b and positive leading coefficient for a>=3. Thus the positive gamma and inverse-gamma terms give the unique optimum for n>=3; K_1,1 has only the increasing linear term. Leading powers of K and R give both scaling regimes. A separate full matrix-unit generator solve at J=1.25, gamma=1.5 gave T=0.496, 1.106, 0.24 and 0.422222222222 for (a,b)=(1,4),(4,1),(1,1),(2,2); it also matched the reported minima for n>2, with residuals below 5e−16. Replay: /workspace/branches/0b87a800-a3f8-45d4-a874-e6f2dfef92b8/replay_record4.py. These finite checks and the supplied verification notes are not proofs of the full family.

## originality

PASS

Pass is for the all-size adjacency-biclique signed return, optimum and scaling, not for the Haken–Strobl equation, resolvent method or known one-edge boundary. The closest same-day indexed result has the same observable in a different Hamiltonian family; the comparison is based on its formula, not its date.

## value

PASS

The signed centered integral is a natural zero-frequency equilibrium occupation correlation, and the complete bipartite family separates imbalance and start-class effects while remaining explicit. The formula gives exact quantitative dephasing tradeoffs, distinguishes a one-edge boundary with no positive optimum, and shows why a fixed starting part and proportionally growing parts have different optimal scalings. These are meaningful benchmarks for zero-frequency dynamics, not proxies claimed to optimize mixing or transport times.

The dated certificate retains the supplied scientific assessment, sources and limitations.
