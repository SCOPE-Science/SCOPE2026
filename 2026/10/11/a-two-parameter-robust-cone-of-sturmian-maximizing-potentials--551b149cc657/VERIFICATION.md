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

The proof was checked symbolically from the definitions and against the focal preprint's proof of Theorem C.

For each invariant probability \(\nu\), set \(D_1=\alpha-\int\Phi\,d\nu\) and \(D_2=\int\Psi\,d\nu\). The source proves \(D_1,D_2\ge0\) and, before replacing coefficients by a common constant,
\[
W_\theta(\nu,\mu_\alpha)\le (1-\theta)^{-2}D_1+[1+2(1-\theta)^{-3}]D_2.
\]
The weighted potential gap is exactly \(pD_1+qD_2\). Multiplying the right-hand side of the Wasserstein estimate by \(\min\{p(1-\theta)^2,q/[1+2(1-\theta)^{-3}]\}\) is therefore termwise bounded above by that gap.

For perturbations, the only additional input is the defining dual estimate for Wasserstein distance against a Lipschitz test function. Strict inequality of the perturbation seminorm gives a strictly positive optimization gap for every distinct invariant probability.

Boundary checks: \(p,q>0\) makes the certified margin positive; no claim is made at \(p=0\) or \(q=0\). At \(p=q=1\), the margin reduces to the published radius \([1+2(1-\theta)^{-3}]^{-1}\). The cone proof uses no hidden compactness or differentiability assumption beyond the symbolic Lipschitz setting already present in the source.

No numerical experiment, finite enumeration, or timeout is used as evidence for the theorem. The quantitative radius is sufficient, not claimed optimal.
