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

# Exact verification instructions and limits

Use Python 3 standard library, in the same directory as the supplied `verify.py` and `certificates.json`:

```sh
python3 verify.py
```

The verifier lists all prime-power box elements for \(N=1,2,3,4\) and tests every distinct pair with integer `isqrt`. For \(N=3\) it finds \(27\) vertices and \(10\) edges; it checks a \(21\)-element independent set and six pairwise disjoint edges. For \(N=4\) it finds \(256\) vertices and \(408\) edges; it checks a \(144\)-element independent set and \(112\) pairwise disjoint edges. The ratio-count tables are independently regenerated. The test then checks the \(\Phi_5\) membership and face diagonals of \((240,252,275)\).

Observed final output: `PASS: f(1)=1, f(2)=4, f(3)=21, f(4)=144; triangle at n=5`.

The universal bipartiteness statement is proved separately by the parity argument and the persistent triangle. No bound on \(f(N)\) for \(N\ge5\) is verified or asserted, and none of these checks constitutes an independent external audit.
