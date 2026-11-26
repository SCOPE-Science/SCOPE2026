# Independent mathematical audit

## correctness

PASS

On the weighted oval C^{2n+2}+(n+1)S²=1 the coordinate determinant is nonzero. Differentiation gives z'=−z+nκz²C^nS² and s'=z bκ in time η, with z=R^n and bκ=1+κC^{n+1}S bounded below by 1−|κ|/(2√(n+1)). In phase the equation becomes z_s=aκ z−1/bκ. Its affine map has slope exp(Λκ) and negative intercept; the unique fixed solution has positive numerator divided by 1−exp(−Λκ) at every phase and is positive exactly when κ>0. At κ=0 the map is a strict translation. No higher iterates give new admissible periodic solutions. This use of the affine equation is only on positive segments; the proof sentence about crossing phases must not be taken to assert that all nonzero initial data complete a revolution. All closed trajectories do. Integrating the periodic log-radius equation gives the time T=Λκ and the section derivative gives exp(T). Independently, in the stated integral substitute t=sin θ, average cos²θ with sin²θ by θ↦π/2−θ, then put x=2θ and use tan x on the half-range. The integral is π/(4√δ) for δ=1−κ²/[4(n+1)], giving exactly T=π nκ/((n+1)^{3/2}√δ). Expansion yields both stated constants. Equilibrium elimination gives n²(u^n)²−nκu^n+n+1=0. At the positive discriminant threshold the scalar equation has nonzero second derivative and parameter derivative, and the other eigenvalue in the plane is 1; this also checks the saddle-node terminology. Neither this nor the period asymptotic classifies cycles at or beyond the threshold. Independent direct-plane shooting by antipodal half return gives four periods including T(2,1)=1.26296776680; independent angular quadrature matches the elementary expression. Replay: python3 /workspace/branches/independent_replay.py 1 (SciPy); output /workspace/branches/independent_replay.out. Frozen verify.py inspected, not run.

## originality

PASS

The supported distinct claim is quantitative: the exact dependence of the balance-time minimal period on κ throughout the positive open interval and the sharp one-sided limits, with the stated signed-coefficient classification proved in that setting. The fixed-coefficient numerical observation and Floquet relation were already known; neither receives novelty credit. Classical phase-portrait classification creates qualitative overlap risk, but the available statements do not mechanically supply this period law with the given parameter, constants and time convention.

## value

PASS

The η-period was previously available numerically for a motivating coefficient. A natural variation of that coefficient now gives an exact law throughout the rotating regime and quantifies the slowdown at the nonzero-equilibrium threshold, while retaining the original balance-time convention. The elementary evaluation makes the dependence particularly usable. The result does not rely for significance on a standard Floquet identity, the equilibrium discriminant alone, or additional blow-up claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
