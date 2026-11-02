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

# Reproducible exact finite checks

Execute `python3 VERIFY.py` in a directory containing that standalone file; it requires only Python 3 and its standard library. The script constructs all simplices directly from Hamming distances; checks the entire \((16,80,160,120,16)\) face vector; tests all nine cross-polytope chain boundaries; verifies that the precisely listed 25-by-25 matrix minor has determinant \(-1\) by exact Bareiss elimination; checks the free simplex-level antipodal involution; and checks quotient cell-orbit counts \((8,40,80,60,8)\) and their mod-two boundary ranks \((7,32,47,8)\). Its expected output begins `Q4_ANTIPODAL_RP3_WEDGE_FOUR_S3_UNIMODULAR_BASIS_OK`.

The unimodularity claim uses actual degree-three chain matrices and provides an integral lattice certificate, not just rational rank tests. The proof of global homotopy equivalence additionally uses the published simply-connected nine-sphere homotopy classification, the elementary theory of free double coverings, and the integral homology Whitehead theorem; those latter mathematical inputs are reasoned in the result text, not independently checked by this script. No independent external audit is claimed.
