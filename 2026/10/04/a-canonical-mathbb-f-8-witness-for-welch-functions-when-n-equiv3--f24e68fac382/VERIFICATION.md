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

The infinite argument is the proof in `RESULT.md`. The standalone exact regression script `verify.py` models \(\mathbb F_8\) as \(\mathbb F_2[z]/(z^3+z+1)\). It verifies three items: every nonzero field element has seventh power one; for every odd multiple of three through \(n=201\), the Welch exponent restricts to exponent \(5\) modulo \(7\) and the value-sum on \(\mathbb F_8\) is zero; and the Hou--Zhao polynomial \(g(x,y)\) vanishes for all \(64\) pairs in \(\mathbb F_8^2\).

Replay with `python3 verify.py`. The observed output is:

`VERIFY_OK n_cases=34 subfield_sum=0 g_pairs=64`

The finite range is only a regression check. The proof for all \(n\equiv3\pmod6\) uses the congruence \(m\equiv1\pmod3\) and finite-field subfield theory, so no extrapolation from the checked range is made.
