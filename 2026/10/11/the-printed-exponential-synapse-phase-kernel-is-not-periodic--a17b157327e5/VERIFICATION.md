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

The source reset rule states that the synaptic gate jumps to \(1\) whenever the presynaptic neuron spikes and otherwise solves \(\dot s=-\beta s\). On one period this gives \(s(t)=e^{-\beta t}\) after choosing the spike as phase zero, and cyclic phase therefore gives \(s_\phi(t)=e^{-\beta((t+\phi)\bmod T)}\).

The printed one-branch expression was substituted directly into the source interaction integral. It yields a constant multiple of \(e^{-\beta\phi}\); its odd part is a constant multiple of \(\sinh(\beta\phi)\). Hence it is not periodic and, unless identically zero, has no half-period zero. This conflicts with the source's earlier structural statement that the interaction is periodic and with its anti-phase equilibrium at half a period.

The correction is local and exact. No numerical experiment is required. The verification does not assess unpublished code, so it does not claim that the numerical figures were computed from the erroneous literal formula.
