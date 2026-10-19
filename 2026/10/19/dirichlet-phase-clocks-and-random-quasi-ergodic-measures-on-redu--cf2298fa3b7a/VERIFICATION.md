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

# Finite exact-rational verification

Execute `python3 verify.py` using Python's standard library. The verifier independently enumerates all positive-probability survivor paths in the explicit five-state example for 12 horizons, and checks the resulting exact rational total weights against separately computed matrix powers. It checks both maximal-component route formulas, every exact uniform-composition weight along the direct route, and the first two conditional occupation moments. Separately, it checks twelve powers of a two-state primitive Perron block against its closed spectral projection and verifies the Perron-Doob row normalizations. Finally, it computes both effective route weights using the subcritical geometric resolvent. A second six-state example has a genuinely nonscalar two-state primitive subcritical component \(\frac1{32}\begin{pmatrix}3&1\\1&3\end{pmatrix}\), with resolvent \(\begin{pmatrix}5/3&1/3\\1/3&5/3\end{pmatrix}\). The script verifies sixteen exact matrix-power and nontrivial component-route identities across eight horizons; the detour has limiting path weight \(1/24\).

The recorded execution result was:

`VERIFY_OK: 12 exact survival matrix/path comparisons; 24 maximal-route identities; 478 exact composition-moment checks; 12 non-scalar Perron-projector checks; two resolved route weights; 16 nonscalar subcritical resolvent/path comparisons`

These are exact finite-instance checks; they **do not** validate all possible finite matrices, the passage to an infinite time horizon, the Dirichlet weak limit, or universal historical novelty. Those conclusions rely on the analytical proof in `RESULT.md`, in particular the Perron-gap bounds and the asymptotics of weak compositions.
