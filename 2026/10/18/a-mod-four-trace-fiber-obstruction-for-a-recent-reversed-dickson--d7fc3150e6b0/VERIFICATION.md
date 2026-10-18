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

# Verification record

Run `python verify_trace.py` without third-party dependencies. The program implements polynomial-basis multiplication in binary extensions of degrees 8, 12 and 16 (irreducible defining polynomials `0x11B`, `0x1009`, `0x1002B`), then independently computes trace values and the explicit polynomial on every field element. Output in the current run:

```
q=4: trace-zero inputs at w=0: 64; per nonzero w: 0; total: 64
q=8: trace-zero inputs at w=0: 512; per nonzero w: 32; total: 736
q=16: trace-zero inputs at w=0: 4096; per nonzero w: 0; total: 4096
VERIFY_OK
```

The infinite proof rests on the displayed Artin--Schreier reduction and exact \(\mathbb F_{16}\) classification, not on these finite samples. No independent audit or external formal certification is asserted.
