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

Conditioning on the inside value set and ordered outside of a consecutive block leaves exactly the internal inversions as the variable Mallows weight. The increasing endpoints are consecutive in internal rank precisely for an up-cover; their contribution is d−1 inversions, with d possible rank pairs and [d−1]_q! for the remaining internal entries. This yields the exact all-n, all-gap enumerator, including d=1 and d=n−1. The frozen wording incorrectly suggests each gap polynomial has actual degree N−1. Removing the two q-integer factors and including q^(d−1) gives its degree N−d and minimum exponent d−1; N−1 is the ambient reflection grade and actual degree only for the total and d=1. The repaired finding states both facts explicitly, consistent with the padded-vector test. The coefficient identity was separately checked at every gap for n=4 and n=8; n=8 gives 341136 total at q=1. The reciprocal relation for the mean strictly dominates q>1 by 1/q; its derivatives at 0+ and 1 have opposite strict signs for n≥4, so compactness on [0,1] gives the claimed optimizer location, not uniqueness. Geometric bounds give linear order for fixed q≠1; the exact uniform sum is (n+1)H_n−2n. These checks validate the corrected statement.

## originality

PASS

The repair credits that the boxed-cover event is known and that its exact uniform probability by gap is already published. The retained result is the nonuniform lower-inversion-rank count at each position span and the induced full Mallows mean with distinct optimizer and growth laws. The inspected catalogue and primary comparators do not count this rank-refined statistic or imply those nonuniform statements without the new endpoint-inversion enumeration. Rank reflection itself is not a separate novelty claim.

## value

PASS

The low-endpoint rank and position-span census refines a natural degree statistic studied in strong Bruhat order, and gives an exact first moment throughout the full Mallows family. It distinguishes the uniform law’s growth and shows that the uniform parameter does not maximize the finite-n mean. Those are consequences of nonuniform information unavailable from the already known uniform gap counts, rather than isolated finite checks or mere parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
