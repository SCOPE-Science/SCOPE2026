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

The three degree-five factors vanish at β, β³ and β⁵, respectively, with all their distinct Frobenius conjugates; these orbits include the required six roots. The product 0x8faf has degree 15, so the labeled code consists bijectively of the 2^16 nonwrapping products h g with deg h<16. Independent replay: python3 /workspace/branches/independent-04.py /workspace/source/2026/10/19/exact-cyclic-b-symbol-spectrum-and-sharp-mds-transition-of-the-b--bf34348efdf4/SPECTRUM.csv. It derived the product, exhausted its multiples, counted each start by backwards scanning its maximal zero length in a doubled circular word, and matched every CSV coefficient at all 31 widths. Even though the scan starts from the high-degree end, reversing the circular order only permutes the sets of positions of length-b arcs and preserves the count of zero arcs. The minima matched (7,11,15,18,20,21,22,23,24,25,26,27,28,29,30,31) followed by 31, giving equality only at widths 5–16. The replay verified all fourteen complementary-support ranks by explicitly forming each XOR span and finding 8192 elements. Cyclic shifts and deg g=15 rule out 16 consecutive zeros; the rank test rules out two disjoint 9-arcs of zeros. For a unique maximal long run of length ℓ, rotating its complement into positions 0 through 30−ℓ gives a multiplier h of degree 15−ℓ with both endpoints 1. There are 1 or 2^(14−ℓ) such multipliers, and 31 choices of run position without duplication. The ℓ−b+1 zero windows give the claimed coefficient law, also independently checked against the replay through width 31. Frozen supporting programs were read, not run. Minor portability issue: the frozen Python checker uses int.bit_count (Python 3.10+), despite claiming Python 3.8+, and the C++ checker uses a compiler builtin. The independent standard-library replay succeeds without either assumption.

## originality

PASS

Credit is confined to the exact intermediate-window coefficients, the sharp transition into Singleton equality, and the explicit geometric tail and support obstruction at widths 9–15 for this code. The code parameters, Hamming row, broad cyclic-code stability and full-weight plateau for widths at least the dimension are prior. The inspected earlier sources do not give or imply the distinctive intermediate-width results.

## value

PASS

This natural small BCH code and the primitive cyclic order are independently identified in coding theory. Its complete weight laws at intermediate read widths answer how overlapping windows distinguish nonzero words, not just the Hamming minimum. A researcher can use the exact MDS onset and coefficients as a benchmark in b-symbol coding, while the structural proof explains geometric multiplicities rather than merely reporting a brute-force count. No new high-width stability theorem or infinite-family extension is needed or claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
