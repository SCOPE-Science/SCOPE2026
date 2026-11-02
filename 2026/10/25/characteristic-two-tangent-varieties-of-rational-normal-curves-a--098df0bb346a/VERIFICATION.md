---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Differentiate p(t)=[1:t:...:t^d] in char2; odd derivative coordinates survive, even ones vanish. For tangent parameter lambda, putting u=t² and v=t+lambda gives even coordinates u^j and odd coordinates vu^j. On projective closure these are the standard monomial parametrizations of S(m,m-1) if d=2m, and S(m,m) if d=2m+1. Both summands positive for d>=3 so image is smooth and degree a+b=d-1. Image function field is k(u,v) while incidence source is k(t,v), giving purely inseparable degree2. Direct parity and monomial checks for d=3..19 support the uniform algebraic proof; no finite extrapolation used.

## originality

PASS

Kaji 1989 supplies general positive-characteristic Gauss/ruled-surface theory, Furukawa–Ito general Gauss images and inseparability, and Ishikawa real differential tangent varieties. No inspected theorem explicitly yields the parity-dependent scroll splitting type and exact incidence inseparability degree for this standard rational normal curve. A more general positive-characteristic tangent-scroll theorem could imply the result and remains a priority risk.

## value

PASS

It gives an all-degree characteristic-dependent global geometric classification and exact inseparability, distinguishing smooth char2 tangential images from familiar characteristic-zero singular developables. The invariant is intrinsic to a classical projective variety, not an arbitrary sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
