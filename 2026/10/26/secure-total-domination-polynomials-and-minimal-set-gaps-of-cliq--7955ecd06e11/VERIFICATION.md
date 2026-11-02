---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Start from open-neighborhood total domination and defender exchange, not a scalar bound. If center omitted, each clique requires >=2 selected, and all swaps within a clique or a swap of a selected clique member into the center retain total domination. If center included but one clique empty, the empty clique vertex has only center as possible defender and exchange leaves it isolated; therefore >=1 per clique is necessary and sufficient, with within-clique swaps. Independent subset choices give F_B=z Π((1+z)^ri−1)+Π((1+z)^ri−1−ri z); stripping redundant vertices yields minimal families with sizes t+1 and 2t and M_B=(Π ri)z^(t+1)+(Π C(ri,2))z^(2t). Independent direct defender-exchange checks across 2/3 sized blades and original verify.py enumeration corroborated; all t,ri by logical case proof.

## originality

PASS

Jha 2020 considers minimum secure-total-domination on cographs, including this family in its scope. Thus the scalar gamma_st=t+1 is not presented as independent novelty. Its algorithm does not as such determine the number of all sets or inclusion-minimal spectra. Cabrera Martínez et al. 2019 supplies the definition/bounds; published Resultary complete-multipartite secure-total polynomial concerns a nonisomorphic different graph class (bouquet has induced 2K2), and dissociation polynomial on generalized windmills concerns a different property. Best-of-knowledge O rests on the complete two-polynomial count and unbounded missing-cardinality phenomenon. Some direct publisher full article retrieval was limited.

## value

PASS

Complete enumerators across arbitrary heterogeneous clique sizes and an arbitrarily large inclusion-minimal cardinality gap for connected chordal cographs distinguish robust guarding solutions beyond an already tractable scalar optimum. The family and invariant are natural in total domination and graph block structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
