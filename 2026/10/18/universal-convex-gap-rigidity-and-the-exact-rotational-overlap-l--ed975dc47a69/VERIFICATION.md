---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Each fine-grid interval of angular width b=2π/m contains at most one coarse normal. Modulo b, the n coarse residues form q=n/gcd(n,m) equally spaced offsets occurring d times; this gives exact gap list and identity E_f=(m−n)f(b)+d∑[f(kh−t)+f((q−k)h+t)] including collision phases f(0)=0. Symmetry and strict convexity yield unique midpoint min and aligned max, without assuming f is increasing. A circumscribed tangential polygon has area r²∑tan(g/2). Uniform angular phase and integral of tan yield claimed mean and CDF; Taylor at minimizing phase and derivative at maximum establish density endpoint laws; cubic power-sum identity yields π³r²d²/(4nm³)+O_n(m^-5) for fixed n. Independent direct merged-normal computation across 280 (n,m,t) configurations matched formula with maximum absolute rounding discrepancy 3.55e-14; these checks supplement proof.

## originality

PASS

Existing area formula for tangential polygons, circumscribed outer-size polygon problems and congruent-copy random intersections are prior, but differ from unequal-order equal-inradius intersection normal-grid overlap. General convex rearrangement principles alone do not give the gcd-resolved gap multiset, exact full phase law, area distribution and sharp arithmetic oscillation.

## value

PASS

Natural intersection and rotational statistics of two unequal regular polygons under a common circle normalization. The all-convex-energy extremizer theorem and exact all-n<m distribution resolve a genuine geometric/arithmetic gap, not an arbitrary unmotivated finite slice or a renamed textbook polygon-area identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
