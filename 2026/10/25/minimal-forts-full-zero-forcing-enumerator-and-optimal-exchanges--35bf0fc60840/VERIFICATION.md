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
# Reproducibility and verification

Run `python3 verify.py` with the standard Python 3 library. The script creates adjacency lists directly from the definition, tests every initial white set for \(n=4,5,6,7,8\), tests an independently programmed chronological single-force procedure for \(n=4,5,6\), constructs all inclusion-minimal forts for \(n=4,5,6,7\), builds all minimum-solution exchanges, and verifies every claimed degree, count and connectivity assertion. It terminates with the exact line `ALL_VERIFY_OK`.

Observed output:
```
n=4 white_coefficients={0: 1, 1: 9, 2: 36, 3: 66, 4: 42} minimum_sets=42 exchange_edges=150 connected=YES CHECK_OK
n=5 white_coefficients={0: 1, 1: 11, 2: 55, 3: 130, 4: 120} minimum_sets=120 exchange_edges=690 connected=YES CHECK_OK
n=6 white_coefficients={0: 1, 1: 13, 2: 78, 3: 225, 4: 270} minimum_sets=270 exchange_edges=2130 connected=YES CHECK_OK
n=7 white_coefficients={0: 1, 1: 15, 2: 105, 3: 357, 4: 525} minimum_sets=525 exchange_edges=5250 connected=YES CHECK_OK
n=8 white_coefficients={0: 1, 1: 17, 2: 136, 3: 532, 4: 924} minimum_sets=924 exchange_edges=11172 connected=YES CHECK_OK
ALL_VERIFY_OK
```

Finite enumeration is not an infinite proof. The separate combinatorial argument in `RESULT.md` proves all formulas and connectivity for every integer \(n\ge4\). No independent audit has been performed.
