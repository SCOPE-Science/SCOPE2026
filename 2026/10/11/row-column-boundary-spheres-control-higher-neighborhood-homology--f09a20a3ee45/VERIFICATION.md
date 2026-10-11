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

# Reproducibility and limitations

Execute `python3 verify_rook.py` using Python 3 and its standard library. This enumerates the full **open** neighborhood complexes for eight small boards, checks that every mixed face of at least three vertices has exactly one common-neighbor center, and verifies all local cross-edge attachment descriptions and the predicted relative Euler characteristic. It independently computes mod-two boundary ranks of both the full and core complexes, confirms the predicted higher homology dimensions, and checks the signed row/column permutation action on integral oriented boundary chains.

The expected output is embedded as `verification_output.txt`, with a final `VERIFY_OK` line. These calculations verify finitely many parameters and coefficients \(\mathbb F_2\) for homology; the all-integer, integral and representation-theoretic claims rely on the written universal cofiber and oriented-boundary proofs. No external or independent audit has been performed.
