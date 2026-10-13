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
# Verification

The recent source was checked at Theorems 1.1 and 1.2, Propositions 4.1 and 4.2, Corollary 5.3, and Proposition 6.5. Corollary 5.3 states that every positive-rank divisor on a metric banana path has a lift to a positive-rank divisor on a smooth proper curve with the same skeleton and the same genus.

Choose a divisor \(D\) of minimal positive-rank degree
\[
d=\operatorname{gon}(\Gamma).
\]
The lifted divisor has degree \(d\), so the resulting curve \(X\) satisfies \(\operatorname{gon}(X)\le d\).

The Amini--Baker specialization inequality was checked independently: divisor rank cannot decrease when passing from a smooth proper curve to its associated tropical data, and the underlying metric-graph rank is at least the metrized-complex rank. Consequently any positive-rank divisor \(A\) on \(X\) specializes to a positive-rank divisor on \(\Gamma\) with the same degree. Therefore
\[
\deg(A)\ge d,
\]
and hence \(\operatorname{gon}(X)\ge d\). This gives exact equality.

The broader comparison with Amini--Baker--Brugallé--Rabinoff was inspected in the full paper. Their general non-augmented gonality-lifting discussion allows increasing vertex genera, while their augmented examples show that exact gonality-preserving lifting is not automatic in general. The genus-preserving banana-path conclusion is therefore a materially stronger specialization of the new divisor-lifting theorem.

No finite experiment, heuristic enumeration, or inaccessible premise is used in the proof. No assertion is made about uniqueness, every possible lift, or higher-rank gonality-sequence preservation.
