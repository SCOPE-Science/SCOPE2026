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
Run `python3 verify.py` using the standard Python 3 library. The included `verification_output.txt` is the actual output obtained with the embedded script. The direct computation checks the graph-adjacency fort definition for all nonempty subsets of \(T_n\) at \(2\le n\le7\), evaluates minimality against **every** nonempty proper subset, and compares its complete coefficient distributions with the independently implemented star-component and cycle counts. It checks \(2{,}131{,}018\) subset masks, including empty masks counted in the total mask capacity, and evaluates the finite component recurrence through \(n=20\).

The code cannot certify the theorem at unbounded \(n\) or independently establish bibliographic novelty. The rigorous proof for arbitrary \(n\) is given in `RESULT.md`; no Lean, external expert validation, or independent audit was performed.
