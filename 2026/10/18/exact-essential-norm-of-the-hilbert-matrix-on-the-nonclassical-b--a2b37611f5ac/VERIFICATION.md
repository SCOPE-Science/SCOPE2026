---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

On the complex derivative-weighted Bloch space with precise additive norm |f(0)|+sup_z(1-|z|²)^α|f′(z)|, 1<α<2, integration of a derivative bound gives |f(t)|<=|f(0)|+||f||_*F(t), F(t)=∫_0^t(1-s²)^-α ds, integrable near t=1 exactly for α<2. The Hilbert derivative kernel asymptotically yields A_α(r)=(1-r²)^α∫ tF(t)/(1-tr)² dt→B(α-1,2-α), while constant-function contribution vanishes at boundary. Compact D_ρH approximations give essential norm upper bound by positive radial kernel domination; for lower bound f_n′(z)=z^n/[2^α(1-(1-n^-4)z)^α] are unit-ball functions, locally tend to zero and, as elements of little Bloch embedded in C0(𝔻), are weakly null by finite-measure duality; any compact K kills them. Rescaling at r_n=1-n^-2 gives the sharp same beta boundary integral, showing ≥C_α for every compact K. It is critical that this is weak convergence in full Bloch, not merely local compact-open convergence. Independently computed B(α-1,2-α)=B(2-α,α)/(α-1), yielding constants 4.44288293816, π, 4.44288293816 for α=1.25,1.5,1.75. These Beta diagnostics supplement, not prove, the weak-null argument.

## originality

PASS

The final claim, not its title or shared elementary ingredients, was compared against statement-level prior implications, published records and highly relevant primary literature. The named check objects and actual inspections below support best-of-knowledge originality, with inaccessible material separately identified as residual risk.

## value

PASS

The exact essential norm is the natural Calkin-space invariant determining the noncompact component of the Hilbert integral operator on the SAME derivative-weighted α-Bloch space. It is not determined by prior full operator-norm estimates: compact approximation can reduce norm. The constructed weakly-null boundary family supplies a meaningful obstruction, and the matching dilation upper bound gives an exact parameter-dependent coefficient; a future operator-theory comparison can use this invariant directly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
