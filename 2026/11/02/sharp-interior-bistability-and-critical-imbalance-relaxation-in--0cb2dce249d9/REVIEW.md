# Independent mathematical audit

## correctness

PASS

PASS. Exact equilibria: diagonal r+a r²=1 and off-diagonal x+y=1/a, xy=(1-a)/a², giving x,y=(1/2±sqrt(a-3/4))/a and existence precisely 3/4<a<1. The positive equilibrium Jacobian has off-diagonal -2axy, negative trace and det=(1-a)(4a-3)/a² at asymmetric branches; diagonal antisymmetric eigenvalue crosses 0 at a=3/4. Since a<1, each per-capita growth is uniformly positive at sufficiently small abundance after bounding the other species by 1+epsilon; logistic comparisons give compact interior omega limits. Dulac multiplier 1/(xy) yields negative divergence -1/x-1/y, excluding periodic/homoclinic cycles; together with finite equilibrium structure this enforces global convergence. The difference sign is invariant and the diagonal is precisely the saddle stable manifold. For a=3/4 with s=(x+y)/2,d=(x-y)/2, independent SymPy algebra gives s=2/3-(3/8)d²+O(d⁴) center branch, d’=-(3/8)d³+O(d⁵), so t d²→4/3, and the stated limits follow. Strictly diagonal data converge exponentially, an explicit exception. Checked a=13/16 sink coordinates (12/13,4/13) and reverse.

## originality

PASS

PASS, qualified. Nonlinear two-species coexistence bistability is already explicitly demonstrated by Vet et al. 2018 with mutualism plus competition, hence that generic phenomenon is NOT new. Cui et al 2024 gives a general higher-order Lotka–Volterra analysis with sufficient global/uniqueness results. Neither inspected relevant result implies the precise pure quadratic cross-inhibition normal form with sharp a=3/4, complete diagonal basin partition, and physical-time critical amplitudes. Literature on generic supercritical pitchforks explains the local exponent abstractly but not automatically these coefficients/global basins. A canonical normal-form equivalent in older ODE literature remains possible.

## value

PASS

PASS. The model is a natural exchange-symmetric minimal two-competitor extension of logistic interaction by a quadratic competitor-density term; mutual invasion need not imply one unique coexistence state. A globally exact basin boundary, a sharp phase diagram, and the t^-1/2 relaxation coefficient at a degenerate threshold are specific useful dynamical quantities beyond routine linearization or a generic pitchfork label.

The dated certificate retains the supplied scientific assessment, sources and limitations.
