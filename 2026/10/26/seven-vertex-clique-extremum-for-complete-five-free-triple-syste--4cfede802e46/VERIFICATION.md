---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

On exactly seven vertices, K5^(3)-freeness is equivalent to a missing-triple family M covering every five-subset. Since no clique size>=5 is allowed and every 0,1,2-subset is a clique, c(G)=1+7+21+(35-t)+(35-s)=99-t-s where t=|M| and s counts 4-subsets containing a missing triple. Every valid nonempty M may be relabelled to contain one fixed triple; the certificate exhausts combinations of the other 34 triples for each t<=8, with case counts C(34,t-1). I read both source enumerators and implemented an independent compiled C++ verifier using binary-mask rather than source lexicographic enumeration. It examined exactly 1,34,561,5984,46376,278256,1344904,5379616 normalized families for t=1..8. Covering counts are 0,0,0,0,245,15300,235992,1861744; minimum feasible four-shadows for t=5,6,7 are 17,19,20. Every 8-family (covering or not) has shadow >=16, so every larger family contains an 8-subfamily and by monotonicity has t+s>=8+16=24. Thus feasible t<=7 have t+s>=22, and only t=5,s=17 ties. The independent code identified precisely five normalized minimizers and verified each equals the set of triples internal to a 3+4 partition, with 35 total distinct labelled templates. Each balanced partition has t=5,s=17, covers all 21 five-sets and gives c=77; no other equality cases. This establishes the whole finite theorem by exhaustive bounded enumeration plus an analytic monotonicity extension. A compiler/build is required to reproduce the C++ certificate, but the finite case space, loops and representation were independently checked; no timeout, sampling, or log-only inference.

## originality

PASS

Best-knowledge PASS for the exact n=7 total-clique extremum and all equality systems, not for the known extremal construction, the T(7,5,3)=5 covering number, or the general large-order theorem. The 1994 Boyer–Kreher–Radziszowski–Sidorenko paper already classifies minimum (n,5,3) covering systems for n<=13, so the minimum missing-family size is prior work; the separate four-shadow optimization, global t>=8 exclusion, and 77-clique uniqueness are not shown by the sources materially inspected. Full 1994 text could not be read from RIT (403)/ResearchGate, and authorized institutional retrieval reported disconnected VPN: possible implicit prior coverage is a real residual risk, not a claim of noncoverage. The 2026 Chen–Deng–Hou–Liu–Zhang Theorem 1.5 asserts the same extremal construction for sufficiently large n with unspecified n0 and its proof fixes large constants; it does not imply n=7. Frankl–Gryaznov–Talebanfard Conjecture 14 is conjectural and yields only floor(78.765625)=78 at (n,r,ell)=(7,3,4); its Theorem 13 applies r>= (1-1/d)n, which fails here (4<14/3). Bodnár 2023 gives asymptotic generalized Turán density, not this exact seven-order total. The published six-vertex result establishes 49 and its own equality class, without seven-vertex implication. Genuine named searches plus full accessible primary comparisons support a bounded originality judgment, not a priority guarantee.

## value

PASS

The forbidden K5^(3)-clique count is a natural extremal objective from Frankl–Gryaznov–Talebanfard's conjecture and Chen et al.'s eventual sharp theorem. n=7 is the first odd order following a published exact n=6 determination; seven is not an arbitrary slice when testing the balanced 3+4 optimizer and finite parity behavior. The new exact bound 77 and complete 35-labelled equality classification are natural finite-order facts not mechanically obtained from the known T(7,5,3)=5, because the full upper-four-shadow score and families with t>5 must also be controlled. A future extremal-hypergraph study of exact finite thresholds or small forbidden-clique catalogues can use the precise n=7 base case and equality classification. This is a self-contained finite theorem, not a claim about general n or global conjecture resolution; correctness of code or novelty alone did not decide value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
