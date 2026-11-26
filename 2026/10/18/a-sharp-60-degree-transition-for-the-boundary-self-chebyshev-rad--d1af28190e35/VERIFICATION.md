---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

I rederived the minimax on the closed first-quadrant edge x=(u(1−t),vt). Squared distance has its boundary maximum at a vertex; quadrant signs make the two negative-axis vertices dominate. Their squared distances divided by v² are r(2−t)²+t² and r(1−t)²+(1+t)². The first strictly decreases up to t=1, including the square where its derivative vanishes only at that endpoint. The crossing t*=(3r−1)/(2(r+1)) is exactly 1/2 to the right of the second quadratic's vertex. Thus the envelope has its unique edge minimum at t* for 1≤r<3, and at 1 otherwise, including equality at r=3. Substitution and the four sign symmetries give the stated values and all centers (four interior-to-edge centers collapsing onto two short-diagonal endpoints). For the area ratio the derivative on the first branch has sign (r−1)(r²−14r+1), negative on 1<r≤3, versus positive for r>3; its unique minimum is 2/√3 at r=3. The ratio δ²/(u²+v²) decreases from 5/4 to 1 and is thereafter constant, yielding both L/δ bounds and their exact equality sets. The angle relation is r=cot²(φ/2). No degenerate rhombus is included. The frozen rational checker was inspected, not executed; its grid is not needed for the continuous proof.

## originality

PASS

The square endpoint is already published. The supported contribution is the all-shapes boundary-constrained rhombus profile, complete center transition and sharp equality families, including the fixed-area extremizer and fixed-perimeter plateau. The compared sources do not give or mechanically imply these classifications.

## value

PASS

The geometry solves the full natural rhombus class for an established boundary minimax invariant. The sharp center bifurcation and the contrast between the unique 60° fixed-area minimizer and the fixed-perimeter minimizing plateau give information not available from the square endpoint or the global quadrilateral bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
