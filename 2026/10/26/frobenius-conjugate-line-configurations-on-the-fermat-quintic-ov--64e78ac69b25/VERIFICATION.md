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

# Reproducibility and limits

Execute `python3 verify.py` with Python 3 standard library, in this directory. It uses the explicitly represented field \(\mathbb F_{16}=\mathbb F_2[\alpha]/(\alpha^4+\alpha+1)\), enumerates all \(70161\) reduced-row-echelon two-dimensional subspaces of \(\mathbb F_{16}^4\), selects \(325\) Hermitian generators, identifies \(75\) coordinate-pair lines and \(250\) others, and checks the \(3+2+320=325\) Frobenius cycle decomposition. It independently compares row-rank intersection and two-by-two determinant tests for all size-four Frobenius orbits, and verifies the four orbit-graph counts, five small-field generators, six clique centers, and sampled global valency. The deterministic success output begins `VERIFY_OK`.

The algebraic field-of-definition argument \(L^{(16)}=L\) precedes finite enumeration; this justifies exhaustive inference over the algebraic closure. The vanishing of \(H^0(L,N_{L/S})\) proves the scheme has no infinitesimal embedded line deformations. The program is an ordinary arithmetic certificate, not a formal or independent theorem prover. No independent scientific audit has been performed. Potential equivalent formulations in historical polar-space literature were not exhaustively excluded.
