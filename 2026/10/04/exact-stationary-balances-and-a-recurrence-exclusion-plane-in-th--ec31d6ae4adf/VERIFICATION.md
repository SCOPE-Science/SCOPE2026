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

The proof depends on exact polynomial identities, not on a finite trajectory census. The bundled `verify.py` uses symbolic expansion of the five-real-dimensional form of the complex Chen equations and checks:

1. \(Ls=2a(R-s)\).
2. \(LI=(c_1-a)I+c_2(s+R)\).
3. For \(G=aR-(a+c_1)s/2\),
   \[
   LG=|\dot X|^2-a c_2I+a(2c_1-a-Z)s.
   \]
4. For \(V=s-2aZ\),
   \[
   LV=-2as+2abZ.
   \]
5. Algebraic elimination of the stationary mixed phase moment gives
   \[
   (c_1-a)\left[M-(2c_1-a)S-\frac Ea\right]=2c_2^2S.
   \]

The checker also verifies the special rotating-orbit reduction against the published formulas \(c_1=28\) and \(\omega=2ac_2/(a-28)\).

Limits: symbolic verification checks the algebraic identities only. The invariant-measure averaging step and support-invariance argument are mathematical deductions given in `RESULT.md`; they are not replaced by numerical simulation. No claim is made about existence or uniqueness of noncompact trajectories.
