# Independent mathematical audit

## correctness

PASS

Wang §3.3 equations (2)–(4) give the three payoff differences; substitution produces exactly the frozen brackets and respects the stated positive costs and inspection-rate constraints. This is not Wang's numerical regime. The cube and y=z are invariant, and x increases to 1 by logistic comparison. On the diagonal, the stable branch at (1,rho) starts strictly between rho and T(x)=rho+eps(1-x): its eigenslope in 1-x is a0 eps/(a0+L1), with a0=rho(1-rho), L1=1+eps(1-rho). At w=T the contact derivative of w-T is +eps xdot, so the branch cannot leave this strip in continuation backwards; crossing rho would instead prevent forward convergence to the saddle. The strip, xdot>0 and continuation of the scalar analytic graph yield its full interior domain. Monotonicity then gives a unique backward limit w at x=0, which must be invariant there, hence w=s=rho+eps. For arbitrary diagonal initial data w can switch monotonicity only from decreasing to increasing, so w tends to 0, rho, or 1. The stable branch is the only interior set tending to rho, and scalar order in x separates the other two limits. I checked the cusp without invoking a node linearization theorem: write v=s-h, and x v'=A(x,v)(v-eps x) with A=(s-v)(1-s+v)/[(1-x)(1+eps(1-s+v))]. Then A tends to kappa in (0,1) and v>eps x. For any kappa+delta<1, x v'/v <= kappa+delta near zero gives v>=C x^(kappa+delta); substituting this back gives x v'/v>=kappa/2 near zero, hence v=O(x^(kappa/2)). Now the logarithmic derivative of v/x^kappa is O((x+v+x/v)/x), integrable at zero, proving a finite strictly positive ratio limit. For the response, writing eta=h(x(t))-rho gives eta'=a0[eta-eps(1-x(t))]+O(eps²) uniformly by the barriers. Integrating against exp(-a0 t) from 0 to infinity selects the bounded solution. The x-logit differs from x's unperturbed logit by at most eps t, so its substitution under the exponential weight costs O(eps²); this yields the exact pointwise first variation. In the lower 3D box the two growth brackets stay bounded above by negative numbers fixed by the initial shares; in the upper box they stay positively bounded below. This proves convergence and the two volume bounds, including the 1/400 unsampled lower box. Independent replay `python /workspace/branches/independent_audit_replay.py` checks two response step sizes by backward logit integration, not a proof of the basin or cusp.

## originality

PASS

The payoff model and the finite symmetric-grid protocol are prior; the verified distinct claim is the exact global separator on a symmetric slice of a different admissible parameter family, with enclosure, nonvanishing fractional endpoint law, first-order response, and an explicit positive-volume box missed by the nine starts. The proof uses established comparison and invariant-manifold ideas rather than a new general separatrix theorem.

## value

PASS

The exact threshold fills a gap left by testing initial conditions on a finite symmetric grid. Its sharp barriers and endpoint scaling quantify how substantially the initial cooperation share needed for convergence can change as regulation becomes rare. The explicit basin box is a rigorous counterexample to inferring full coverage merely from nine cooperative outcomes in an admissible regime, not a claim about what happened in Wang's run. No stochastic-learning result, exact 3D basin volume or policy inference is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
