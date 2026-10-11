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

The standalone `verify.py` contains the 31 triangular facets and uses only the Python standard library. It reconstructs the full complex and every induced deletion on nine vertices. Boundary ranks are computed with exact `Fraction` arithmetic.

Expected full-complex check: \(f=(10,40,31)\) and rational Betti vector \((1,0,0)\).

Expected deletion check: every deletion has \(\beta_0=1\), \(\beta_2=0\), and the first-Betti multiset \(\{3,3,3,3,3,2,2,2,1,1\}\). The script additionally checks \(\beta_1=t_v-e_v+1\) for every source-labeled vertex.

Scientific limits: this replay establishes rational homology only. It does not test integral torsion or the homotopy type of the deletions. Noncontractibility of the undeleted complex is a premise from the cited source rather than a conclusion of the verifier.
