# Independent mathematical audit

## correctness

PASS

The full three-state no-self-loop stationary-flow polytope has affine coordinates (a,b,J), c=1-a-b, activities a_i>=|J|. Constant affine Euclidean Jacobian and a triangle cross-section of scale (1-3|J|) give w=3|J| with density 3(1-w)² and independent uniform Dirichlet(1,1,1) simplex activities; the balanced stationary section fixes activities 1/3 and yields uniform w. The exact entropy-production expression is Σ=w/3 sum_i log[1+2w/(3(1-w)u_i)] and balanced Σ=w log((1+w)/(1-w)). Direct independent SymPy integration of four explicit terms gives E_sta=-1/2+log(9/4)=0.31093021621632877 and E_bal=1. The pointwise exponential bound δ^{-t} prod u_i^{-t/3}, δ=1-w, is integrable under 3δ² and Dirichlet marginal exactly for t<3; an interior simplex patch supplies divergence for t>=3. Balanced δ-uniform yields t<1 and P(Σ>s)~2e^{-s}; exponential Markov bound combined with matching interior patch gives full-ensemble log-tail rate -3. No density or constant prefactor for full tail claimed.

## originality

PASS

PASS for the nonlinear entropy-production push-forward expectations and the two sharp moment/tail thresholds, not for the underlying uniform flow hyperensemble, current densities or normalization. Hartle–Kumar–Wolpert explicitly introduce exactly the joint flow matrix and derive |J| density and mean |J| in §IV.2.2 but do not compute these Σ statistics. General stochastic thermodynamic entropy production is standard; a change of current prior alone does not compute nonlinear full-ensemble Σ. The exact comparison of these two natural measures is motivated. An earlier general Dirichlet/log-affinity identity could imply this special case, remaining priority risk.

## value

PASS

The object is the minimally cyclic stationary Markov chain where hyperensemble flow geometry is explicit. Predicting EΣ and its tail scale for two natural reference priors is a meaningful statistic beyond mean current; it exposes a sharp threefold change of integrability from a physically motivated conditioning, not merely a normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
