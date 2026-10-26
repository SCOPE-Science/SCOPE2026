# Scientific review: certified oscillatory sector in a nonreciprocal Ising mean field

## Correctness: PASS
The proof handles every \(J>1\), \(K\ge J-1\) including equality. The crucial fixed-point reduction uses the strictly increasing map \(\operatorname{arctanh}(u)/u\), giving a contradiction to oppositely signed equilibrium factors. The origin is a repelling hyperbolic focus; all other orbits are bounded and exclude its neighborhood eventually, so Poincare--Bendixson applies to their complete omega-limits. The angular inequality is established by monotonicity of \(\tanh(s)/s\), and the period bounds follow from winding number one and strict speed inequalities. Reproducible finite corroboration: 50,000 scalar comparisons, 175 root-search starts and 7,000 trajectory checks; the global claims rest on proof, not sampling.

## Originality: PASS, with residual priority risk
Avni et al. [arXiv:2311.05471 and arXiv:2409.07481] establish the model and its swap-phase phenomenology; the detailed follow-up calculates numerically the fixed-point and cycle phase diagram and near-critical bifurcations. It does not state this simple global sufficient coupling sector, the all-nonzero-data omega-limit conclusion, or the two-sided period certificate. Seung et al. (NeurIPS 1997) prove sufficient fixed-point *convergence* conditions for a broad neural-network class, not the new strong-coupling oscillation guarantee. Blom et al. (arXiv:2407.20312) treat correlation-dependent lattice onset, which does not imply the particular global mean-field bound. The strictest unresolved risk is an unidentified general sigmoidal planar-network theorem that could imply the claim as a corollary; semantic mathematical-record searches did not reveal equivalent coverage and cannot establish definitive priority.

## Mathematical value: PASS
The initial nonreciprocal Ising phase diagram is largely numerical outside small-amplitude bifurcation theory. An explicit unbounded region with a proof for **all initial conditions**, and a calculable upper period bound away from the static-to-cycle transition, provides a structural guarantee useful for choosing robust mean-field oscillatory parameters. The result is not just a local Hopf calculation or an arbitrary evaluated parameter example. The region and period constants are sufficient rather than optimal, and this does not settle uniqueness or fluctuating-lattice stability.

## Limitations and closest literature
The result is deterministic, spatially homogeneous and two-dimensional. It does not certify a noisy thermodynamic time crystal. Model, swap phase and standard Poincare--Bendixson theorem are pre-existing. Priority is not independently validated.

Self-review: passed. Independent audit: not yet performed.
