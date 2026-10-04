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

The claim verified is \(\operatorname{ASP}(3,5,2)=\operatorname{ASB}(3,5,2)=10\).

Run `python3 artifacts/verify.py` with `artifacts/witness_certificate.json` in the same directory. The program uses only the Python standard library and performs two logically separate checks.

First, it enumerates every multiplicity vector on the seven nonzero vectors of \(\mathbb F_2^3\) with total length \(3\) through \(9\), filters to rank \(3\), reconstructs all inclusion-minimal recovery sets, and checks whether five pairwise disjoint recoveries exist for each stored column type. The rank-\(3\) counts are \(28,119,329,742,1478,2702,4634\), and the number satisfying five-all-symbol PIR is zero at every length.

Second, it reconstructs the ten-column witness \((2,3,4,4,5,5,6,6,7,7)\), checks the five-all-symbol PIR condition, exhausts all \(252\) five-request multisets of its six stored types for the stronger batch condition, and independently validates every row of the stored recovery certificate. Certificate validation checks request completeness and uniqueness, five recoveries per row, exact target multiplicities, index ranges, pairwise disjointness, and linear-span recovery over \(\mathbb F_2\).

The expected final marker is `VERIFY_OK ASP(3,5,2)=ASB(3,5,2)=10`.

The verification proves only this finite parameter statement. It is not evidence for other dimensions, request counts, or alphabets, and no independent audit has been performed.
