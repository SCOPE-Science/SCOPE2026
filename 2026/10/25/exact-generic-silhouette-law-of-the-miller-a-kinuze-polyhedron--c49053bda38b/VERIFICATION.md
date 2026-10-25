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

# Verification notes

Run `python3 verify_j37.py` using the Python 3 standard library; no external data files are needed. The complete supporting-face enumeration uses exact \(\mathbb Q(\sqrt2)\) arithmetic on the stated \(24\) vertices. It reconstructs \(26\) supporting facets and \(48\) edges, the three generating rigid symmetries, all eight potential facet-normal change families, and the sign of every face on each of the \(54\) open chambers within a fundamental wedge. It checks two exact dihedral-angle classes with \(24\) edges each, evaluates the finite spherical-triangle probability expression, and independently reconstructs \(1800\) projected convex hulls. Successful execution ends with `ALL_J37_SILHOUETTE_CHECKS_OK`.

The continuum conclusion follows from complete algebraic event enumeration and constant signs within every open cell; finite random views are solely independent geometric cross-checks. Spherical angles and their final decimal evaluations use floating-point evaluation of an explicitly stated closed algebraic arctangent formula; the exact formula is the mathematical assertion.

Historical novelty was compared against original geometric classification, selected projection references, and random-silhouette asymptotic literature. Other references could exist. No independent mathematical audit has yet been performed.
