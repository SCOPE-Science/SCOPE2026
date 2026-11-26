---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For i=2,3 the integral potential 0 at v_i and 1 at all other vertices proves K~4v_i. For 4v_2-4p the real potential is unique modulo constants by connectedness and positive conductances; there can be no extra bends away from the divisor. Independently eliminate an interior p on ij: with s=t/ell_ij its potential is (1-s)U_i+sU_j+4ell_ij s(1-s). The resulting outgoing-slope balances on the original four vertices are D=4 delta_2-4(1-s)delta_i-4s delta_j. Since D_2-D_3=4(U_3-U_2), this recovers 1-t for edges 02,12 and 1+t for 03,13 on the unsplit edge 23. For p on 23, symmetry gives U_0=U_1=(U_2+U_3)/2 and U_3-U_2=2t, hence slope -t on 02. All these witnesses are nonintegral on the relevant open edge. For p on 01, U_3-U_2=1 and D_0-D_1=(2+2/lambda)(U_1-U_0)=8s-4. The v_3 equation gives U_1-U_0=2k+1 for k=U_3-U_0. The balances at v_0 and p give the remaining split slopes 1-2k and -3-2k, so every slope is integral iff k is integral. Its open range is between -(3lambda+1)/(2(lambda+1)) and (lambda-1)/(2(lambda+1)), admitting -1 and 0 exactly when lambda>1. Solving gives the two displayed interior coordinates. The reduced balance also applies directly at s=0 for p=v_0, where k lies strictly between -3/2 and -1/2 and is integral only at lambda=1; exchange 0 and 1 for the other endpoint. At lambda=1 the same 0/1 vertex potential gives both endpoints. This proves the finding for real lengths, including irrational ones. The frozen rational-grid code was inspected, not run, and is not used to exhaust the graph.

## originality

PASS

The equilateral fiber and the genus-three gap-sequence formulation are prior. The supported distinct result is the complete one-edge phase diagram away from equality, with the exact threshold and interior locations. The inspected stronger-looking results characterize the condition or count broader objects, but do not supply this location theorem.

## value

PASS

Varying a single edge is the simplest test of how the equilateral tetrahedron's subcanonical vertices persist. The result gives a complete continuum classification with a sharp one-sided threshold: shortening removes two points and lengthening moves them into the varying edge with explicit coordinates. It supplies a natural exact benchmark for the exceptional genus-three canonical gap condition without purporting to classify weaker Weierstrass loci or lifting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
