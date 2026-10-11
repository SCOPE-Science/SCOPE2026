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
# Verification

The bundled `verify.py` uses only the Python standard library and reconstructs the Petersen graph before doing any topology calculation. It enumerates every nonempty matching, obtaining 331 faces and face vector
\[
(15,75,145,90,6).
\]

It then reconstructs the stated element-order matching, verifies all 160 pairs, enumerates all 975 Hasse covers, reverses exactly the matched covers, and checks acyclicity by topological sorting. The only critical dimensions are one cell in dimension \(0\), five cells in dimension \(2\), and five cells in dimension \(3\).

For a separate chain-level check, it builds all simplicial boundary matrices over \(\mathbf F_2\). Their ranks are \(14,61,79,6\), which gives reduced Betti ranks
\[
\widetilde\beta_2=5,\qquad \widetilde\beta_3=5,
\]
and zero in the remaining dimensions.

For the homotopy-type step, the verifier keeps integral incidence signs and recursively substitutes along the acyclic matched pairs. The resulting Morse boundary matrix from the five critical \(3\)-cells to the five critical \(2\)-cells is exactly the zero integer matrix. This is the critical check that rules out nontrivial degree attachments hidden by the face vector. The mathematical proof then uses that the Morse \(2\)-skeleton is \(\bigvee^5S^2\), so Hurewicz identifies attaching homotopy classes with their integral degree vectors.

Run `python verify.py`. A successful replay ends with `VERIFY_OK`. `verification_output.txt` records one such replay. The script proves only the finite Petersen-graph statement; it does not test or claim an infinite family.
