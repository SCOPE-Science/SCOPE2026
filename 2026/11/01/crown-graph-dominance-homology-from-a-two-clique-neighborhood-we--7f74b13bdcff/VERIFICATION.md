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

`verify_crown_topology.py` uses only the Python standard library. Its `build(n)` explicitly constructs the \(2n\)-vertex crown graph, its graph complement, the Lovász open-neighborhood complex, the dominance complex and the two subcomplexes in the proof. For every \(n=4,5,6,7,8\) it compares duality membership over all \(2^{2n}\) subsets, tests the entire subcomplex union and intersection as sets of faces, and computes reduced mod-two homology of the open-neighborhood complex. Direct mod-two dominance boundary ranks are computed for \(n=4,5,6\); the more expensive large-cutoff cases use exact face duality but do not construct those direct boundary matrices.

The recorded results in `verification_output.txt` include neighborhood Betti ranks \(7\) at degree two for \(n=4\); ranks \(11,2\) at degrees two and three for \(n=5\); and ranks \(19,2\) at degrees two and four for \(n=6\). Every check passed. The script and its output are included alongside this file, so these assertions can be replayed.

The **integral** and **all-integer** statements follow from a separate explicit sphere-wedge homotopy proof and integral combinatorial Alexander duality, not from the finite mod-two computation. No Smith normal form of the large dominance boundary matrices is claimed. A published duality theorem is used as a cited lemma, not independently rediscovered. No equivariant statement or dominance homotopy decomposition is claimed.
