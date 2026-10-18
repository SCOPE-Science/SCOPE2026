---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For a centered ellipsoid apply linear invariance and evaluate the Euclidean-ball Holmes–Thompson polar-volume integral V_E(R)=n ω_n∫_0^ρ t^{n-1}(1-t²)^(-(n+1)/2)dt with ρ=1−e^(−R). Substitute t=tanh s and z=artanh ρ=0.5 log(2e^R−1), obtaining V_E=n ω_n∫_0^z sinh^(n−1)s ds. Published Hanner formula gives V_H=(4^n/(n!ω_n)) z^n. The quotient is a positive constant times z^(−n)∫_0^z sinh^(n−1)s ds = ∫_0^1 u^(n−1)(sinh(zu)/(zu))^(n−1)du, strictly increasing for n≥2 because d(sinh x/x)/dx=(x cosh x−sinh x)/x²>0. z(R) increases strictly, proving ALL 0<r<R two-radius comparisons, not merely tested radii. For n=1 exponent zero gives equality. Independent high-precision numerical checks for n=2,3,6 at z=0.1,0.3,0.9,2 supported algebra but cannot prove the quantified theorem; actual verifier.py similarly only finite consistency.

## originality

PASS

Faifman’s ellipsoid integral and Faifman–Vernicos–Walsh’s Hanner formula are prior ingredients; the latter states the two-radius inequality for arbitrary symmetric convex bodies as explicit Conjecture 10.2. Their one-radius lower bound cannot entail monotonicity of the ellipsoid/Hanner quotient. A separate exact hyperbolic-sine normalization and monotonicity proves the ellipsoid subcase. No covering statement was located in inspected primary passages; the simplicity creates a candid unindexed-notes risk.

## value

PASS

An explicit uniform all-dimensional special case of an open two-radius Funk-volume conjecture is a motivated standalone comparison, not a routine single-value substitution. The strict monotonicity across every radius adds control not supplied by the previously known fixed-radius Hanner bound and is potentially useful for interpreting reversed Bishop–Gromov behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
