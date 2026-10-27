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
# Reproducible verification

Run `python verify.py` with Python 3 and `networkx` available. No input downloads are required. The verifier reconstructs all its trees and uses exact integer/rational arithmetic.

Actual observed output included:

```
TREE_ORDER_PASS 2 nonisomorphic 1 min 0 max 0
TREE_ORDER_PASS 3 nonisomorphic 1 min -1/16 max -1/16
TREE_ORDER_PASS 4 nonisomorphic 2 min -25/64 max 0
TREE_ORDER_PASS 5 nonisomorphic 3 min -193/256 max 1/16
TREE_ORDER_PASS 6 nonisomorphic 6 min -1121/1024 max 1/8
TREE_ORDER_PASS 7 nonisomorphic 11 min -5761/4096 max 3/16
TREE_ORDER_PASS 8 nonisomorphic 23 min -27777/16384 max 1/4
TREE_ORDER_PASS 9 nonisomorphic 47 min -129025/65536 max 5/16
TREE_ORDER_PASS 10 nonisomorphic 106 min -585217/262144 max 3/8
TREE_ORDER_PASS 11 nonisomorphic 235 min -2611201/1048576 max 7/16
TREE_ORDER_PASS 12 nonisomorphic 551 min -11511809/4194304 max 1/2
EXACT_ORIENTATION_COUNTS_PASS 94
STRICT_PENDANT_PATH_TRANSFERS_PASS 12002
VERIFY_OK
```

The code exhaustively enumerates orientations only through order nine. Its checks of larger trees and edge grafts are finite structural checks, not an infinite proof; the general results rely on the analytic argument in RESULT.md. The external Python `networkx` package is needed to generate unlabeled trees; no other package or data input is needed. No independent audit was performed.
