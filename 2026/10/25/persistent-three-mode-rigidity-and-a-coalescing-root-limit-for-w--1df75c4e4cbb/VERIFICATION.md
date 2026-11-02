---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. For probability weight (alpha+1)(1-|z|^2)^alpha dA/pi, radial moments m_k=k!/(beta)_k and angular orthogonality give the exact fourth moment |a|^4+4m1|ab|^2+m2|b^2+2ac|^2+4m3|bc|^2+m4|c|^4. Positive cross term forces phase alignment at every interior maximizer. Set x=|a|, y=sqrt(m1)|b|, z=sqrt(m2)|c| with x^2+y^2+z^2=1. The exact homogeneous quartic has C=2beta/(beta+1), D=4sqrt(C), E=12beta/(beta+2), F=6beta(beta+1)/((beta+2)(beta+3)). Coordinate face x=0 or z=0 has strictly positive first-order improvement from Dxy^2z when the remaining relevant coordinates are positive; the y=0 face gains derivative at least 2x^4+(E-4)x^2z^2+(E-2F)z^4>0, including endpoints; pure y is improved too. Algebra independently verifies E-4=8(beta-1)/(beta+2)>0 and E-2F=24beta/((beta+2)(beta+3))>0. Thus every beta>1 maximizer uses three modes. At beta=infinity the unique maximizer is (x,t=y^2,z)=(0,0,1) using the negative-definite quadratic bound; finite coefficients yield x,t=O(beta^-1). Rescale x=u/beta,t=v/beta: the limiting strict concave Q=-8u^2+4sqrt(2)uv-4v^2+24v achieves unique max 48 at (sqrt(2),4), giving F=6-24/beta+84/beta^2 and the asserted K expansion. The exact (y,z) coordinate-face optimum contributes 36/beta^2 above F; other faces are inferior, giving the gap 12/beta^2. Coefficient and polynomial-root limits follow from moment normalization and monic rescaling. I independently verified the rational identities, asymptotic Laurent coefficients and numerical optimizer localization at beta=100,1000, and inspected actual CHECKER.py; no finite check is treated as an asymptotic proof.

## originality

PASS

PASS, qualified: same-measure sharp degree-two optimizer and full beta->infinity three-mode/root/gap analysis are not the previously published general weight-changing or degree-uniform inequalities.

## value

PASS

PASS. The sharp same-measure norm of the minimal nonlinear polynomial family is a natural analytic invariant. It is structurally surprising that even as the measure concentrates and both rescaled roots coalesce, every exact finite-weight optimizer needs three modes, with a quantified nonzero 12/beta^2 advantage. This is not just routine radial moment computation: the global boundary exclusion and limiting optimizer structure make a meaningful complete classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
