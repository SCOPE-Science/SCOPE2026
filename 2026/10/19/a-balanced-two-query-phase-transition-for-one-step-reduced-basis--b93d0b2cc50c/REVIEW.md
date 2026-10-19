# Scientific assessment

## Correctness — PASS
For every real spectral ratio \(t>1\), exact one-step PCG is a line minimization in the preconditioned residual direction. Direct substitution proves both active two-eigenvalue errors, including their unnormalized energy scaling and prescribed workload weights. An exact rational-square identity and a completely factored derivative establish the sharp \(t=3\) boundary and the uniqueness, attainability, and formula of the optimizer above it. Diagonalization independently establishes the spectral-condition-number obstruction. The attached symbolic and exact-rational checks reproduce the critical algebra; finite testing does not replace the proof. No assertion extends to other distributions or later iterations.

## Originality — PASS, subject to bibliographic risk
The closest primary source, Fan–Hu–Zhang (arXiv:2609.11097v1, §§3.1–3.5), defines the Type-I regularized reduced-basis inverse but studies nonsingularity, Richardson, and flexible GMRES rather than a shared one-step PCG parameter across multiple right-hand sides. Diouane–Gürol–Mouhtal–Orban (arXiv:2603.28969v1, §§3–4) already formulate finite-budget spectral placement for a fixed initial residual; the general motivation and one-residual objective are not new. Earlier multiple-right-hand-side deflation work provides context. The exact balanced two-query workload bifurcation, unique constrained Type-I parameter, and its contrast with unchanged condition number are not supplied by these inspected statements. A differently formulated average-case Krylov optimization in older literature remains an explicit residual bibliographic risk, not an established novelty guarantee.

## Mathematical value — PASS
Two right-hand sides must share one scalar parameter in multi-query solves; selecting it by worst eigenvalue ratio alone can be uninformative. The mathematically natural workload weights equalize each query's contribution to initial squared energy error, and the theorem supplies an exact yes/no criterion for whether tuning this genuinely shared regularization is worthwhile for a single PCG step. Its sharp \(t=3\) phase transition, unique finite optimizer, and closed-form mean-error gain give a reproducible, meaningful example in which unchanged spectral condition number coexists with strict finite-budget improvement. The example is four-dimensional and not a performance prediction for general PDE discretizations.

## Closest literature and limitations
Primary sources: Fan, Hu, Zhang, arXiv:2609.11097v1; Diouane, Gürol, Mouhtal, Orban, arXiv:2603.28969v1. Earlier multiple-RHS deflation: Stathopoulos and Orginos, arXiv:0707.0131. The exact theorem is limited to the stated SPD matrix, invariant reduced subspace, balanced two-point workload, standard exact-arithmetic PCG, and one update. The proof establishes mathematical identities rather than any measured runtime advantage.

Self-review: passed. Independent audit: not yet performed.
