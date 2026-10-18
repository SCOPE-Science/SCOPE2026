---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At zero-delay update the vector (x_t,x_{t-1}) resets to (-x_t/5,x_t), giving a rank-one reset and an exact positive renewal process indexed by gaps between D=0 events. The renewal kernel has b_1=p/25 and b_{L+1}=(1-p)^2*p^(L-1)*(e1^T A1^L v)^2, v=(-1/5,1). A rational resolvent for the A1 symmetric moment map gives 1-B(1)=24*(432p^3-156p^2-305p+125)/[25*(6p-5)*(36p^2+35p+25)] below 5/6, with B infinite above. Aperiodic positive-kernel renewal theorem gives exponential decay for B(1)<1, nonzero critical renewal level when =1 and exponential growth when >1; last-zero decomposition transfers to E[x_t^2]. Independently recomputed symbolic 6x6 moment transfer determinant -24*cubic/3125, B mass rational, 3 real roots including 0.4267763163 and 0.7912257351, positive Lyapunov matrix at p=1/2. All-p claim rests on renewal argument rather than finitely many simulated delays.

## originality

PASS

Dutta et al. 2018 full original PMLR text gives step-size-restricted sufficient bounds for asynchronous stochastic gradient descent and a conditional freshness p0; its Theorem 3 does not classify Markov-persistence p at overrelaxed step 6/5. Arjevani--Shamir--Srebro 2020 full original text fixes delay tau (rather than Markov switching) and supplies complexity estimates via generating functions, not this exact two-crossover mean-square region. General Markov-jump moment transfer criteria are known and not claimed new. A separate indexed randomized Gauss--Seidel delay-law result concerns iid bounded delay and another algorithm, so it does not entail this correlated two-state cubic. Unindexed equivalent jump-linear-system examples remain an originality risk.

## value

PASS

All p share the same 1/2 fresh-gradient marginal but correlation alone changes the exact stability regime twice. The sharp rational cubic frontier is a precise counterexample to explanations based solely on expected staleness and a motivated stochastic-optimization stability test. It is not a queue-system universal law or an arbitrary one-shot algebra identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
