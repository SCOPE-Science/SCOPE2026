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

The actual orbit-union complex K_m is homeomorphic to the genuine geometric fixed set: an invariant face contributes one orbit-barycenter vertex for each whole orbit in its support, and fixed barycentric weights give the inverse. Direct maximum-Hamming-distance casework shows the orbit graph consists of two VR(Q_m;2) copies joined by 2^m matching A/B bridges, and independent C_z cone vertices, each with link two contractible m-simplices plus m+1 bridge edges, hence m circles. These links attach along difference loops x_w x_z^{-1}. As the lower-cube complexes are simply connected (the published wedge-of-3-spheres theorem, with small m simplices), maps of graph links are determined by these words. Homotopy cofiber reduction and spanning-tree cancellation eliminate the 2^m-1 bridge generators integrally, leaving m 2^m-(2^m-1) 2-spheres and the two existing 3-sphere wedges. Checked small m=1..4 by separately constructing Hamming orbit unions and mod-two boundaries; finite tests do not prove integral homotopy but agree on ranks. No theorem for arbitrary permutations/other radii.

## originality

PASS

Best-of-knowledge PASS: the relevant ambient homotopy theorem supplies c_m but not geometric fixed points. The 2026 hyperoctahedral representation theorem gives rational ambient character, which can determine a Lefschetz number but not the integral fixed-space homotopy type; the 2026 Cambridge paper studies ambient connectivity and Tor/cohomology. Neither the latter nor the scale-three paper states the orbit barycenter/cone-link theorem. A coordinate flip has a different orbit structure. Exact and alias Resultary/web queries yielded no dominating geometric transposition-fixed homotopy theorem; this absence alone is not novelty proof. Full text of the representation paper was unavailable in this run, a material priority risk.

## value

PASS

A coordinate transposition is an elementary natural hypercube symmetry. The complete all-n integral geometric fixed-space homotopy classification distinguishes exponentially many S^2 summands from the ambient scale-two Rips space, with genuinely mixed S^2/S^3 wedges starting n=5. Its explicit orbit model and integral attaching-word reduction are structural, reusable mathematical information, not a numerical sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
