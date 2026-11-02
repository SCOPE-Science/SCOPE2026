# Scientific review

## Correctness — PASS

The claim is an unrestricted **optimal value** and an exact description of the invariant optimizer family, not a uniqueness claim about arbitrary optimal matrices. Group averaging is valid because the reversible stationary distribution is unchanged by within-class permutations and swapping the equal-mass classes. The complete quotient and fiber eigenspaces give precisely four nonstationary eigenvalues. For fixed \(y\), the lower envelope of \(\max\{u,|w|\}\) is attained at \(x=2(a-y)/3\). The remaining one-variable minimax is solved by explicit monotone crossings and active endpoint constraints; all boundary formulas agree. The support statements about *all* optimal matrices use zero sums of nonnegative edge flows or self-loops after symmetrization. The exact rational verifier checks complete matrices, detailed balance and relevant eigenspaces. Finite checks do not certify the infinitely quantified statement; its algebraic proof does.

## Originality — PASS (qualified)

The closest known results are the 2004 fastest-mixing reversible SDP and its explicit complete-bipartite solution, and the 2009 exact block decomposition for complete multipartite symmetric chains. The 2004 bipartite special case already covers the low-\(a\) support pattern and is **not** claimed as new. The 2009 general decomposition is a method for solving an SDP, not an explicit evaluation of the mass-dependent tripartite minimax, its nontrivial four rational regimes or the separate threshold at \(a=1/4\) distinguishing optional from forced transitions. The exact claim was not found in the searched mathematical records or inspected primary sections. A blanket absence from all specialized literature cannot be established; the inspected later clique-lifting work concerns a different graph class and unindexed specialized literature remains a risk.

## Mathematical value — PASS

The fixed-equilibrium-distribution optimization is a standard numerical/convex optimization problem. Here a natural three-community network exhibits a complete **four-phase** closed-form solution, exact mixing-rate and support boundaries, and a nonuniqueness interval. Community *masses*, rather than the numbers of vertices, govern the transitions, allowing the same rule to apply across different discretizations. The threshold \(a=1/4\) for unavoidable edges differs from the threshold \(a=1/6\) at which such edges first occur in an optimum, which is a useful structural distinction that a single reported SDP optimizer can hide. This is more than a graph-label substitution or a single numerical example.

## Closest literature and residual limitations

Boyd–Diaconis–Xiao (2004), pages 683–685, and Boyd–Diaconis–Parrilo–Xiao (2009), pages 812–813, are the principal overlap checks. The latter explicitly supplies the multipartite eigenblock reduction, so that underlying technique must not be represented as novel. Later clique-lifted topology results assume within-fiber clique edges absent here; nevertheless unindexed specialized earlier or later treatments remain a risk. Exact optimization concerns SLEM, not finite-horizon total variation, and no all-unrestricted-optimizer classification is supplied.

Self-review: passed. Independent audit: not yet performed.
