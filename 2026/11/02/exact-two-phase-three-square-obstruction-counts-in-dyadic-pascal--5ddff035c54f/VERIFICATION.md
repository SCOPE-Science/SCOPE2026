---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Put N=2^r and k=2^t u with u odd. In the product for binom(N−1,k−1), all factors 1−N/i are odd, and for r≥3 only i=N/4,N/2,3N/4 can differ from 1 modulo 8. They give successive factors 5,7,5, hence cumulative products 1,5,3,7 with the block indexed by floor((k−1)/(N/4)). Using binom(N,k)=(N/k)binom(N−1,k−1) and u^(−1)=u modulo 8 gives valuation r−t and exactly the stated signed odd part. The three-square theorem then gives both required conditions. Write s=r−t: only even s≥2 qualify. For s≥6 each of the four blocks is balanced among odd u modulo 8 and contributes 2^(s−5), since the sign is constant at fixed t even when t=0. The block edges are not eligible odd u for s≥4. For s=4 and t>0, exactly u=1,5,11,15 qualify; for s=4,t=0 none qualify. For s=2 and r≥3 the two u=1,3 lie on block edges and use q=0,2 respectively, so both qualify. Rows r=1,2 and both endpoints check directly. This gives the two starting values 0, the next two values 2, and for r≥5 the sum 6+sum_{s=6,8,…,2 floor(r/2)}2^(s−3)=(2^(2 floor(r/2)−1)+10)/3. The even and odd normalized limits are respectively 1/6 and 1/12. The supplied verifier was inspected but not executed; it compares direct integer rows through r=13 and residue-only counts through r=20. Those checks are finite, while the valuation and block argument proves the full claim.

## originality

PASS

Pass on the supported distinct result: the dyadic binomial position test together with the full exact row counts and alternating densities. Neither classical three-square obstruction nor general binomial congruence methods alone give these counts without determining the residues, handling the low-valuation block sizes and summing. The closest available catalogue comparisons have different sequences or statistics. Some highly relevant older papers could not be compared in full; this limitations-qualified pass is not a priority certification.

## value

PASS

Dyadic rows are a natural binary test family for the classical Pascal representability problem. The row census answers a precise distribution question, and the different limiting densities show that even on powers of two there is no single limiting row proportion. The per-position criterion and boundary counts explain that phenomenon and are usable without building the large binomial coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
