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

The proof has two independent components. The structural argument uses only upper-interval cardinalities and their overlaps in the Boolean three-cube. The finite replay independently enumerates every decoder map at lengths two and three.

`verify.py` accepts a decoder exactly when each of the four messages has some first-write representative whose coordinatewise upper interval contains all four decoder labels. This condition is equivalent to existence of a monotone second-write choice for every desired second message. The script checks all \(4^4=256\) length-two maps and all \(4^8=65,536\) length-three maps.

Expected output:
`VERIFY_OK n2_valid=0 n3_valid=24 all_antipodal=true one_output_relabeling_class=true`

The replay establishes the finite census only for the exact parameters in the claim. The infinite-looking uniqueness statement is not extrapolated from the census: it is proved directly for the complete three-cube. No claim is made about larger numbers of cells, messages, or writes.
