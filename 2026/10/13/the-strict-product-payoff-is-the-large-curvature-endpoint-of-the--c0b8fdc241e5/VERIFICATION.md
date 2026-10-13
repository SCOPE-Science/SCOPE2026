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
The bundled checker exhausts all eight binary triad configurations and verifies
\[
\max\left|
(S/3)^\gamma-\mathbf 1_{\{S=3\}}
\right|=(2/3)^\gamma.
\]
It then constructs all one-update transition probabilities on a complete three-player pairwise graph with one triad, where
\[
d_i^{(2)}=2,\qquad d_i^{(3)}=1,\qquad q_*=\frac13,
\]
using the published normalized payoff, Fermi rule, and mutation step. For several \(\gamma\), it verifies
\[
\sup_x\|P_\gamma(x,\cdot)-P_\infty(x,\cdot)\|_{\mathrm{TV}}
\le\frac32\alpha r q_*(2/3)^\gamma.
\]
The finite replay checks implementation consistency; the general theorem is analytic.
