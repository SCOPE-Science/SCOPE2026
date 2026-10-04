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

The universal proof is analytic. Its critical steps are:

1. Translate one singleton label to \(0\).
2. Use the exact induced-difference criterion to separate every nonzero difference from \(A-A\) from the edge-difference sets \(-A\) and \(z-A\).
3. If an element lay in both \(-A\) and \(z-A\), then \(z\) itself would lie in \(A-A\), colliding with the edge between the two singleton vertices.
4. Count the three disjoint sets: \(|A-A|\ge n\), \(|-A|=n\), and \(|z-A|=n\).
5. Check the matching construction inside \(\operatorname{Cay}(\mathbb Z_3\times\mathbb Z_n,S)\), where \(S\) consists of elements with nonzero first coordinate.

The bundled `verify.py` independently enumerates every finite abelian group type of orders below \(3n\) and every normalized labeling candidate for \(2\le n\le5\); it finds no smaller host. It then checks the explicit order-\(3n\) construction and the three-set disjointness identities for every \(2\le n\le50\). This finite computation is a stress test only and does not extend the universal claim by enumeration.

Scientific limit: no assertion is made for complete multipartite graphs outside the \(K_{1,1,n}\) family.

Replay output: `ALL CHECKS PASSED; exhaustive_n=2..5; host_types=30; normalized_label_candidates=26938; constructions_n=2..50`
