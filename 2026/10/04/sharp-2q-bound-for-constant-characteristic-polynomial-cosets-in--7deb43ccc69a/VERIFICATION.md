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

The symbolic proof is the primary verification. It uses only the two-dimensional Cayley--Hamilton identity, nondegeneracy of the trace pairing on \(\mathfrak{sl}_2(\mathbb F_q)\) in odd characteristic, and the elementary count of norm-one elements in split, nonsplit, and dual-number quadratic algebras.

The accompanying `verify_constant_charpoly_gl2.py` performs an independent finite replay for \(q=3\) and \(q=5\). It enumerates every subgroup of \(\mathrm{SL}_2(\mathbb F_q)\), tests every invertible \(x\), verifies abelianness of each qualifying subgroup, and checks \(|H|\leq2q\). Its output is stored in `verification_output.txt` and ends in `VERIFY_OK`.

The computation is not an exhaustive proof for arbitrary \(q\); it is a regression check of the general argument. Characteristic two is not tested or claimed. Independent audit has not been performed.
