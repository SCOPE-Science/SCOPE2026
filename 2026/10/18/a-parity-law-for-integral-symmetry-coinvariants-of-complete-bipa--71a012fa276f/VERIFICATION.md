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
The artifact `verify.py` requires only Python 3 and the standard library. From a directory containing the script, run `python3 verify.py`. The expected output is in `verify-output.txt`.

The verifier independently builds the original oriented-simplex presentation reduced modulo two, including pure-subset relations, all higher-simplex boundaries, and all within-part adjacent transposition relations. It then computes its binary quotient dimension using exact bitset elimination. Separately it builds the much smaller color-count boundary presentation and evaluates the closed parity formula. All three agree for 70 triples with part sizes two through five, and the latter two agree for all \(2\le m,n\le35\), \(2\le r<m+n\).

The verifier alone does **not** prove integrality, exponent two, or any all-parameter claim. These follow from the signed orbit-module argument and the exact chain presentation proved in `RESULT.md`. No integral torsion in the underlying higher-independence homology, full integral group module, or quotient-space homology is claimed.
