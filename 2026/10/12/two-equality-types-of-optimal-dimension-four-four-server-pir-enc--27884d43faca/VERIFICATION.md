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

`verify_pir44.py` reconstructs every multiset of nine nonzero columns in \(\mathbb F_2^4\), checks the published necessary minimum-distance condition, and then tests four-recoverability of all \(15\) nonzero targets by two separate exact algorithms.

The first algorithm performs direct recursive packing of four pairwise disjoint recovery masks. The second constructs all unions of two disjoint recovery masks and asks for two disjoint such unions. Agreement is required target-by-target for all \(1345\) candidates with minimum distance at least \(4\).

The script then checks whether the good targets span rank \(4\), generates every element of \(\operatorname{GL}(4,2)\), partitions all accepted multisets into group orbits, and checks the stabilizer sizes by orbit-stabilizer. It also verifies that the length-nine projective generator transcribed from the short-block literature belongs to the projective orbit.

Expected terminal output:

`VERIFY_OK ambient=817190 d4=1345 basis_flexible=1120 standard_basis=896 projective=280 one_double=840 orbits=280,840 stabilizers=72,24 algorithms_agree=true`

The proof uses the published facts that every binary \(k\)-PIR code has minimum distance at least \(k\) and that \(P(4,4)=9\). The computation is finite; it makes no claim about nonlinear PIR encoders or other dimensions/lengths.
