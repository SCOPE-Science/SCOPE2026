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

`verify_ferro_xyz_dm_gap.py` evaluates the two published concurrence branches directly.

For several strict ferromagnetic parameter sets, it checks the defining edge equalities, the ordering
\[
D_-<D_c<D_+,
\]
and the equivalence between positive concurrence and lying outside the claimed zero interval.

It also checks that
\[
\frac{D_+(T)-D_-(T)}
{(2\nu_c/D_c)T e^{-2A/T}}
\]
approaches \(1\) as \(T\) decreases.

The numerical replay is supplementary. The optimizer boundary and low-temperature width are proved analytically in `RESULT.md`.

No independent audit has been performed.
