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

By source Theorem 1.7 the first Fourier zero k≈3.83171224396365 occurs in facet-normal directions. Compare P+tB with homothetic polygon Q_t=(1+t/r)P sharing offset facet support lines: the difference is 12 disjoint vertex caps, each area [tan(pi/12)-pi/12]t² and diameter O(t). Their Fourier effect is cap-area times sum of vertex cosines plus O(t³). The Fourier transform of Q_t scales exactly. A simple real root persists in this direction by implicit function theorem; derivative F′(k)<0. Since κ is infimum of all zero radii, the perturbed directional root is a valid one-sided upper bound. Steiner area expansion cancels the first-order root displacement, leaving η=-c*(sumcos/F′(k)-6k/pi)>0. Independent high-precision direct 12-edge divergence calculation gave k=3.8317122439636479540700049, F′=-0.65991482843667124, η=0.00014158574849173963225. Source mpmath interval checker separately brackets the sign; neither test alone proves the analytic remainder.

## originality

PASS

The 2026 full primary Gómez-Serrano–Levitin–Platt–Polterovich article proves the dodecagon has maximal κ among regular even-sided polygons and fixes nearest-zero directions; the open unrestricted convex maximizer problem is not settled. Published Resultary affine-orbit theorem treats area-preserving linear images, not outer Minkowski addition by a disk. The present one-sided quadratic perturbation gives a distinct nonlinear local stability direction; best-of-knowledge novelty with specialist variational literature risk.

## value

PASS

The global dodecagon extremizer conjecture makes local perturbations mathematically motivated; this explicit certified second-order decrease under the canonical Minkowski-disk rounding direction provides a precise geometric stability test and sign, without claiming global maximality or all variations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
