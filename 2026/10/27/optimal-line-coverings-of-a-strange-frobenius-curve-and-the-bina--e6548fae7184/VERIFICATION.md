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
# Finite verification and proof limits

Run `python3 verify_frobenius_spread.py` in a standard Python 3 interpreter. The checker uses the irreducible cubics \(u^3-u-1\) over \(\mathbb F_3\) and \(u^3+2u+1\) over \(\mathbb F_5\), evaluates all graph secants and confirms that every unordered pair appears in exactly one maximal block. It checks the zero first-moment identity, a conventional parallel spread, and a nonparallel spread. It separately constructs the characteristic-two non-spread optimal five-line cover over \(\mathbb F_8\).

Expected terminal lines include:
```
VERIFY_OK p=3 q=27 maximal_secants=117 point_degree=13 affine_2_design=351_pairs parallel_and_nonparallel_spreads=9_blocks all_block_first_moments_zero
VERIFY_OK p=5 q=125 maximal_secants=775 point_degree=31 affine_2_design=7750_pairs parallel_and_nonparallel_spreads=25_blocks all_block_first_moments_zero
VERIFY_OK exact_small_field_models
VERIFY_OK binary_F8_nonspread_optimal_cover=5 secants=4 doubled=1 hole=7 extra_infinity_line=1
```
The general proof is symbolic and combinatorial; no assertion of exhaustive computation at untested extension degrees is made. This verification is self-review only. The cited originating source provides the numerical optimal covering number independently of the new classification.
