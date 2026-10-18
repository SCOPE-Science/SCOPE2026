---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The truncated tetrahedral graph is the 12 ordered distinct symbol pairs with edges for common first coordinate or reversing order, giving 18 edges and diameter three. Every integer-scale intrinsic graph Čech nerve was reconstructed from parity-dependent closed vertex/edge neighborhood generators; all face vectors and graph distances agree with RESULT.md. Independently built and fully checked acyclic discrete-Morse matchings at r0..6, with critical cells r1 (0:1,1:7), r2 (0:1,1:3), r3 (0:1,2:9), r4 (0:1,3:15,4:8), r5 (0:1,7:5), r6 (0:1). At r4 I computed the integral signed gradient-path Morse 15x8 matrix independently in trunc_integral.py: rank 4, Smith diagonal four 1s and zeros, selected (rows 0,1,2,4; columns 2,3,4,5) minor +1 and 30 nonzero entries. Integral attaching-degree classification gives wedge11 S3 ∨ wedge4 S4, not simply a rational-Betti guess. r1→r2 H1 map onto because every new distance-two edge is homologous via a Čech triangle to an old two-edge path; free abelian rank7→rank3 gives 3 long and 4 short H1 bars. Higher stages have distinct nonzero degrees, so complete integral barcode follows. Calculations finite but exhaustive for this graph.

## originality

PASS

PASS best-of-knowledge for all real scales of intrinsic graph Čech and integral barcode; exact mixed-dimensional integral r4 Morse attaching matrix and persistence ranks are distinct from any inspected Platonic hypercube or same-graph Rips result. Prior Čech generator lemma credited; Resultary search unavailable and residual priority risk retained.

## value

PASS

The truncated tetrahedral graph is a natural Archimedean 1-skeleton whose intrinsic Čech filtration differs dramatically from known metric-graph Rips; the mixed-dimensional r4 integral wedge and surviving long H1 intervals provide specific, meaningful topology beyond an isolated Betti entry. Complete classification across every real scale plus exact integral boundary torsion control is a reusable finite case relevant to graph Čech persistence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
