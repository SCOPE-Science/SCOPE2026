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
# Reproducible verification

Execute `python verify_morse.py` and `python verify_homology.py` with a standard Python 3 interpreter. Neither program imports third-party packages. All graph data, face enumeration, differential coefficients and expected values are generated from the ordered-pair definition in the accompanying result.

The integral verifier constructs all \(1949\) and \(28820\) nonempty faces, matches \(959\) and \(13922\) pairs respectively, and verifies complete topological orderings of directed Hasse incidence graphs with \(7340\) and \(138660\) arrows. It produces critical cell multiplicities \((1,6,24)\) in dimensions \((0,3,4)\), and \((1,7,968)\) in dimensions \((0,4,5)\). In both cases it calculates the signed integral Morse differential, checks a unit entry, and checks the vanishing of all two-by-two minors through exact cross-product identities. These checks establish that the integral Smith form has one unit invariant and otherwise zeros.

The independent verifier enumerates all allowable partial functions and computes boundary ranks modulo \(2,3,5\). For \(m=5\), the ranks of the non-augmented differentials from dimensions \(0\) through \(4\) are \((0,19,131,389,421)\); for \(m=6\) they are \((0,29,331,1869,5301,6393)\), giving the reduced Betti vectors in RESULT.md. These field computations are cross-checks, not a substitute for the integral attaching-degree calculation.

All computations terminate on the two stated finite graphs. No assertion about infinite families, a universally exhaustive external literature search, or independent mathematical validation follows from these certificates.
