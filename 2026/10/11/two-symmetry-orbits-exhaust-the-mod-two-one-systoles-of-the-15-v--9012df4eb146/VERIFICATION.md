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

The standalone `verify.py` embeds the complete 75-facet complex and the three published generators for the action labeled `15^15 = [3]A5 = GL(2,4)`.

It performs these exact checks:

1. Reconstruct all faces and verify the face vector \(f=(15,90,150,75)\).
2. Compute binary Gaussian-elimination ranks \(14\) for the edge boundary map and \(74\) for the triangle boundary span, giving \(\dim H_1=2\).
3. Exhaust all \(455\) triples: \(150\) are triangles, \(120\) are missing triangles whose three edges are present, and \(185\) lack at least one edge.
4. Reduce all \(120\) missing-triangle boundaries modulo the triangular-boundary span; none is zero, and the three nonzero quotient classes occur \(40\) times each.
5. Generate the permutation group from the three published generators, obtain \(180\) elements, and verify that every element preserves the 75-facet set.
6. Compute the action on missing triangles, obtaining orbit sizes \(90\) and \(30\) with representatives \({1,2,10}\) and \({1,2,12}\), and verify class counts \(30,30,30\) and \(10,10,10\) within the two orbits.

The exact recorded output is stored in `verification_output.txt`. The computation establishes only the finite theorem for this complex. The assertion that this generated 180-element action is the full simplicial automorphism group uses the published classification entry identifying action `15^15` with the full group \(\mathrm{GL}(2,4)\); the verifier independently confirms the generators preserve the complex and generate 180 elements.
