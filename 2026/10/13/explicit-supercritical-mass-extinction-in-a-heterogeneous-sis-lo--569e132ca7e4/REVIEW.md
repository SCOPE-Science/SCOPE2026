# Scientific review: an explicit supercritical-mass extinction construction

## Correctness — PASS

The claim concerns the Neumann mass-action system with immobile susceptibles, infection diffusivity \(10\), \(\beta=1-3\cos(\pi x)/4\), \(\gamma=2\beta\), and \(S_0=9/4+\cos(\pi x)\). For any \(H^1\) test function, mean/mean-zero decomposition and the Neumann Poincare inequality force \(\sigma(10,\beta(S_0-r))\le-1/16\); the proof supplies the exact cross-term and Young constants. An admissible witness \(\ell=(199+\cos(\pi x))/200\) has \(\sigma\le-17/400\) and mass \(9/4+1/800\). The perturbed principal eigenfunction exists by the source's Lemma 2.4, its comparison eigenvalue is at most \(-9/200\), and the infection comparison/bootstrap yields \(\|I(\cdot,t)\|_\infty\le10^{-4}e^{-t/25}\). The susceptible change never exceeds \(7/1280<1/100\). Conservation and positivity place \(N\) strictly between \(9/4\) and \(N^*_{S_0,r}\). The standalone arithmetic verifier returned `VERIFY_OK`; infinite-dimensional claims are established analytically, not inferred from finite experiments.

## Originality — PASS, with stated access risks

Salako and Wu [1], read in the full open version, explicitly leave this extinction alternative unresolved in Remark 3.6: prior Theorem 3.3 allows it but does not exhibit actual data in the open mass interval. The exact new result is the **simultaneous realization** of a strictly positive disease-free basin, total mass exceeding both \(\int r\) and \(\int S_0\), and an explicit strict lower bound on \(N^*_{S_0,r}\). Source Corollary 3.5 applies to constant transmission or fixed-sign initial risk, none of which holds here. The Castellano–Salako multiplicity preprint [2] was inspected including theorem statements, proofs and appendix constructions; it concerns equilibria for positive susceptible diffusion, not this trajectory at exactly zero diffusion. Deng [4] uses a nonconservative Dirichlet problem. [3] could be inspected only through its abstract; its emphasis is asymptotic endemic equilibria as both diffusion rates tend to zero. Text-search/database nonmatches alone are not novelty proofs. A complete equivalent result in inaccessible or unindexed literature remains a residual risk.

## Value — PASS

This supplies a concrete analytic resolution of a specific published open alternative and demonstrates that heterogeneous transmission weighted against initial susceptible density can overturn the naive total-mass persistence criterion. The construction has strictly positive initial infecteds, an explicit quantitative extinction rate, and a certified population interval, rather than a boundary or trivial disease-free initial state. Its applicability is intentionally limited to a concrete one-dimensional heterogeneous profile.

## Closest literature and limitations

[1] is the defining source and closest published result. [2] studies related equilibrium multiplicity with positive susceptible movement; [3] is an incompletely accessible limit-of-equilibria study; [4] differs in boundary conditions. Exact uniqueness against all unpublished or unindexed research is neither asserted nor demonstrated. This is not a global basin classification or an assertion of generic extinction for all supercritical masses.

Self-review: passed. Independent audit: not yet performed.
