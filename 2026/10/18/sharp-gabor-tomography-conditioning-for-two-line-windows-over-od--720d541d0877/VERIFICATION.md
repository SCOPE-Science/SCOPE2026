---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The two self-intersections give q times the respective translation/frequency delta terms (the horizontal one weighted by |c|²), and the two mixed intersections give the displayed character phases. Weyl conjugation diagonalizes the Hilbert–Schmidt frame operator by character orthogonality, giving eigenvalues N|A_c/Q_c|² and largest N from the identity. For both translation coordinates nonzero, relative frequencies range uniformly over p roots, so some resultant is at most 2|c| sin(π/(2p)). The norm bound Q_c≥2(q−1)|c| is strict except at c=−1. There the minimum is 2 sin(π/(2p)) before normalization; the remaining cases give either a sum of two roots, q−2, −2 or 2(q−1). The support at c=−1 cannot have a nonzero translation period (its size is not divisible by p). A modulation constant on a punctured axis has phase equal to its inverse by the two arguments t and −t, hence phase one in odd characteristic; requiring this on both axes forces trivial modulation. This proves uniqueness of the largest eigenvalue. Two closest relative phases contribute 2(q−1)²q²/p off-axis and 4(q−1)q²/p on one axis. At q=3 the additional q−2 cases contribute 12+4, giving 64. Independent direct sums at q=3,5,9 give bottom multiplicities 64,240,4320, with top multiplicity one in each case (python -B /workspace/branches/audit-replay.py 1). The character argument, not the finite replay, proves the claim for all odd prime powers.

## originality

PASS

The supported advance is the sharp weighted two-line minimax, its unique optimizer and extremal multiplicities. Neither operator-frame conditioning via ambiguity coefficients nor the Weyl/Gram spectrum machinery is new.

## value

PASS

In the natural support family of two lines, canceling the intersection yields an operator basis from only 2(q−1) support sites. Characteristic rather than field size controls the closest opposing phase; the exact minimax quantifies amplification and the multiplicities count least stable Weyl directions. This is a sharp sparse tomography design result on a stated family, not an optimum over arbitrary windows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
