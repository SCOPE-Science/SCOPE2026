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

Execute `python3 checker.py` in the directory containing this document. The script uses only the Python 3 standard library and prints `ALL_CHECKS_OK` on success. It constructs all local nonempty antichains of nonempty subsets of carriers of sizes \(1\), \(2\), and \(3\); enumerates every Boolean valuation on the products; checks the local necessity-and-sufficiency conditions and the exact one-way and two-way counts; tests the point-containing special class; and evaluates the global oriented count for \((m,n)\in\{(1,1),(1,2),(2,1),(2,2)\}\).

Observed output includes `pair 2 2 all 16 horizontal_eq 15 both_eq 14`, `pair 3 3 all 324 horizontal_eq 203 both_eq 131`, `global 2 2 all 256 oriented_eq 207`, and `ALL_CHECKS_OK`.

The calculations use exact finite integer and Boolean operations. The symbolic proof supplies quantification over arbitrary finite carrier sizes; the experiments are not proofs beyond the enumerated sizes. The program does not verify an external publication or independent priority. No independent audit has been performed.
