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

## Reproduction

Run `python3 verify_petersen_kneser.py --certificate regenerated.json`; it must finish with `KG_VERIFIER_PASS` and the figures \(49{,}920\) states, \(377{,}280\) moves, \(21\) orbits, radius \(7\), diameter \(8\), and \(2{,}880\) unordered diametral pairs. The generated JSON should agree in data with `certificate.json`.

Compile `g++ -std=c++17 -O2 verify_petersen_gp.cpp -o independent_gp` and run `./independent_gp`; it must print `INDEPENDENT_GP_MATCHING_VERIFICATION_PASS`, and its summary confirms the same state, edge, degree, eccentricity, and distance-eight-pair counts. The two source codes use distinct Petersen realizations, enumerators and component-finding routines.

## Scope and checks

The Python enumerator branches on *all* legal colours at the currently most constrained edge. The C++ enumerator independently checks every ordered decomposition into four matchings. Each constructs all legal bichromatic-component moves and searches all state orbits under graph and palette automorphisms. BFS covers the entire 49,920-state graph from an orbit representative, and automorphism invariance lifts each BFS result to the whole orbit. Orbit sizes sum to 49,920, and the orbitwise distance-eight counts sum to 5,760 ordered pairs, hence 2,880 unordered pairs. Neither implementation depends on randomization or third-party graph data.

The certificate records the complete 21 orbit representatives, sphere sizes, orbit sizes, degrees and exact distance-eight targets; it does not constitute a separate formal proof without the included source. The 2010 universal connectedness theorem and the previously published count of four-edge-colourings are not attributed to this computation. Independent audit: not performed.
