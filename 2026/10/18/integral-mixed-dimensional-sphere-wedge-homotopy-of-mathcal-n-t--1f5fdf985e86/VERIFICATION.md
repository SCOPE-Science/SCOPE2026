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
# Reproduction and limits

Run `python3 verify.py` in this directory and compare its JSON stdout with `verification_output.json`. Python standard library only; the computation uses explicit arbitrary-precision integers and no randomness or floating-point approximations.

The verifier constructs open neighborhoods of the 21 two-element subsets, tests all 2,097,151 nonempty candidate subsets against an independently evaluated witness condition, and reconstructs the complete 18,494-face complex. The matching has exactly 9,120 pairs and 254 critical faces. The entire 98,805-incidence directed Hasse graph is topologically sorted without a directed cycle. Exactly one critical cell has dimension zero, 246 have dimension three, and seven have dimension four.

With lexicographic vertex orientations, each critical four-cell has zero integral Morse boundary on critical three-cells. Two different exact implementations agree: signed unit-pivot elimination through matched three–four pairs and reverse-order integer gradient-path recursion. All seven 246-component columns vanish identically. The three-skeleton is a wedge of three-spheres and the Hurewicz isomorphism turns the zero degree columns into null attaching maps. This supplies the integral homotopy type, rather than interpreting field homology as an infinite proof.

The output includes SHA-256 digests for sorted full faces, ordered matching pairs and sorted critical masks. This finite certificate does not establish an all-parameter result, and does not supply independent mathematical audit.
