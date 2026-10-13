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

The theorem is proved symbolically for every prime power \(q\). The accompanying `verify.py` is a bounded stress check and is not used to infer the universal result.

The checker exhaustively enumerates every automorphism for \(q=2,3,4,5,7\). It uses ordinary modular arithmetic for the prime fields and an explicit polynomial model
\[
\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)
\]
for the non-prime field. For every quotient matrix \(A\in\operatorname{GL}_2\) and every central covector, it constructs \(\phi-I\), computes its rank by finite-field Gaussian elimination, and accumulates the fixed-space dimension.

A fresh replay produced:

`q=2 total=24 spectrum={1: 14, 2: 9, 3: 1} burnside_orbits=3`

`q=3 total=432 spectrum={0: 108, 1: 291, 2: 32, 3: 1} burnside_orbits=3`

`q=4 total=2880 spectrum={0: 1280, 1: 1524, 2: 75, 3: 1} burnside_orbits=3`

`q=5 total=12000 spectrum={0: 6750, 1: 5105, 2: 144, 3: 1} burnside_orbits=3`

`q=7 total=98784 spectrum={0: 68600, 1: 29799, 2: 384, 3: 1} burnside_orbits=3`

`VERIFY_OK`

The test explicitly covers the exceptional field \(\mathbb F_2\), where the dimension-zero fiber has size \(0\), and the extension field \(\mathbb F_4\). No finite enumeration proves the all-\(q\) theorem; the proof in `RESULT.md` supplies the universal argument.
