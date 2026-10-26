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

# Verification and mathematical dependencies

1. The ordered configuration \(F\subset(\mathbb P^n)^d\) has complement of complex codimension \(n\). For \(n\ge2\), this preserves \(H^1(-,\mathbb Z)=0\), \(H^2(-,\mathbb Z)=\mathbb Z^d\), and simple connectivity.
2. The free covering with group \(\mathfrak S_d\) has \(H^2(\mathfrak S_d,\mathbb Z)=\mathbb Z/2\). The sign bundle realizes this torsion and the symmetric external tensor \(L\) realizes the primitive invariant free class. Therefore \(c_1:\operatorname{Pic}(U)\to H^2(U,\mathbb Z)\) is an isomorphism.
3. Let \(\dim_{\mathbb C}X=N\), \(\dim_{\mathbb C}(X\setminus U)\le N-n\). Since \(2N-2>2(N-n)+1\) for \(n\ge2\), Borel--Moore localization induces the required isomorphism at degree \(2N-2\). Chow localization works because \(n>1\).
4. For a collision partition, the group \(\prod_i\mathfrak S_{\lambda_i}\) has a sign character for each \(\lambda_i\ge2\) and has no pseudo-reflection in the tangent representation because each moved point contributes at least \(n\) nonfixed directions. The local invariant-ring character theorem gives \((\mathbb Z/2)^r\); the global sign restricts to its diagonal.
5. The determinant of a transposition of two \(n\)-dimensional blocks is \((-1)^n\), and a cycle of length \(\ell\) has age \(n(\ell-1)/2\), verifying canonical parity and the Reid--Tai boundary.

These are exact theoretical checks; no numerical experiment, machine certification, or external independent verification is claimed. Published supporting facts are cited in RESULT.md. The codimension-two cokernel is explicitly outside this theorem.
