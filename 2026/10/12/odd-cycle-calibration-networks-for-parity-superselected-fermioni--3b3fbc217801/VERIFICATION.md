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

The analytic proof uses only the source pair-response identity on valid calibration edges and elementary finite-dimensional linear algebra.

For a calibration graph \(G\), the unsigned incidence matrix \(B_G\) satisfies \(s=B_Gb\) and \(Q_G=B_G^{\mathsf T}B_G\). The kernel calculation is exact: \(B_Gx=0\) requires adjacent coordinates to be negatives, so a connected bipartite component carries a nonzero alternating vector, whereas an odd cycle forces that vector to vanish. This establishes the identifiability criterion for every finite graph.

The stability inequality is the exact operator-norm identity
\[
\|B_G^{\dagger}\|_2
=\lambda_{\min}(Q_G)^{-1/2}
\]
when \(Q_G\) is positive definite. No stochastic independence is assumed. The edgewise error bound follows from \(\|e\|_2\le\sqrt{|E|}\eta\).

The edge-minimality argument uses only that every connected non-bipartite graph has at least one cycle and therefore at least as many edges as vertices; equality means unicyclic, and identifiability makes the unique cycle odd.

The standalone standard-library script `artifacts/verify.py` was executed from the final package directory and returned `VERIFY_OK`. It verifies exact recovery for sample odd cycles, exhibits the even-cycle alternating kernel, and checks the stated odd-cycle least-eigenvalue formula numerically for several sizes. These finite checks do not replace the all-graph proof.

Limits: this verification does not test physical embeddability of an arbitrary abstract marker graph and does not re-prove the source paper's Proposition 5.8. The theorem assumes that proposition's termwise-separation hypotheses hold on every selected edge and that any marker used for target correction satisfies the source's target-marker separation requirement.
