---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Zhang's full arXiv text gives the odd-sector eigenvectors \((|01\rangle\pm e^{i\theta}|10\rangle)/\sqrt2\) with \(\theta=\arctan D\), the two-copy product-Pauli teleportation channel, and the published fixed-Bell-basis average fidelity. The proposed one-qubit phase gate converts those eigenvectors to ordinary Bell states without changing the thermal eigenvalues. Recomputing the four Bell overlaps gives \(q_0=b+\nu,q_1=q_2=a,q_3=b-\nu\); Bloch-sphere averaging on the source's odd-parity logical qubit gives the displayed aligned formula. In the unaligned basis only the real coherence survives, replacing \(\nu\) by \(\nu/\sqrt{1+D^2}\), which reproduces the source formula. Direct algebra yields the nonnegative gain, strict exactly for \(JD\ne0\), and the large-\(|D|\) limits follow from the leading hyperbolic terms. The frozen verifier was read and checks the same identities and representative channel averages.

## originality

PASS

The full Zhang source explicitly calls its fixed-basis expression maximal and states the strong-DM limit \(2/3\); it does not include local DM-phase compensation. General singlet-fraction/local-unitary theory makes basis optimization conceptually natural but does not state this source-specific two-resource logical-qubit formula or its exact positive gain. A closely related 2010 DM-orientation teleportation paper is retained as a concrete residual coverage risk because only accessible preview-level material was available in this run.

## value

PASS

This is a motivated operational correction to a published maximality and asymptotic interpretation: a known local phase compensation changes the strong-DM conclusion from the classical boundary to unit average fidelity while preserving the same thermal resources and Bell/Pauli architecture. That is a substantive counterexample/boundary result rather than a cosmetic reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
