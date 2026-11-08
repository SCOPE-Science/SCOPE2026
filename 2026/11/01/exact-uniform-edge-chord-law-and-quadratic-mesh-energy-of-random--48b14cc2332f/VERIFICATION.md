---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Read actual RESULT.md and numerical verifier and inspected the Akopyan–Edelsbrunner–Nikitenko spherical Blaschke–Petkantschin primary decomposition. A uniformly selected facet and uniformly selected one of its three edges samples each of the deterministic 3n-6 edges uniformly. The two circumcap branches t=4b(1-b) yield independent B~Beta(n-1,2) and area-weighted unit-circle triangle shape. Integrating third angle gives I(alpha)=4sin²(alpha/2)+(pi-alpha)sin(alpha), with integral 6pi; the two-to-one chord substitution produces the stated nonnegative U density. E U²=5/2, E[4B(1-B)]=8(n-1)/((n+1)(n+2)), yielding E L²=20(n-1)/((n+1)(n+2)) and expected total energy 60(n-1)(n-2)/((n+1)(n+2)); expected area separately supplied by prior source gives 15/pi for the ratio of expectations. Beta-to-Gamma convergence proves weak scaling. Independent quadrature verified U moments 1, 128/(27pi), 5/2, 70/9, and the exact expected energy for n=4,5,9,20; these are checks, not finite-n evidence for all n.

## originality

PASS

The main 2020 spherical-polytope source provides general facet radius/shape decomposition, expected area and total first-length edge expectation, but it does not evaluate this explicit normalized angular chord density or the squared-edge energy. The calculation is a substantive application rather than merely paraphrasing an existing first-moment table.

## value

PASS

Uniformly sampled graph-edge lengths are a natural mesh statistic for random inscribed spherical polytopes; the full finite-n law enables every moment and the large-n Gamma scaling. The exact expected sum of squared chord lengths relative to already known mean surface area yields a universal mesh-quality benchmark, sharper than a first-length average and distinct from the deterministic equilateral triangle lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
