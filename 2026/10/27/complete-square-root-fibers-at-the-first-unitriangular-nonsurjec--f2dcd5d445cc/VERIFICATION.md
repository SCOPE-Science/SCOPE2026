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

The standalone `verify.py` is included with the complete mathematical result. Run it with `python3 verify.py` in an ordinary Python 3 environment; it requires only the standard library.

The code exhaustively enumerates the \(q^{10}\) inputs of the square polynomial for \(q=2\) and \(q=4\), evaluates the predicted fiber of every one of the \(q^6\) target matrices, and compares the multiplicities exactly. It checks total multiplicity \(q^{10}\), image size \(q^6-q^5+q^4+q^3-q^2\), and identity-fiber size \(5q^6-4q^5\). It implements \(\mathbb F_4=\mathbb F_2[T]/(T^2+T+1)\) using binary polynomial arithmetic.

The verifier additionally checks literal five-by-five matrix squaring against the specialized six-coordinate formula for all binary inputs and for a deterministic quaternary sample. The observed output was:

```
PASS 2 image 52 domain 1024 zero_fiber 192 targets 64
PASS 4 image 3376 domain 1048576 zero_fiber 16384 targets 4096
VERIFY_OK_UT5_SQUARE_FIBERS
```

This is finite computational evidence only. The infinite statement for every extension degree follows from the field-independent proof by four root cases, not from extrapolation of the tests. No independent audit has been conducted.
