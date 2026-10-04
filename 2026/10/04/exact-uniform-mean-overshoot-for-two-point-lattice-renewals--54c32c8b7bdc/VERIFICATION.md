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

The proof is analytic. The finite checker is an independent replay of the
algebraic identities and recurrence, not a certificate for the infinite
statement.

`verify_two_point_overshoot.py` uses exact rational arithmetic. For each tested
rational \(p\) and integer \(m\), it:

1. evaluates the initial overshoot expectation directly from the first-long-jump
   decomposition;
2. compares it with the closed form;
3. checks the exact difference identity
   \[
   e_b-e_{b-1}=\mu q^b-1;
   \]
4. locates the maximizing index using exact rational inequalities;
5. generates later values from
   \[
   e_b=q e_{b-1}+p e_{b-m};
   \]
6. checks that the recurrence never exceeds the theorem's initial maximum over
   the replay window.

The infinite extension is justified separately by the convex-combination
maximum principle in the written proof. The checker therefore does not infer an
infinite theorem from finite enumeration.

Originality was assessed by statement-level comparison with classical renewal
inequalities and the closest retrieved public results. Independent audit has
not been performed.

Exact-rational replay result: `VERIFY_OK cases=4560`.
