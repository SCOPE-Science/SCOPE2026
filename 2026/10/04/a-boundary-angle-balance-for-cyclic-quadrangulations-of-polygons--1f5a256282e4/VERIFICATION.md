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

The claim was checked as an exact finite-cell-complex argument.

1. Edge incidence gives \(4F=2E_{\mathrm{int}}+B\), so the boundary length \(B\) is even; all face walks are even, hence the connected plane mesh graph is bipartite.
2. Each cyclic quadrilateral contributes exactly \(\pi\) of angle mass to either bipartition color because its same-color vertices are opposite.
3. Re-indexing those angles by vertices gives
\[
F\pi=2\pi I_C+\sum_{v\in C\cap\partial P}\theta_v.
\]
4. For a square, this becomes \(F=2I_C+B/2-m_C/2\), so each color contains an even number of the four geometric square corners.
5. Exhaustive enumeration of the eight even-total side-parity patterns confirms that exactly the patterns with two adjacent odd side counts create a forbidden \(3\)-to-\(1\) corner-color split.

No floating-point computation or external certificate is used. The proof does not cover T-junction dissections.
