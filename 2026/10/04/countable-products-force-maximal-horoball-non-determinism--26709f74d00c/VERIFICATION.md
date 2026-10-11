---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For any compatible metric \(d\) on the compact countable product, uniform equivalence with a standard summable product metric gives a finite coordinate prefix whose equality forces \(d<\varepsilon\). Infinitely many non-singleton factors supply a distinct pair differing only beyond that prefix. Coordinatewise dynamics preserve equality of the prefix for every group element, so that same pair stays \(\varepsilon\)-close under the whole group. The horoball conclusion is therefore immediate for every horofunction. The expansiveness boundary follows: infinitely many non-singletons forbid any expansivity constant, while a finite product is expansive exactly when each non-singleton factor is expansive.

## originality

PASS

The new horofunction invariant paper defines the non-deterministic sets and proves broad group-dependent restrictions, but its inspected text does not state this countable-product mechanism. A 2014 paper does state that a countable product is expansive iff every factor is expansive, but its converse proof tries to extract a uniform positive constant from coordinate constants divided by exponentially shrinking weights; the tail construction directly refutes that countable-product direction. Current published-finding search returned no earlier correct finite-support expansiveness classification or the stronger global-orbit-closeness implication for every horoball.

## value

PASS

The theorem gives a sharp if-and-only-if boundary for expansiveness of countable coordinate products and immediately forces the newly introduced horoball nondeterminism invariant to be maximal. It also corrects a published countable-product expansiveness claim. The argument is elementary, but the boundary and correction are structurally motivated rather than a routine isolated exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
