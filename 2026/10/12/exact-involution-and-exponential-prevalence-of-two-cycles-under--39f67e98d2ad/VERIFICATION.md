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

The standalone `verify.py` enumerates all simple undirected intralayer graph pairs and all spin configurations for \(N=1,2,3\), with coupling \(j=\Delta+1\). It verifies that each local sign-field update equals \((A,B)\mapsto(-B,-A)\), that the update squared is the identity, that exactly \(2^N\) microstates are fixed, and that the remaining states partition into exactly \((4^N-2^N)/2\) two-cycle orbits.

With exact rational arithmetic, it also sums the paper's independent product initialization law at biases \(r\in\{1/3,1/2,2/3\}\), obtaining the claimed stationary and homogeneous-polarized probabilities for these sizes. An explicit complete-graph example tests the boundary at and below the maximum degree.

The checker is a bounded reproducibility test, not an exhaustive proof at all population sizes. The universal proof comes from the deterministic sign-dominance inequality, the fixed-point equation, and independent Bernoulli counting. It does not examine coupling strengths outside the specified strong-antagonism domain, noisy updates at nonzero fields, or asymptotic dynamics of a smooth regularization. Independent audit has not been performed.
