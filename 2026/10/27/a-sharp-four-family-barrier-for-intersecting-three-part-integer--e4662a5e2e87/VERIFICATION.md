---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

## Direct mathematical verification

The proof in `RESULT.md` shows that distinct fixed-sum triples share at most one distinct part value. Any nontrivial pairwise-intersecting family has three members with three different pairwise intersection values. The fixed-sum identities rule out two different additional members, whether a triangle member has three distinct parts or a repeated part. This proves the size-four bound for all positive sums without relying on computation.

The explicit four-member witnesses have sum \(n\), satisfy pairwise intersection, lack a shared common value, and are pairwise different for all \(n\ge8\). Deleting the centered part gives a bijection from a full star to partitions of the remaining sum into two positive summands, proving the exact star cardinalities. Orders \(3\) through \(8\) are listed/treated separately in the proof.

## Reproducible finite checks

Run `python3 verify.py` with Python 3 and standard library only. It performs a complete Bron–Kerbosch maximal-clique enumeration on the graph of partitions for every \(3\le n\le20\). It checks the exact maximum-family size, the nonstar bound, equality families and center labels for \(11\le n\le20\), and explicit constructive witnesses for \(8\le n\le100\).

The executable run output is embedded as `verification_output.txt` and ends in `VERIFY_OK`. No sampled computation is substituted for the infinite proof. No independent or external audit has occurred.

## Limits

This certifies the supplied self-review finite and symbolic checks, not novelty by search alone. It does not address partitions with other numbers of parts or higher intersection demands.
