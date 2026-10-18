---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The complete subgroup lists consist of P=<pe>, E=<pe,f>, p cyclic p^2 subgroups C_t and p order-p subgroups Q_s in the abelian group; the analogous P,E,C_t,Q_s hold in the modular group. Only P<E, P<C_t and Q_s<E occur, giving a balanced double star. In the abelian group an automorphism e -> a e+b f, f -> pc e + d f induces paired leaf affine maps of slopes d/a and a/d, translations b/a and c/d; all valid parameters give Aut size p^3(p-1)^2. In the modular group a->a^i b^j, b->a^(pk)b induces inverse slopes and two free translations, total Aut size p^3(p-1). The images both have order p^2(p-1) and kernels divide to p(p-1),p. A double star has full Aut of order 2(p!)^2. Algebraic parametrizations work for all odd p; source verifier enumerates p=3,5,7 only.

## originality

PASS

Devi–Rajkumar arXiv:1604.08259 expressly observe subgroup-lattice (therefore inclusion-graph) isomorphism for these groups; this part is NOT original. Ou–Wong–Wang 2020 concerns nilpotent inclusion graph diameters and apparently cyclic-group automorphism groups. Neither inspected relevant statement supplies the natural map Aut(group)->Aut(graph), its identical image on both groups and differing kernels. New claim is about symmetry retained/lost, not graphs alone.

## value

PASS

Two nonisomorphic groups have indistinguishable subgroup inclusion graphs and even identical induced graph permutation images. Computing their different kernels quantifies information lost by passing to graph structure, a natural obstruction to group reconstruction. The contrast is a nontrivial structural invariant across every odd prime, not a numerical coincidence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
