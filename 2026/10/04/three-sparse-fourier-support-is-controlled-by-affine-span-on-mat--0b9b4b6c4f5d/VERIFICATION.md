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

The proof is analytic. Its critical checks are:

1. For a translated support \(\{0,a,b\}\), restriction \(\widehat G\to\widehat H\) with \(H=\langle a,b\rangle\) has constant fiber size \(|G|/|H|\), so Fourier-support cardinality scales exactly by that factor.
2. A two-generated subgroup of \(\mathbb Z_4^d\) containing three support points has one of exactly four isomorphism types: \(\mathbb Z_4\), \(\mathbb Z_2^2\), \(\mathbb Z_4\times\mathbb Z_2\), or \(\mathbb Z_4^2\).
3. The local Fourier sums have at most two, one, two, and two zeros, respectively. The bounds are sharp by the explicit coefficient triples in `RESULT.md`.
4. `artifacts/verify.py` independently exhausts every three-point support in \(\mathbb Z_4^2\) using exact Gaussian-integer character values. It verifies the predicted attainable sets for all \(560\) supports and prints `VERIFY_OK`.

Replay command:

`python3 artifacts/verify.py`

Expected terminal lines include `VERIFY_OK`, span counts `{'C4': 96, 'C2xC2': 16, 'C4xC2': 192, 'C4xC4': 256}`, and global sizes `[8, 12, 14, 15, 16]`.

The finite replay is not a proof for arbitrary \(d\); the arbitrary-dimensional step is the exact character-restriction argument in `RESULT.md`.
