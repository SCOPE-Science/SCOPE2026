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

# Checks and reproducibility

The standalone Python 3 program `verify_linked_lines.py` uses exact arithmetic modulo the prime \(101\). It builds six explicitly embedded coordinate-line trees, verifies the intersection incidence pattern, and checks the ranks of all restricted multihomogeneous monomials of multidegrees in \(\{0,1,2\}^h\) for \(h=2,3,4,5\). Expected rank is \(1+\sum_vd_v\). The observed output was:

```
VERIFY_OK 6 trees, 684 multidegrees, prime 101
```

Run: `python3 verify_linked_lines.py`. These finite tests check neither all linked nets nor arbitrary multidegrees. The mathematical argument relies on the published component/Chow/normal-crossings/Hilbert-polynomial theorems and the established irreducibility theorem for the diagonal Hilbert scheme; their hypotheses are explicitly matched in the proof. No independent audit has been performed.
