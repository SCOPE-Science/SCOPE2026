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

# Verification of the exact common-image extremal count

The proof in `RESULT.md` establishes the theorem for every field and every positive integer \(r\). The following independent finite computations are a reproducible corroboration, not a replacement for the proof.

Run with Python 3 from the directory containing these scripts. The final two scripts require NumPy:

```sh
python verify_binary.py
python verify_ternary.py
python verify_centralizer.py
```

Observed results on the packaged source files:

```text
squarezero_rank2 210
extremal_pairs 2520
expected 2520
planes 130
GL2 48
enumerated B 6240 extremal for fixed A 144 expected 144
VERIFY_Q3_OK
[[1, 0], [0, 1]] centralizer_alg_dim 16
[[1, 0], [0, 2]] centralizer_alg_dim 14
[[1, 1], [0, 1]] centralizer_alg_dim 14
VERIFY_CENTRALIZER_OK
```

The binary program exhausts all \(4\times4\) binary matrices to identify rank-two square-zero first and second factors, and tests all ordered pairs of these factors. The ternary program enumerates all two-dimensional image subspaces and all isomorphisms from their quotients over \(\mathbb F_3\), exhaustively checking the \(6240\) possible second factors for one fixed rank-two square-zero first factor. The centralizer program independently solves the full simultaneous linear commutation system for three selected \(8\times8\) pairs. These computations do not exhaust all fields or higher dimensions. The theorem does not assert scheme-theoretic reducedness, and this package does not provide an independent human audit.
