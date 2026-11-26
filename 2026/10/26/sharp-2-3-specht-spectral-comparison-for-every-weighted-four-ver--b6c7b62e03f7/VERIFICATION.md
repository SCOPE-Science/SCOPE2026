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

A transposition fixes the matching containing its edge and swaps the other two matchings. On the sum-zero quotient, the triangle Laplacian with weights a,b,c therefore realizes (2,2); its two eigenvalues have sum 2W and product 3(ab+bc+ca), giving minimum W-sqrt(Delta). The (2,1,1) module is the sign twist of (3,1), so its minimum is 2W-Lambda where Lambda is the largest eigenvalue of the ordinary Laplacian restricted to the sum-zero space. Each edge contributes the outer product of the difference of its two vertex-coordinate rows in the Hadamard basis. This gives diagonal b+c,a+c,a+b and off-diagonal entries the three opposite-edge differences. Hence tr(M^2) <= 2W^2+2Delta. For deviations from mean 2W/3, the two other deviations sum to minus the largest deviation, so the latter is bounded by sqrt((2/3)(tr(M^2)-4W^2/3)). It follows that Lambda <= 2W/3 + (2/3)sqrt(W^2+3Delta), and 0<=sqrt(Delta)<=W implies sqrt(W^2+3Delta)<=W+sqrt(Delta). This proves the key comparison with no division by a gap. The dominance chain's remaining distinct pairs are covered by Aldous for (3,1) or the upper bound 2W on all spectra for the sign representation. The disconnected case of the Aldous comparison follows by adding positive rates and passing to the limit by eigenvalue continuity. The unit star has standard sum-zero eigenvalues 1,1,4 and bundles (1,1,1), giving exact ratio 2/3.

## originality

PASS

Credit only the uniform sharp lower bound for arbitrary weighted four-vertex graphs. Alon's Conjecture 1.5 is exactly the more general proposed comparison and the unit-star obstruction and equality are known. The strongest inspected theorems do not supply the sharp unrestricted four-vertex lower bound. This is an assessment of the distinct proved claim, not of priority beyond the consulted evidence.

## value

PASS

The four-vertex dominance chain is the first to contain a comparison not settled by the ordinary interchange gap or the sign endpoint, and the star shows that its constant cannot be one. Settling the sharp constant on the whole nonnegative cone is a complete and natural test of the general conjecture. The trace proof explains the uniform result beyond the examples and special weight classes already in the literature.

The dated certificate retains the supplied scientific assessment, sources and limitations.
