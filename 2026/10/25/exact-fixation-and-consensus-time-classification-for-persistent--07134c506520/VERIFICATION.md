---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For K3 with six equally likely ordered focal/speaker choices, two opinion colors, pre-update zealot flags c_i=1_{eta_i>=1}, full reset on disagreement and Δη>=1, the flag process is an exact closed finite Markov chain. Reconstructed all six mixed (z,m) classes, including probability complement when tracked color becomes majority and unanimous boundaries. Harmonic residuals confirm f(z,m)=[105+36z-(25+4z)m+binom(m,2)]/339 and mean time g(z,m)=[621+366z+(105+3z)m-87binom(m,2)]/131. Every mixed state hits consensus with probability≥1/9 in two attempts by twice choosing a minority focal voter against majority speaker; hence hitting equations uniquely determine finite expectations and absorption probabilities. Independent Fraction enumeration verified all 48 labeled mixed-state probability and mean-time identities. Numerators establish minority wins above 1/3 iff z=1,m=0, and all six mean times exceed classical 3; at N=2 every opposing pair resolves at first update. No large-N generalization claimed.

## originality

PASS

Best-of-knowledge originality: the full-reset zealot mechanism is credited to prior PVM authors; inspected primary model/coarsening material does not state the exact K3 six-class rational fixation and time census. The classification is a concrete new-looking microscopic consequence requiring exact finite analysis.

## value

PASS

A complete all-confidence-flag classification of the smallest nontrivial complete-graph persistent-voter process supplies a motivated microscopic benchmark and sharp counterexample to classical voter initial-fraction fixation. The six exact probabilities and mean times resolve concrete questions at the first network size where intrinsic zealotry matters; value does not depend on a large-network theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
