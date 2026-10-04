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

The packaged `verify.py` reconstructs the derivative of the Lyapunov--Krasovskii functional without the predator-mass correction and checks symbolically that all delayed transmission terms cancel. It verifies the remaining expression exactly before and after imposing \(\beta\bar S=d_2\).

The universal sign of the added predator-mass contribution is analytic: for nonnegative \(q\) and \(h\),
\[
0\le \int_0^\infty h(a)q(t,a)\,da\le \|h\|_\infty Q(t).
\]
Choosing \(c\|h\|_\infty\le1\) yields the derivative bound in `RESULT.md`.

The checker does not certify the infinite-time limit by sampling. Those limits follow from the proved dissipation integral, eventual positivity of \(S\), Barbalat's lemma, the susceptible balance, scalar comparison for \(Q\), and the characteristic formula for the age transport equation. No convergence rate for \(I\) at equality is asserted.
