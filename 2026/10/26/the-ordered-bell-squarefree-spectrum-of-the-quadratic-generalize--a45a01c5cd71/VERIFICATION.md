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
# Verification evidence

`verify_quadratic.py` uses only Python standard-library integer arithmetic. It independently evaluates the original floor-defined recurrence for 600 indices, the divisor recurrence through 40,000 indices, factors all tested indices and builds Stirling/Fubini coefficients. It checks the exact formula on 24,309 squarefree indices, parity on 15,690 nonsquarefree indices and the equivalence of \(s(n)=-1\) to primality. Actual execution returned:

```
VERIFY_OK 40000 600 24309 15690
```

The unrestricted proof is the Boolean-lattice and Dirichlet-convolution argument in `RESULT.md`, not the finite experiment. Every claimed range, normalization and exceptional condition is contained there. No independent audit or external certificate has been performed.
