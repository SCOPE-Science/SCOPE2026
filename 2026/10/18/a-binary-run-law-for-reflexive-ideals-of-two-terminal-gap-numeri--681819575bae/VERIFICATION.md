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

For m>=3 the conductor is 2m and sums of positive semigroup elements reach the conductor. A normalized ideal is determined by the gaps it adds, and closure is tested by adding semigroup members to those gaps. In the one-gap family every included low gap x forces c=2m-1 via c-x in the semigroup; once c is included every low subset is allowed. Pairing complementary integers about c proves symmetry and the Frobenius-witness argument gives biduality. In the two-gap family, adding only b=2m-2 permits just the optional low gap 1 because c-x belongs to S for all other low x. Adding only c permits just the optional m-1 because b-x belongs to S for all smaller low x. With neither, no low gap is allowed, and with both, every low subset is allowed. The classification includes the endpoint m=3, where the positive semigroup block below the conductor is {3}. For I != S the colon is contained in S and excludes 0; its elements are at least m, hence both terminal gaps are in the bidual. With both gaps in I, an element m+j of S below the conductor belongs to the colon exactly when low gaps m-2-j and m-1-j are both absent. The colon contains the entire conductor tail, and for x<0 the tail witness 2m-1-x excludes x from the bidual. An absent low gap stays absent precisely when it lies in a missing adjacent pair, including the single available neighbor at a boundary. Thus the bidual fills just the singleton missing positions, and the base S accounts for the extra reflexive ideal. Counting k runs of zeros by their 2k minimal zeros and k-1 separators proves the binomial sum, and the regular-language decomposition gives the rational series and recurrence. The characteristic polynomial has one real root lambda in (1,2) (both critical values are negative), with conjugate roots of modulus 1/sqrt(lambda). A simple-pole calculation gives the stated positive residue constant and the asymptotic density; bounded arithmetic independently gives lambda=1.7548776662466927 and C=0.722124418303113. Frozen verification documentation and script were read, not replayed. The script checks finite conductor windows for m=3 through 13; exclusion of negative integers is analytic, and the theorem does not depend on exhaustion over an unbounded parameter. The repaired RESULT, REVIEW and slogan retain the correct census, identify the known numerator and narrow the distinct claim.

## originality

PASS

PASS is for the repaired census of the entire normalized-ideal families, especially the exact five exceptional ideals outside the Boolean family in the two-gap case, and the resulting exact density with that denominator. No novelty is credited for the all-reflexive symmetric case, the word sequence, or the local bidual rule claimed in the original: the proof of the indexed sliding-window theorem works without a new step for r=2 and yields the reflexive subfamily. The comparator’s theorem as stated excludes r=2; this is proof-level coverage, not literal statement coverage or a priority decision. Its quotient calculation discards information about which partial terminal selections yield valid ideals and does not supply the complete normalized-ideal census. The repair separates the two enumerations and supplies the comparison explicitly.

## value

PASS

The surviving result is a complete classification of the ambient normalized-ideal families for a natural terminal-gap deletion, not a new name for a word sequence or just a fixed-point count. It identifies the exact boundary exceptions outside the Boolean family and supplies the denominator needed when sampling all normalized ideals, an invariant not recoverable by counting only reflexive ones. It quantifies the change from universal reflexivity to exponentially sparse reflexivity with an exact finite-m proportion rather than a density heuristic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
