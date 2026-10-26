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
The bundled `verify.py` iterates over each binary word with \(a,b\ge3\) and \(a+b\le15\), computes the scattered \(01\) count, directly tests all eight length-three subsequences, and checks the proposed exception count for every \(c\). It also checks the bound of at most two exceptions and the global total \(3(a+b)-6\). The program uses only Python's standard library. Run `python3 verify.py`; the expected result is included in `checks.txt`.

The computation tests finitely many words. The proof's six avoidance-family classification and overlap accounting establish the infinite parameter statement; neither the script nor any output log establishes originality or independent validation.
