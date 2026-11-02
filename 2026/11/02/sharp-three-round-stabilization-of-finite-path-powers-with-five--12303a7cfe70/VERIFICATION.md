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

# Reproducibility and limits

The all-parameter proof consists of the four exact pair-extension criteria, the five resulting pointed-profile sets, and the three-move matching strategy in `RESULT.md`. The two-vertex-domination sentence proves sharpness at each fixed radius; the neighborhood-containment sentence distinguishes stable path from stable cycle powers. This mathematical proof is separate from finite experiment.

Run `bash reproduce.sh` in the directory containing all packaged artifacts using Python 3's standard library. The script executes `verify_pathpowers_rank3.py` and `check_pathpair_formula.py` and compares each stdout stream byte-for-byte against its packaged `.stdout` file. The former checks 89,205 ordered pairs across 90 stable graphs for the symbolic mask/profile formula and separately evaluates complete three-round logical types for five stable radius representatives and all 36 smaller noncomplete path powers; it also checks the immediately preceding boundary at five radii and one stable cycle example. The latter independently enumerates actual third vertices for 105,200 pairs in 96 stable graphs and independently checks the five-profile partition. A successful replay prints `REPRODUCE_OK`.

Finite checks establish only the stated finite cases. The infinite all-radius assertion uses the mathematical interval proof, not extrapolation. The least-representative proof is exact finite exhaustion of all smaller path-power parameters; it does not establish any external unique-priority claim. No independent audit or certification has been performed.
