# Independent mathematical audit

## correctness

PASS

Read actual pinned product-of-row-simplices graph-segmentation quadratic with K>=3, graph nonnegative and no isolated vertices, symmetric normalized Laplacian, one-hot supervised targets and fidelity weights omega_i>=0. Holding other rows fixed gives Hessian (q_i-2/eps) I_K with q_i=(L_s)ii+omega_i; for eps<2/M each row edge is strictly concave, so a fractional relative local minimizer is impossible. Every vertex local minimum has strictly positive outgoing simplex-edge derivatives, implying a strict full-product local minimum by the finite tangent cone argument. Independent categorical row rounding changes exactly diagonal graph and fidelity terms: E[E(V)]=E(U)-sum_i(1/eps-q_i/2)(1-||u_i||^2). This proves hard global minimizer existence at eps=2/M and exact gap for smaller eps. The two-node supervised witness with L=[[1,-1],[-1,1]], omega=(1,0), x=(e1+e2)/2, y=e2 has fractional local minima for eps in [1,2), strict above 1, and hard global competitor energy zero; thus 2/M uniform bound is sharp. Independently computed the rounding identity in exact fractions for a nontrivial soft input and confirmed the witness edge-gradient margins.

## originality

PASS

Faccio et al. obtained integrality through full Hessian strict concavity at eps<2/lambda_max(L_s+Domega). The diagonal-row threshold can remain valid even when that full Hessian is indefinite; the witness demonstrates strict improvement. Cardinality-constrained graph partition relaxations have different feasible sets. The elementary diagonal perturbation technique is known; the concrete sharp model-specific theorem and boundary witness are the contribution.

## value

PASS

A sharp implementable local-minimum integrality threshold for a named multiclass graph segmentation objective improves the full matrix spectral condition; the exact categorical-rounding energy gap and labeled two-vertex nonglobal fractional witness identify the nontrivial boundary. Results apply to optimization guarantees without requiring prescribed class sizes, so not merely an elementary restatement of a spectral bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
