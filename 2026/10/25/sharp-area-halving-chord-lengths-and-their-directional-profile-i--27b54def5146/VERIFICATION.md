---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

A compact convex polygon admits a unique area-bisecting offset for each line normal because clipped area is strictly increasing through the supporting interval. Dihedral symmetry reduces normals to one sector 0<=phi<=delta. The proof establishes the two support intersection edges remain the same reflected pair throughout that entire sector (including triangular n=3). Subtracting the fixed polygonal cap from the wedge gives constant area of a triangle with endpoint ray distances a,b from the common reflected vertex, so ab is constant. Express a/b=exp(2s); elementary direction trigonometry gives tan(phi)=cot(delta)*tanh(s) (with sign absorbed by orientation) and the cosine rule yields the displayed L(phi). Strict increase with |phi| follows from positive tan(delta), giving exact min/max and endpoint equality cases. Direct independent polygon clipping/binary search of the half-area offset, entirely separate from the analytic formula, agreed for each of n=3,5,7,9,17,31 at seven normal angles per sector with max error 9e-16. Taylor expansion gives difference R*pi^2/(4n^2). Finite confirmation alone is not a universal proof; sector containment and wedge-area geometry are the universal arguments.

## originality

PASS

General area-halving chord inequalities, hyperbolic bisection envelopes and the regular-pentagon picture are acknowledged prior mathematics. The exact complete direction-by-direction length law, strict monotonicity and sharp all-odd-n extremal formulas are not stated in inspected primary sources. The 91-page Berele--Catoiu 2022 envelope work is a serious plausible fuller predecessor but inaccessible; its abstract cannot be used to declare NOT_COVERING. This risk does not itself invalidate a best-of-knowledge originality PASS.

## value

PASS

Area-halving distances are classical natural convex-geometric invariants; regular odd polygons form the canonical nonsymmetric case contrasting even polygons and disks. The exact full directional profile determines both sharp extrema, equality orientations and rate of circular convergence, rather than a tiny unmotivated numerical case. It benchmarks earlier general inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
