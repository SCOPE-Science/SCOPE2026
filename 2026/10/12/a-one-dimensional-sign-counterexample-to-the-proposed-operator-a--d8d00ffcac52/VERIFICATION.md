---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The primary paper's Assumption4 says ⟨b_k(x),x−x*⟩≤η⟨Q(x),x−x*⟩, but its Lemma1 uses this as a lower bound to derive ≥µ(1−η)||x−x*||². With x*=0 and b=-2x, the printed condition holds (-2x²≤0) yet Q+b=-x reverses descent. The projected recursion gives x1=1 and xk=1 forever. The source's differentiability/compact convex set/strong convexity/quasi-gradient linear-growth/boundedness/zero-noise hypotheses are satisfied. Independent exact rational replay ran 20 steps, showing no rate decay. The correct sufficient sign for the specific contraction line is ⟨b,d⟩≥−η⟨Q,d⟩, coupled with a separately valid Q lower bound; no full replacement theorem is claimed.

## originality

PASS

The concrete scalar construction directly refutes a specific published Assumption4-to-Lemma1 inference. Standard relative-gradient-error robustness results impose genuinely different magnitude/angle controls and do not supply an already printed correction to this article.

## value

PASS

The counterexample invalidates the core deterministic contraction estimate and advertised strong-convexity rate under the paper's printed assumption. Even a one-dimensional witness is scientifically valuable because it pinpoints the exact missing direction of bias control in an apparently broad convergence claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
