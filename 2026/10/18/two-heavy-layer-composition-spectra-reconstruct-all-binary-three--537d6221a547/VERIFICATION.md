---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

With w=0^a 1 0^b 1 0^c 1 0^d, exact disjoint factor-boundary enumeration gives P3=t^(b+c+3)S_a S_d and P2=t^(b+2)S_a S_c+t^(c+2)S_b S_d. min degree and max degree of P3 recover b+c and total word length; the coefficient staircase of normalized P3 recovers unordered outer gaps {a,d}, and min degree of P2 recovers min(b,c), hence unordered interior gaps {b,c}. At most two reversal-orbits remain; comparing them gives nonzero Δ=(S_a-S_d)t²(t^b-t^c)/(1-t) if a≠d and b≠c. Thus all boundary cases including zero gaps are covered. Independent exhaustive direct substring counts for all words with exactly three ones of lengths 3..16 confirm no non-reversal collisions, but arbitrary length is proved by the polynomial argument. Four-one collision pair 01001101 and 01101001 is prior art and can be independently checked.

## originality

PASS

Best-of-knowledge: Neither exact same reduced map nor stronger result implying its injectivity up to reversal was identified. Full-data reconstruction techniques are background ingredients, while noncollision after deleting entire layers is a separate statement. Source reading, explicit four comparisons and priority risks detailed below.

## value

PASS

Recovering the full sequence from only two filtered heavy composition layers is a natural sharp sparse-marker information threshold. The finding separates the minimal sufficient high-weight factor data from full composition spectra, and the four-marker obstruction proves a meaningful precise boundary. It is useful for string reconstruction with partial observations, not an arbitrary binary-word census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
