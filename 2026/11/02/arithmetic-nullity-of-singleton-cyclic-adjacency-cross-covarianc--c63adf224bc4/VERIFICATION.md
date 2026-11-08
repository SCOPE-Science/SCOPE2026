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

Independently reconstructed deletion of a designated singleton and contraction of a pair: each marginal B_(n-1)/B_n, disjoint joint B_(n-2)/B_n and incident joint zero. Thus the exact rank-one-minus-two-permutation matrix follows entrywise. Strict Bell log convexity gives r>p^2, while Asai--Kubo--Kuo normalized Bell ratio bound r/p^2<=n/(n-1) makes the constant eigenvalue (n-2)r-np^2<0. Fourier diagonalization of P_d gives -r(1+exp(-2πimd/n)) at m!=0; zero iff md=n/2 mod n, having exactly gcd(n,d) solutions when n/gcd even. Independent exact partition enumeration and rational-matrix rank verifies all n=3..7 and displacements; it is not a proof for general n.

## originality

PASS

Callan 2005 establishes aggregate singleton/adja equality in marginal distribution; Munagi 2016 gives circular-displacement total-adjacency bijections; Asai--Kubo--Kuo 2001 supplies the Bell ratio inequality. Those are properly treated as prior ingredients. None inspected establishes local I_i--A_j cross covariances nor its Fourier nullity and displacement rank structure. An unindexed general exchangeable-partition association scheme could imply this, which remains a bounded risk.

## value

PASS

The covariance matrix of two canonical local statistics on uniform set partitions is a natural second-order invariant. Exact support overlap structure, strict sign reversal between incident and disjoint sites, and arithmetic gcd/parity rank-nullity classify dependence across all displacements, yielding information not present in equal marginal distributions. The finite n=6 ranks 5,6,3 demonstrate genuine displacement-dependent structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
