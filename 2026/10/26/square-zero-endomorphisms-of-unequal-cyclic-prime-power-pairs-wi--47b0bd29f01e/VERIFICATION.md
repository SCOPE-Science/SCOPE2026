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

Reconstructed all seven source files, canonical Git tree and complete proof. Each group endomorphism has the unique mixed-modulus matrix T=((u,v),(p^(b-a)w,z)); squaring yields four necessary and sufficient congruences with the proper two row moduli. For a=1, u=0 and the valuation of z² distinguishes the t=vw=0 fiber from the possible odd-b nonzero t; resulting 2p−1 and (p−1)² terms give both formulas. For a=2, the exact Z/p² product-fiber count (zero p(3p−2), valuation-one 2p(p−1), unit p(p−1)) and α=u/p split yield all b≥5 cases. Separately reconstructed b=3 and b=4 where z need not vanish mod p² and α can be forced to −z/p; the algebra gives the advertised boundary expressions. All p, including 2, and every b>a are covered; no assertion for a≥3. Direct generator-image enumeration independently matches 40 bounded (p,a,b) instances, all 87 residue product fibers for p=2,3,5,7 and five symbolic simplifications. Universal truth follows from the p-adic case analysis, not these finite checks.

## originality

PASS

Best-of-knowledge original exact enumeration for two natural mixed cyclic p-group families. Full primary comparisons distinguish general matrix parametrization, nil-clean ring properties, and existence of image-equals-kernel maps from the precise square-zero multiplicity. Complete published-result comparisons of fixed-point automorphism layers and dual-number matrix loci do not imply the claimed four parity-specific formulas. An unknown broader nilpotent endomorphism census remains a real historical risk; absence from searches is not novelty proof.

## value

PASS

The cardinality of {T∈End(G):Im T⊆Ker T} is a natural invariant measuring two-step collapse in a finite abelian group, important for studying the nonunit endomorphism monoid. Its complete value for the first two unequal shorter cyclic exponents, for all primes and arbitrarily large longer exponent, is not a rename of an automorphism count or a known table. The nontrivial new feature at a=2 is the p² product-fiber stratification and low-boundary anomaly; the parity-sensitive Q(a,b+2)=pQ(a,b) is a uniform structural law. The exact formulas stand as a useful count without claiming a general a≥3 classification or downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
