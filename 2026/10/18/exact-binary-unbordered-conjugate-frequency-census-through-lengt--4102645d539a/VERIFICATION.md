---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The frozen FKM recursion enumerates binary necklaces once; its terminal period p is the size of the labeled rotation orbit. For p<n the word and all its rotations are proper powers and hence bordered. For p=n the count of unbordered starting positions is constant on the orbit, so adding n to its bin is correct. Testing borders only through floor(n/2) loses none: a longer border gives period d=n−b<n/2, and using the largest positive multiple of d less than n gives a border of length at most d. An independently written direct exhaustive computation visited every labeled binary word at every length 1–28, without orbit weights. For each border length b it located runs of b consecutive cyclic equalities between bits at distance b, marking the corresponding rotation starts at the shifted positions. Counting unmarked starts reproduced all 29 CSV columns in each of the 28 rows, including every cell at lengths 26–28. At n=28 the first and second raw sums are 2,012,861,088 and 15,596,094,136; division by 2^28 and subtraction of the squared mean yield the stated exact mean and variance. The highest nonzero index is 13 with 5,040 words. Row totals, zero bins and first moments agreed with independent identities. At n=1 both words are unbordered; for n≥2, a nonprimitive word has none and the lexicographically least and greatest rotations of a primitive word are distinct unbordered words, consistent with the missing j=1 bin.

## originality

PASS

The supported distinct claim is the full labeled-word frequency census through 28, including the second moment and extremal multiplicity, not the maximum value 13, the known first moment, or the absence of singleton fibers. Inspected related results cover support, maximum, zero count, first moment, or composition-restricted fibers. None supplies or mechanically determines the remaining unrestricted table at this cutoff on the evidence inspected.

## value

PASS

The statistic is motivated by the established extremal and mean problems for unbordered conjugates: they leave open how typical or rare any number of unbordered starts is. The table measures this variation across all labeled binary words at 28 consecutive lengths. At n=28 alone it distinguishes a central bin of 73,564,148 words at j=8 from just 5,040 of 2^28 words at the known maximum. A researcher studying dependence between rotations, exact moments or near-extremal populations can use these actual frequencies; neither the first moment nor a low-weight slice supplies them. The bounded cutoff is a reproducible complete census, not a substitute for an asymptotic distribution theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
