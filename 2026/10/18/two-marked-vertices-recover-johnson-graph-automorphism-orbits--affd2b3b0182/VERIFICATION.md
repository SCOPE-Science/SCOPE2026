---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For all n>=2k>=6 and distinct k-subset anchors A,B, independently reconstructed the Johnson distance induction and 1-WL statistic. With a=k-b,c=n-k-b, zone variables (t,u,v,z) satisfy p=k-t-u, q=k-t-v, M_--=z(a-t), M_++=t(c-z). Their difference equals a(p+q-k)+(2k-n)t: for n>2k this recovers t; at n=2k the quadratic identifies exactly the complement/swap involution (a-z,b-v,b-u,a-t). Zone-preserving permutations and balanced complementation give actual automorphisms transitive on the predicted classes; hence the partition is both no finer and no coarser than full pointwise-stabilizer orbits by round k+1. Burnside gives the balanced correction (a+1)(b+1). Independently constructed ordinary color-refinement graphs and tested six (n,k,b) instances, including (8,4,2) and (9,4,2). Finite tests do not prove the general theorem, which depends on these identities and automorphisms.

## originality

PASS

The exact all-k>=3 two-root 1-WL-stabilizer orbit equality, its k+1 bound, balanced involution and class enumerator were not implied by inspected Johnson automorphism, equitable two-colouring, or k=2 Tinhofer statements. In particular, knowing an orbit group cannot prove color refinement attains its orbit partition. A general 2026 hierarchy characterization concerns all possible individualized sets rather than identifying this particular Johnson family. Best-of-knowledge priority; terminology overlap with pointed association schemes remains a risk.

## value

PASS

Johnson graphs are a central distance-regular family and individualization/refinement is a standard invariant in counting logic and graph isomorphism. The exact two-anchor stabilizer partition for all parameters, the symmetry jump at n=2k and explicit polynomial/Burnside orbit enumeration are structural, reusable classifications, not an arbitrary tiny numerical sample. The order-of-refinement bound is a useful uniform logical complexity estimate, without claiming tightness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
