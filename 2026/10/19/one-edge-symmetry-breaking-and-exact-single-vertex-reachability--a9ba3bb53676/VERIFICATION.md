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

Even/odd parity in the distinguished bit reduces the Laplacian to L(Q_m) and L(Q_m)+2I+2(c-1)e_0e_0^T. The first summand sees all m+1 distinct Walsh levels from any vertex by the nonzero squared spectral weights. The odd radial restriction has the stated off-diagonals from shell incidence and has cyclic endpoints. In each Walsh level exactly one direction is radial, so all odd nonradial levels are already counted. On the radial block a nonzero defect removes every unperturbed level: at an unperturbed root the perturbed characteristic determinant is the rank-one shift times a nonzero endpoint cofactor, since that endpoint sees every simple eigenvector. Positivity for c>0 also excludes zero, so the new radial levels are disjoint from the even levels. The shell spectral measure has resolvent diagonal det(zI-G)det(zI-F)/det(zI-J). A simple full eigenvalue with vanishing spectral weight has an eigenvector zero at the shell; recurrence forces both sides nonzero. Conversely common block eigenvalues give such an eigenvector by scaling their nonzero boundary coordinates to cancel at that row. This proves the gcd deficit, including no deficit at endpoints. The left block's characteristic polynomial and first-endpoint cofactor have no common root, so each right-block eigenvalue gives at most one conductance. At c=1 Walsh support on Q_d gives d+1 directly. For m=2 the lone interior collision is c=1; for m=3,j=1 the blocks have levels 3+2c and 5±sqrt(3), respectively. Hence the first nonunit rank drops are exactly as claimed in the exhibited shell.

## originality

PASS

The distinct claim is the exact dependence on both the input vertex shell and the conductance, including the adjacent-block coincidence count. Coordinate-input spectral support, the uniform cube and at least the defect-edge endpoint case of Q_2 are not new. Close defect and cube results do not supply the claimed all-vertex formula.

## value

PASS

One modified conductance is a minimal symmetry-breaking intervention on a canonical graph, for which the reachable dimension from a specified vertex is a natural exact control invariant. The equality identifies the sharp gain over the unperturbed cube and pinpoints isolated conductances that hide simple modes, showing exactly why a generic spectral count cannot replace the input-dependent theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
