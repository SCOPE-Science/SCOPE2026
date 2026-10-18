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
# Reproducibility checks

Run `python3 verify_p25.py` beside `morse_certificate.json`; compare stdout with `verification_output.txt`. No packages beyond Python 3's standard library are required. The script reconstructs \(\mathbb F_{25}\), its nonzero square set, all graph adjacencies, all \(515\) clique faces, the entire face-poset incidence graph and the signed Lefschetz traces for all \(25\) translations. It checks exactly \(225\) disjoint matching pairs and \(65\) critical cells, and visits all \(515\) vertices of the oriented face-poset graph in a complete topological sort. The expected mod-two boundary ranks are \((24,126,60,15)\), and the expected second Betti number is \(64\).

The inference from the verified acyclic Morse matching to integral homotopy uses discrete-Morse theory: one critical \(0\)-cell, no critical \(1\)-cells, and \(64\) critical \(2\)-cells imply a wedge of \(64\) two-spheres. This does not rely on mod-two ranks as an integral proof. The module decomposition is rational; an integral lattice or full quotient-space integral homology calculation is not verified or claimed. Independent scientific validation has not been performed.
