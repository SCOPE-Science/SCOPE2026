---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
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

The proof reduces first modulo coordinatewise commutators, then analyzes the abelian kernel extension. The exact T-module sequence 0 to K to A^T to T to 0 and Shapiro's H1(T,A^T)=0 give the coinvariant extension by T tensor T; the transgression is the alternating subgroup, canonically the exterior square. Using |T tensor T|=|T| |exterior-square T|^2 gives |G^ab|=|R^ab| |T| |exterior-square T|. The compensation argument also correctly places every coordinate copy of R' in G'. A fresh small-case check for R=T=(C2)^2 gives abelianization order 32, matching 4*4*2; this computation is corroborative, not the proof.

## originality

PASS

The parent paper defines exactly this kernel-wreath group and proves regularity, quotient preservation, iteration and simplicity, but its full text contains no abelianization or exterior-square formula. Fresh Resultary and targeted wreath-product/abelianization searches returned the audited record as the exact hit and no earlier theorem that implies this kernel formula for arbitrary finite abelian target T.

## value

PASS

This is an exact natural invariant of a newly introduced group construction. It distinguishes cyclic from noncyclic target steps through a genuine exterior-square correction and controls how multiplicative abelian quotients grow under iteration; it is neither an arbitrary slice nor a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
