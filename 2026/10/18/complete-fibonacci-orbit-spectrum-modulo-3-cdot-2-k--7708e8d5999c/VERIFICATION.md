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

# Reproduction and limits

Run `python3 verify.py` in a clean Python 3 environment. It uses only the standard library. On success it prints `VERIFY_OK`. Its independent enumeration checks all state-orbit lengths and multiplicities at moduli `24,48,96,192,384`, every power-of-two local modulus through `128`, the local modulo-three spectrum, and exact matrix bases. No arithmetic floating point and no network are used.

The infinite theorem does not follow from this finite test; inspect the matrix-lifting argument and the CRT gcd/lcm orbit product proof in `RESULT.md`. The enumerations were run from the embedded code and passed. The available examination is self-review only; independent audit and validation are not performed.
