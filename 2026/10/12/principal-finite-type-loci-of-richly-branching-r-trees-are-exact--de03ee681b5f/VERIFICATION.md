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

The proof has two logically distinct parts.

First, the model-theoretic part uses published results for \(\mathrm{rbRT}_r\): quantifier elimination and pseudometric determination of finite types, the type metric, the interval description of one-types, continuum density of two-types, and the characterization of principal types by a single piecewise segment from \(p\).

Second, the new metric extraction is elementary. A principal tuple with radial vector \(\mathbf t\) has pairwise distances \(|t_i-t_j|\). For two radial vectors \(\mathbf t\) and \(\mathbf s\), every simultaneous realization satisfies
\[
\max_i d(a_i,b_i)\ge \max_i|t_i-s_i|,
\]
while placing both tuples on the same ray attains equality. This proves the \(\ell_\infty\) formula exactly.

The bundled `verify.py` replays these finite metric identities using exact rational arithmetic. It checks radial tree pseudometrics on rational grids through arity \(5\), telescoping of the sorted piecewise path, exact same-ray attainment of the sup distance, and preservation of the maximum metric under the coordinate-repetition map used in the density argument through arity \(10\). It terminates with:

`VERIFY_OK 3366437 exact assertions`

The checker is not an independent audit and does not attempt to verify the cited model-theoretic theorems. Its role is to guard the algebraic and finite metric steps of the deduction.
