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

# Verification record

The scientific argument proves the theorem for every integer \(n\ge3\) by an exact distance classification, exhaustive *symbolic* clique-family classification, relative cone collapses, and a simply-connected homotopy-pushout decomposition. In particular the wedge assertion is integral; it does not follow merely from a mod-prime homology test.

To check the finite instances independently, run `python3 verify.py` from the directory containing this document. The executable uses Python's standard library only, generates the unrescaled signed root configurations directly, enumerates geometric maximal cliques using Bron–Kerbosch search, and compares them exactly with the four proposed facet families. It enumerates the induced simplices and computes all boundary-matrix ranks over \(\mathbb F_2\) by exact bit-vector elimination. The tests for \(n=3,4,5,6\) returned `VERIFY_OK`.

At \(n=3\) the computed Betti vector in degrees \(0,1,2\) is \((1,0,9)\). At \(n=4\), in degrees \(0,1,2,3\), it is \((1,0,32,1)\); at \(n=5\) it is \((1,0,80,0,1)\); at \(n=6\) it is \((1,0,160,0,0,1)\). The complete maximal-facet counts are respectively \(52,136,312,668\). The finite computations are confirmation of combinatorics and boundary matrices, not a proof for unbounded \(n\) and not an independent audit. There are no numerical approximations in the verifier.

No code asserts a complete filtration beyond radius \(\sqrt3\), and no certificate for integral symmetry modules or later homotopy transitions is claimed.
