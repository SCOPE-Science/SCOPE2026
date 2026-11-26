# Independent mathematical audit

## correctness

PASS

Each coordinate has i.i.d. scalar multiplier a=1 or 1−2α before momentum; its draw count has odd parity with probability q=[1−(1−2/m)^r]/2. Within-step coordinate correlations do not enter the sum of squares. For β<1 the mean companion B is Schur by the quadratic Jury inequalities. The Lyapunov entries satisfy W22=W11 and W12=(μ+β)W11/(1+β), yielding the stated impulse energy. In the squared-error convolution, innovations are martingale differences. The nonnegative kernel mass is below one exactly when 1−α−α(1−2q)β−β²>0; an exponentially weighted kernel yields decay there. At or above unit mass with β<1, exponential tilting to unit mass gives an aperiodic renewal with finite mean and summable forcing positive at its first index. The renewal limit is strictly positive, unweighted at equality and exponentially growing in the unweighted sequence above it. For β≥1 the mean roots are either a conjugate pair with modulus √β, or positive reals both >1 (use product β and p(1)=1−μ>0); the synchronized nonzero initialization cannot decay. Jensen therefore excludes mean-square convergence. For β>0 the covariance operator squared maps any nonzero positive semidefinite matrix to a positive definite one: rank-one inputs with nonzero first coordinate have two noncollinear output vectors in one step, and an input with zero first coordinate has nonzero first coordinate after one step. This also justifies the spectral factor interpretation. At β=0 the radius v is simple. Eliminating the lower covariance entries gives ρ'(0)=2μ(v−μ)/v and at α=1/2 the second derivative 2q/(1−q). Parity gives the asserted r-monotonicity and m=2 plateau. Independent symbolic elimination and exact-rational covariance trajectories at q=1/2, α=3/4 (β=2/5, 1/2, 3/5) checked the derivatives and decay/critical/growth example. The critical iterates round to 0.75 at the sampled large indices from unit initial error; the limit is exactly 3/4, as the critical recurrence preserves s_k−u_k/2+s_(k−1)/4=3/4 and u_k tends to half the limiting s_k. Replay: python -B /workspace/branches/frozen_recheck.py 2.

## originality

PASS

The exact boundary and phase classification for all relaxation parameters and reflection parities, including positive finite critical limit, and the local rate law for q<1/2 survive the antecedent checks. Do not credit the unrelaxed single-reflection stability special case, the q=1/2 local sign transition, the basic covariance method, or the momentum-free tightness claim as new.

## value

PASS

Identity systems isolate the intrinsic effect of reflection and inertia without conditioning. A sharp second-moment boundary, positive critical plateau and explicit mean/second-moment separation give useful benchmarks for method design and for interpreting weaker sufficient bounds. The local acceleration sign versus relaxation also delineates when a small momentum perturbation is helpful; the known two-coordinate behavior alone does not establish its persistence at other parities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
