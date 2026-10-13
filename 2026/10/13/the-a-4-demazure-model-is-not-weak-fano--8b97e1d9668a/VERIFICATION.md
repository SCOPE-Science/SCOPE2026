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

The initiating source was checked at the complete \(C_1\) subdivision and at Proposition 7.6. It gives
\[
v_1=\frac{\gamma_3+\gamma_4}{3}
\]
and replaces the multiplicity-three cone by
\[
\operatorname{Cone}(\gamma_1,\gamma_2,\gamma_3,v_1),
\qquad
\operatorname{Cone}(\gamma_1,\gamma_2,v_1,\gamma_4).
\]
Proposition 7.6 confirms these as part of the final smooth projective fan.

Their shared wall is \(\operatorname{Cone}(\gamma_1,\gamma_2,v_1)\), so its wall relation is exactly
\[
\gamma_3+\gamma_4-3v_1=0.
\]
The smooth-toric wall-intersection rule was independently checked in an open-access reference: each coefficient is the intersection number of the associated invariant divisor with the wall curve, and the anticanonical degree is the sum of all coefficients. Hence
\[
(-K)\cdot C=1+1-3=-1.
\]
This is an exact integral computation, not a numerical experiment.

The full initiating text was also searched for the natural prior-coverage terms. “nef” and “anticanonical” do not occur, and the occurrence of “Fano” is bibliographic rather than a positivity claim about \(Y(A_4)\).

Limits checked: the proof establishes only one negative invariant curve and therefore non-nefness; it does not determine the entire Mori cone, nef cone, or all negative curves.
