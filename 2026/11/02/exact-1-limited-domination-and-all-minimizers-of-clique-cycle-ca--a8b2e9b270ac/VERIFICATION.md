---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproducibility
The unchanged companion `verify.cpp` uses finite direct adjacency checks for ten graphs and a cyclic column dynamic program for 3≤m≤8, 3≤n≤34. It includes checks for n=3 and multiples of four as context outside the narrowed finding. Build with `c++ -O2 -std=c++17 verify.cpp -o verify` and run `./verify`. The universal classification and the labelled counts are proved in `RESULT.md` by the full-block and gap constraints; the finite checks do not replace that proof.
