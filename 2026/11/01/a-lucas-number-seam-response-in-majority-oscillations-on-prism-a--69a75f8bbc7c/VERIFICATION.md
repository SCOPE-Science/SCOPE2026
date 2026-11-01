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

# Reproduction of finite checks

Run `python3 verify_twist_majority.py` in the same directory as this document. It uses only the Python standard library. The recorded output is in `verification_output.txt` and ends in `TWISTED_LADDER_MAJORITY_VERIFY_OK`.

The code directly evaluates the majority rule for all \(2^{2n}\) labelled initial configurations of each of two graphs for every \(3\le n\le10\). It separately exhausts binary cyclic words of lengths \(3\) through \(15\), checks exact edge bijections for the temporal covers up to \(n=30\), and evaluates the Lucas discrepancy formula through \(n=1000\). The direct configuration count is \(2{,}796{,}160\); zero numerical approximation is used. All these finite ranges were actually checked.

The infinite-family conclusions rest on the displayed transfer-matrix characteristic polynomial, the forced rung-state argument, the explicit graph-cover isomorphisms, and the integer energy proof. No exhaustive check of all large graphs, basin sizes, or prior literature is asserted. This is a self-review only; independent audit evidence is absent.
