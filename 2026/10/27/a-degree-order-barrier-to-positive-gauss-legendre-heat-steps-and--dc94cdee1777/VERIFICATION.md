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

On nonconstant eigenmodes, μ/(d−μ)=μ/d+μ²/[d(d−μ)]. For connected d-regular G the first sum is −1 after division by d; the second is at least (Nd−d²)/(2d²) since μ≥−d. This gives tr(AL⁺)≥(N−3d)/(2d). Equality at N=3d would require every nonconstant μ to be 0 or −d. The trace then forces a single −d, but the second moment requires a nonconstant squared sum of 2d², not d². Thus an actual edge has L⁺_uv>0 by the undirected edge trace sum. Completing the square in the scalar numerator gives positivity, the denominator is no smaller for h≥0, and the constant mode is fixed. Expansion on each positive Laplacian eigenmode gives T=I−12L⁺/h+O(h^(−2)), establishing negativity on the fixed edge for all sufficiently large finite h without instability. For C_3 square C_3 use the constant and orthogonal complement projectors of each K_3 factor: with A=3h²+3h+1 and B=3h²+6h+4 one gets R(3h)=1−12h/B and R(6h)=1−6h/A. The adjacent and nonadjacent coefficients give 4h(h+1)/(AB) and 2h²(3h+2)/(AB); subtracting four of each from 1 yields the claimed diagonal. The entries are strictly positive at h>0 and at h=0 the matrix is I. All other tori in the stated range have N≥12 and d=4, so fail unconditional positivity. The exact-rational support and recorded output were inspected but not executed; the all-graph result does not depend on the seven finite regressions.

## originality

PASS

The supported distinct claims are the actual-edge obstruction for all connected simple regular graphs at the sufficient order–degree threshold and the resulting complete all-step cycle-product classification. The exceptional positive rook graph is covered by the earlier strongly regular classification as acknowledged. Prior distance-regular M-property bounds give the same ratio in a narrower graph class with a weaker off-diagonal witness; general absolute monotonicity does not classify these graphs. No priority claim is made for those inputs or the nine-vertex case.

## value

PASS

Distinguishing preservation of nonnegative data from spectral stability matters for graph heat integration. The sufficient condition depends only on coarse graph structure and locates a failing transition on an existing edge without a graph-specific calculation. It also settles all cycle-product sizes in the stated range, rather than extrapolating from a few grids or claiming that all positive steps fail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
