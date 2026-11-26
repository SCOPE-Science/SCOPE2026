# Independent mathematical audit

## correctness

PASS

The proposed weight solves the labelled-state master equation. An incoming clockwise hop exists for each positive target gap of the particle immediately preceding that hop; the predecessor weight times the hop rate equals the target weight times the preceding particle's rate. Summing over gaps gives exactly the outgoing hop flux. At each blocked color I, incoming minus outgoing flip flux is the target weight times (wR)_I/w_I. This vanishes by stationarity of R, without pairwise reversibility. Conversely, within this positive weight family one can put all vacancies in one gap and color all M-1 blocked particles I; then the master equation forces (wR)_I=0. The proof's gap-connectivity step omits the lift for the absolute root position: cut the ring after a vacant site and move each original particle once, in reverse clockwise order. Every move is legal and the net effect is a translation by one site at fixed cyclic gap/color data. This supplies the lift needed for irreducibility with fixed site labels. Positive rates let vacancies be routed around the cyclic boxes to empty any chosen box; irreducibility of R then lets its color be set before routing to the target gaps. Counting pairs (physical state, marked particle) gives L/M times the ordered box partition function, without a periodicity exception. A given box contributes weight w_I Z_{M-1,V} when blocked at color I, which gives the claimed net rate. Independent exact labelled enumeration of all 27 states at L=3, M=2, alpha=(1,2,3), u=2, v=1 gave zero residuals, weight sum 33/2, and J_12=1/3.

## originality

PASS

The model, zero-range mapping and form of the weights are prior. The supported distinction is removal of a claimed pairwise necessary condition for the same model, with arbitrary irreducible blocked-color dynamics and an exact current that can distinguish stationary processes with identical equal-time laws. The arXiv v1 citation locator in the record is wrong: the three key equations are (28)–(30), not (47)–(49). The primary text verifies the substantive comparison despite this bibliographic error.

## value

PASS

This gives a concrete counterexample to a published necessity claim and an exact characterization for the natural gap-weight family. The finite-size coefficient quantifies internal nonequilibrium circulation that is invisible to every equal-time lattice statistic for fixed hopping rates in the cyclic example. This matters for inference about rates from static observations and is not just another reversible example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
