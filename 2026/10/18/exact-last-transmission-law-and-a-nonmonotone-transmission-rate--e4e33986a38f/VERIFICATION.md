---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limitations

The analytic checks reconstruct the transition rates of the nearest-neighbor model, the initial \(\operatorname{Exp}(2\lambda)\) clock, the two independent one-sided compound birth/death fronts, and both the zero atoms and positive densities of their last-transmission offsets. Direct integration gives the exact time law; differentiating its expectation gives the unique positive root of the cubic. The proof applies for every finite \(\lambda>0\).

Run `python verify.py`. This standalone source implements the original sitewise continuous-time Markov process with no finite-boundary truncation, and fixed-seed Monte Carlo comparisons of the CDF and means at four transmission rates; it also checks exact rational identities and root calculations. Execution succeeded. Since each sample almost surely visits finitely many sites, each simulated trajectory requires finitely many events. Numerical Monte Carlo and finite rational checks cannot prove the infinite-line theorem, whose conclusion rests on the analytic graphical argument. These tests do not establish scientific priority or independent validation.

The last **new transmission** is distinct from the later absorption time. The claim is limited to nearest neighbors, no forgetting, unit stifling intensity, one initial spreader, and time-homogeneous Poisson transition rates. An inaccessible broader historic paper may affect the priority assessment; independent audit and replication have not been conducted.
