---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For five repeated copies of a nonzero query \(q\), every minimal locality-two recovery is either one column of type \(q\) or one of the three complementary type-pairs \(\{u,u+q\}\). Thus the maximum repeated-query capacity is \(A_q=c_q+\sum\min(c_u,c_v)\), which must be at least five for all seven nonzero vectors. Summing over \(q\) counts each unordered pair of distinct column types exactly once and gives \(35\le n+\sum_{u<v}\min(c_u,c_v)\). For seven nonnegative integer multiplicities of total ten, the pair-minimum sum is Schur-concave under unit balancing and is maximized by a \(2,2,2,1,1,1,1\) profile with value 24, contradicting the required 35. Hence \(n\ge11\). For the witness multiplicities \(1,1,1,2,2,2,2\), the exact package verifier checks every one of the 462 five-query multisets and finds disjoint locality-two recoveries. An independent reimplementation also verified all 462 query multisets for that witness. The lower bound is analytic and the upper bound is a complete finite check.

## originality

PASS

Oksner, Hollmann, Riet and Skachek introduce and analyze exactly the bounded-recovery-set \([n,k,t,r]\) functional-batch framework, including general lower bounds for \(r=2\) and numerical tables. Their full searchable text does not state the exact \(k=3,t=5,r=2\) value; its displayed \(r=2\) table focuses on the simplex/double-simplex request counts such as \(t=8\) at \(k=3\). The unrestricted functional-batch literature treats a different optimization without the locality-two cap. Current Resultary searches for dimension three, five requests and locality two returned neighboring four-request and general-code results but no exact length-eleven theorem. The repeated-query lower obstruction and the complete length-eleven witness therefore remain a new parameter determination.

## value

PASS

The parameter is the first intermediate request count beyond the seven-column four-request simplex point in dimension three and before the doubled-simplex eight-request point. Proving that locality two forces length eleven gives a sharp small-parameter benchmark for the newly formalized bounded-recovery model, while the repeated-query obstruction is a simple structural lower-bound device that may transfer to neighboring cases. The finite computation is exhaustive on a natural boundary problem rather than an arbitrary census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
