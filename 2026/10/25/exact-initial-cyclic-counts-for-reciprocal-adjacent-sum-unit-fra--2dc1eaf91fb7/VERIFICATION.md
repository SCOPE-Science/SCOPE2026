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

# Reproducibility

The C11 program `verify_counts.c` carries out exact exhaustive enumeration for every circular size \(3\le n\le13\). Compile with `cc -O3 -std=c11 -Wall -Wextra -pedantic verify_counts.c -o verify_counts` and run `./verify_counts`; its output terminates in `VERIFY_OK`. The exact-rational Python3 implementation `crosscheck.py` performs independent checks at the first feasible sizes and terminates in `CROSSCHECK_OK`.

The finite proof depends on exhaustive branching, a unique canonical representative per dihedral orbit, and an integer test using \(L_n=\operatorname{lcm}(3,\ldots,2n-1)\). The checked finite maximum \(L_{13}=26771144400\) bounds every intermediate sum safely below \(2^{64}\). The code also checks the published OEIS A322070 *linear* table as a cross-calibration; that preexisting sequence is not a new result.

All observations concern \(n\le13\). No computation outside that range or independent audit is asserted.
