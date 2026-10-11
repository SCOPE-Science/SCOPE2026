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

The exact full-dimensional convex-body error is reduced analytically to
\[
E=\max_{v\in S^2}|2q(v)-1|,
\qquad q(v)=\sum_{i=1}^3w_i|\langle u_i,v\rangle|.
\]
The source theorem is restated and its critical Minkowski step checked: for any unit \(v\), the even normalized measures
\[
(1-\tau)(\delta_v+\delta_{-v})/2+\tau\sigma
\]
have zero first moment and full-dimensional support for every \(\tau>0\); Minkowski existence realizes them as convex-body surface area measures. The limiting estimator ratio therefore achieves the claimed potential supremum without assuming a degenerate planar body is admissible.

The proof of the minimax rule is global: no enumeration of sample configurations is assumed. The quantitative bounds follow from
\[
L=\frac13-\frac\varepsilon2>0,
\qquad L\le w_i\le1-2L,
\qquad |\langle u_i,v_i\rangle|\ge\frac{L}{w_i}
\]
where \(v_i\) is any unit vector perpendicular to the two other measurement axes. Explicit algebra gives
\[
1-\left(\frac{2-3\varepsilon}{2+6\varepsilon}\right)^2
=\frac{9\varepsilon(4+3\varepsilon)}{4(1+3\varepsilon)^2}.
\]

For the sharp exponent witness, the two-by-two tilted coordinate matrix has inverse column norms \(\sec\theta\) and \(\sec\theta\); the third column norm is \(1\). Its support-function minimum is \(\cos\theta/3\), and maximizing over the eight sign sums gives \(\sqrt{3+2\sin\theta}/3\). The package checker replays these algebraic consequences but is not substituted for the exact general proof.

Limitations: the coefficient in the angular estimate is not certified best possible; only the square-root exponent is. The known orthogonal-grid error value is attributed to earlier work.
