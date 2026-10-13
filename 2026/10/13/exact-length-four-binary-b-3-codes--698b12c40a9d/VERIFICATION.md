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

Run `python3 verify.py` in the package directory. The script uses only the Python standard library and reconstructs the complete finite search space from definitions.

It performs these checks:

1. Constructs all sixteen words of \(\{0,1\}^4\).
2. Implements the \(B_3\) predicate twice: once using explicit coordinate-sum tuples and once using an independent base-four encoding of the same sums.
3. Checks all \(inom{16}{6}=8008\) six-subsets and requires both predicates to agree; exactly 656 pass.
4. Checks all \(inom{16}{7}=11440\) seven-subsets and requires both predicates to reject each one. Because the \(B_3\) property is hereditary, this proves the upper bound six.
5. Generates every element of \((C_2)^4times S_4\), of order 384, and partitions all 656 maxima into complete orbits.
6. Recomputes the orbit partition independently by canonical representatives and checks that both methods give orbit sizes \(16,64,96,96,192,192\).

Expected terminal line:

`VERIFY_OK maximum=6 labeled_maxima=656 orbits=6 orbit_sizes=16,64,96,96,192,192`

The verifier's canonical census serialization has SHA-256 `b5e7a2ad97c9c608797740bd17f220c740fa1ae4623085f61478a1cf810d9748`.

The finite verification proves only the stated block-length-four theorem. It does not prove an asymptotic bound or establish priority in the literature.
