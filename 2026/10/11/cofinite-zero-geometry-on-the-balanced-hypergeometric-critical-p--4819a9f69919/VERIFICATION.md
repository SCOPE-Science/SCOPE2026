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
# Verification record

The baseline sector-uniform \({}_1F_2\) asymptotic was checked against equation (2.1) of Cho–Chung–Park, DOI 10.1007/s11075-025-02158-x. Under \(b+c=3a+\tfrac12\) it yields exactly \(\sigma=2a\), model \(R+\cos(z-\pi a)\), and first sinusoidal correction \(d/(2z)\). Nonvanishing of the normalization on the right half-plane and simple-model-root condition \(|R|\ne1\) were checked.

The proof explicitly establishes absence of uncounted large zeros via an exponential lower bound away from a periodic disk family. Rouché counts exactly one per disk; reflection confirms real zeros in the real-model regime. The first-order location expansion follows from Taylor's theorem and the nonzero sine at each limiting root. The counting coefficient is two roots per period \(2\pi\).

Exact special-parameter checks: \((a,b,c)=(\tfrac12,\tfrac14,\tfrac74)\) has \(R=-1/\sqrt2\). At \((\tfrac14,\tfrac18,\tfrac98)\), exact rational substitution gives \(d=-3/16\). The strict nonreal-regime example follows from \(\Gamma(1/4)>16/5\) and \(\pi<22/7\), without numerical certification.

Limits: the published asymptotic is used as input, not reproved; exceptional bounded zeros are not enumerated; the coalescent \(|R|=1\) case is outside the claim. No independent audit has been performed.
