---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS for precisely the first five inclusive Euclidean Vietoris–Rips thresholds of the unscaled 24 signed coordinate permutations of (1+sqrt(2),1,1), and only intervals before squared radius 16+8sqrt(2). The seven squared pair-distance shells in Z[sqrt(2)] have exact multiplicities (48,36,48,48,36,48,12); the first five simplex face vectors are (24,48,8), (24,84,80,18), (24,132,248,186,48), (24,180,576,906,744,304,48), and (24,216,944,2202,2904,2236,960,192,8). Independently reconstructed all 24 vertices and 276 exact distances, enumerated every clique, all mod-2 boundary ranks and stage Betti vectors, and independently replayed ACTUAL Git certificate data in a separately implemented exact arithmetic JS checker. The certificate independently checked all 5,420 free-face collapse pairs against current cofaces: 8 at the first stage leave a connected (24 vertices,40 edges) graph with first Betti number 17; 36 at the second stage leave a closed connected triangulated surface (24,66,44) with each vertex link a circle and Euler characteristic two, hence S^2; 216 and 1,288 further relative collapses leave exactly the INCLUDED second-stage complex and preserve integral inclusion maps; 3,872 fifth-stage pairs leave a 3-dimensional complex (24,216,944,758). All 36 fifth-shell new edges have a new triangle with two older edges, so every loop reduces to the simply connected previous stage. Independently replayed 751 actual integer +/-1 pivot operations on the signed 944 by 758 third boundary, with zero remaining matrix: image is primitive, kernel is Z^7 and cokernel is torsion-free rank 193. Since the reduced 3-complex is connected and simply connected, rank im boundary_2=216-24+1=193; hence H_2=0, H_3=Z^7, and no higher homology. Hurewicz and homological Whitehead, not merely mod-two Betti counts, yield a wedge of seven 3-spheres. The independent Python checker also compared graph-metric second and third powers against Euclidean shells three and five for EVERY unordered pair, and obtained integral-proof-consistent Betti vectors (1,17,0); (1,0,1,0); (1,0,1,0,0); (1,0,1,0,0,0,0); (1,0,0,7,0,0,0,0,0). The finite exact certificate is exhaustive for THIS finite vertex set, not a claim about all solids or larger radii.

## originality

PASS

Best-of-knowledge PASS only for the precise additional early Euclidean sphere threshold, inclusion-preserving persistence and especially the integral graph-scale-three wedge of seven 3-spheres. Already published 24-vertex graph-radius-one wedge17 S1 and graph-radius-two 638-face sphere are not claimed new. The exact same-object paper was fully checked, as were Platonic-solid and graph-power primaries and the relevant dissertation. No reviewed source states a stronger theorem implying the new 9686-face integral result. This is a bounded priority finding, not global novelty certification.

## value

PASS

The unscaled rhombicuboctahedron is a canonical 24-point Archimedean metric configuration. A complete classification of the first five Euclidean Rips thresholds, the strictly earlier Euclidean birth of the boundary S2 than the coarse graph-distance-two threshold, inclusion-level simple homotopy persistence across two intermediate metric shells, and the sharp transition to seven integral S3 summands are natural topological persistence facts. The fifth-stage wedge and integral torsion control are not just a replay of the known graph-scale-two sphere, and supply a mathematically motivated target for finite Rips computations beyond Platonic solids. The theorem is explicitly limited to its five shells and is not asserted as a general-solid or full-filtration classification. Its motivation is geometric and topological, not merely computational reproducibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
