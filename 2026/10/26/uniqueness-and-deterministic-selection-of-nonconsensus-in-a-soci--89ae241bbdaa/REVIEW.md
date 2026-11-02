# Independent mathematical audit

## correctness

PASS

Any nontrivial fixed point has all coordinates strictly in (0,1), by connectivity and positivity. Odds o(s)=s/(1-s) is strictly convex, so an interior fixed point yields u=o(x)<=Gamma W u and complement yields Gamma^-1W analogue; Perron equality would force neighbor-value equality and via odd cycles a constant fixed point impossible if Gamma!=I. Conversely if both radii >1, small positive Perron eigenvectors give monotone strict lower/upper sub- and supersolutions, whose iterates converge. For uniqueness, maximize odds ratio R>1 between two alleged interior fixed points; strict concavity of T_R(s)=Rs/(1+(R-1)s) and equality at an optimizing coordinate force all neighbors to be maximizers with equal values; graph connectivity and odd cycle force constant equilibrium, contradiction. Bracketing gives auxiliary iteration from any interior state. Tang et al Theorems 3 and 4 give almost-sure approach to equilibrium set and endpoint repulsion/convergence; bounded urn increments convert finite-set approach to convergence, yielding unique x*. Independent exact rational triangle equilibrium (3/4,1/4,1/2) and both positive Perron subeigenvector certificates checked. No claim of new stochastic approximation theorem.

## originality

PASS

Best-of-knowledge originality is confined to uniqueness of interior equilibrium on arbitrary connected nonbipartite undirected weighted graphs and deterministic stochastic selection. The original model paper explicitly states interior isolation/uniqueness remains unclear, while its endpoint spectral tests and convergence-to-equilibria already exist and are NOT claimed novel. The follow-up inference paper and general nonlinear Perron theories were compared at implication level.

## value

PASS

The motivating network model explicitly left open whether general nonconsensus equilibria are unique; strict odds/Jensen propagation resolves that gap and upgrades set-valued almost-sure attraction to deterministic asymptotic selection. Gives a constructive fixed-point algorithm and exact double-Perron regime; not a routine numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
