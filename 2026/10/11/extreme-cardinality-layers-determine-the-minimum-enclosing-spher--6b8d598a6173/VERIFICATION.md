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
The arbitrary-\(d\), arbitrary-\(S\) proof is given in `RESULT.md`.

Critical checks:
- the source vertex set is exactly the union of the selected Hamming-weight layers;
- the barycenter of the complete weight-\(s\) layer is \((s/d)\mathbf1\);
- averaging squared distances from \(z=t\mathbf1+w\), \(w\perp\mathbf1\), gives \(q_s(t)+\|w\|^2\);
- a diagonal center attains \(q_s(t)\) exactly on every vertex in that layer;
- \(q_s(t)=dt^2+s(1-2t)\) is affine in \(s\), so only \(\min S\) and \(\max S\) control the envelope;
- the unique one-variable minimizer is the projection of \(d/2\) onto \([\min S,\max S]\), divided by \(d\);
- the squared radius is \(h(d-h)/d\);
- strict endpoint-layer differences give the exact contact set;
- the \(\|w\|^2\) term and strict one-variable minimizer give center uniqueness.

`verify.py` checks every nonempty \(S\subseteq\{0,\ldots,d\}\) for \(1\le d\le8\) with exact rational arithmetic, verifying all layer distances, contact sets, and the lower-bound objective. Finite computation is corroborative only and does not assess originality.
