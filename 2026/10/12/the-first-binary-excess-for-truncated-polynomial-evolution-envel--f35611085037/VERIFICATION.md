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

Run `python3 verify.py` in a directory containing the script. It uses only the Python standard library. It constructs the exact upper-triangular matrices of the multiplication tensor for \(\mathbb F_2[t]/(t^n)\), \(n=1,2,3,4\). It exhaustively tests all candidate linear-functional support subsets until it finds the smallest length, reporting minimum sizes \(1,3,5,8\). For the fourth case it separately enumerates all \(\binom{15}{7}=6435\) seven-functional supports, all failing target-span membership, and evaluates the displayed eight-term multiplication formula on every ordered pair of sixteen elements.

Expected terminal lines are `LOWER_BOUND_6435_SEVEN_SUPPORTS_OK`, `EXPLICIT_EIGHT_TERM_DECOMPOSITION_256_PRODUCTS_OK`, and `VERIFY_OK`. The test contains no probability, tolerances, or external files. Its exhaustiveness applies only to the explicitly enumerated finite field/dimensions. The general equivalence between an ideal evolution envelope and symmetric bilinear decomposition is established symbolically in `RESULT.md`.
