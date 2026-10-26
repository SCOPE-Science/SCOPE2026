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

The standalone `verify.py` uses only Python's standard library. It exhaustively generates all \(2^4=16\) binary operations on two labels and all \(3^9=19683\) operations on three labels. For each operation it computes successive monoid powers using \((f\triangleleft g)(a,b)=g(f(a,b),f(b,a))\) and directly tests equality of consecutive powers and commutativity. A second, separately implemented test computes directed cycles of \(T_f\) and the number of reached diagonal fixed points. The two predicates agree for every operation in both enumerations.

The measured coefficients are \((4,2)\) for \(n=2\) and \((2187,1458,243)\) for \(n=3\); each agrees with \(\binom nr r n^{n^2-r-2}\). The actual script output is:

```text
n = 2 verified coefficients = {1: 4, 2: 2}
n = 3 verified coefficients = {1: 2187, 2: 1458, 3: 243}
VERIFY_OK
```

The infinite theorem is verified mathematically by the two prescribed-root forest determinants and the equivariant functional-graph reduction, not by extrapolation from these finite computations. The script does not validate novelty or external priority; a full-text comparison with one foundational 2022 journal paper was unavailable. No independent audit was conducted.
