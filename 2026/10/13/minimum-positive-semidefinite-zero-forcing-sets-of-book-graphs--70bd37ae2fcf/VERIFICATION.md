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

The symbolic proof covers every integer \(n\ge1\). The accompanying script independently constructs the book graph from its edge definition and implements the PSD color-change rule by recomputing connected components of the current white graph after every force.

For each \(1\le n\le12\), the script checks every singleton and every two-vertex subset. It confirms that no singleton is forcing, that a pair is forcing exactly when it is the spine pair, a same-page pair, or a spine-page pair, and that the number of forcing pairs is exactly \(5n+1\).

The finite computation is a boundary and regression check. It does not prove the theorem for untested orders; the infinite statement rests on the case-complete symbolic proof in \(\texttt{RESULT.md}\). The script uses only the Python standard library.
