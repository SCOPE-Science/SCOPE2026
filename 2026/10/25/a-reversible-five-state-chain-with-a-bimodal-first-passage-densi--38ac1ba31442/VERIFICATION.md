---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For an irreducible symmetric-rate five-state generator, killing the target gives the displayed real-symmetric 4x4 Q. The passage density f=e_0^T exp(Qt)r has derivative e_0^T exp(Qt)Qr. Four sign samples at t=0.01,0.03,0.10,0.30 are +,-,+,-, with certified rational 400th-order Taylor intervals and spectral-norm tail <2e-107; independent expm checks give ~11.15970,-0.67305,0.02506,-0.13653. They force two interior maxima. For <=4 total states there are <=3 real exponential eigenmodes; the derivative of a nonzero sum of at most m distinct real exponentials has at most m-1 zeros, hence two maxima requiring three zeros need >=4 transient states. Repeated eigenvalues combine because reversibility diagonalizes Q. Initial state, target, full-chain irreducibility and uniform detailed balance checked.

## originality

PASS

The exact minimal five total states for a bimodal first-passage density in an irreducible finite reversible CTMC with one fixed start and one target was not located in inspected primary sources. Spectral expansions and birth-death unimodality are established antecedents, but a general spectral representation alone does not imply the specific minimal bimodal witness. A particularly close 1987 reversible-chain paper was inaccessible in full; best-of-knowledge PASS with explicit priority risk.

## value

PASS

First-passage modality is natural in stochastic kinetics; showing that reversibility alone permits two density peaks, with a sharp state-minimal counterexample, identifies a meaningful boundary beyond the birth-death unimodality class. The claim does not classify all graphs/rate matrices or higher multimodality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
