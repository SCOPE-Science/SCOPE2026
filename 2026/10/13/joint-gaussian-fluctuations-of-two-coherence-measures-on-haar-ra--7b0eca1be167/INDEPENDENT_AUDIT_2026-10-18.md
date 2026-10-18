# Independent mathematical audit

## correctness

PASS

For complex Haar states the squared basis amplitudes are exactly Dirichlet(1,...,1), represented by independent Exp(1) variables E_j divided by their sum. Rebuilt the formulas L=(sum sqrt(p))^2-1 and H=-sum p log p, Dirichlet mixed moments Gamma(d)/Gamma(d+sum s_j) prod Gamma(1+s_j), and log derivatives: E L=pi(d-1)/4 and E H=h_d-1. Fourth-moment index patterns give finite Var(L); mixed exponent derivatives give Cov(L,H)=pi(d-1)(3 log2-2)/(2(d+1)), including the d=2 no-three-distinct-index boundary. Apply multivariate i.i.d. CLT to (sqrt E,E,E log E), and delta method for f(a,b,c)=a^2/b, g=log b-c/b with gradients (sqrt pi,-pi/4,0) and (0,2-gamma,-1). Exact asymptotic Sigma entries pi-5pi^2/16, pi(3 log2-2)/2, pi^2/3-3. Independent numerical arithmetic confirms Sigma=(0.05734127824937,0.12478648186561,0.28986813369645), determinant 0.0010497432535>0, correlation ~0.96790697. Functional independence of sqrt(x), x, x log(x) under Exp density ensures strict nondegeneracy in all dimensions of limit. Random simulations are unnecessary to establish this CLT; no finite-d Gaussian law or convergence rate is claimed.

## originality

PASS

Best-of-knowledge originality after independent statement/implication comparison, published-record semantic search and relevant primary material inspection. The known premises and residual risks below are credited, not silently treated as novel.

## value

PASS

Joint fluctuations determine how much one operationally standard coherence monotone predicts another on Haar-random complex pure states. Nonzero limiting determinant and residual linear-prediction entropy variance are more informative than known separate means/concentration bounds. Exact finite covariance supplies a calibrated quantitative bridge between l1 coherence and relative-entropy coherence; although the probabilistic technique is standard, this particular joint invariant has motivation independent of generic delta-method exercises.

The dated certificate retains the supplied scientific assessment, sources and limitations.
