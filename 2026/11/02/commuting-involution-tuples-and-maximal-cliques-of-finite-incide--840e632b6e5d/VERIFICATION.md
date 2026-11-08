---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For any nonempty finite poset P, odd q, each commuting k-tuple of involutions in its incidence algebra yields orthogonal sign-character idempotents e_eps=2^(-k)Π_i(1+eps_i a_i), which are conjugate to diagonal sign projectors by explicit unit u=Σ_eps e_eps d_eps∈1+J. The diagonal coloring c:P->[2^k] is invariant under unipotent conjugation; stabilizer size q^(m-d(c)) for d(c) differently colored comparable pairs, so C_k=Σ_c q^d(c)=Σ_(F⊆E)q^(m-|F|)(1-q)^|F|(2^k)^κ(F), the exact Potts/random-cluster expansion. Every commuting clique embeds into a full diagonal sign subgroup (size 2^n), whose unipotent normalizer is trivial, giving exactly q^m maximal cliques. Stirling inversion counts distinct commuting subsets; all odd q and k recover Tutte, and q→∞ normalized C_k approaches chromatic polynomial at 2^k. Independent direct F3 three-element-chain enumeration found 56 involutions and 976 ordered commuting pairs, matching Potts formula. General proof rests on idempotent conjugation, not finite enumeration.

## originality

PASS

Qualified O PASS for all-arity commuting involution counts, precise Potts evaluation, complete maximal-clique conjugacy census and Tutte/chromatic recovery. Gargate and Gargate papers classify/count individual involutions and higher-potent elements in incidence algebras, so k=1 and diagonal-sign setup are prior. Their inspected statements do not supply simultaneous tuple counting or q^m maximal cliques. Simultaneous diagonalization of split semisimple commutative subalgebras is standard, but the graph polynomial identification for arbitrary posets and the entire tuple census were not verified as prior. Published Resultary matches deal other commuting graphs, not incidence algebra involution k-tuples.

## value

PASS

Natural extension of involution enumeration to all commuting tuples produces a genuine exact Potts/Tutte connection, classifies every maximal elementary abelian 2-subgroup, and records how algebraic tuple statistics forget poset orientation; reusable all-arity classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
