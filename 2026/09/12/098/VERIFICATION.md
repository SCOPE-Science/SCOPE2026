---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The construction gives an analytic infinite counterexample family. With \(t=s^2\), \(N=s^6\), prime \(p\ge s^4\), and \(D=3s(t-1)+1\), one has \(N\le p^{3/2}\), \(D\le3s^3\), and sufficiently many primitive positive normals to form at least \(N\) planes. Distinct indexed planes stay distinct modulo \(p\): proportional normals would have integer cross-products of absolute value below \(p\), hence zero, and primitive positivity then fixes the normal; the intercept range is also below \(p\). For each primitive normal every grid point lies on exactly one intercept plane, so the total incidence mass over the full family is \(N|S|\). Selecting the top \(N\) planes therefore gives \(I\ge N^2/D\ge N^{3/2}/3\), and division by \(N^{17/12}\) diverges like \(N^{1/12}/3\). The package script was read completely; its finite checks are corroborative, while the large-\(s\) conclusion is the analytic averaging argument.

## originality

PASS

Best-of-knowledge original for the specific Cartesian-grid restricted disproof. Rudnev’s general point–plane theorem is known to be sharp without additional assumptions, and this creates real overlap risk, but the inspected statements did not show that a prior sharpness example already has the audited equal Cartesian-product point set and the same small-normal plane family. Fresh semantic search found no earlier exact construction; therefore the restricted target is not shown to be a direct corollary of the located prior examples.

## value

PASS

The construction directly resolves a proposed uniform Cartesian-grid incidence improvement by showing the obstruction persists even under the product-set restriction. It supplies a scalable analytic counterexample family and identifies small-normal directions as the mechanism, which is a motivated boundary result for incidence theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
