# Low-intensity concentration for the hyperbolic Poisson–Voronoi Palm typical-cell area

## Context
Let C_lambda be the Palm typical cell of a stationary Poisson–Voronoi tessellation of the curvature -1 hyperbolic plane at intensity lambda>0, and let A_lambda=area(C_lambda). Set M(lambda)=lambda^2 E[A_lambda^2] and V(lambda)=lambda^2 Var(A_lambda)=M(lambda)-1.

## Rigorous result
1. E[A_lambda]=1/lambda.
2. For every lambda>0, 1<M(lambda)<=2 and hence 0<V(lambda)<=1.
3. As lambda->0, M(lambda)->1 and V(lambda)->0. Equivalently, lambda A_lambda->1 in L2.
4. Consequently there is no constant a>0 such that Var(A_lambda)>=a/lambda^2 for all lambda>0. A strictly decreasing positive V on (0,infinity) is also impossible, because its right limit at 0 is 0.

## Proof
For y at hyperbolic distance r from the Palm nucleus o, the event y in C_lambda is the void event for the ball D(y,r), so P(y in C_lambda)=exp(-lambda B(r)), where B(r)=2pi(cosh r-1). Radial area substitution v=B(r) gives E[A_lambda]=integral_0^infinity exp(-lambda v)dv=1/lambda.

For two points y1,y2, Slivnyak–Mecke gives joint coverage probability exp(-lambda U), where U=v1+v2-I and I is the intersection area of the two exclusion disks. After w_i=lambda v_i,
M(lambda)=(2pi)^(-1) integral exp(-(w1+w2)+lambda I_lambda) dw1 dw2 dtheta.
Because 0<=I<=min(v1,v2), the integrand is bounded between exp(-(w1+w2)) and exp(-max(w1,w2)); the latter is integrable and has total integral 2 after angular normalization. This gives 1<=M<=2, with strict M>1 because positive-overlap configurations have positive measure.

Fix w1,w2>0 and theta not congruent to 0. The corresponding radii R_i=B^{-1}(w_i/lambda) diverge as lambda->0. Hyperbolic cosine-law asymptotics give d(y1,y2)-(R1+R2)->log((1-cos theta)/2), so the two large disks converge locally to distinct horoballs through o. Their intersection has finite area for nonzero angular separation. Hence I_lambda remains bounded for each such triple and lambda I_lambda->0. The exceptional theta=0 set has measure zero. Dominated convergence with the exp(-max(w1,w2)) envelope yields M(lambda)->1.

Since E[lambda A_lambda]=1, E[(lambda A_lambda-1)^2]=M(lambda)-1=V(lambda)->0.

## Numerical illustration only
The retained deterministic script reports V(0.5) about 0.238743, V(1) about 0.256639, V(2) about 0.267480, and a Euclidean-model value about 0.280152. These numbers are useful diagnostics, but this record no longer calls the finite-lambda interval or the high-intensity Euclidean limit rigorously certified: the supplied inner lens quadrature has no proved interval enclosure.

## Reproducibility
`artifacts/compute_moment.py` and `artifacts/bounded_test_results.json` are retained unchanged as numerical evidence.

## Literature context
- D'Achille, Curien, Enriquez, Lyons, Ünel, Ideal Poisson–Voronoi tessellations on hyperbolic spaces, arXiv:2303.16831.
- D'Achille, Thäle, Face volume densities of positive-intensity and ideal Poisson–Voronoi tessellations in hyperbolic spaces, arXiv:2606.26049.
