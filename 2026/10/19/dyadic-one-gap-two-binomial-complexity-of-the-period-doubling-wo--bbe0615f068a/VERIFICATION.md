---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

At length 2^m a window contains exactly one multiple of 2^m. The other valuations are fixed by residue, and both exceptional bits are realized for each start residue by taking a suitable positive multiple. The resulting two cyclic words have different weights; one is doubled with weight equal to 2 modulo 4, forcing least cyclic period n/2, and the other has odd weight and least cyclic period n. With no adjacent cyclic ones, subtracting adjacent counts from all scattered counts reduces the profile exactly to (weight, T+first bit, first+last bit), T the unrestricted 01 count. Rotating d places changes T by nB-kd with B the weight crossed. For the doubled word this is always even, so equal T+first bit requires d a multiple of n/2. In the primitive orbit, 3k=n±1 forces distinct collision shifts to be ±3. Checking shift +3, even m would require 1 to 0 as initial bits and makes the endpoint sums different; odd m requires 0 to 1 and equal endpoint sums exactly at cyclic 10101. Pairs are disjoint since each start has a unique end, with different initial bits. Odd m centers have valuation odd and at least three (including cyclic center n), giving the geometric sum (n+4)/12. The n=4 and n=8 boundary cases are included.

## originality

PASS

The observation statistic itself is known, the ordinary dyadic two-binomial injectivity is known, and the cyclic-orbit description has documented overlap. None of those results gives the exact coincidences after forbidding adjacent selections. The inspected same-statistic exact result uses Thue–Morse, and the inspected same-word Abelian collision result uses contiguous counts. The supported distinct contribution is the dyadic one-gap class count and explicit shift-three collision law for period doubling.

## value

PASS

For a canonical automatic word the result measures exactly how excluding neighboring selections changes factor distinguishability at the substitution scales: no information loss at even exponents and an explicit infinite set of isolated two-way ambiguities at odd exponents. The shift and motif classification identifies the ambiguous factors rather than just giving a finite table or a count, and this is not implied by ordinary binomial injectivity or orbit enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
