---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Rebuilt all inputs S_n with no 11, all DISTINCT one-coordinate deletion shadows, including endpoint positions and possible outputs with 11. Source artifacts/certificates.json provides every short code, n<=5 transversal, n6/n7 exact rational primal/dual pair at 4 and 6, and weighted conflict cliques totaling 15/4 and 23/4 that cover each eligible input. Independently verified all seven explicit certificate instances in integer-scaled rational arithmetic: all constraints, every clique pairwise shadow intersection, every cover weight, disjoint code shadows, and exact totals. Thus A_6<=floor(15/4)=3 and A_7<=floor(23/4)=5 while exhibited codes attain; fractional strong duality from matching primal/dual certs. Separately calculated all seven integer and LP optima via independent scipy optimization, matching all profiles. Proof is genuinely complete finite certificates, not only solver log.

## originality

PASS

Kulkarni–Kiyavash 2012 uses hypergraph fractional transversals for deletion codes and constrained-source treatments but with different run-length endpoint conventions; its general results yield far looser upper estimates (121/15 and 73/6 for n6,7 as cited), and the published numerical unrestricted tables do not imply the stated Fibonacci-language LP/ILP separation. Resultary published unrestricted length-six single deletion maximum 10, different from constrained maximum three.

## value

PASS

This locates the first integrality failure of the natural deletion-shadow packing relaxation for a standard Fibonacci constrained language and gives exact dual plus weighted-clique certificates for two first-gap lengths. First finite cutoffs are mathematically motivated by comparing a canonical relaxation to code optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
