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
The proof is symbolic and independent of finite enumeration.

For \(K\ge Z\), let \(U=K/Z\), let \(s=\dim_{\mathbf F_p}U\), and let \(S=\langle U\rangle_{\mathbf F_q}\) have dimension \(d\). Direct commutator computation gives
\[
C(K)/Z=S^\perp.
\]
Nondegeneracy yields
\[
|S^\perp|=q^{2n-d},
\]
and hence
\[
m(K)=q^{2n+2}p^{s-fd}.
\]
Equality with the maximum is equivalent to \(s=fd\), i.e. to \(U\) being \(\mathbf F_q\)-linear.

The packaged checker exhaustively enumerates all additive subspaces for
\[
(n,q)=(2,2),(2,3),(1,4).
\]
It constructs field spans and symplectic annihilators directly and verifies the measure formula and equality criterion. The \(\mathbf F_4\) case uses \(\mathbf F_2[t]/(t^2+t+1)\) and explicitly verifies the nonprime-field monotonicity obstruction.

The checker returns `VERIFY_OK`.

Finite enumeration is not used as a proof of the universal statement.
