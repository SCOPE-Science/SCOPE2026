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

The deterministic proof was reconstructed from the e-BH definition with all quantifiers and boundary cases checked. The key facts are: \(K/(\alpha r)>1\) for every \(r>m\); terminal full discovery therefore forces \(k^\star=m\); every nonnull must have reached \(K/(\alpha m)\); and first-passage parking attains the coordinatewise lower bound simultaneously.

`verify.py` replays the finite combinatorial checks using exact rational arithmetic. It checks the common-threshold boundary across small integer parameter grids and exhaustively searches all terminal sample-count tuples for a deliberately nonmonotone three-signal example. The script must print `VERIFY_OK`.

The expectation identity is not inferred from finite computation. It follows analytically from Wald's identity under the stated assumptions \(\mathbb E|X_{i1}|<\infty\), \(\mathbb E\tau_i<\infty\), iid increments, and positive mean \(D_i\). No renewal approximation, asymptotic overshoot formula, or distribution-free bound on \(O_i\) is claimed.

Public-source comparison inspected the exact e-BH definition, the 2026 simple-alternative upper and lower sample-complexity statements, its expected-stopping crossing level, the 2022 bandit stopping rule, and the stopped-e-BH filtration result. The remaining risk is that a later or uninspected source may state the same short sharp consequence explicitly.
