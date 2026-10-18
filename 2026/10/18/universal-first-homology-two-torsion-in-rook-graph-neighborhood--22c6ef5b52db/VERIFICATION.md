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

# Verification of the rook-graph first-homology theorem

The symbolic proof in `RESULT.md` treats an arbitrary abelian coefficient group and every \(m,n\ge4\). The five independent finite checks below do not establish the infinite theorem.

Run `python3 artifacts/verify.py` from the directory containing this file. The program constructs each open-neighborhood simplex directly from the rook-graph adjacency definition, enumerates its distinct edges and triangles, confirms that the one-skeleton is complete, checks the diagonal parity cochain on every triangle and a nontrivial L-shaped cycle, and computes the triangle-boundary ranks over the three finite fields of characteristics \(2,3,5\). The expected output is embedded as `artifacts/verification_output.txt`.

Actual verified mod-prime first Betti numbers were \((1,0,0)\) in characteristics \((2,3,5)\) for rectangles \((4,4),(4,5),(5,5),(5,6),(6,6)\). Characteristic comparisons by themselves do **not** distinguish all possible integral torsion orders, so the exact \(\mathbb Z/2\) conclusion instead uses the natural cohomology calculation for every abelian coefficient group plus the universal coefficient theorem.

The supporting literature checks established that the published sphere-wedge classification applies to **closed** neighborhoods, whereas the present torsion theorem concerns **open** neighborhoods. The full original text of one relevant older fundamental-group reference was inaccessible; it remains an originality risk. No external or independent validation is represented by these checks.
