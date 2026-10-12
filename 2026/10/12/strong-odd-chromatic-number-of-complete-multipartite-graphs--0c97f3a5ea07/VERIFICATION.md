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
The universal proof has two exact steps. First, properness confines each color class to one partite class. A vertex in any other part sees that color on the entire class, so strong oddness is equivalent to every color class having odd size. Second, an odd part size is one positive odd summand, whereas an even part size requires at least two positive odd summands and admits the split \(1+(n_i-1)\). Summing over parts gives \(r+e\).

`artifacts/verify.py` independently enumerates canonical set partitions of the vertex set, interpreted as colorings, for every nontrivial complete-multipartite part-size profile of orders \(2\) through \(8\). For each coloring it tests properness and every neighborhood-color multiplicity directly. It then compares the brute-force optimum with the closed formula.

A successful replay prints:

`ALL CHECKS PASSED; profiles=58; canonical_colorings_checked=101632; orders=2..8`

The finite enumeration is a stress test only and is not used to prove the statement for arbitrary part sizes.
