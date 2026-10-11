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
The theorem is proved symbolically in `RESULT.md`; finite experiments are not used as an infinite proof.

Verified source premises:
- Chen's factor-orbit model identifies correlation matrices with row-normalized factors modulo an orthogonal action.
- With ambient parameter \(k=n\), the squared quotient distance is the infimum over \(O(n)\) of the sum of squared rowwise spherical angles.
- The source explicitly distinguishes the metrics for different ambient \(k\) and recommends \(k=n\) on the full elliptope.
- The source states that the general angular alignment optimization does not have a closed-form solution and supplies a numerical Riemannian-gradient algorithm.

Verified mathematical steps:
- For an \(s\)-dimensional row span with orthogonal projection \(P\), the rowwise registered cosine is at most \(\sqrt{P_{ii}}\).
- The diagonal of \(P\) lies in \([0,1]^n\) and sums to \(s\).
- For \(f(p)=\arccos^2\sqrt p\), strict convexity follows from
  \[
  f''(p)=
  \frac{2(\sin(2\theta)-2\theta\cos(2\theta))}{\sin^3(2\theta)},
  \qquad p=\cos^2\theta,
  \]
  because the numerator vanishes at \(0\) and has derivative \(4\theta\sin(2\theta)>0\).
- Real Schur--Horn gives a rank-\(r\) projection with constant diagonal \(r/n\), establishing sharpness for every \(n\ge r\).
- Equality in the projection bound and Jensen's inequality gives the complete minimizer set.

`verify.py` performs deterministic numerical checks of the convexity expression and exact matrix checks for explicit constant-diagonal projection families. It is corroborative only.
