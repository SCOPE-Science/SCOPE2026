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

# Reproducibility and limits

Run `python verify.py` from the directory containing this document. The checker requires only Python's standard library and performs deterministic numerical diagnostics; no external data or network connection is required.

It enumerates all **63** coprime integer parameter pairs \((p,q)\) with even \(4\le q\le34\) and \(1\le p<q/2\). For each pair it independently constructs the two half-plane normal families, deduplicates their directions, builds the polygon from successive tangent-line intersections, computes its shoelace area, and compares it against \(N h^2\tan(\pi/N)\). It checks that \(F(u)=-u\) and that three interior points, including the center, retain strict alternating half-plane signs through a complete \(q\)-iterate return. All tests pass with the tolerances stated in the code.

The theorem's proof is analytical for **all** admissible even denominators, independent of the tested cutoff. The checker does not certify every possible boundary orbit, nor does finite sampling prove originality or any infinite-dimensional/general-denominator assertion.

The proof fixes the relevant branch convention on the real axis; all classified polygon cells lie strictly off that axis throughout their trajectories. Independent audit: not performed.
