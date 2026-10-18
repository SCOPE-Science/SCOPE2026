---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For ordered two-particle configurations on the graph K_m with coincidences permitted precisely at original vertices (m≥4), Ramos Theorem 3.2 identifies the natural cubical model as K_m×K_m with exactly E=binom(m,2) interiors of diagonal edge squares deleted. Integral relative long exact sequence yields Q:H1(K_m;Z)⊗H1(K_m;Z)→Z^E taking coordinatewise products of oriented edge coefficients. For every edge ab, distinct c,d outside {a,b} exist and the triangle cycles abc and abd overlap only on that edge, so Q maps their tensor product to ±one standard edge coordinate; hence surjective INTEGRALLY. H1(Y)=Z^{2b}, H2(Y)=ker Q free of rank b²−E, no higher homology, where b=binom(m−1,2). For a permutation π, trace on oriented edge chain is binom(f,2)−t and trace on U=H1(K_m;Q) is p=binom(f,2)−t−f+1; fixed unordered edges F=binom(f,2)+t. Graded swap acts as minus flip on U⊗U and minus on removed edge-square module; exact equivariant characters are H1(π,1)=2p, H1(π,τ)=0, H2(π,1)=p²−F, H2(π,τ)=F−p(π²), with + swap eigenspace wedge²U. Independently computed triangle cycle product Q rank E for m=4,5 yielding Betti (1,6,3), (1,12,26); full all-m proof is symbolic, not finite extrapolation.

## originality

PASS

Ramos (2017) supplies the natural sink cubical model and studies general graphs in high particle number and exact tree cases; it does not give this all-m complete-graph integral edgewise-product calculation or S_m×C2 character. Later Ramos–He Yun complete-graph representation results concern collision-free, not vertex-sink, spaces. Resultary published anchored spaces require occupation of designated anchors and allow collisions elsewhere, a different topology; those ranks cannot imply the current characters. The complete-graph all-m integral surjectivity and swap character remain best-of-knowledge original.

## value

PASS

The complete graph is a canonical highly symmetric graph and the all-vertex sink convention is a natural and distinct collision model. A uniform integral additive-homology classification with no torsion and the full S_m×C2 character reveals nontrivial sign and edge-permutation structure invisible to nonequivariant ranks. The edgewise cycle-product surjectivity is reusable for comparing other graph families and genuinely mathematical, not a mere finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
