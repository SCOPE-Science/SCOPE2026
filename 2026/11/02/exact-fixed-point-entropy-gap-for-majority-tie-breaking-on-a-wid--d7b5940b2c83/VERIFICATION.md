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
The package provides `verify_torus.py` and `requirements.txt`; execute `python -m pip install -r requirements.txt`, then `python verify_torus.py` in the extracted package directory. This script reconstructs the transfer matrix from the precise four-neighbor majority test, checks its full characteristic polynomial over exact integers via SymPy, and checks n=3 through n=6 using a distinct vertex-adjacency enumerator. It also tests no-isolated-symbol cyclic words and a separate trace computation. The script was executed successfully from the embedded bytes after packaging.

The finite tests alone do not establish the arbitrary-length counts; the cyclic transfer bijections, exact determinant identity, root bound and RMM column obstruction supply that argument. No independent expert audit or external certification has been performed. The random-tie statement counts absorbing singletons only and does not classify other recurrent classes.
