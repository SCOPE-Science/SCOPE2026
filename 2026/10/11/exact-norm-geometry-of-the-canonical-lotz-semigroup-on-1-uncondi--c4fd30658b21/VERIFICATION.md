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

For a bounded scalar sequence \(c=(c_n)\), the 1-unconditional hypothesis gives \(\|M_c\|\le\sup_n|c_n|\). Testing \(M_c\) on any nonzero vector in block \(X_j\) gives \(\|M_c\|\ge|c_j|\), hence
\[
\|M_c\|=\sup_n|c_n|.
\]
Every operator-norm assertion in the finding is obtained by applying this identity to an explicitly displayed scalar coefficient sequence.

For \(0<s<t\), the scalar function \(h(r)=r^{-s}-r^{-t}\) has derivative \(r^{-t-1}(t-sr^{t-s})\), so it has one maximum at \(r_*=(t/s)^{1/(t-s)}\). Therefore its integer maximum is among the two adjacent integers. When \(s=0\), the coefficients \(1-n^{-t}\) increase to \(1\) and never equal it, giving the separate endpoint formula.

On every half-plane \(\operatorname{Re}z\ge\delta>0\), all coefficient derivatives \((\log n)^k n^{-z}\) are uniformly bounded, and their difference quotients converge uniformly on compact subsets. Because the diagonal multiplier map is isometric in the stated normalization, coefficient holomorphy upgrades to operator-norm holomorphy.

When the blocks are finite-dimensional, the truncation \(F_N(t)\) is finite rank and its coefficient tail has supremum \((N+1)^{-t}\). Thus the compactness conclusion is proved by an explicit norm-convergent finite-rank approximation. No numerical experiment, finite enumeration, or external certificate is used as a substitute for an infinite proof.

The verification does not establish any converse classification, any corresponding equality for unconditional constants greater than one, or optimality of the canonical truncations among all finite-rank operators.
