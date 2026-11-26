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

Work on k[t]/(t^m)⊕k. The cross maps are inclusion into the t^(m−1) socle and evaluation at 0. Their short-block composite is zero because m≥2; in the basis ordered as 1, the short-block basis, t,…,t^(m−1), the determinant is f₀^m a. In multiplying units the long-long commutator has only the socle coefficient uV−Uv, and the two cross-block commutators give the other two minors of the rows (f₀−a,u,v) and (g₀−b,U,V). Thus a nonzero first row requires the second row to be a scalar multiple, whereas a zero row commutes with all units. The equation g₀−b=h′ with g₀,b nonzero has q−1 solutions for h′=0 and q−2 otherwise. This yields stabilizers |G_m|, q^m(q−1), q^(m−1)(q−1)², respectively. Dividing gives the three class sizes; summing element counts divided by their class sizes gives (q−1)(q²+1)q^(m−2). The third stratum is empty at q=2 and the orbit-count identity gives cp=5/8 there and the displayed general cp. The frozen checker and its verification were inspected, not executed. A separately written direct-matrix enumeration (independent_matrix_check.py) matched all class-size multiplicities at (q,m)=(2,2),(3,2),(2,3),(3,3), with 40, 2160, 160 and 19440 ordered commuting pairs, respectively. It is a finite corroboration; the three-minor argument proves uniformity including over extension fields.

## originality

PASS

The supported distinct claim is the all-length, unit-only internal class-size distribution, including the distinction between noncentral classes with equal and unequal diagonal residues. No priority is credited for the module description, the orbit-count identity or the individually known small cases. The strongest checked same-centralizer statements use different orbit domains or stop at low dimension.

## value

PASS

Internal conjugacy sizes are natural finer invariants than order or the number of ambient similarity classes. The full distribution shows exactly what changes as the long Jordan block lengthens and what does not, including the missing unequal-residue stratum at q=2. It supplies a uniform closed benchmark for a basic nonregular family of finite matrix centralizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
