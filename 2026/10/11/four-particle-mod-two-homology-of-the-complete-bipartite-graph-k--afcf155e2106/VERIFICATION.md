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

# Exact chain verification

Run `python3 verify.py` with only Python 3's standard library. The script must print two equal rank/Betti reports for opposite local reference-edge conventions and then `VERIFY_OK`.

The program exhaustively enumerates all reduced weight-four chain generators of \(K_{5,4}\), builds every differential column from the published local halfedge rule, and performs exact Gaussian elimination over \(\mathbb F_2\) using integer bitwise XOR. It checks dimensions \((8855,47740,89460,68120,17461)\), differential ranks \((8854,38873,50306,17461)\), and resulting mod-two Betti dimensions \((1,13,281,353,0)\). It also checks the full \(\partial^2=0\) identity on degree-two through degree-four chains for one complete choice of local references; the second reference choice is computed separately. Finally it evaluates the coefficient of \(t^4\) in Gal's independent Euler series, obtaining \(-84\).

The computation is finite, exhaustive and characteristic two. Neither a failed run nor a timeout would constitute a mathematical impossibility result. It does not establish integral, rational, odd-characteristic or equivariant homology and no independent audit has been performed.
