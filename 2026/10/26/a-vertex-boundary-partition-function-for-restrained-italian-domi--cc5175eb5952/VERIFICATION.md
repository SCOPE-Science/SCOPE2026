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

# Reproducibility and limits

Run `python3 verify.py` from the directory containing the extracted files. The test program uses only Python's standard library and independently enumerates all vertex-label assignments in the corona, checking the original definition and summing weights. It compares the result with a separately constructed coefficient formula for every labeled simple graph of order at most four (75 graphs) and five selected five-vertex graphs (80 graphs in all). The sample program output reports 80 verified graphs, and the verified minimum/coefficient checks for complete graphs, paths, stars and cycles. The program also checks the boundary maximum and maximizer count on paths of orders 1 through 18 and cycles of orders 3 through 18, and directly checks the corona label counts on cycles of orders 3 through 5.

The full proof in RESULT.md supplies an all-orders mathematical argument; finite enumeration neither certifies the formula beyond the checked orders nor establishes literature priority. The relevant full-text comparison with DOI:10.1142/S1793830923500179 remains unavailable, although its public abstract reports only scalar corona values. Independent audit has not been performed.
