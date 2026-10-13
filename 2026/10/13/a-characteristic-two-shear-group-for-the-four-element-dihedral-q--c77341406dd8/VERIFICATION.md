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

The companion `verify.py` uses the Python standard library and runs with `python3 verify.py`. It implements the original nonassociative structure directly from \(e_i e_j=e_{2j-i\bmod4}\) and evaluates preservation of all sixteen ordered basis products.

For \(K=\mathbb F_2\), it constructs all \(65{,}536\) linear endomorphisms, tests invertibility and multiplicativity, and compares the exact resulting set of \(32\) matrices with the independently constructed block-parametrized family. The entire matrix sets agree. For \(K=\mathbb F_4\) and \(K=\mathbb F_8\), it checks every parametrized automorphism, the distinctness of its matrix, and all basis products using extension-field polynomial arithmetic, giving \(512\) and \(8192\) verified matrices, respectively.

Observed successful run:

```
F2_GL4_EXHAUSTIVE_AUTOMORPHISMS 32 PASS
F4_CONSTRUCTED_AUTOMORPHISMS 512 PASS
F8_CONSTRUCTED_AUTOMORPHISMS 8192 PASS
VERIFY_OK
```

No claim is made that the checks exhaust all automorphisms over \(\mathbb F_4\), \(\mathbb F_8\) or arbitrary fields. Exhaustiveness in those cases follows from the proof's intrinsic-annihilator and tensor-stabilizer arguments, not enumeration. Neither correctness nor originality has received independent validation.
