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

The claim is established by a finite-dimensional symbolic argument; no experimental output is needed for correctness.

For an \(r\)-dimensional message subspace \(U\), a face coordinate is identically zero on the resulting subcode exactly when its characteristic vector belongs to \(U^\perp\). Thus the support problem is exactly a maximum-intersection problem with a \((k-r)\)-dimensional linear subspace.

For any \(d\)-dimensional subspace \(W\le\mathbb F_q^k\), row reduction supplies an information set \(P\) of \(d\) coordinate positions, making \(\pi_P|_W\) injective. If \(\chi_\sigma\in W\) is a face vector, then \(\pi_P(\chi_\sigma)=\chi_{\sigma\cap P}\), and \(\sigma\cap P\in\Delta\) by downward closure. Therefore \(|D\cap W|\le|\Delta|_P|\). The coordinate space \(\mathbb F_q^P\) attains equality, proving the maximum exactly.

Limits checked: \(r=1\) gives the source's minimum number of faces containing a vertex; \(r=k\) gives the full length \(|\Delta|-1\). The argument assumes the full vertex set so singleton face columns ensure dimension \(k\). It does not address the complementary anticode.
