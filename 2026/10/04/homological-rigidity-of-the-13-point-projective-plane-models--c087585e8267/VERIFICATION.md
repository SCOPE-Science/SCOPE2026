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

`artifacts/verify.py` reconstructs the 13-point poset and performs all finite checks from scratch using only the Python standard library.

It verifies order-complex simplex counts \(13,36,24\), that every edge belongs to two triangles, every vertex link is a connected cycle, Euler characteristic \(1\), and \(\dim_{\mathbf F_2}H_1=1\). It constructs a non-coboundary \(1\)-cocycle and verifies a six-edge cycle pairs nontrivially with it.

The exhaustive backtracking search uses cover inequalities, equivalent to full isotonicity because the complete order is their transitive closure. It enumerates 562333 self-maps. Exactly 24 act nontrivially on the chosen homology generator, exactly 24 are bijective, and zero non-bijective maps have nonzero action. Each bijection is additionally checked to have an isotone inverse.

`artifacts/verification_output.txt` records `VERIFY_OK`.

Limits: this verifies direct self-maps of the stated finite models; no independent external audit has been performed.
