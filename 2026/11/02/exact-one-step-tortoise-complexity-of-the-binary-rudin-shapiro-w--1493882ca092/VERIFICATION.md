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

The constant-length morphism has exactly eight adjacent two-letter factors and covers any length-L language via the image of all two-blocks under a power 2^j>=L. The finite certificate establishes eight length-five four-letter left-special prefixes with exactly {ac,db} two-letter contexts and injective binary coding on 56 length-eight factors. This promotes binary left-special factors of length m>=10 to both 01z and 10z contexts, of which exactly 8 exist using Berthé p(m)=8m-8. At n=12, exhaustive image classification gives only eight doubletons of type 01z/10z; no 00000 factor and a fixed-prefix inheritance argument exclude all other longer collisions, so rho(n)=8n-16 for n>=12. Independent direct initial binary generation yielded stated rho(1..12) and n=16,24,32. Binary and morphic conventions match the primary source.

## originality

PASS

Campbell and Rampersad introduce the tortoise invariant and bound its long-length deficit for linearly complex binary words with bounded 1-gaps. Their concrete formulas analyze Thue–Morse and paperfolding; Rudin–Shapiro is mentioned only as background to another complexity theory. Berthé established p(n)=8n-8 but did not evaluate tortoise images. The persistent exact deficit eight and threshold twelve are substantive special-context new computations with an infinite inheritance proof.

## value

PASS

Rudin–Shapiro is a canonical automatic sequence, and tortoise quotient complexity is a recently introduced nontrivial equivalence invariant. A sharp eventually linear formula, exact collision count and threshold reveal stability across all lengths, not a finite tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
