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

# Verification and limits

Run `python3 verify.py` using Python 3 and no external dependencies. The script reconstructs graph distances, enumerates every scale-two metric clique, independently builds the diamond/square/triangle model, and checks their exact equality. It confirms that each of the listed \(54n\) elementary pairs is a valid free-face pair, that the survivor equals a standard torus triangulation, and that each of the \(2n\) added triangles meets the base exactly in its boundary. It computes mod-two boundary ranks of the *full* complex, rather than assuming the target homology.

Executed parameter values: \(n=7,8,9,10,11\) with first cycle length six. All tests passed. The printed Betti values are \(eta_1=1\) and \(eta_2=2n\), with higher reduced homology zero. The exact output is in `verification_output.txt`.

**Finite/infinite boundary.** These enumerations validate finite instances and the specified collapses only in their tested sizes. The proof in RESULT.md derives the general clique classification, local free-face uniqueness, primitive attaching loop, and cellular homotopy decomposition symbolically for every integer \(n\ge7\). No independent audit or theorem-proving certificate is claimed.
