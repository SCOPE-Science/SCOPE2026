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

# Mathematical verification

The universal theorem is analytic. The exact starting-block comparison is \(p_{k+2+t}-p_{k+1+t}=\lambda^2(S_{k+t}-T_t)\) for \(0\le t\le k-2\). Vandermonde convolution and \((i+j+2)!\ge(i+1)!(j+2)!\) imply \(S_{k+t}\le S_kT_t\), while the exceptional comparison for \(k=2\) follows from \(\lambda_2^\star=2(\sqrt7-2)>6/5\). The recurrence then extends the strict initial block to all larger indices.

The included checker can be run without downloads or additional packages:

```sh
python3 verify.py
```

It uses only Python integer arithmetic and exact rational coefficients. The bounded check verifies the initial generating-function expansion and difference identities for orders 2 through 17, checks the nonnegative coefficients of the dominance difference, and evaluates finite sequences at rational rates. The confirmed output reports 504 exact checks and a rational bracket for the second-order threshold. Finite tests do not certify every order, every real parameter, or the infinite sequence; those quantifiers follow exclusively from the proof. No external independent audit was performed.
