---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Used the complete multipartite matrix-tree product τ(K_(b1,...,br))=N^(r−2)Π(N−b_h)^(b_h−1). Force one leaf: choose any of n−a_i external neighbor vertices and a tree of G−u; force two leaves in different parts: for n>=3 delete both, choose (n−a_i−1)(n−a_j−1) neighbors in surviving core. Exact ratio simplification gives p_i and p_i p_jQ_ij, accounting for singleton and disconnected-core boundary cases and n=2 separately. Every Q factor is <=1; r>=3 has strict first factor <1. Expanding logarithms at positive limiting proportions gives the claimed n^-1 correction and asymptotic. Independent full Prüfer enumeration across 10 multipartite sizes (n<=7, counting up to 2800 valid trees per case) with exact rational leaf moments reproduced the formulas and covariance signs, including cases [1,1,1] −1/9, [2,2,2] −33/256, [3,2,2] −1377/12250. Finite checks are not used as proof at all n.

## originality

PASS

Eğecioğlu–Remmel 1994 proves the spanning-tree product and part of one-vertex leaf expectation, all credited. Remmel–Williamson 2002 develops degree-marked generating functions encoding much of the finite joint law in principle. The universal strict negative covariance sign for every non-bipartite part structure and its sharp n-asymptotic coefficient are the new explicit dependence conclusion, not a new tree enumerator.

## value

PASS

A qualitative sign theorem valid for every positive part vector (sharp r=2 equality boundary) and exact asymptotic coefficient for natural class-stratified degree-one statistics in uniform spanning trees. The sign/scale information is not a trivial restatement of the classical enumerator and can be used to study multipartite dependency and fluctuations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
