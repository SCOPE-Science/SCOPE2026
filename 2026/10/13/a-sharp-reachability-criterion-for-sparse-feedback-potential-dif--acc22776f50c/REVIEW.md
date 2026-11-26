# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 21–69. Compare trajectories from the same initial state. No observation edge leaves R_i for its complement. All players outside R_i are opponents whose unchanged feedback rules thus see identical inputs at time t; their uncoupled updates preserve equality at t+1. Induction gives exact state-action invariance outside R_i, so under the support separation each nuisance stage cancels and the unilateral payoff difference equals the potential difference. Any maximizer therefore passes the Nash comparison in the admissible class. Sharpness uses a simple path to k in the intersection, scalar dynamics x_next=a and a distinct scheduled copy at each edge. The zero initial state and baseline give zero potential, which is a global upper bound; the unilateral impulse gives exactly −δ²∑_{r=0}^m α^r+α^m Cδ, positive for the displayed interval. For m=2, α=1/2, C=1 and δ=1/20 the gain is 13/1600. Extra edges are allowed, not forced to be active. Supports are permitted dependency sets, so no necessity is claimed for every individual nuisance function. The theorem compares feedback policies from the initial state for which the potential is maximized; it does not assert off-path optimality from other states or existence. Read VERIFICATION.md and verify.py without running the uploaded verifier; the universal result rests on the induction and smooth finite-stage counterexample.

## originality

PASS

The own-state-only conclusion and the abstract policy-potential decomposition are established prior results. The distinct result supported here is their concrete sharp support criterion for directed sparse feedback with uncoupled dynamics, including the converse counterexample for every supplied observation graph with a reachable nuisance vertex. An inaccessible adjacent finite-horizon paper leaves the specific risk documented below.

## value

PASS

The criterion allows feedback to use some other players' states while retaining a single maximization formulation, which own-state-only sufficiency cannot explain. Transitive rather than direct influence is essential, as the smooth witness gives a deviation that reaches a payoff-relevant player only after several stages. The matching necessity for a guarantee based only on support makes the distinction actionable without claiming optimizer existence or equilibrium at off-path states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
