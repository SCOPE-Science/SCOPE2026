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

For n>=5, q=cos(2pi/n)>0, all n+1 vertices survive exactly if the projected apex planar point Q=-h(u_x,u_y)/u_z violates precisely one side-support inequality of the regular base. Each such cell is triangle with vertices (c,+/-s),(d,0), d=c/q; all other support inequalities hold by convexity. Haar normal projects to isotropic planar Cauchy density h/(2pi(h²+|Q|²)^(3/2)). The triangle solid angle gives p_n(h)=n/pi arctan[2s(d-c)h/D_n(h²)] with D_n(x)=(1+q+2x)sqrt(x+d²)+2(cd+x)sqrt(x+1). For G(x)=(a+2x)sqrt(x+t), 2xG_prime-G has strictly positive derivative, so the sum H_n=2xD_prime-D crosses zero exactly once; this is an analytic all-n proof, not a numerical root search. h_6=sqrt(3/5), p_6=6/pi arctan(sqrt2/22); Taylor analysis yields h_n->1/sqrt2 and n² p_n(h_n)->2pi²/(3sqrt3). Independently integrated triangular Cauchy density and rederived solid-angle equality for n=5,6,8; checks are corroborative only.

## originality

PASS

The assessed result treats all centered unit-circumradius right REGULAR n-gonal pyramids n>=5, including an exact one-triangle spherical-probability law, strict global uniqueness of the optimal height, a closed hexagon benchmark, and sharp inverse-square many-sided asymptotics. The closest published Resultary rectangular-pyramid theorem was read in full: its n=4 one-visible-side cells are unbounded strips and its formulas do not imply this bounded-triangle n>=5 statement or n->infinity asymptotic. Known silhouette-average results and the standard solid-angle identity are antecedents, not claimed discoveries. Best-of-knowledge originality PASS, not exhaustive priority.

## value

PASS

The all-vertex shadow event is a natural exact distributional statistic, and the theorem solves the nontrivial geometric visibility and shape-optimization problem for the complete regular polygonal pyramid family n>=5. The n^-2 decay and optimal height limit are meaningful asymptotic invariants, not a renamed solid-angle computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
