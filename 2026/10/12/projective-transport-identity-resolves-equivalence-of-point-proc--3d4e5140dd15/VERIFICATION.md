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
# Verification
The proof concerns finite-intensity point processes on a Polish space. The decisive infinite argument is a compactness passage from nested finite partitions to one coupling minimizing the full signed-measure variation norm.

The structural identities independently checked are:
\[
\sum_{A\in\mathcal P_n}|\mu(A)-\nu(A)|\uparrow|\mu-\nu|(E),
\qquad
|\mu-\nu|(E)=a+b,
\qquad
\sup_A|\mu(A)-\nu(A)|=\max(a,b),
\]
where \(a,b\) are the Hahn--Jordan masses.

Run the standalone, standard-library-only checker with `python3 verify.py`. It exactly solves a two-by-two transport program for random point configurations on three sites under all five set partitions, compares it to optimal full variation and set-supremum variation costs, and tests both sharp deterministic examples. Its expected terminal line is

`VERIFY_OK projective=1.250000000000 kr=1.000000000000 partitions=5`

These finite calculations cannot establish the universal projective limit; that part is proved analytically through Polish compactness, almost-sure continuity of continuity partitions, measurable disintegration, and monotone convergence. No experiment is treated as an infinite certificate.
