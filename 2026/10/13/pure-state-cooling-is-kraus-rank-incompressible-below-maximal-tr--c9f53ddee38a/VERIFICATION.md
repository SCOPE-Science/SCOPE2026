---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For a minimal Kraus family K_j, the linear map psi -> (⟨G|K_j|psi⟩)_j has rank at most r. If r<d, a unit vector in its kernel is sent to a state supported on G-perp, attaining norm difference 2; the triangle inequality gives the matching upper bound. The exact replacer has Choi matrix I_d tensor |G⟩⟨G|, with rank d. A pure m-mode environment gives at most 2^m Kraus operators after a single coherent unitary evolution and final trace, so uniform error below 2 implies m>=N. In the unconstrained model the exact replacer dilation at m=N can be extended to a joint unitary. Yu–Chen–Lin's model and Theorem 1 provide the stated 2N-mode comparison under their physical hypotheses. No numerical experiment is required.

## originality

PASS

Credit the established environment-rank equivalence, exact pure-output rank bound and the existing cooling protocol. The distinct assertion supported by the bounded review is the maximal worst-case statewise trace-norm error for every rank-deficient approximant to a pure replacer and its sharp no-reset resource consequence, not the exact rank or the cooling construction alone.

## value

PASS

The result isolates a sharp discontinuity for worst-case cooling: even tolerance arbitrarily close to the maximum yields no environment compression relative to exact replacement. This turns the bath resource comparison into a quantitative statement against the unconstrained information-theoretic minimum, rather than simply restating the exact replacer's rank or counting the modes used by an existing protocol.

The dated certificate retains the supplied scientific assessment, sources and limitations.
