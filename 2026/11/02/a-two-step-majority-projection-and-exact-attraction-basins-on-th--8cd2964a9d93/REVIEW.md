# Assessment of the Heawood majority census

## Correctness — PASS

The object is the fourteen-vertex cubic point–line incidence graph of the order-two projective plane. A synchronous, open-neighbor binary majority rule has no ties. Both Fano shores have seven binary subset states. The exact ten-case point-subset classification proves that the two-step map on either shore is an idempotent projection onto 58 subsets, forcing \(F^4=F^2\). The involution on recurrent states is an explicit swap of two 58-element symbols. This independently derives the 58 fixed states, 1,653 primitive two-cycle orbits, basin sizes and first-entry distributions. A concrete two-point initial state needs two updates, proving sharpness. The ten cases partition the full 128-subset domain; no extrapolation from finite sample sizes is used.

The Python checker generates the Fano lines by binary XOR, verifies all 128 point and 128 line subset maps, then traverses all 16,384 full configurations. A separately implemented C++17 functional-digraph checker uses an explicitly listed incidence relation, independently computes cycles, entrance times, basins and the iterate identity. Both were run, with complete matching outputs and assertions passing. Finite exhaustive verification is corroboration of, not a replacement for, the all-state proof.

## Originality — PASS with stated residual priority risk

Classical finite symmetric-threshold theory already implies eventual periods one or two. The candidate's precise claim is the stronger, Heawood-specific idempotent two-step projection, the 58-element recurrent-symbol swap, the exact five-class basin distribution, and the sharp two-update entrance clock. Full text inspected for Tamuz–Tessler and Benjamini–Chan–O'Donnell–Tamuz–Tan discusses majority dynamics and general convergence without any Heawood/Fano orbit or basin enumeration. Every page of Agur–Fraenkel–Klein's fixed-point-count article addresses a different one-dimensional, self-inclusive majority rule. Goles–Olivos's classical period theorem is cited, not claimed as new; its full text was not accessed for page-level comparison. Targeted indexed research searches found Heawood homology and unrelated parity automata, but no implication to the graph-specific numerical and structural claim. Equivalent overlooked historical work remains possible; no database-negative claim establishes absolute priority.

## Mathematical value — PASS

The Heawood graph is the unique seven-point Fano incidence graph, a canonical smallest 3-regular girth-six graph. The theorem identifies an exact, sharply contracting nonlinear dynamical projection from 16,384 configurations to a swap on 58 by 58 Fano-geometric symbols. The 28 noncollinear triples give a transparent interpretation of nonconstant equilibria as alternating 6-cycles. Exceptional attraction weights separate the two constant equilibria and the single largest two-cycle basin; the first-entry distribution is exact. These are natural complete recurrence and basin invariants for this canonical finite graph, rather than arbitrarily chosen partial statistics.

## Comparison, source scope and limitations

Primary references and first-public identifiers: Tamuz and Tessler (arXiv:1307.4035, 2013-07-15); Benjamini et al. (arXiv:1405.2486, 2014-05-11); Agur, Fraenkel and Klein (Discrete Mathematics 70, 1988); Goles and Olivos (Discrete Mathematics 30, 1980). The established general bound on recurrent periods and the standard Fano geometry are excluded from novelty claims. The proof does not extend by assumption to larger projective planes, other cubic graphs, asynchronous rules or self-inclusive majority. Exact historical priority is not externally certified.

Self-review: passed. Independent audit: not yet performed.
