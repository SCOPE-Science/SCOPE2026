---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The submitted support note supplies the missing six-cell section-mask argument that Khetan's prime-square proof does not cover. For a rational kernel-line denominator d, factor d=βD where D is 2,3-smooth and gcd(β,6)=1; the parent dilation and common-zero lemmas then give a common nontrivial root of every section mask, ruling out singleton sections. The only six-point section profiles are (3,3), (2,4), and (2,2,2). The parent polynomial/fibre lemmas plus the submitted unequal-prime product argument handle two independent section directions: a 2-by-2 grid cannot contain six cells, the 2-by-3 case is the full product and admits a periodic orbit point, mixed (2,4) cases violate grid divisibility, and two (2,2,2) directions yield the K3,3-minus-matching incidence graph whose three two-term root equations multiply to a contradiction. Thus a transverse pair of infinite-common-zero directions forces the product case, where the original tiling is periodic; otherwise there is at most one infinite-common-zero direction. Finite-exception kernel directions need not be parallel. Khetan's Theorem 3.16 finite spectral cover and Theorem 3.18 Case (2) orbit-limit extraction then apply with cardinality 6: the only cardinality-specific step there is a coprimality claim, here gcd(α,6)=1. The resulting limit is an F-tiling in the orbit closure and is 1-periodic. I read the full relevant primary sections including the previously inaccessible end of Theorem 3.18's proof; this assessment is not an inference from the abstract or result statement alone.

## originality

PASS

Khetan explicitly leaves the six-cell case open while proving prime-square cases and providing an eight-cell counterexample. The submitted argument contributes a new mixed-prime six-cell root/profile and grid-incidence exclusion, so the conclusion does not follow by simply putting p=2 or 3 in that paper. The later Tan–Zhang existence of some fully periodic complement for 2q tiles has different quantifiers and appeared after the September 17 finding: it does not guarantee a periodic point in every given tiling's orbit closure. Current corpus and literature checks found no equivalent or stronger prior orbit-closure theorem for all six-cell tiles.

## value

PASS

This closes the first composite non-prime-power cell count left open in the decisive 2026 periodicity paper while preserving the difficult 'every given tiling has a periodic orbit-limit' quantifier. It isolates a reusable mixed-prime section-profile and incidence obstruction and sharpens the known contrast with the eight-cell counterexample. The result has standalone mathematical value beyond an expository rearrangement of a cited theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
