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

The checker constructs each square-page book graph, computes all-pairs shortest-path distances, and reconstructs every resolving neighborhood from the defining distance inequality.

For every \(4\le r\le10\), it verifies the complete resolving-neighborhood table and confirms \(\kappa(B_r)=4\). It checks the page-pair incidence certificate showing that summing all two-page constraints yields the lower bound \(rk/2\).

For seven rational values of \(k\) spanning \([1,4]\), it verifies the uniform candidate exactly with rational arithmetic. It also replays the \(r=4\) uniqueness algebra and checks explicit asymmetric minimum functions for \(r\ge6\) and \(1\le k\le2\).

Recorded output:

```text
VERIFY_OK
book_parameters_checked = 7
parameters r = 4..10
resolving_neighborhood_pairs_checked = 896
uniform_candidate_checks = 49
dual_certificate_parameters_checked = 7
asymmetric_optimum_examples_checked = 15
all resolving-neighborhood tables matched the theorem
all kappa values equal 4
all dual certificates give lower bound r*k/2
all uniform candidates attain r*k/2 for sampled rational k in [1,4]
r=4 uniqueness algebra replayed exactly
asymmetric minima verified for r>=6 and k<=2
```

The finite checks corroborate the symbolic proof. They do not replace the argument for arbitrary real \(k\in[1,4]\) or arbitrary \(r\ge4\).
