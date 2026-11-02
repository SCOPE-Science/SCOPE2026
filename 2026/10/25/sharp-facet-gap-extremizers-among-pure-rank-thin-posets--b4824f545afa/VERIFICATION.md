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

For each finite nonempty pure graded P with rank sizes 1 or 2, h ranks and m=n-h doubleton ranks, use standard irredundant facets: gap G=n+number_of_maximal_chains-(min+max)-number_of_Hasse_edges. Adding a missing adjacent-rank cover u<v creates L(u)U(v) chains and one edge; the gap increases by L(u)U(v)-1>=0. Full layered completion has rank indicators x_i in {0,1} and G=2^m-m-1-sum_i x_i x_{i+1}. The minimum adjacency among m ones in h slots is max(0,2m-h-1), giving the fixed h,m formula and sharp constructions. For h>=3 any optimal incomplete cover is impossible: if the profile has adjacent doubletons then complete all but one missing cover, and its last insertion creates 2^(m-2) chains, gain 2^(m-2)-1>0 for m>=3; optimal m<=2 has no adjacent doubletons. h<=2 all gaps vanish. Optimize m<=floor(n/2) to obtain even M_n=2^(n/2)-n and odd M_n=2^((n-1)/2)-n+2, with exactly the stated complete-layer equality classes for n>=5. Independent binary rank-profile checks covered 62 cases. Source verifier enumerates 206,516 pure cover arrangements to h=7, inspected as code but not independently replayed end-to-end. These are not universal proofs.

## originality

PASS

Qualified PASS for the exact two-parameter facet-gap maximum and complete equality classes for pure rank-thin posets. Stanley facet formulas, Bhandari et al. gap constructions, Fourier general local gap formula and small-gap cases, and Ahmad et al. rank-poset f-vector monotonicity are prior work. Their inspected statements do not yield the global height-and-size extremum directly, though Fourier full text could not be read; a possible stronger implication in that paper remains a priority risk, not automatic failure.

## value

PASS

This is a motivated sharp classification of a natural difference of facet counts of two classical polytopes, establishing both an explicit fixed-height/order extremum and a parity-dependent fixed-size extremum with all maximizers. Completing cover graphs and minimizing doubleton adjacency provide a structural extremal explanation, not merely enumerating small cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
