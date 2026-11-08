---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For a+b=2h>0, season half-width t=T/2>0, g>0 and real mean r, both seasonal matrices have trace 2(r-h). Their traceless parts M1,M2 satisfy M1²=κ_-²I, M2²=κ_+²I and half tr(M2M1)=h²-g², giving the exact normalized monodromy half-trace C_p(t) with p=ab. The rational Laplace identity C_hat=s/(s²-4h²)[1-16g²p/((s²-4h²)(s²-4g²))]^{-1} yields a Volterra series in p with nonnegative causal kernel and strictly positive convolution coefficients at t>0. Thus C_p(t)>C_0(t)=cosh(2ht)>1 for p>0, strictly increasing for p from zero to h², and λ=r-h+T^{-1}arcosh C_p(T/2) increases strictly. Balancing a=b uniquely maximizes; one-way boundaries both give λ=r. For r<0 a viability threshold exists iff balanced λ>0, with unique p_* solving C=cosh((h-r)T); critical equality covered. Taylor fourth coefficient C_p−cosh(2ht)=(2/3)g²p t⁴+O(t⁶) produces λ−r=g²p T²/(24h)+O(T⁴). Independent scipy matrix exponentials for h=g=1,T=4,r=-1/5 reproduce endpoint -0.2, imbalanced -0.0024963625 and balanced +0.0426584316. Finite values are only corroboration.

## originality

PASS

PASS on the sharp fixed-total-transport-rate directional balancing law for equal-mean exactly antiphase square waves. The most relevant Benaïm et al 2023 primary paper treats non-symmetric migration but its §4.3 compares fixed migration direction and varying scalar intensity with unequal local means; it shows numerical Floquet curves, not a theorem that at fixed a+b all periods and contrasts optimize at a=b. Supplementary S1 concerns three-patch directional migration. Broader growth criteria do not imply this strict p=ab ordering. Specialized equivalent spectral inequalities remain a realistic but not decisive priority risk.

## value

PASS

Migration direction is a natural controllable resource under a fixed total-rate budget; its exact optimizer and sharp necessary-and-sufficient survival corridor resolve a concrete model design problem, including strictness, equality and one-way boundary. The positive Volterra kernel supplies structural explanation, not arbitrary parameter fitting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
