# Independent mathematical audit

## correctness

PASS

The update is the exact beta1=beta2=0 denominator-smoothed scalar Adam specialization T(x)=x(1-eta/h(|x|)), h(r)=r+eps r^{-(p-2)} for p>2. h is strictly convex and coercive with unique minimum at r*=((p-2)eps)^(1/(p-1)), yielding eta_c=2(p-1)r*/(p-2). Eta below eta_c means radial multiplier in (0,2) for all nonzero radii, strictly decreasing radii and convergence to zero. Equality gives nonzero symmetric 2-cycle; above threshold exactly two symmetric radii r_-<r*<r_+, with two-step derivative (1-2(p-1)eps/(r^(p-1)+eps))² >1 for inner and <1 for outer; 0 locally attracts since eta/h(r)->0 as r->0. h Taylor at r* gives sqrt splitting and eventual radial recurrence gives exact k|x_k|^(p-2) limit eps/((p-2)eta) along nonterminating zero-convergent paths. Independent rational p=3 eps=1 eta=5 gives cycle radii 1/2,2 and squared multipliers 121/25,1/25.

## originality

PASS

The special memoryless p>2 nonlinear map has a saddle-node pair away from locally stable zero, unlike quadratic flip thresholds or the two-memory Adam model. Generic one-dimensional bifurcation methods are prior.

## value

PASS

The exact global stability frontier, distant saddle-node pair of symmetric cycles, nonlinear coexistence with an attracting minimizer and algebraic convergence rate describe a genuine sharp obstruction in a natural normalized-gradient optimization update. It is a bounded but meaningful dynamical classification, not merely exhibiting one counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
