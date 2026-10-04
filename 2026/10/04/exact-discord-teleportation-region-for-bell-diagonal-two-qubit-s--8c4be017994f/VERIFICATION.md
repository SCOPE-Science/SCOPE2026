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

The proof was reconstructed symbolically from the Bell-basis eigenvalues. For ordered magnitudes \(s_1\ge s_2\ge s_3\) with \(q=s_1+s_2+s_3\in[1,3]\), physicality reduces to \(s_1+s_2-s_3\le1\), hence to the exact polygon
\[
(q-1)/2\le s_3\le q/3,\qquad s_3\le s_2\le(q-s_3)/2.
\]
The objective \(D_G=(s_2^2+s_3^2)/3\) is minimized at the lower-left edge endpoint and maximized, after maximizing in \(s_2\), at one of the two endpoints in \(s_3\). Their difference is exactly
\[
\frac{13(q-3)(q-15/13)}{432},
\]
which supplies the crossover without numerical approximation.

The included `verify.py` independently checks the formulas with exact rational arithmetic on a dense finite Bell-probability grid and on both extremal families. These checks test transcription and boundary behavior; they are not used to infer the infinite-state theorem.

Unproved limits: no claim is made outside Bell-diagonal states, outside the normalized Hilbert–Schmidt convention, or for teleportation performance functionals other than the standard optimized average fidelity.
