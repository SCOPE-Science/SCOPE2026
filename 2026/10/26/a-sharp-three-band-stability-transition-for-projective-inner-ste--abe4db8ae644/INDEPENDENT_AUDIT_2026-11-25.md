# Independent mathematical audit

## correctness

PASS

The published tableau gives, in the signed inner Euler coordinate z=1−λx, R=z[1+c(z²−1)] with c=(1−λ)/(2λ)>0. For z<−1 it gives R<−1. On [−1,1] the two inequalities reduce to 1+c z(z−1)≥0 and 1+c z(z+1)≥0. Their minima are 1−c/4, attained at z=±1/2. At c>4 their negative intervals lie in different halves, giving the claimed disjoint gaps and endpoints; at c=4 the amplifier is 4z³−3z and has the two interior neutral modes; at c<4 every interior mode contracts strictly. Mapping back and expanding the discriminant gives the claimed widths and asymptotics. The independent exact-rational stage replay is `python3 /workspace/independent_checks.py 4`; the proof, not that grid, handles the continuum. The frozen checker uses floating-point band cutoffs for some predictions, though the amplification values are rational. The opening reference to damping must be read as weak stability at the threshold and at the two outer endpoints, as stated precisely in the theorem.

## originality

PASS

Only the complete quantitative real-axis classification passes, not the method, scalar stability criterion, or qualitative existence of separated stable regions. The closest prior work determines the polynomial implicitly by its tableau and RK formula, but does not solve the two parameter-dependent inequalities. The sign analysis that produces the exact topology, endpoint and neutrality classification is a short further calculation, not a specialization of a prior classification theorem found in the checked texts.

## value

PASS

This is a complete classification for a naturally motivated published stiff integrator, not an isolated cubic evaluation. It tells when any spectrum inside the inner Euler interval is weakly stable, when interior modes actually decay, and which spectral gaps are required otherwise. The critical neutral exceptions and diverging small-ratio gap widths are concrete benchmarks. The value is restricted to the real scalar spectrum, not general complex, nonlinear or nonnormal stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
