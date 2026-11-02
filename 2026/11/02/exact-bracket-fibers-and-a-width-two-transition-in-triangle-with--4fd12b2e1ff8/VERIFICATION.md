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

The standalone Python 3 standard-library program `verify.py` constructs every ordered pair of vertex-coordinate vectors for each stated small finite field and number of leaves. It calculates the determinant on every graph edge and compares the resulting complete fiber histogram against the explicit five-branch theorem; it does not implement the proof's geometric case split. Cases are \((q,r)=(2,0),(2,1),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1)\). For \(q=4\), multiplication is performed in the polynomial quotient \(\mathbb F_2[u]/(u^2+u+1)\), rather than integer arithmetic modulo four.

Run `python3 verify.py`. It must end with `TRIANGLE_LEAF_BRACKET_FIBERS_OK 13`. Direct output also lists the input-pair total, attained output count, missing count and zero-fiber size for each case. This checked computation is finite and does not establish the all-field theorem; the proof in `RESULT.md` is the general argument. The verification uses vertex pairs only. For pairs in the full Lie algebra, the theorem separately accounts for the \(q^{2(r+3)}\) free central-coordinate factor.
