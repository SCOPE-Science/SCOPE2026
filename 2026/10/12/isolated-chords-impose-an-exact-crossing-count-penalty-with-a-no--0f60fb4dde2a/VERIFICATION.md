---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For a distinguished rooted chord enclosing 2k points and leaving 2(n−1−k) outside, isolation is equivalent to no crossing of the two arcs; conditional independent matchings make EX=[C(k,2)+C(n−1−k,2)]/3. Root symmetry multiplies by n, while unconditional EX=n(n−1)/6; subtracting gives a strictly negative sum with summand n−1+k(n−1−k). End terms k=0,n−1 are circularly adjacent chords and yield -2n(n−1)/(3(2n−1)); k=1,n−2 give the non-simple -1/3 limit, with remaining terms O(1/n) in covariance via geometric-ratio bounds. Independently generated all perfect matchings and rational covariances for n=2 through 6; exact concordance including equality only at n=2. Separate finite checks are not used as the all-n proof.

## originality

PASS

Same mathematical objects, parameters, quantifiers, and prior implications were compared using the identified primary material and a fresh published-findings semantic query. No covering prior theorem was identified in the material read; the listed residual risks limit this best-of-knowledge assessment.

## value

PASS

The two natural statistics of a random chord intersection graph, its isolated-vertex count and edge count, have a novel exact dependence law. The surprising nonvanishing -1/3 covariance correction from chords whose expected count tends to zero is a substantial probabilistic refinement, not recoverable by replacing all isolates with simple chords.

The dated certificate retains the supplied scientific assessment, sources and limitations.
