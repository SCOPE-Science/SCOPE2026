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
# Verification of modular Jordan-plane counts

Reproduce with `python verification/jordan_plane_verify.py` using the Python standard library. The checker constructs the finite fields \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) (the last as \(\mathbb F_2[t]/(t^2+t+1)\)), performs independent matrix products, and solves the fixed-second-matrix commutator system by elimination. It exhaustively enumerates all ordered matrix pairs for \((q,n)=(2,2),(3,2),(4,2),(2,3)\), obtaining totals \(40,153,1216,2192\), respectively. It compares direct and linear-algebraic fiber counts, checks the Jordan-block eligibility in those cases, samples \(500\) second matrices each for \((3,3)\) and \((4,3)\), and expands the product through dimension five for field orders \(2,3,4,5\). It confirms all extracted coefficients become integers after multiplication by the full general-linear-group order. The success marker is `VERIFY_OK_JORDAN_PLANE`.

These experiments do not certify the infinite family. The general statement follows from the trace-pairing argument, the rational-canonical divisibility condition and the explicit centralizer-weighted orbit enumeration in the proof. Historical equivalence and independent audit remain open limits.
