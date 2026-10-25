# Independent mathematical audit

## correctness

PASS

The precisely specified planar polynomial resource/replicator flow has two frozen Allee roots r_±(x) with r_−′=−Δ/λ(x)<0, λ(x)≥λ0. The saddle (r_−(0),0) has unstable resource eigenvalue Tr_−(0)λ0 and stable cooperator eigenvalue −wr_−(0). Its stable branch solves h′=−(T/w)g(h,x)/[x(1−x)], with slope h′(0)=−TΔ/(w+Tλ0). The invariant scalar graph has barriers r_−(x)<h(x)<r_−(0); on lower contact h′=0 and r_−′<0, while upper contact has h′<0. Continuation to x=1 follows boundedness and logarithmic blowup otherwise; h(1)=r_−(1). Monotonic x for positive R, Barbalat on finite resource integral and scalar asymptotic sign-crossing give only 0,r_−(0),r_+(0) limits; uniqueness of scalar phase trajectories and the saddle stable manifold separate their basins. Comparison of different k=T/w yields strict h increases with w. For z=h−r_−, the differential comparison z′≤−4Tλ0 z/w+Δ/λ0 proves explicit uniform O(w) bound. Independently integrated the separator with SciPy solve_ivp at A=1/10,c=1/2,d=3/2,T=2,w=1, x=.5: h=0.23295910703649278 vs r_−(x)=0.2298437881283576; re-derived barrier and signs symbolically. Numerical values do not certify continuum claims.

## originality

PASS

Best-of-knowledge PASS for the nonlinear exact global basin separator and its strict w-dependence and uniform slow-greed bound, beyond the same-source qualitative bistability and straight-line interpolation. The source system itself and bistable fixed points are not new.

## value

PASS

The separatrix is the operationally relevant survival/extinction threshold in a natural Allee common-resource system: the source substitutes a linear approximation. Showing the exact dividing stable manifold, its strict greed-rate ordering and a uniform slow-greed error bound corrects a meaningful phase-diagram ambiguity and yields quantitative parameter guidance; far from textbook root-finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
