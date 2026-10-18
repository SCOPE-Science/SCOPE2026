---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For c in [-1/2,1/2], use omega(z)=z v(z) to express preSchwarzian(z)=v+c z v² and S_f=(1+2czv)v' +(c-1/2)v²-czv³-(1/2)c²z²v^4. Apply Schwarz–Pick |v'|<=(1-|v|²)/(1-|z|²). With r=|z|,s=|v|,u=1-r², for c>=0 the upper envelope F_+(c,r,s) is convex quadratic in c, with explicit nonnegative 1-F_+(0,r,s) and 1-F_+(1/2,r,s) polynomial decompositions. For c=-d the exact 1-F_- identity is (r-dus)²+us²(1/2-d-d²)+ur²s²(d²+d+1/2)+drus³(1+r²-(drus)/2); all terms nonnegative iff d<=d_*=(sqrt3-1)/2 in the demonstrated interval. Equality/uniform gap forces z->0,v(0)=0 and |v'(0)|=1; Schwarz equality then v=e^{i theta}z, yielding exactly normalized rotation family and norm 1. For d>d_* choose disk automorphism with v(r)=-s and r=ds; alignment makes F_- exact and its s² coefficient d²+d-1/2 positive, establishing a counterexample for sufficiently small s. Ahlfors–Weill then supplies K<=3 as sufficient, not optimal. Independent SymPy verified the full F_- SOS identity and critical expansion exactly.

## originality

PASS

Best-knowledge novel signed-quadratic explicit radical phase boundary and complete norm-one extremizer classification. Highly relevant general 2011 Kanas–Sugawa variational framework is recognized as underlying the optimization, but reading its theorem and proof did not show an already evaluated signed quadratic target or equality rigidity. The source defining positive targets treats Hankel determinants only.

## value

PASS

The entire real univalence parameter range of the natural quadratic subordination target has a sharp Schwarzian norm-one threshold, with explicit counterexamples on the other side and complete equality rigidity. This is a motivated analytic phase diagram, not a parameter renaming or an unsupported quasiconformal optimality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
