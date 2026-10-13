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

The symbolic proof is the authority for the all-dimension theorem. The executable check is a finite consistency test of the defining-set identities and the local formula.

`verify.py` reconstructs the two class-(a)/(b) trinomials over exact polynomial-basis models of \(\mathbb F_{2^m}\) for \(m=5,7,9\). It checks that the punctured images coincide and have cardinality \(2^{m-1}\). For every coordinate \(d\) in that common image, it directly counts pairs \(y,y+d\) that stay in the defining set, evaluates
\[
G_4(d)=\sum_y(-1)^{\operatorname{Tr}(y^{17}+dy^3)},
\]
and verifies
\[
8\rho(d)=2^m-G_4(d).
\]
It also checks the global count
\[
A_3(C_D^\perp)=\frac{2^m(2^m-2)}{48}
\]
and confirms that every nonzero computed quadratic sum has a magnitude allowed by a radical dimension in \(\{1,3,5,7\}\).

A replay from the packaged verifier produced:

`m=5 n=16 A3=20 repair={0: 1, 4: 15}`

`m=7 n=64 A3=336 repair={14: 22, 16: 28, 18: 14}`

`m=9 n=256 A3=5440 repair={60: 72, 64: 129, 68: 54, 72: 1}`

`VERIFY_OK`

The computation does not enumerate infinitely many dimensions and does not establish the symbolic Walsh or quadratic-form lemmas by experiment. Those steps are proved in `RESULT.md` from the stated source identity and standard finite-field Fourier and quadratic-form arguments.
