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
Run `python3 CHECK.py` in the package directory. The script uses only the Python standard library. It regenerates decoder states and transitions directly from the two codeword lengths and the exceptional prefix, performs exhaustive reachable-subset breadth-first searches for \(2\le m\le9\), checks an explicit reset word, and independently checks its claimed intermediate images. The exact expected stdout is embedded as `CHECK_OUTPUT.txt`. This finite verification does not establish the full theorem; the unrestricted proof rests on the modular count of exceptional length-\(m+1\) completions and elimination of the only possible shorter candidate.

No independent audit was conducted. The bibliographic novelty assessment has a residual access limitation for the full 2009 Huffman-code paper.
