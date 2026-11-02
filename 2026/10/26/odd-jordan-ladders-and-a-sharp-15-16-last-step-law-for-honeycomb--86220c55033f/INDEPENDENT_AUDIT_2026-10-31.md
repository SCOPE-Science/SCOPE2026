# Independent mathematical audit

## correctness

PASS

PASS: From the specified undirected honeycomb edge rule, verified the two-sublattice adjacency matrix [[0,P],[Q,0]] with Laurent polynomials P=1+X+Y and Q=1+X^-1+Y^-1. Over F4 Frobenius factorization (X^3-1)^k produces nine local frequency cells; precisely the two conjugate primitive-third-root pairs have P=Q=0 constant term. Their nonzero Jacobian makes P,Q formal truncated coordinates p,q, each with p^k=q^k=0. On each singular component powers of [[0,p],[q,0]] have ranks 2(k-t)^2 at even index and 2(k-t-1)(k-t) at odd index until zero. Both cells combined yield four nilpotent blocks at every odd length 1..2k-1 and a 14k² invertible sector. Fitting decomposition gives all cumulative transient counts and 15/16 at the final depth, including k=1. Independent direct GF(2) adjacency-power rank elimination verifies k=1,2,4 for all stages; the local-algebra proof, not extrapolation, establishes every a.

## originality

PASS

PASS (bounded): Hasegawa et al. compute complex Bloch zero modes of the honeycomb, Kirby–Mallion–Pollak study toroidal polyhex spectra, and Bulitko supplies general finite-group additive automata; none of the material actually read establishes the characteristic-two nilpotent Jordan ladder or full transient-depth census. Broader finite-field symbolic methods are well known and could imply the calculation after specialization; inaccessible 1993 text remains a historical-priority risk.

## value

PASS

PASS: This exact natural family uses characteristic-two thickening at the two honeycomb Dirac-frequency cells to produce unbounded odd-length Jordan ladders and a size-independent 15/16 terminal-transient proportion. The complete recurrent dimension and sharp all-depth count are structural invariants of the specified graph automaton, rather than a small grid experiment or routine graph-spectrum restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
