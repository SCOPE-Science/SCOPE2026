---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The actual theorem concerns any fixed positive-integer species abundance multiset with total N<=13 under uniform fixed-m without-replacement samples. For species presence indicators I_i, P(I_i=0)=C(N-a_i,m)/C(N,m) and P(I_i=I_j=0)=C(N-a_i-a_j,m)/C(N,m); expansion of Var(sum I_i) gives the stated source equation (1) with q_ij-q_iq_j. Nondecreasing positive integer partitions enumerate each species-label permutation class once; the partition recursion is exhaustive by induction on remaining total. Independently and without importing the source verifier, enumerated all 2^N subsets of the N labelled individuals for every partition of N=1..13, accumulated exact E[K_m],E[K_m^2], used rational arithmetic for every m, and tested BOTH strict inequalities at each possible m=2..N-1. Partition counts for N=3..13 were 3,5,7,11,15,22,30,42,56,77,101 (total 369), none below N=13 double peaked, and only (1,6,6) among the 101 profiles of N=13 gave >=2 strict local maxima at m=(3,6). Exact witness rational sequence matched all 13 source fractions; N=1,2 impossible by number of interior positions. Source verifier uses independent hypergeometric convolution checking every cell; its code and scope were inspected, but not blindly treated as a proof merely from its success statement. This is a complete finite sharp-cutoff proof, not an assertion about all larger N.

## originality

PASS

Best-of-knowledge sharp-threshold and uniqueness classification appears new relative to inspected primary sources and published research records. Exact moment formulas have been known since 1975 and are not claimed new. The full Nipperess–Matsen 2013 marked-tree variance theorem specializes to the exact old abundance-census moment identity, but does not state/exhibit the all-integer-partition first two-peak cutoff. Tong 1983 majorization statements compare populations at the same sample depth; the independent occupancy published results use iid draws and different covariance objects. Published prior tables do not demonstrate the unique (1,6,6) two-peak witness in the checked sources. Priority remains qualified because some older full texts were inaccessible and search is nonexhaustive.

## value

PASS

Finite rarefaction is an established mathematically meaningful model: the variance of observed richness versus sample depth is a natural uncertainty invariant for a fixed census. It need not have a single peak even though expected richness rises. Establishing the FIRST census where strict variance re-rise occurs and proving UNIQUE first-layer abundance multiset and both sample-depth peaks is a natural complete sharp finite classification, not a random unmotivated numeric slice or textbook substitution. The example (1,6,6) has one singleton and two equal abundant species, explaining competing early and intermediate sources of variance; m>=8 collapses to the singleton Bernoulli variance m(13-m)/169. This exact boundary can prevent an unjustified single-peak heuristic in rarefaction-depth uncertainty planning. No downstream theorem, asymptotic family, or claimed broad ecological application is needed for the bounded standalone result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
