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

Run `python3 verify.py`.

The checker uses the standard ternary weights \(\mu(\mathtt a)=1\), \(\mu(\mathtt b)=2\), and \(\mu(\mathtt c)=3\). It exhaustively enumerates all \(29{,}520\) ternary words of lengths \(2\) through \(9\), computes every factor-weight signature, reconstructs the unique standard weighted prefix normal form from successive signature differences, and checks that the reconstructed word has the same signature.

For each length it computes both the largest \(\ell_1\)-distance from a word to its normal form and the largest difference in the number of \(\mathtt c\)'s inside any factor-weight equivalence class. The expected sequences are checked exactly. The two sharp construction families are also replayed for every length from \(2\) through \(30\).

The finite replay is not used to infer the all-length statement. The infinite upper bound and sharpness follow from the symbolic argument in `RESULT.md`. Independent audit has not been performed.
