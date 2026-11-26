# Independent mathematical audit

## correctness

PASS

For t>0 the entropy minimizer is the positive diagonal scaling of the kernel. The ordinary rows and columns factor with their residual marginals, and the four block masses x,y,z,w are x,p-x,q-x,1-p-q+x. Cross odds xw=t yz follow from scaling invariance and yield the unique feasible positive solution. A hard zero is feasible iff p+q<=1; at x=0 the proportional residual-block condition minimizes the entropy also on the Hall boundary by continuity or by strict convexity on the remaining positive support. Comparing the soft and hard solutions, each block has a constant sign of entrywise difference and absolute mass change x, so TV=2x exactly. An independent upper bound follows from w>=x and yz<=((p+q)/2-x)^2, giving x<=sqrt(t)(1/2-x), with equality exactly at p=q=1/2. For p+q<=1-kappa, the same quadratic increases with pq for fixed s=p+q and along p=q=s/2 increases with s: its x derivative is positive at the root while the s derivative is -(1-t)x-ts/2. The slack maximizer is s=1-kappa, and rationalizing its root gives the recorded formula. Fixed positive kappa gives x_max=(1-kappa)^2 t/(4 kappa)+O_kappa(t^2); when kappa/sqrt(t) tends to u the limit x_max/sqrt(t)=(sqrt(u^2+1)-u)/2 follows by division of the denominator by sqrt(t). Solving the worst-case TV inequality gives the stated sharp M budget. For the rate, row updating differentiates to -D_r^{-1}P_t and column updating then to -D_c^{-1}P_t^T, giving the stated product. Whitening splits the matrix into the orthogonal marginal directions (singular value 1) and one residual rank-one term (singular value |x-pq|/sqrt(p(1-p)q(1-q))). Its square is the nongauge rate. Applying the two displayed AM-GM inequalities to the four positive masses gives the sharp bound; for t<1 both must be equalities, equivalent to x=w,y=z and p=q=1/2. At t=1, all rates vanish, while the leakage is still maximized only at p=q=1/2. The proof's description of two nonzero singular values should be read as at most two at this endpoint; its formula and conclusion correctly include the zero value. As an exact balanced check, t=1/9 gives x=1/8, TV=1/4, and lambda=1/4. Read RESULT.md lines 11–65, VERIFICATION.md and verify.py. The 8,467 recorded finite assertions were not rerun; the proof covers all finite dimensions. The factor is local and for a full sweep on log scaling modulo constants, not a global iteration count.

## originality

PASS

Credit the dimension-free hard-mask TV minimax, its penalty budget and Hall-slack crossover, and their exact joint comparison with the local rate. Do not credit the odds equation, general local derivative, or the worst-rate number in isolation: the rate bound is a Birkhoff specialization and equality at the balanced binary plan is immediate from its spectrum. The known contraction and scaling statements and the closest catalogue originals do not give the sharp hard-mask TV comparison on the Hall-feasible marginal domain or its slack-dependent maximization.

## value

PASS

Replacing an actual forbidden cell with a finite big-M penalty is a natural operation. The result gives the exact worst-case error budget in the transport plan, shows that Hall equality changes the penalty exponent, and determines the transition in the same regime where the local iteration can be slowest. The uniform TV constant and moving-slack behavior provide precise information not supplied by a projective bound or an odds identity at a single pair of marginals. This is not a new general Sinkhorn complexity bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
