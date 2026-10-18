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

# Finite and analytic verification

The claim is the sharp probability of nonrepresentability of a row-normalized independent-uniform stochastic matrix when one prescribed deterministic map is disallowed. The analytical argument has five independently articulated steps in `RESULT.md`: (1) support-polytope criterion with constructive coupling, (2) exact coordinate density envelope, (3) Dirichlet-simplex integral coefficient, (4) gamma concentration plus uniform integrability, and (5) exponentially small exceptional-corner contribution. The \(n=2\) boundary is treated separately. No computer enumeration is offered as a proof for all \(n\).

Run `python verify.py` with Python 3, NumPy and SciPy. An actual execution completed **259 finite checks**: 240 linear-programming comparisons for \(n=2,3\), 10 numerical density identities for the \(n=3\) Irwin–Hall ratio, six Dirichlet importance-sampling corrections, and three logarithmic normalization checks. Very-near-boundary LP instances are excluded only when the sign is at or below a specified numerical tolerance, to prevent treating a solver-tolerance decision as mathematical evidence. The sampled importance ratios, ordered by dimensions \(5,8,12,20,40,80\), were \(0.956741,0.977207,0.984713,0.991160,0.995598,0.998153\). These estimates support but cannot establish their infinite-dimensional limit.

The independent-uniform input distribution and exact \(\mathrm{Beta}(a,b)\) Dirichlet comparison marginals are crucial: substituting Dirichlet-distributed transition rows changes the event probability. The error term in the asymptotic is an unspecified relative \(o(1)\). No independent audit has been performed.
