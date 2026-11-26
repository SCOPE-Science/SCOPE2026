# Independent mathematical audit

## correctness

PASS

For raw payoffs and positive gaps, summing the successor-versus-predecessor inequalities on any cycle of length at least three gives the cycle-sum lower bound. An independent sufficiency check uses chosen payoffs x_i: for a nonmutual arrow i→j, setting the reverse entry to x_i−ε requires exactly x_j−x_i≥δ_j−ε. On each long cycle these differences can be assigned by distributing nonnegative slack of total |C|ε−Σ_C δ; on a loop use a freely chosen diagonal, on a two-cycle use equal chosen payoffs, and propagate the inequalities outward over each in-tree. Use a common shift and set other competing entries to a small common positive constant. This realizes any ε at least the greatest long-cycle mean, including ε=0 when no such cycle exists and the vacuous n=1 case. The source's symmetric depth-ranked tree assignment also works; it has no conflict with long-cycle reverse entries. The restricted-map count follows from choosing cyclic labels, an involution, and the specified-root forest, with the k=n term interpreted separately. Lagrange inversion and dominated convergence give the stated known asymptotic. VERIFICATION.md and check.py were inspected; the exact witness enumeration and numerical LP results there are recorded finite evidence, not fresh executions or proofs for arbitrary real gaps.

## originality

PASS

Credit the sharp prescribed-map, heterogeneous-margin payoff realization, not the classical cycle-mean method, unconstrained topology realization, or any of the enumeration. The inspected earlier sources and indexed variants do not cover the full quantitative payoff claim.

## value

PASS

The invariant measures a natural cost in the partner-choice model, not merely whether representation is possible. It locates all obstructions in long cycles, shows that even large margins in the trees cost no skew, and distinguishes a worst cycle's average from the largest single gap. Exact attainment and the common-gap phase boundary are usable in specifying reciprocal payoff tolerances. No value credit is assigned to the known count or to empirical predictions outside the raw-payoff model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
