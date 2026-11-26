---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Repaired RESULT.md passes; frozen RESULT.md line 9 was false if read as norm attainment at both endpoints. On any interior point of an edge vw the kernel column is a strict convex combination of the two vertex columns. At v those columns are 6C_d and -6C_d q_d, hence opposite on positive arclength. Each vertex column has mass Lambda_d, so every interior column has strictly smaller mass; Tonelli against |f| proves strict inequality for every nonzero L1 input. The sign of a vertex row attains the L-infinity norm because values along incident edges approach the vertex value. Kernel symmetry gives equality of the operator norms, not of attainment. Independently, each edge contributes the 2-by-2 Gram block with diagonal 1/3 and off-diagonal 1/6; the operator is bounded below on the regular tree. At positive radial distance the Green equation is 2d h_r+h_{r-1}+(d-1)h_{r+1}=0, and at zero it is 2d h_0+d h_1=1. Its summable solution is h_r=C_d(-q_d)^r. Integrating the two triangles on an edge gives (1+q_d^2)/(2(1+q_d)); the shell counts d(d-1)^r and the Green equation give the stated Lambda_d. The smaller root decreases with d, is asymptotic to 1/(2d), and gives the line value 2 at d=2. In the Neumann series each walk step has norm at most 1/2 and |D^{-1}T*f| is bounded by ||f||_infinity/2, yielding 3 and a tail (3/2)2^{-K}. Rooted regular tree data agree for the first K terms under the girth and ball hypotheses, so the two tails give 3*2^{-K}; large finite balls and then large d prove finite-tree sharpness. These are analytic checks; the frozen finite checker was inspected, not run. The repaired finding preserves the exact norms, range, and convergence statements.

## originality

PASS

Best-knowledge pass for the exact branching degree profile, unit-edge finite-tree sharpness and quantitative local convergence. The general bound 3, the mass-matrix method, L1/L-infinity norm equality by symmetry and the line case are not independent novelty claims. The attainment correction is a consequence of the computed columns, not a separate priority claim.

## value

PASS

The exact stability norm distinguishes line geometry from branching and quantifies how much stability can be lost as degree grows. Its two finite transfers make the branching law relevant to actual finite tree approximants and finite graphs of large girth, not just to one Green function. None of these uses requires the false endpoint-attainment assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
