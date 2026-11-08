---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Reconstructed continuous-time Markov chain +/0/- with run termination alpha, rest departure beta, freshly biased direction w=2p-1, and stable Ornstein–Uhlenbeck filter. Its stationary distribution and joint generator recurrence (nI-Q^T)m_n=nV m_(n-1) give M1,M2,M3 without moment closure. Independently computed SymPy inverse systems and simplified central third moment exactly to the stated P(a,b,w) numerator divided by positive denominator. Independent Brownian Gaussian contributes zero third cumulant. For fixed a>0 and w in (0,1), P decreases strictly on (0,a) from positive to negative and stays negative for b>=a; unique root b*(a,w)<a increases strictly in w and approaches a as w->1. w=0 symmetric exceptional case and w=1 endpoint separated. Finite numerical tests do not establish the all-parameter sign proof.

## originality

PASS

Best-of-knowledge original biased finite-duration run/rest confined skewness sign diagram. Sun–Ye–Podgornik exact finite tumbling harmonic trap uses unbiased reorientation and explicitly lists biased orientations as future work. Basu et al. handle symmetric three-state trap; Guéneau–Majumdar–Schehr biased velocities use instantaneous switches without positive resting phase; Santra–Olsen–Gupta biased intermittent motion is unconfined. Although standard generator recurrences compute moments, an explicit unique rate frontier is not an inspected corollary.

## value

PASS

Natural experimentally interpretable distinction: displacement mean stays positive while shape skewness reverses at a single polarization-dependent rest-to-run threshold, robust to independent thermal noise. An exact phase diagram for a tractable but nontrivial three-state model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
