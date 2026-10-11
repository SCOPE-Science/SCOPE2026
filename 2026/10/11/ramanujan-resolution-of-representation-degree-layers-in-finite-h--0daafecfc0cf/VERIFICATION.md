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
The proof is analytic and finite. It uses the exact finite-Heisenberg representation classification, central-character spectral projections, and elementary Ramanujan-sum arithmetic.

The accompanying `verify.py` uses exact rational arithmetic and checks, for every \(2\le n\le120\) and every divisor \(m\mid n\):

1. the complete degree-count identity for the regular representation;
2. the kernel total variation \(2^{\omega(m)}\varphi(m)/m\);
3. exact idempotence of every central Ramanujan kernel;
4. pairwise convolution orthogonality for distinct degree layers;
5. the exact identity resolution over all divisors of \(n\);
6. \(\operatorname{rank}\Pi_m=n^2\varphi(m)\);
7. the complementary total-variation formula; and
8. endpoint contractivity exactly for powers of two.

The replay command is `python verify.py`. The expected terminal line is:

`VERIFY_OK n=2..120 degree_layers=601 exact_fraction_checks=all`

No finite computation is used to infer the universal theorem. The checks only corroborate the closed proof and its normalization conventions.
