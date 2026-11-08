# Independent mathematical audit

## correctness

PASS

For geometric noise D followed by H=exp(bh[[-2,1],[1,−2]]), the nonnegative matrices preserve orthant positivity. The independent diagonal lognormal moments exactly close on s=(E X1²+E X2²)/2, c=E X1X2 with K=e^(−4η)[[μcosh2η,sinh2η],[μsinh2η,cosh2η]] and μ=e^(vh). The positive Perron root controls all second moments and dominates the antisymmetric mode. det(I−K)=0 gives μ*=z(2z²+z+1)/(z²+z+2), z=e^(2η), and therefore the stated v*/b=2+η^−1 log((2e^(4η)+e^(2η)+1)/(e^(4η)+e^(2η)+2)). The analytic φ''<0 factorization proves strict decrease 3→2; continuous Itô covariance exponent changes sign at v=3b. At η=log2, μ=7, independent exact K has det(I−K)=−9/256 while 2<v/b<3. Independently verified symbolic concavity factor and rational witness. Finite checks are corroborative only.

## originality

PASS

The general covariance spectral-radius criterion is classical and Bréhier–Cohen–Ulander already introduced the positive noise/heat splitting. The assessed claim is the model-specific closed-form strictly decreasing boundary, unique finite-step cutoff, and explicit stable-SDE/unstable-splitting witness. Original primary finite-horizon convergence results and general covariance criteria do not directly yield this evaluation, though hidden specialist closed formulas remain a priority risk.

## value

PASS

The exact distinction between pathwise positivity and long-term mean-square stability under splitting is a substantive numerical-analysis boundary. It quantifies the timestep range where a stable physical diffusion becomes unstable under a positivity-preserving integrator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
