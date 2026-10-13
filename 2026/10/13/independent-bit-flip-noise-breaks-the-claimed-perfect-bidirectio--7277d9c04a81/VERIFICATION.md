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

The proof is analytic. The resource factorization follows directly from six disjoint Hadamard-CNOT Bell-pair preparations. Independent bit flips on both halves of a Bell pair have odd parity with probability \(q=2p(1-p)\), and the standard teleportation theorem maps the resulting Bell-diagonal resource to the channel \((1-q)\rho+qX\rho X\). The overlap calculation for the source's Eq. (36) family then gives
\[
F_{\mathrm{Bi}}=1-2q(1-q)(2a^2-1)^2.
\]

The bundled `artifacts/verify.py` uses only Python's standard library and exact rational arithmetic. It checks the parity-average expression against the closed form for multiple rational values of \(a^2\) and \(p\), verifies the exact counterexample \(F_{\mathrm{Bi}}(0,1/2)=1/2\), and checks that the literal common-Kraus-index reading has completeness factor \((1-p)^{12}+p^{12}\neq1\) at an interior noise strength. These finite checks corroborate the algebra and do not replace the symbolic derivation.

The verification does not test the cyclic protocol or any noise model other than bit flip.
