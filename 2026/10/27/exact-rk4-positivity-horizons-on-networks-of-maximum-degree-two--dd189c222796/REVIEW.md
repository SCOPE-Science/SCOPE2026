# Scientific review

## Correctness — PASS

The result is a complete graph-family classification, not an extrapolation from sampled sizes. The proof uses the fourth-degree update polynomial and the classification of connected maximum-degree-two graphs into paths and cycles. It identifies every possible walk-local entry polynomial: diagonals are positive by an explicit sum of squares, distance-two entries by negative quadratic discriminants, distance-four entries by positive walk counts, and nearest-neighbor cubics by strictly negative derivatives. Distance-three entries provide exact upper-bound witnesses in the infinite families, with an explicit extra four-step route in the seven-cycle. All exception thresholds are checked against the other entry classes. The included standalone SymPy program checks exact coefficient identities, signs, and root-isolation intervals; its finite matrix tests corroborate but do not prove the locality argument.

## Originality — PASS, qualified

The principal closest antecedent, Gottlieb, Shu and Tadmor (2001), proves the fourth-degree classical RK stability polynomial's convex-Euler decomposition in its equation (3.5), **already implying positivity below the forward-Euler restriction**. That known sufficient result is explicitly credited rather than presented as new. The new statement adds exact *necessary and sufficient* graph-indexed horizons, permanent post-horizon negative witnesses, the sharp path-size transition, and the exceptional seven-cycle bypass. Ketcheson, Gottlieb and Macdonald (2011) study strong-stability-preserving two-step integrators, a different method class; the inspected text provides no exact path/cycle horizon. Hundsdorfer et al. (1995) is about advection and flux limiting; only an abstract could be inspected, leaving limited residual source risk. Related published mathematical records describing implicit Padé, Crank–Nicolson, and Fehlberg methods have different update polynomials and do not imply these numerical thresholds. No exhaustive historical-uniqueness claim is made.

## Value — PASS

The natural maximal-degree-two class models one-dimensional finite-volume diffusion and simple continuous-time random walks with either reflecting ends or periodic boundary. Exact nonnegativity matters whenever a numerical update is interpreted as a probability transition. The result resolves the whole class, not a bespoke parameter slice, and quantifies precisely when the known forward-Euler bound is sharp versus conservative. A four-walk bypass in the seven-cycle explains a nonmonotone finite-size exception; the locality argument proves its absence in larger cycles. The exact first negative entry is a usable stress test for method implementations.

## Limitations and closest sources

Unit edge rates and completed classical RK4 only. Published general SSP guarantees cover part of the positive region but do not determine the sharp upper endpoint. The inspection of the 1995 advection paper was abstract-only; an unindexed exactly equivalent classification remains a residual originality risk. No independent audit was commissioned or performed.

Self-review: passed. Independent audit: not yet performed.
