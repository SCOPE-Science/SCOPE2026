---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

From the actual pinned RESULT.md, m>=2, a=2^(m-1), x>=0 and P_m=(1+e^[-2(2a-1)x])/[2(1+e^(-2ax))]. Verified hyperbolic-sine cancellation against the original El Allati et al. Eq. (18). In q=e^(-2x), the derivative numerator is q^(a-1)[(2a-1)q^(a-1)+(a-1)q^(2a-1)-a], whose bracket is strictly increasing from -a to 2a-2, proving one interior minimum (q decreases with x). At its root u=q^a, the equation limits to 2u+u^2=1, with the only (0,1) solution sqrt(2)-1. This proves scaled minimizer 2^m*x_m -> log(1+sqrt2), minimum -> sqrt2-1, and global uniform deviation 3/2-sqrt2. The fixed-t boundary profile follows by substituting x=t/2^m; fixed x>0 tends to 1/2, x=0 equals 1/2 exactly. Independently computed minimizers m=2,3,4,6,12 against both limits and verified the derivative sign analytically. The underlying quantum-state derivation is not independently validated; this is a conditional formula theorem.

## originality

PASS

The new claim was compared at the level of mathematical implication against the explicitly identified primary sources and Resultary findings. Existing core definitions/classical identities are credited; no stronger previously published result covering the precise new structure was found in material inspected, subject to named residual risks.

## value

PASS

The new quantitative boundary-layer profile resolves precisely what a published physical interpretation of large-participant intensity independence means: pointwise convergence conceals a nonvanishing global success-probability deficit. The sharp layer width 2^(-m), unique minimum and exact worst-case limit have direct operational meaning for a specific quantum-network success metric rather than being an arbitrary change of variables; no claims about fidelity or experimental devices are made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
