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

# Reproduction notes

Compile `verify.cpp` with a conforming C++17 compiler and run the executable. Successful execution prints ten records and then `VERIFY_OK`. For each length \(n\), the six columns are \(n\), distinct factor count, necklace count, singleton-necklace count, two-factor-necklace count, and full-rotation-necklace count.

The enumeration is exhaustive, not a sample: every factor must intersect one of eight occurring adjacent substitution-state block pairs. The verifier establishes that pair set from a fixed-point prefix and checks closure under the morphism. It also cross-checks the binary projection against a second, direct numerical definition of the Rudin–Shapiro word and uses simpler independent algorithms for the smaller instances. All counts use exact integer and string operations. The verified range is \(4\le k\le13\), with no extrapolation outside it.
