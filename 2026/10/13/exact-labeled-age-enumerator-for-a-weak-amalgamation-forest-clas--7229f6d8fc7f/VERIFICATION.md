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

`verify.py` carries out two logically separate checks. First it uses exact rational formal-power-series arithmetic to solve the planted-state equations through degree 12, constructs the vertex-rooted and dissymmetry series, exponentiates the connected series, and asserts every displayed connected and forest coefficient. Second, it ignores the species equations: it enumerates all labeled trees through 7 vertices using Prüfer codes and all labeled simple graphs through 6 vertices by edge subsets, checking acyclicity and the no-adjacent-high-vertices condition directly. Both independent finite enumerations agree with the formal EGF coefficients, and the script prints `VERIFY_OK`.

Replay with:

```text
python3 verify.py
```
