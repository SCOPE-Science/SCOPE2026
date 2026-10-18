# Independent mathematical audit

## correctness

PASS

From Stillfjord–Williamson Eq.(3.2), zero damping epsilon=0 gives T_j(1)=1 and omega1=1/s², so a single shared sampled curvature lambda through all s internal stages yields y1=(1-alpha lambda/s²)y0 and yj=2(1-alpha lambda/s²) y_(j-1)-y_(j-2). Therefore macro multiplier is T_s(1-alpha lambda/s²). With alpha=s²t/ell, t∈(0,2), kappa>2/t, multipliers a_s=cos(s arccos(1-t)) with |a|<=1 and b_s=(-1)^s cosh(s arcosh(kappa t-1)) with |b|>1. Independent macrostep sampling implies exact all-q moment law [((1-p)|a|^q+p|b|^q)]^n and sharp p_q=(1-|a|^q)/(|b|^q-|a|^q), including p_q=0 when |a|=1. p2~4 sin²(s theta)e^(-2s gamma) uniformly in phase. If 0<|a|<1, strong law gives exponent (1-p)log|a|+p log|b| and Jensen strictly implies p_as>p2. If a=0, first low-curvature sample annihilates iterate a.s., while p|b|^q>1 can make moments diverge. Exact witness (s,t,kappa,p)=(3,1,3,.01) has (a,b)=(0,-26), E[x_n]=(-13/50)^n x0 and E[x_n²]=(169/25)^n x0². Independently computed rational Chebyshev recurrences for s<=8 and several curvatures, verifying exact witness; all-n arguments are analytic.

## originality

PASS

The original 2022 SRKCD article specifies same-sample stages, convergence upper bounds and stabilized polynomial mechanics but does not give exact per-moment sharp rare-curvature frequency or near-sure-extinction/mean-square divergence. Deterministic Chebyshev-gradient spectral stability treats a max-curvature stability interval rather than iid across macrosteps.

## value

PASS

Shows the exact probability threshold at which rare stiff mini-batches overturn the quadratic deterministic stage window and separates almost-sure convergence, finite-time extinction and exploding high moments. The exponential-in-s stage penalty and exact resonance witness are informative boundary phenomena for stabilized stochastic optimization, with explicit limited assumptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
