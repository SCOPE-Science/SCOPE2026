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
For a symmetric random-walk proposal
\[
q(v^*\mid v)=q(v\mid v^*),
\]
the Metropolis–Hastings acceptance probability for target \(\pi\) is
\[
\alpha(v,v^*)=
\min\!\left\{1,\frac{\pi(v^*)}{\pi(v)}\right\}.
\]

The source's conditional posterior from Eq. (3.5) was implemented up to its normalizing constant. For
\[
(\gamma,\eta,\xi)=(1.2,1.8,0.9),
\]
\[
x=(0.7,1.3,2.0),\qquad y=(0.8,1.7),
\]
and the move \(0.7\to1.0\), the packaged checker obtains a nonunit target ratio.

It then compares the forward and reverse probability fluxes under a symmetric displacement-only acceptance rule. They differ by the target-density ratio, directly exhibiting failure of detailed balance.

The finite example is supplemental. The general proof is the cancellation argument for symmetric proposal and acceptance kernels.
