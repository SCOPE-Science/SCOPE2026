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

The accepted claim was checked by direct symbolic reconstruction. The concentration branch uses \(K_t=t|0\rangle\langle0|+|1\rangle\langle1|\) with \(t=\tan\theta/\tan\phi\); the output coefficients are proportional to those of \( |\psi_\phi\rangle \) and the squared norm is \(\sin^2\theta/\sin^2\phi\). The dilution branch uses the particle-hole conjugate filter and has squared norm \(\cos^2\theta/\cos^2\phi\).

For the upper bound, a successful fine-grained terminal branch can be corrected by local Gaussian unitaries to diagonal parity-even form without changing its effect operator. Exact conversion then forces one equality for the \(|00\rangle\) component and one for the \(|11\rangle\) component. Summing over successful branches and taking the corresponding diagonal matrix elements of terminal Kraus completeness yields the two independent probability inequalities. Their minimum is therefore universal in the stated protocol class.

The Gaussianity of the filter used for concentration was checked against Appendix D.1 of arXiv:2609.15059v1; the dilution filter is its particle-hole conjugate. The unrestricted-LOCC benchmark was checked against Vidal's primary theorem. No numerical grid, optimization log, or finite enumeration is used to justify the universal statement.

Limits: this verification does not extend the theorem to unresolved multi-Kraus Gaussian instruments, many-copy protocols, catalysts, or approximate conversion. Independent audit has not been performed.
