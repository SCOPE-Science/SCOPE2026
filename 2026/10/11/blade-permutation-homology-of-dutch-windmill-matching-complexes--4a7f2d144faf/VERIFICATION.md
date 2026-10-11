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

The proof has two independently checkable layers.

First, the symbolic argument reduces every character value to the path matching recurrence
\[
a_r=a_{r-1}-a_{r-2},\qquad a_0=1,\quad a_1=0,
\]
and the exact fixed-matching formula
\[
F(\pi)=A^{c(\pi)}-2f(\pi)BA^{c(\pi)-1},
\quad A=a_{m-2},\quad B=a_{m-3}.
\]
The simplicial orientation calculation gives \(\widetilde L(\pi)=-F(\pi)\). Combining this with the single-degree homology from Donovan--Scoville Theorem 5.8 yields the claimed characters.

Second, `artifacts/verify.py` enumerates every matching directly for \(n=2,3\) and \(m=4,5,7,8\). For every blade permutation it computes the signed fixed-simplex trace on augmented simplicial chains and checks equality with both the symbolic formula and the closed representation character. The saved output `artifacts/verification_output.txt` ends with `VERIFY_OK`.

The exhaustive finite cases are regression checks only. They are not used to extrapolate the all-parameter theorem. The infinite quantifiers are discharged by the recurrence and fixed-simplex factorization.
