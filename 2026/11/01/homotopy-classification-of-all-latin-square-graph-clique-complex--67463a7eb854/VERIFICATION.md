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

Run from a directory containing all packaged files:

```sh
python3 latin_square_checker.py
```

The checker is standalone Python 3.9+ and uses only its standard library. Its deterministic completed run printed:

```text
cyclic_5: f=[25, 150, 250, 75, 15] boundary_ranks={1: 24, 2: 126, 3: 60, 4: 15} H_2_rank=64 intercalates=0 symbol_edges=50 rook_rectangles=100 six_triangle_disks=50
cyclic_6: f=[36, 270, 540, 279, 108, 18] boundary_ranks={1: 35, 2: 235, 3: 189, 4: 90, 5: 18} H_2_rank=116 intercalates=9 symbol_edges=90 rook_rectangles=225 six_triangle_disks=144
nonabelian_S3_6: f=[36, 270, 540, 297, 108, 18] boundary_ranks={1: 35, 2: 235, 3: 207, 4: 90, 5: 18} H_2_rank=98 intercalates=27 symbol_edges=90 rook_rectangles=225 six_triangle_disks=162
cyclic_7: f=[49, 441, 1029, 735, 441, 147, 21] boundary_ranks={1: 48, 2: 393, 3: 420, 4: 315, 5: 126, 6: 21} H_2_rank=216 intercalates=0 symbol_edges=147 rook_rectangles=441 six_triangle_disks=294
VERIFY_OK
```

Each computation checks every symbol-edge replacement triangle and every rook rectangle's explicit two- or six-triangle filling. The clique enumeration includes independent Bron--Kerbosch maximal-clique enumeration, exact face counts, and GF(2) boundary matrix ranks. It also checks the predicted intercalate-corrected Betti rank and vanishing of the other reduced homology ranks in each tested case. The universal proof appears in RESULT.md and does not infer any infinite claim from these four finite calculations. Source [1] supplies all-field homology for every Latin square of order at least five. No direct integral Smith-normal-form computation or external independent audit is asserted.
