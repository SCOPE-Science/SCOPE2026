---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Unitary reduction to z=(z′,z_n), s=||z′||² gives u=−(1−s)^q. Its Levi eigenvalues include q(1−s)^{q−1} and radial q(1−s)^{q−2}(1−qs), nonnegative for 0<q<=1; missing z_n curvature means top Monge--Ampère vanishes. On each fixed z′ complex disk |z_n|<sqrt(1−s), any admissible PSH minorant w has boundary upper limit <=−(1−s)^q and the one-variable subharmonic maximum principle forces w<=u. Conversely u is PSH and lies below φ=−|z_n|^{2q} since |z_n|²<1−s, giving envelope equality; the unit-sphere trace matches. Minimum u=−1 iff z′=0. For q>1 the radial eigenvalue is negative whenever s>1/q, available for n>=2, so same closed form is not PSH. The analytic proof is full, not inferred from experiments.

## originality

PASS

Best-of-knowledge: the 2026 Dao--Nguyen paper establishes maximality, continuity and boundary principles for a broad obstacle class, but its inspected ball examples are logarithmic or divisor-based and do not state the explicit all-0<q<=1 one-coordinate finite obstacle or the q>1 Levi threshold.

## value

PASS

PASS: This is a complete exact solution of a natural continuous family of finite superharmonic obstacles, with a holomorphic disk-filling minimum set and sharp failure threshold for an explicit geometric ansatz. The disk-fiber comparison plus Levi sign are motivated exact boundary phenomena beyond restating abstract existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
