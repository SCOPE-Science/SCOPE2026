---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Kayacan's criterion reduces ordinary domination to covering every minimal subgroup. In exponent \(p\), every nonidentity element has order \(p\), so maximal-subgroup replacement converts the problem to covering \(V=G/Z(G)\cong\mathbb F_p^{2n}\) by hyperplanes. At most \(p\) hyperplanes cannot cover \(V\), while the \(p+1\) hyperplanes through a codimension-two subspace do; their lifts all contain \(Z(G)\), hence form a clique, and \(p+1\) is even. In exponent \(p^2\), odd-prime class-two collection gives \((xy)^p=x^py^p\); the nonzero homomorphism \(x\mapsto x^p\) maps onto the order-\(p\) center, so its index-\(p\) kernel contains every order-\(p\) subgroup and dominates alone. Pairing that kernel with \(Z(G)\) gives sharp total and paired value \(2\).

## originality

PASS

Kayacan supplies the general minimal-subgroup covering criterion but does not specialize it to extraspecial groups; full-text search found no extraspecial or Frattini specialization. Resultary searches located domination results for abelian and dihedral subgroup-intersection graphs and for extraspecial noncommuting graphs, all different families or graph constructions. The exact exponent dichotomy and the simultaneous total/paired values require additional extraspecial structure and are not stated by the checked broader sources.

## value

PASS

The theorem gives a complete and sharply contrasting domination profile for a canonical nonabelian \(p\)-group family, and the profile detects the two odd-prime exponent types. It combines a finite-geometry cover mechanism with a power-kernel mechanism, which is mathematically more informative than isolated small-group calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
