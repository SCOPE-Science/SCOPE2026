---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For active sets A⊆L,B⊆R, F(A,B)=(f(B),g(A)), where each one-sided map sends ∅ to whole part, matched singleton {i} to {i}, and other subsets to ∅. Because p,q>=2 the image consists of the (k+2) symbols ∅,whole,{i} per side and F² is identity on this image, giving F³=F and exact fixed/2-cycle counts. Each recurrent state has explicit predecessor fiber h_q or 1 in its first coordinate times h_p or 1 in the second, h_p=2^p-k-1,h_q=2^q-k-1. Summing fibers of the phase(s) proves all basin sizes and the global sum 2^(p+q); boundary (2,2,2) and k=0 separately hold. The giant basin ratio is 1-(k+1)(2^-p+2^-q)+((k+1)²+1)/2^(p+q), proving uniform limit. Independent actual graph-level neighborhood enumeration checked all 32 cases with 2<=p,q<=4; source supplies larger checks. Finite checks support, do not substitute for exact map reduction.

## originality

PASS

Open-NOR on graph joins, F³=F and the general fixed-state link to independent sets are known and not claimed new. The explicit k-dependent orbit creation, all individual basin fibers and uniform giant-basin limit were not established by inspected general graph Boolean dynamics literature, subject to an uninspected full 2011 fixed-point paper.

## value

PASS

The exact attraction-basin spectrum detects a nontrivial phenomenon: deleting k disjoint edges creates quadratic numbers of oscillations while almost every initial configuration still enters one universal 2-cycle. It is a motivated complete family classification beyond qualitative period bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
