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

# Reproduction and mathematical verification

Execute `python3 verify.py` in the directory containing the checker. It requires Python 3 and no third-party libraries.

The checker enumerates all nonzero singular \(2\times2\) matrices in \(\mathbb F_q\) for \(q=2,3,4,5\), with \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). For every pair, it evaluates both products and checks that the ordinary simple-graph adjacency is equivalent to the independently reconstructed kernel/image type incidence. Every type must contain exactly \(q-1\) matrices. The reduced integer matrix \(B=(q-1)H-D\) is then constructed, and its characteristic polynomial is computed coefficient-by-coefficient with an exact Faddeev–LeVerrier recurrence; all coefficients match the derived factorization. For \(q=2,3\), the full graph characteristic polynomial is independently recomputed and matched as well.

Observed full checker output:

```
q=2 vertices=9 type_quotient=9 characteristic_poly_OK
q=3 vertices=32 type_quotient=16 characteristic_poly_OK
q=4 vertices=75 type_quotient=25 characteristic_poly_OK
q=5 vertices=144 type_quotient=36 characteristic_poly_OK
VERIFY_OK
```

The tested instances are **not** a proof for arbitrary prime powers. The proof is the invariant-space decomposition and polynomial calculation in RESULT.md, which explicitly covers all \(q\ge2\). Computation in the ordinary characteristic-zero integers (for the real graph spectrum) must not be confused with field-characteristic rank. No independent audit or external certification was performed.
