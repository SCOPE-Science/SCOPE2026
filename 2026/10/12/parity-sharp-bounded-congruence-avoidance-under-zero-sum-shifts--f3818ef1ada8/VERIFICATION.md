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

The universal theorem is justified by the proof in `RESULT.md`; finite enumeration is supporting evidence only.

`artifacts/verify_radius.py` performs the following checks:

- exhausts every pair of forbidden residues for several odd primes and verifies a radius-\(1\) zero-sum pair;
- exhausts every forbidden-residue triple for several odd primes and verifies a radius-\(2\) zero-sum triple;
- exhausts full profiles for several \((m,\ell)\) ranges using dynamic programming and the claimed radius \(B_m\);
- checks the sharp lower-bound obstructions for radius \(0\) and, for odd \(m\), radius \(1\);
- independently counts the zero-sum triples in \([-2,2]^3\) and obtains \(19\).

The script was replayed from its packaged path before the files were embedded. The exact stdout is preserved in `artifacts/verification_output.txt`.

The computation does not prove the theorem for unbounded \(m\) or \(\ell\). The infinite proof rests instead on the pair argument, the \(19>15\) triple count for \(\ell\ge5\), the explicit \(\ell=3\) lift, and the parity lower bound.
