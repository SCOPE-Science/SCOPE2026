---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Universality and homogeneity turn the labelled extensions into precisely the injective ordered types disjoint from the named star. Given the hub-and-tuple core, the one-leaf triangle tests are sufficient: with two old leaves their distance is 2, between the difference and sum of any two entries in {1,2,3}. Thus the leaf choices are independent, also for n=0; the hub vector itself is admissible. A non-2 hub entry bounds the base by 2·3^(k−1), and with hub entries all 2 a length-1 tuple edge forbids two of nine pairs. A length-3 edge forbids just the pair (1,1). Two length-3 edges have 22 assignments on three coordinates if incident, and 64 on four if disjoint, with 64<3·22. For any additional length-3 edge, putting 1 exactly on its endpoints and 2 elsewhere exhibits a newly forbidden assignment. These bounds give the unique unrestricted core, the single length-3 edge cores and the two incident length-3 edge cores, all admissible since their distances are 2 and 3. Their counts are 1, C(k,2), and 3C(k,3). Integer bases give the stated remainder, and (8/9)^2<22/27 gives the reciprocal probability estimate. Direct triangle counting for k=1,2 gives the small spectra; the recorded finite checks are corroboration, not the basis of the all-k proof.

## originality

PASS

The closest located one-type partition-function result and the classical extension criterion are real antecedents to the leaf count. Neither the checked statements nor their direct implications cover the distribution of leaf counts over tuple cores or identify and count the cores at the three largest bases. Pass is for that specified tuple-spectrum result, not for the classical extension criterion or the one-type case in isolation.

## value

PASS

The spectrum gives exact counts for every star size and fixed tuple arity and identifies the geometries that create the first two deviations from equilateral dominance. The incidence-sensitive third base and the exact multiplicities are information that a one-type formula or a leading growth-rate estimate does not supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
