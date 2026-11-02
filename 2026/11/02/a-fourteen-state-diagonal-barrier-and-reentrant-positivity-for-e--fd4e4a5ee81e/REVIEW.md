# Scientific review

## Correctness — PASS
The endpoint is explicitly defined by the unmodified two-level Richardson combination, and the cyclic-resolvent expansion gives every matrix entry as a positive denominator times an integer polynomial. Sturm variation counts for dimensions two through fourteen establish all finite-dimensional root counts; exact rational witnesses at timestep six and a monotone analytic tail inequality cover every dimension at least fourteen. The complete fourteen-state classification follows from the unique isolated root of the thirteenth-hop coefficient and the two isolated diagonal roots. An embedded standalone rational/SymPy verifier passes 234 checks, including direct matrix-inverse reconstructions. Root-count computation is exact and finite; the infinite-dimensional dimension statement uses an independent inequality, not enumeration.

## Originality — PASS (subject to stated coverage risk)
The 2008 Constantinescu–Sandu report constructs extrapolation and treats linear stability, but does not supply the cycle kernel or positivity classification. The closely related published scalar Richardson sign barrier proves a scalar-decay threshold only; its statement does not imply the fourteen-state diagonal onset or disconnected complete positivity set. The 2021 Quezada de Luna–Ketcheson paper applies limiting to implicit-Euler extrapolation, rather than classifying the unmodified finite-state endpoint. Earlier periodic-advection positivity studies use different rational integrators or different generators. Exact published-finding corpus queries and accessible previous-claim comparisons found no statement covering the new claim; a missed specialized earlier result remains possible.

## Mathematical value — PASS
Directed cycles are a canonical finite Markov-advection model and implicit Euler is positivity preserving there for every timestep. Determining exactly how an accuracy-improving extrapolation destroys, recovers and destroys positivity is a structural numerical-analysis question rather than an arbitrary parameter computation. The first diagonal-negative dimension, the sharp four-to-five-state small-step transition, and the exact three-piece safe set at the onset give useful boundaries for choosing step sizes and distinguish matrix positivity from ordinary scalar stability.

## Closest literature and limits
The strongest conceptual overlap is the published scalar Richardson positivity result; the 2008 method-construction report and later bound-limiting work are background rather than covering results. The theorem does not classify full positive-step sets for every dimension above fourteen, does not include nonlinear flux limiting or nonuniform cycle rates, and has not been independently audited. The exact polynomial and rational evidence can be reproduced with `verify.py`.

Self-review: passed. Independent audit: not yet performed.
