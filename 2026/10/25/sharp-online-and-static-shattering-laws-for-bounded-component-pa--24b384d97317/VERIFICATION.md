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

The source `verify.py` is a standalone standard-library Python verifier. It enumerates irreflexive directed relations as Boolean adjacency matrices, filters the exact transitivity and antisymmetry conditions, computes finite shattering ranks directly from the resulting concept class, and checks every branch and terminal witness of both accompanying certificates. The distinct `build_certificate.py` generator enumerates each unordered pair in three orientation states and independently derives the trees by Littlestone recurrence. Actual verifier output is in `verification_output.txt`.

For all \(n\ge1\), the arbitrary-size bounded-component VC classification is proved by a transitive-reduction equivalence and Mantel's bound, not by extrapolating finite computations. For \(b\le4\), the unrestricted Littlestone identity follows from the positive-coordinate mistake upper bound and concatenation of certified finite trees. The Python verification covers the local certificates and small cases, not the infinite quantifiers.

No independent audit, external certification, or historical-priority guarantee is asserted.
