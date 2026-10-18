---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Direct chip-firing at one grain per occupied vertex transports each binary grain to its successor, so the entire list of firing supports is S+t modulo n (no transient). Because gcd(n,k)=1, multiplication by k^(-1) modulo n is a permutation taking R_a={a,a+k,...,a+(L_a−1)k} to exactly L_a successive residues. Its translated faces give the complete circular-interval nerve N(n,L_a−1), and complementary supports likewise N(n,n−L_a−1). Verify Adamaszek et al Theorem 3.6: when (k−2)/(k−1)<r/n<(k−1)/k one gets S^(2k−3), with equality at lower endpoint producing wedge of n-r-1=L_a copies of S^(2k−4). Algebra r/n>(k−2)/(k−1) iff q+s>(1+δ_a)(k−1), precisely T_a>0; equality similarly. Independently enumerated all eight support translates and their modular images for n=8,k=3,a=0,1,2: interval facet equality holds, T=(0,0,2). Full 2014 theorem, not finite homology, proves all parameters and integral homotopy types. The R_a result needs k<n/2 style bound L_a−1<n/2, true for q≥2 and n=kq+s.

## originality

PASS

Original 2026 Riihimäki–Smith explicitly states disconnected k-point residue support in Lemma 3.17 and a complementary S^(k−2) guess in Conjecture 3.18. Both are contradicted on coprime wrap-around parameters, including n=5,k=2; so those statements cannot cover the correction. The older general circular-arc nerve Theorem 3.6 ALREADY covers the homotopy classification after a simplicial isomorphism; this is credited fully and limits novelty to the specific avalanche-to-nerve identification and sharp arithmetic transition. 2026 Theorem 3.21 concerns consecutive firing support and has a different conversion premise; checked full relevant original passages. Semantic published database ranked only this same current result and unrelated directed complexes. Unindexed applications remain possible.

## value

PASS

Fixes concrete erroneous unrestricted statements in a new sandpile-topology model on an infinite coprime parameter family and identifies the exact mechanism (finite interval residue classes wrap on the cyclic vertex group). The n=8,k=3 representative-dependent topological split is a meaningful sharp boundary of a classification, not a small isolated counterexample or a restatement of the nerve theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
