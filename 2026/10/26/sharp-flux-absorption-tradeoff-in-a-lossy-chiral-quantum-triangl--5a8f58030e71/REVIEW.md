# Review of the sharp flux–absorption tradeoff

## Correctness — PASS

For \(\sin\phi\ne0\), the dissipativity identity forces any non-decaying eigenvector to vanish at the trap, which would require \(e^{i\phi}=\pm1\), a contradiction. Thus the system is exponentially stable. The explicit Hermitian \(Q\) satisfies \(A^\dagger Q+QA=-I\) identically and so equals the convergent survival integral. The resulting scalar function reduces the flux problem to a single sine variable with one strict minimum; the remaining absorber-strength minimization proves the sharp bound and all equality cases. The actual embedded `check.py` passes 11 symbolic checks and 139 independent numerical/optimization tests. Numerical sampling alone does not prove the result.

## Originality — PASS on inspected evidence

Zimborás et al. (arXiv:1208.4049) give the closely related three-vertex chiral switch, sink dynamics and **half-arrival** optimization, while Lu et al. (arXiv:1405.6209) address unitary transfer and time-reversal symmetry. Longhi (arXiv:1312.4693) studies a continuum non-Hermitian ring spectrum. The later Finocchiaro et al. study (arXiv:2507.10669) uses periodic projective measurements and optimizes detection probability, a different dynamics and functional. Their results establish neither the continuous-loss integrated-survival formula nor its sharp joint optimizer under their stated objectives. Relevant published mathematical-index searches did not return an implication-dominating theorem; this is not proof that no equivalent historical formulation exists. Possible uninspected equivalent work remains a priority risk.

## Mathematical value — PASS

The exact minimization answers a natural quantum routing design question: how should a fixed coherent triangle be threaded with flux and how strongly should its only target site absorb to minimize expected capture time? At weak absorption the best flux is not maximally chiral, and a sharp threshold changes the optimizer count from two to one. The separate global optimum captures the competing loss and quantum-Zeno penalties. Neither a generic Lyapunov solution method nor a single fixed-flux example automatically determines these strict thresholds and equality conditions.

## Scope and residual risks

The physical Hamiltonian and absorption mechanism are idealized, and no result is claimed for longer rings, nonuniform couplings, discrete measurements or finite-time performance. The main historical-priority risk is an equivalent calculation in older quantum-transport literature not identified by the inspected manuscripts and research-index searches. The code is an ordinary algebraic/numerical reproducibility aid; it is not independent scientific validation.

Self-review: passed. Independent audit: not yet performed.
