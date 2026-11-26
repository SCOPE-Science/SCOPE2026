# Independent mathematical audit

## correctness

PASS

The frozen proof makes a false inference at RESULT.md line 50: all zeros seeing ones in the current phase does not persist, e.g. all ones vacuously satisfy it and then reach all resting in two updates. The recorded capped checker tests that predicate on the sixth image and computes projected periods, but does not explicitly verify the three-phase lifting of recurrent capped states. The replacement corrects the proof without changing the displayed law. Hub colors and the two nonempty masks of present nonhub colors determine the next projected state. For a resting nonhub, the same-color class has no effect on its excitation, and for a resting hub only its own nonhub set and the other hub matter. At a phase, the test evolve(s)=rotate(s) is equivalent to every actual vertex rotating: a blocked hub is detected in its coordinate and a blocked resting nonhub class is detected because its next mask lacks color 1. The new bounded certificate, run as `python3 /workspace/repairs/3/support_certificate.py`, followed all 441 mask orbits, checked fixed all-resting states and every phase of every recurrent three-cycle, and proved lifted periodicity no later than time six (five for extinction). An earlier labelled periodic state would project to an earlier periodic mask state, so entry times are exact. For each shore with mask S, the labelled count is the EGF (exp(z)-1)^|S|. Exact polynomial equality in E=exp(z), F=exp(w), clearing denominators by six, verifies all 13 layer formulas: E-1, 2(E^2-1), 3(E^3-1) give 1, 2^a, 3^a at positive nonhub sizes. This is a finite exhaustive proof of all-size identities, not graph-size interpolation. It verifies the period-three witness (h,k,S,T)=(0,2,{1},{0,1}), realizable for a>=2, b>=3 and mirrored when appropriate, and the singleton-mask restriction and time-five witness for (2,2). For recurrent configurations, the all-three-colors shore is self-supporting; a shore with a missing color has all nonhubs one phase behind its hub and needs the hub successor color across the bridge. Both shores cannot have the latter form; inclusion–exclusion and the hub phase choices give 9AB+3(A+B), with one orbit per three recurrent states. The extinction counts sum to 9(X-1)(Y-1), giving the stated probability. The run reported PASS for the 441 states, recurrent lifting, all thirteen identities and sharpness. The two original supplementary code paths and their recorded outputs were inspected, not executed. This is not Lean verification.

## originality

PASS

The replacement gives priority credit for the aggregate extinction law, the general period dichotomy specialized to these cliques and the five-step extinction upper bound. The distinct claim is the exact first-entry census, its palindromic transient period-three layers, the sharp six-step surviving cutoff, and the graph-specific recurrent orbit count and description.

## value

PASS

A single edge bottlenecks excitation between internally complete neighborhoods. The first-entry law quantifies how that bottleneck affects both extinction and surviving rotating states, at a precision the prior synchronization and excitation-rate results cannot distinguish. A size-independent sharp cutoff, full labelled entrance layers with a non-obvious period-three symmetry, and recurrent counts provide a useful exact benchmark for finite-graph excitable dynamics. The value does not depend on repackaging the already implied aggregate extinction probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
