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
The all-parameter theorem is proved symbolically in `RESULT.md`.

Critical checks:
- the published vertices are exactly the permutations of the \(n+1\) displayed layers;
- uniqueness of a Euclidean minimum enclosing ball plus coordinate-permutation invariance forces a diagonal center;
- after translating by \(-\mathbf1\), every layer has squared-distance function \(Q_k(s)=n s^2-2S_k s+T_k\);
- the adjacent identity \(Q_k-Q_{k+1}=\lambda_k(\lambda_k-2s)\) makes the maximum layer index monotone with \(s\);
- \(D_k=2S_k-n\lambda_{k-1}\) and \(nb-D_k=n\lambda_k-2S_k\) are the exact left and right tests for whether the quadratic minimizer \(S_k/n\) lies in its active interval;
- \(D_{k+1}-D_k=-b(2k+n)-2(a-1)<0\), so the threshold rule is exhaustive;
- the radius is obtained by direct substitution into the active-layer quadratic;
- in the classical case the threshold inequality is \(k(k+n-1)\ge n(n-1)\), yielding the explicit ceiling formula and golden-ratio limit.

`verify.py` independently replays the minimax problem over a large finite box by enumerating every layer and every candidate breakpoint/quadratic minimum. This is corroborative only and does not replace the arbitrary-parameter proof.
