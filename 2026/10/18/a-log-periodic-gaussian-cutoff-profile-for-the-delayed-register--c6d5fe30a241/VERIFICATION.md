---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

At t=mk+r, register rotation sends distinct multiplier sets to distinct original coordinates, giving exactly k−r independent product-sign biases u=a^m and r biases v=a^(m+1) and the finite TV double-binomial sum. With centered time floor k(log k/(2b)+s), b=−log a, phase θ={log k/(2b)+s}, the sum of squared biases tends to e^(−2bs+2bθ)[(1−θ)+θ e^(−2b)], with max bias O(k^(−1/2)). Taylor expansion plus bounded-array CLT yields Gaussian log-likelihood N(−z²/2,z²) and TV=2Φ(z/2)−1. H_b(θ)>1 in interior but H_b(0)=H_b(1)=1, giving distinct subsequential curves; chi-square and Hellinger yield the order-k cutoff window. Independently checked finite exact small-k product laws against explicit transition iteration; finite tests do not certify CLT.

## originality

PASS

Judd–Esposito explicitly covers stationarity/state-independence and complete-k-block TV law for this delayed-register model; those are treated as prior. A two-bias partial-block identity and log-periodic Gaussian subsequential profile are not verified from the accessible source text; the manuscript’s full text was inaccessible, so the priority comparison retains that serious risk. Levin–Tankala concerns a distinct XOR-based randomization kernel.

## value

PASS

This is a concrete transition-kernel example of lattice-phase nonconvergence of a cutoff profile despite sharp total variation cutoff. It quantifies the cyclic update schedule at partial block times and supplies an exact finite-time formula and nonconstant phase correction beyond the previously published complete-block identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
