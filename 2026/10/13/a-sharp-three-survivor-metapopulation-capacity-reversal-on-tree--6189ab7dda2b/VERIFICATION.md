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

The supporting complete file `verify.py` is executable by Python 3 without third-party packages or any external files. Run `python verify.py` from the directory containing the delivered files.

The actual observed output was:

`VERIFY_OK labeled_trees=18247 three_patch_samples=615482 symbolic_charpoly_checks=2701`

The checker enumerates all \(n^{n-2}\) labeled trees at each integer order \(3\le n\le7\) by Prüfer words, counts every three-site subset, and verifies the exact law, wedge bounds, extremizer degree conditions and the two-site invariance. It separately expands symbolic determinants of selected three-by-three adjacency matrices, checking \(\det(xI-A)=x^3-e x\) for their induced edge counts \(e\in\{0,1,2\}\).

The complete mathematical proof in `RESULT.md` covers every finite \(n\ge4\). Enumeration through seven vertices cannot establish an all-order claim; it is a reproducibility and algebra cross-check. The threshold is a spectral proxy under the model assumptions, not a direct stochastic survival probability. The full text of a relevant 2003 article remained inaccessible, and no independent audit has occurred.
