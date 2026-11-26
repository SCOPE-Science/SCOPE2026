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

Each element of order p² generates one of p subgroups H_i, distinguished by slope modulo p; every H_i has the same order-p line. Torsion elements have order p and lie on one of p+1 lines. A generator of order p² fails to generate a cyclic subgroup with an element on any of the other lines; an order-p element fails with a point on a different line. Thus only the identity is in the cyclicizer. This gives the claimed independent twin classes P,A_i,B_j of sizes s=p−1, a=ps, s, with P joined only to the B side and all distinct A/B parts mutually joined. At most one white per class is possible. For odd p a blue mate remains in any white class. Write (e,r,t) for white P, A and B class counts. If r≥3, no A or B source can force as long as those three A classes are white, and P cannot remove an A even if it forces a lone B. If t≥2 and e+r+t≥3 every blue source has at least two white neighbors. Two white B classes alone peel via their blue mates. For t≤1,r≤2, P removes a lone B; then blue A vertices peel the at most two A whites, and a B vertex removes P if necessary. Hence the stated exact criterion. All pairs of distinct classes are admissible; their total weight is (N²−[(p+1)s²+pa²])/2. The three-class weight is s(pa)(ps)+binom(p,2)a²(ps+s), and the four-class weight is s binom(p,2)a²(ps). These simplify to the displayed coefficients and match the asserted minimum profiles. For p=2 I constructed each two-generator subgroup by modular sums, then exhausted all 128 white sets via containment of a nonempty fort; the census is 20,18,7,1 in degrees 4 through 7 with precisely the stated seven minimum omission profiles (weights 4,4,4,2,2,2,2). Replay: python3 /workspace/branches/independent_exact_checks.py, check_noncyl_p2(). The packaged tests were read; the odd-prime proof does not rely on them.

## originality

PASS

The graph definition and cyclicizer facts are established, and generic polynomial coefficients and twin obstructions are not new here. The supported distinct claim is the exact family enumerator with the maximum white-set classification for this mixed-exponent group, including the singleton-class boundary. The sources compared do not provide a dominating formula or the profile classification for this graph.

## value

PASS

This mixed-exponent abelian group is a natural case where order-p elements and order-p² generators visibly differ in the graph. The exact forcing classification describes all smallest seeds in terms of that subgroup geometry, and explains why the allowable number of white vertices stays bounded as the graph grows and why it changes when three classes become singletons at p=2. It supplies both a family benchmark for forcing polynomials on group graphs and explicit seed choices; those are useful independently of graph reconstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
