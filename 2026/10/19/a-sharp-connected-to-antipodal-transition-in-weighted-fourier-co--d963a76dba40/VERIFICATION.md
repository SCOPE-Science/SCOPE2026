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

Pass on /workspace/repairs/5/RESULT.md, not on the frozen proof as printed. Frozen line 54 doubles the first-mode term at opposite centers; the factor must be p(1+c)(1−y). Indeed, (sin a−sin b)²=(1+cos(a+b))(1−cos(a−b)). The erroneous expression already gives the wrong one-arc limit at y=c, whereas the corrected expression gives the printed arc value. The repair also limits the first strict convexity comparison to interior separations, not the antipodal endpoint. Weak-* compactness gives attainment; at any maximizer the nonzero first variation must be maximized as a linear functional, so thresholding its nonconstant degree-two polynomial forces a binary upper-level set of at most two arcs modulo null sets. Complementation reduces to α≤1/2. For fixed positive widths the energy is strictly convex in cos d, so only touching and antipodal centers need be considered. At the latter it is strictly convex in y on [c,1], leaving only the single-arc limit and the equal antipodal pair, including exactly both geometries at a tie. The Toeplitz trace-square calculation counts both directions for each pair and gives the printed weights. The supporting script was inspected, not executed; it checks direct integrations but does not check the erroneous simplified polynomial. Independent exact identities and endpoints were replayed in /workspace/branches/dc685221-6e30-4cd7-9b46-7640afa92cb9/record5_exact_replay.py. The replay is algebraic, not a substitute for the compactness and equality arguments.

## originality

PASS

The corrected two-frequency weighted maximum and complete equality transition are distinct from the strongest inspected first-mode rigidity and unweighted spectral results. The unweighted three-site arc conclusion is already implied by Abreu–Speckbacher and complements, and is not counted as original. Weighted two-arc superiority is the verified distinction. The comparison supports this scope to the best of current knowledge, not a universal priority claim.

## value

PASS

The repaired theorem solves a natural three-site spectral-mask design problem, predicts a genuine connectivity transition caused by diagonal gain imbalance, and classifies all extremizers, including the tie and arbitrary soft masks. Correcting the coefficient preserves this substantive global result; finite tests alone would not justify it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
