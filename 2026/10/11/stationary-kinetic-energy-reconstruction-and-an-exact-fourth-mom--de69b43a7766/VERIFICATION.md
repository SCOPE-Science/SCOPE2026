---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS. Invariance against antiderivatives H(x) gives E[v|x]=0, and against phi(x)v gives E[phi_prime(x)v²]=E[x phi(x)] with damping term cancelled by the conditional mean. In distributions eta_prime=-x rho; mean x=0 and compact support make q(x)=integral_[x,infty) s rho(ds) compact supported with q_prime=-x rho, and finiteness excludes constant-Lebesgue ambiguity, so eta=q(x)dx. Monomial phi gives hierarchy E[x^k v²]=E[x^(k+2)]/(k+1); stationary energy gives E[(1-x²)v²]=0, hence E[x⁴]=3E[x²]. Cauchy–Schwarz and invariance exclude E[x²]=3 for non-origin invariant measures; kinetic density and zero balance force both sides of |x|=1 visited in kinetic mass. Independent sparse/symbolic generator checks k0..11 and energy confirmed algebra but not distributional argument.

## originality

PASS

PASS best-of-knowledge. Fantuzzi–Goluskin–Huang–Chernyshenko full primary time-average paper studies the identical van der Pol vector field but SOS bounds long-time averages x²+v² rather than exact marginal inversion and the fourth moment identity; complete text and targeted searches were inspected. The virial test-function identity for all compact stationary measures is stronger than a single orbit numerical bound and reconstructs kinetic mass as a function of position law, not inferable from the previously published SOS bounds. The generator calculus is classical, so older unindexed moment identities for this oscillator remain risk.

## value

PASS

PASS. From the physically natural stationary position marginal, the precise kinetic-energy density and all stationary moments are reconstructed, giving a parameter-independent fourth-moment constraint and necessary pump/dissipation threshold crossing for all compact invariant states. The full distributional identity is more meaningful than a single cheap polynomial identity, and could inform moment-bounding of stationary nonlinear oscillations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
