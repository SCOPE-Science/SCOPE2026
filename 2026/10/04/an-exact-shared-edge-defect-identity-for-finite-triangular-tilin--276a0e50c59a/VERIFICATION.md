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

The proof was replayed symbolically from the definitions.

1. For the planar graph obtained by splitting tile sides at all tiling vertices, Euler's relation is
\[
e=v_{\mathrm{bd}}+v_{\mathrm{int}}+t-1.
\]

2. Double counting graph edges against tile-side incidences gives
\[
2e=3t+v_{\mathrm{int}}^*+v_{\mathrm{bd}},
\]
hence
\[
t+2=v_{\mathrm{bd}}+2v_{\mathrm{int}}-v_{\mathrm{int}}^*.
\]

3. Every nonboundary tile side belongs to one stretch, so
\[
\Sigma=3t-v_{\mathrm{bd}}.
\]
A size-\(2\) stretch is exactly a full shared side and contributes no subdividing vertex. If the other stretches have sizes \(3+e_i\), then with \(E=\sum_i e_i\),
\[
v_{\mathrm{int}}^*=p+E,\qquad
\Sigma=2q+3p+E=2q+3v_{\mathrm{int}}^*-2E.
\]

4. Eliminating \(t\) and \(\Sigma\) gives
\[
q=v_{\mathrm{bd}}-3+3\bigl(v_{\mathrm{int}}-v_{\mathrm{int}}^*\bigr)+E.
\]

Boundary checks: \(v_{\mathrm{bd}}\ge k\), \(v_{\mathrm{int}}^*\le v_{\mathrm{int}}\), and \(E\ge0\). Thus \(q\ge v_{\mathrm{bd}}-3\ge k-3\). Standard conforming triangulations of a convex \(k\)-gon attain equality.

Scientific limit: the verification is a same-model reconstruction of the finite proof. It is not an independent audit, and it does not establish that no unindexed prior source contains the same identity.
