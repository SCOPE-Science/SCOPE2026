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

The proof is analytic. The critical steps are: (1) contractivity under the pinching channel associated with \(P\); (2) additivity of the trace norm across the accepted and rejected blocks; (3) \(\|X\|_1\ge|\operatorname{Tr}X|\); and (4) the triangle inequality applied after scaling the two normalized accepted states by the larger acceptance probability.

The sharpness family is diagonal on three basis states, so its trace distances reduce to exact finite sums of absolute values. For \(p\ge q\) and \(c=\min\{1,\tau/p\}\), it has
\[
D(\rho_P,\sigma_P)=c,\qquad D(\rho,\sigma)=\max\{p-q,pc\}\le\tau.
\]
The case \(q\ge p\) follows by swapping the states.

`artifacts/verify.py` checks hundreds of random density-matrix/projector instances and several exact equality regimes. A finite random test cannot prove the universal theorem and is not treated as such. The checker does not test arbitrary effects or multistage postselection because those are outside the claim.
