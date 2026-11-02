---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The normal form of stylic elements is nested strictly increasing N-tableau rows with strictly increasing row minima; generator occurrence iff moved point, so R1=S. Entries in higher rows may only be starts of maximal consecutive support runs, for otherwise their earlier occurrence and a bottom-row predecessor give a double decrement, contradicting one-step image. Conversely upper entries only at run starts cannot cause a double decrement; d1 cannot enter R2 by minimum order. Heights of the b run-start letters with h1=1 are exactly restricted-growth strings, bijective with set partitions, with maximal height equal to number of blocks/rows. Counting support runs via 2b gap endpoints gives binom(n+1,2b), and nonadjacent supports give idempotents. Independent enumeration of ALL N-tableaux through n=8, including 21147 distinct n=8 tableaux, evaluated the quotient by raw generator compositions and matched every fiber and row count. Universality follows from the structural bijection, not enumeration.

## originality

PASS

Abram–Reutenauer proved N-tableau normal forms and total Styl_n cardinality Bell(n+1); Volkov established the Catalan quotient. Stein (October 2026) proved a full-core criterion for general Catalan fibers. Its full-core membership classification does not state the special one-step fiber Stirling profile or the b-run Bell cardinality; extracting it requires the restriction on allowable upper rows and the explicit restricted-growth map.

## value

PASS

The fiber multiplicity of a natural quotient is a meaningful invariant, particularly within the intrinsic 2^n one-step endomorphisms. A canonical partition bijection and stratification by row number reveals multiplicities of idempotent maps and supports, giving exact information not supplied by general membership testing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
