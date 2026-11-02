# Scientific review: finite-timescale endemic oscillations in NOD-SIS

## Correctness — PASS

The construction solves both steady-state equations at \((p,x)=(1/2,-1/2)\) for every positive timescale, computes the exact Jacobian, and proves the imaginary pair crosses with nonzero speed. A third-order exact Taylor calculation in canonical rotating coordinates gives \(\ell_1=27P(\log3)/[4096(3\log3-4)(24\log3-23)^2]<0\). The symbolic checker reconstructs the vector-field derivatives instead of assuming them; elementary rational bounds certify the sign without floating-point reliance. The nondegenerate Hopf theorem therefore establishes a locally orbitally asymptotically stable small cycle on the smaller-timescale side, inside the physical state region. The conclusion is local and makes no numerical infinite-time claim.

## Originality — PASS, subject to bibliographic limits

The exact model appears in Ordorica Arango et al., arXiv:2410.12993v1, Sections III–IV. Its examined main results address stationary behavior, stability regimes, and strong-peer-pressure equilibria, not a certified supercritical Hopf cycle of its homogeneous single-population risk-averse branch. Zhou–Levin–Leonard, arXiv:2007.01424, report oscillations in actSIS with filtered prevalence and distinct contact-feedback equations, notably with heterogeneous attitudes; this cannot be substituted for the nonlinear opinion vector field analyzed here. Additional checks against network risk aversion, opinion-density models, and mathematical research records did not locate the identical coefficient, parameter construction, or a theorem implying it. Novelty is a claim about the examined literature, not mathematical uniqueness of a research discovery. A broader unindexed treatment of planar opinion–epidemic equations remains a residual risk.

## Mathematical value — PASS

An attracting epidemic oscillation in a **single homogeneous risk-averse group** answers a natural dynamic question left unresolved by stationary bifurcation analyses: finite response speed combined with nonlinear peer pressure can sustain variation in infection even in the absence of delay, external excitation, or heterogeneous subgroups. The sharp local threshold and exact sign of the Hopf coefficient distinguish an actual stable epidemic cycle from a mere imaginary spectral crossing. The mechanism bears on whether fixed-point predictions alone capture prevalence dynamics.

## Limitations

The small attracting cycle exists for sufficiently small positive distance below the critical timescale, not for every smaller timescale. Neither global basin, unique cycle, stochastic effect, nor robustness to all biological model extensions is established. Independent bibliographic audit and validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
