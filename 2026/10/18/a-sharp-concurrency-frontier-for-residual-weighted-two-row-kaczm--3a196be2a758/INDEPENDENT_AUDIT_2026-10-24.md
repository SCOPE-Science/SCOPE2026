# Independent mathematical audit

## correctness

PASS

PASS: With T independent stale-snapshot picks, N~Binomial(T,z), z=u²/(u²+v²), and error becomes ((1-βN)u,(1-β(T-N))v). Exact binomial second moments give (1-βT)²+z(1-z)βT[4-β(3T-1)], affine in z(1-z) in [0,1/4]. Endpoint z=0,1 and balanced z=1/2 realize max of A=(1-βT)² and B=1-βT+β²T(T+1)/4. Quadratic crossing βc=4/(3T-1), B minimizer 2/(T+1), A increasing above βc; comparison yields unique β*=2/(T+1), R*=1/(T+1) T≤3, and β*=4/(3T-1), R*=(T+1)²/(3T-1)² T≥3, agreeing at T=3. Uniform fixed half/half sample factor B reaches 1/(T+1), hence strict adaptive disadvantage at T≥4 and limiting 1/9 plateau; contraction iff β∈(0,2/T). Independent Fraction/comb enumeration confirmed 510 binomial identity checks, T=4 exact rate 25/121 and limit 1/9; all-integer proof rests on algebra, not grid.

## originality

PASS

PASS best-of-knowledge: Coleman 2026 analyzes real asynchronous adaptive row sampling empirically with scheduling and stale reads, not an independent frozen-snapshot T-pick mathematical envelope. Moorman/Tu/Molitor/Needell analyze averaged parallel Kaczmarz with fixed sampling; Steinerberger focuses on sequential residual-weighted row choice. Same components do not imply unaveraged state-dependent duplicate-count worst-direction minimax, as verified by equation-level comparison. Resultary yields related cyclic two-row and delay-law results but not this exact shared-snapshot residual-weighted frontier.

## value

PASS

PASS: The sharp concurrency=3 switch and nonzero best worst-batch plateau expose a genuine sample-collision mechanism where adaptive squared-residual importance sampling is provably worse than uniform sampling from T=4 onward. The exact motivated two-row benchmark is a useful stress test for parallel adaptive solvers; no general runtime theorem or large-system result is needed for this focused boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
