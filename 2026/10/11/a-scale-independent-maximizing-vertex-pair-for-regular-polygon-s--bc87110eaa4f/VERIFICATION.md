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

## Exact identities
Set \(\beta=\pi/(2n)\) and \(w_j=\sec\beta(\cos((2j+1)\beta),\sin((2j+1)\beta))\). The primal norm is the maximum of these \(2n\) supporting linear forms, and the dual ball is their convex hull. Convexity and independent support maximization produce the identity
\[
1+\rho_{X_n}(t)=\frac12\max_{j,k}\left(N_n^*(w_j+w_k)+tN_n^*(w_j-w_k)\right).
\]
Regular-polygon isometry reduces to \((w_0,w_k)\) with \(0\le k\le n\), and the exact parity norm identities are
\[
N_n(v_0+v_k)=2q_k\cos(k\beta),\qquad
N_n(v_0-v_k)=2q_{n-k}\sin(k\beta).
\]
This verifies every coefficient in the finite envelope without numerical assumptions. Perpendicularity of the support directions and parity of the regular lattice yield the fixed maximizing pair \((v_0,v_{\lfloor n/2\rfloor})\) for every \(t\).

## Exact decagonal branch crossings
For \(n=5\), the undominated affine functions are
\[
1+s t,\qquad a+b t,\qquad b+a t,\qquad s+t,
\]
where \(s=(\sqrt5-1)/4\), \(a=(1+\sqrt5)/4\), and \(b=(\sqrt5-1)/2\). Their intersections are
\[
\frac{1-a}{b-s}=\frac{\sqrt5-1}{2},\qquad 1,\qquad
\frac{b-s}{1-a}=\frac{\sqrt5+1}{2}.
\]
The slope and intercept orders and these strict inequalities prove that the four lines are the complete upper envelope. The value at unit scale is exactly \(\rho_{X_5}(1)=(3\sqrt5-5)/4\).

## Numerical cross-check and limitations
A separate floating-point check, not used as proof, built all primal vertices and polar supporting vectors for each integer \(2\le n\le17\), and for each of fourteen test scales compared every vertex-pair norm sum against the affine envelope and the canonical pair. All samples agreed to tolerance \(10^{-9}\). Finite tests cannot prove the infinite statement; the general dual argument above does.

No classification of all maximizers, asymptotic stability, or exact formula for irregular polygons is asserted.
