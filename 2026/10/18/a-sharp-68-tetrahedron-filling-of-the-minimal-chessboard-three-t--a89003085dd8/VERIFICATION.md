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

I reconstructed the oriented rook-placement bases by choosing rows and injecting them into columns, sorting the resulting tuples lexicographically. In the independent bounded replay /tmp/opencode/frozen_chessboard_independent.py, integer products using the certificate as data give the eight signed triangles of z, ∂₂z=0, and ∂₃w=3z with 68 distinct coefficients each of magnitude 1. For the stored numerator cochain n, max|n∂₃|=3 on the full 600-element tetrahedral basis and n·z=68, hence y=n/3 has |δy|≤1 and <y,3z>=68. Pairing with arbitrary signed real fillings gives the exact lower bound; integrality of the exhibited primal attains it over both coefficient rings. Dense mod-three elimination gives ranks 423 and 424 before and after adjoining z, proving nonboundary mod three, hence order exactly three integrally. For the orbit, the incompatibility graph on an octahedral support is a three-edge matching. Three row-pairs would need six distinct columns and conversely for three column-pairs. In the two-row-pair case, choose the paired column (5), the two paired rows (10), two of the other three rows (3), and two of the other four columns for the first of the chosen paired rows (6); the rest is forced. The replay exhaustively finds these 900 and their 900 transposes by the alternative condition that each rook has exactly one row-or-column conflict. Row and column permutations are transitive within each type, transposition exchanges them, and the induced signed chain permutations preserve norms, applying also to the negative orientation. This is the minimum coefficient ℓ¹ norm for the specified boundary in this complex, not a census of all optimizers. The frozen VERIFY.py was inspected, not executed.

## originality

PASS

Credit the exact sharp norm 68 for fillings of 3z, with equality even integrally and over the entire indicated orbit. The torsion group and generator are classical. The support count and orbit also appear in the later-dated indexed shortest-carrier result, whose focus is different. The inspected primary and indexed evidence does not yield the optimal norm.

## value

PASS

The smallest square chessboard exhibiting this torsion and its canonical octahedral generator are mathematically motivated before the filling computation. The exact cost answers a natural question not captured by homology, and equality of the real and integral optima rules out fractional savings; the finite certificates give a precise benchmark for any later quantitative study of fillings in these complexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
