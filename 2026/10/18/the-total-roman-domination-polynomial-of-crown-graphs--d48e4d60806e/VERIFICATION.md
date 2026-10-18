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

# Computational verification and mathematical scope
Run `python3 VERIFY_CROWN.py`. The checker independently evaluates the graph condition on all \(3^{2n}\) maps for each \(2\le n\le6\). It compares the complete coefficient tables with integer-polynomial convolution of the claimed formula, not just its minimum coefficient. The exact run printed in `VERIFY_CROWN_OUTPUT.txt` reports \(597861\) total assignments. For \(7\le n\le30\), the code performs arithmetic consistency checks only (not exhaustive enumeration).

The seven-case proof in `RESULT.md` is the justification for all \(n\ge2\). Neither exhaustive finite checks nor reproducible code is an infinite proof or independent scientific certification. The bibliography covers nearby mathematical constructions; equivalent uncatalogued work remains possible.
