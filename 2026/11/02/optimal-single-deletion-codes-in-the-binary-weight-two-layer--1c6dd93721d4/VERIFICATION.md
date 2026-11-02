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
# Reproduction and evidentiary limits

Run `python verify.py` with an unmodified Python 3 standard library. The script recomputes every proposed codeword's literal one-deletion shadow for \(n=2,\ldots,200\), compares the code size with the claimed formula, checks all shadow collisions, and separately constructs the complete weight-two confusability graph for \(n=2,\ldots,10\) to determine the maximum independent-set size via exact branch-and-bound. It returned:

`VERIFY_OK constructed_n=2..200 distinct_outputs=54152 exact_MIS_n=2..10 branch_nodes=75`

The proof's crucial facts are independently inspectable by elementary combinatorics: weight-one shadows consume one or two positions per codeword; adjacent-one words at successive starts cannot coexist; the construction pairs unused odd positions and separates its zero-deletion output shapes. The code tests finite parameter cases only. It does not establish originality or provide independent scientific certification. The source publication date is the publisher's December 6, 2019 first-publication date for DOI:10.3390/e21121202.
