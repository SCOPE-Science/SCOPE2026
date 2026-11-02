# Independent mathematical audit

## correctness

PASS

The specified 6x6 Langevin drift has positive definite stiffness for p,q>0,x>=0, and a Hurwitz generator because terminal damping rules out undamped eigenmodes. Stationary covariance is the unique Lyapunov solution, and equilibrium linearity reduces the flux to T_L=1,T_R=0. Exact 21-unknown symmetric covariance elimination yields det M=-64 det(K) D and det M-det(M_44)=-256 det(K)(S+2), with positive D=2(S+2)^2(4S+3)/(S+1)+8(S+1)(x-x0)^2. Cramer then gives J/(T_L-T_R)=2(S+1)(S+2)/((S+2)^2(4S+3)+4(S+1)^2(x-x0)^2), S=(p+q)/2+((p-q)/2)^2 and x0=(p+q)/2-3/2+1/(2(S+1)). Strict positive denominator coefficient implies the unique x>=0 maximum at max(0,x0). Differentiating x0 with respect to squared terminal contrast gives -1/[2(S+1)^2], and p=q onset (1+sqrt17)/4 is exact. Independent fresh covariance solves corroborate the eliminant; the universal proof is the polynomial identities plus quadratic geometry.

## originality

PASS

Best-of-knowledge new fully optimized three-site special-case formula and exact boundary/interior transition. General harmonic network Green-function/Lyapunov expressions are prior art; the audited result does not claim to invent those methods. It adds an exact globally tunable center pin, asymmetric endpoint contrast parameter and sharp transition.

## value

PASS

The exact resonant-vs-unpinned optimum and strict shift under endpoint mismatch are a naturally motivated control parameter and qualitative transition in the smallest nontrivial open harmonic conductor. Their exact analytic thresholds can serve as finite-chain benchmarks beyond generic transport identities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
