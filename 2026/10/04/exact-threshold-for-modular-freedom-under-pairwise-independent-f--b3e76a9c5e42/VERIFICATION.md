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

The proof is analytic. The checker only replays the moment algebra and explicit
construction.

For each tested triple \((n,q,r)\), `verify_modular_pairwise.py` computes
\[
N=\left\lfloor\frac{n-r}{q}\right\rfloor,\qquad
m=\frac{n-2r}{2q},\qquad
v=\frac{n}{4q^2}
\]
using exact rational arithmetic. When the criterion is feasible, it constructs
the nearest-lattice and endpoint laws on \(J\), mixes them to variance \(v\),
then maps to
\[
K=r+qJ.
\]
It verifies:

- nonnegative probabilities summing to one;
- support in \(\{0,\ldots,n\}\);
- the required congruence class;
- \(\mathbb E K=n/2\);
- \(\mathbb E[K(K-1)]=n(n-1)/4\);
- the \(q^2-1\) all-residue threshold over the replay range;
- the explicit obstruction at \(q^2-2\).

The exchangeable Bernoulli realization then follows exactly from the identities
\[
\Pr(X_i=1)=\frac{\mathbb E K}{n},
\qquad
\Pr(X_i=X_j=1)=\frac{\mathbb E[K(K-1)]}{n(n-1)}.
\]

No finite computation is used to infer the universal threshold.

Originality was checked against the cited full primary texts and the closest
published semantic records. Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK feasible_cases=77952 infeasible_cases=143376 construction_checks=77952 threshold_checks=36639`.
