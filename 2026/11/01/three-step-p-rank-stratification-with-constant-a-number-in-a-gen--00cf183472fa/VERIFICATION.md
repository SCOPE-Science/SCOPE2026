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

Separability is equivalent to b(b^3+a^5) !=0 by derivative F_prime=x(5x^3+2a), and the 6 totally ramified branch points yield genus4. For basis dx/y, dx/y^2, x dx/y^2, x^2 dx/y^2, characteristic7 coefficient extraction gives displayed H with zero first row/column and rank2 lower block for every b!=0, giving a-number2. Normalizing b=1 with u^5=a^5/b^3, the semilinear second iterate uses H^(7)H for matrices of seventh powers; independently expanded every relevant coefficient and all twisted second-iterate 2x2 minors in F7[u]. Their gcd is u^4(u^10-1), and the excluded singular u^5=-1 leaves exceptional u=0 and u^5=1 only. Exceptional actual Cartier stable ranks are 0,1, generic stable rank2. The exact symbolic minor identity establishes geometric loci over F7bar, not just tested finite-field points.

## originality

PASS

Best-of-knowledge originality of the complete final claim after explicit statement/implication comparison; qualified by documented priority risks. The precise gcd u^4(u^10-1) of twisted minors and stable Cartier ranks are new computations relative to these sources, not a direct stated corollary.

## value

PASS

A complete natural one-parameter-after-scaling arithmetic stratification of cyclic trigonal genus4 curves, showing constant a-number2 despite three distinct p-rank strata. The smooth intermediate rank-one stratum is a concrete nontrivial geometric locus. Those invariants are relevant to Jacobian isogeny/arithmetic geometry and are not asserted for the whole moduli space.

The dated certificate retains the supplied scientific assessment, sources and limitations.
