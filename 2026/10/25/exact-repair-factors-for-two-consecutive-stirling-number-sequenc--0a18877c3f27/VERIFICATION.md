---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The Dold divisibility for all n reduces to prime-power local congruences with coprime complementary t. Integer powers settle primes outside 2,3,5. For exceptional primes the weighted power differences normalized by p^r must vanish mod p^h (h=8,3,1); period P=(p−1)p^h in t for units, high-t divisibility for p|j, and p-adic lifting Q_{r+1}≡Q_r mod p^{r−1} for r≥h+3 reduce every index to a finite complete certificate. Independent integer modular arithmetic checked 6752 bounded cells for k12/13. Dold denominator witnesses have lcm 13860, establishing minimality; Stirling growth yields positive Mobius transforms.

## originality

PASS

Miska–Ward (2021) and OEIS A341617 already record both values 13860 as hypothetical finite-check candidates. The asserted contribution is an all-positive-index proof using verified finite prime-power periods plus an explicitly justified lifting argument, not numerical discovery.

## value

PASS

Closing two explicitly conjectural entries in the periodic-orbit realizability table is a meaningful arithmetic result. The proof identifies full finite-to-infinite p-adic certificates and sharp denominator witnesses; the fact is useful even without a formula for all k.

The dated certificate retains the supplied scientific assessment, sources and limitations.
