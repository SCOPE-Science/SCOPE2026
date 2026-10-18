# Independent mathematical audit

## correctness

PASS

Write each component of the mass-action ODE as c_i'=P_i(c)+c_iQ_i(c), where P_i is a sum of nonnegative monomials from reactions producing i without consuming it. Analyticity and positivity of the integrating factor give rate-independent leading exponent 1+min sum_j alpha_{rj}h_j and strictly positive leading coefficient; support closure determines exactly which species activate. Every contributing reactant has strictly smaller exponent, so the cost recursion is acyclic, and at most s nonempty closure rounds give the bound H_s=1+mH_{s-1}. The inflow-plus-serial conversion chain attains equality for all integer m,s, with orders 1,1+m,1+m+m²,... . Independently checked m=1,2,3 serial four-species orders 4,15,40; source exact-rational checker inspected for its 152 bounded tests. Assumes positive rates, polynomial mass action, nonnegative initial data; not an absolute observation-time bound.

## originality

PASS

Peter–Ibrahim 2026 full text proves qualitative admissible species-transition closure; its theorem/sections do not calculate the first nonzero initial-time Taylor exponent or the sharp m-molecularity exponential bound. Soliman–Fages–Radulescu 2014 full primary HTML uses tropical min-plus equilibration under parameter rescaling and opposing dominant reaction fluxes, a distinct asymptotic object. Vance–Arkin–Ross PNAS 2002 addresses causal connectivity of pulses at stationary states (accessible abstract), not universally positive initial-boundary Taylor jets. Resultary semantic search found no stronger primary record besides the exact assigned finding. Best-of-knowledge PASS, retaining risk of old jet/valuation interpretations and the 2021 Peter–Ibrahim–Dittrich full text not read.

## value

PASS

The first nonzero Taylor coefficient quantifies a natural gap between structural activation and numerically visible production in chemical kinetics. An exact min-plus structural invariant and a sharp exponentially large onset order achieved by bimolecular chains supply a complete motivated boundary in all network sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
