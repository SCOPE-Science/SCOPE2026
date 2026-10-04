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

The universal proof is symbolic. Its critical checks are:

1. For a local nonfield factor with \(\mathfrak m^2=0\), nonzero elements of \(\mathfrak m\) form one unit orbit for each one-dimensional residue-field subspace, and every nonzero \(x\in\mathfrak m\) has annihilator \(\mathfrak m\).
2. Substitution into the source entry formula gives exactly three row and column types, with all projective-direction columns equal.
3. The determinant of the distinguished three-by-three minor is \(-hq^2\), hence nonzero.
4. Field factors have a two-by-two matrix of rank \(2\).
5. The source product formula identifies the global matrix, up to ordering, with a Kronecker product; ranks therefore multiply.

`verify.py` uses exact rational Gaussian elimination to reconstruct local matrices for residue-field orders 2, 3, 4, 5, and 7 with dimensions 1 through 3. It checks local rank, the repeated-column structure, the independent three-column core, field rank, and four small Kronecker products. The recorded output begins `VERIFY_OK`.

The finite replay is corroborative only. It does not establish the universal theorem, and no claim is made for \(J(R)^2\ne0\).
