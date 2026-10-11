---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The binary-effect reduction is valid because each branch's optimal Bob success is a supremum of linear functionals of Alice's effect, so the two-branch objective is convex on the qubit effect interval and has a maximizing projection. The dependence on the out-of-trine-plane component can be removed and radial convexity pushes the remaining Bloch vector to the unit circle; trine symmetry reduces the projective axis to one sector. For each posterior weighted trine, the qubit Helstrom dual is exactly a smallest additively weighted enclosing-circle problem, with only pair-active and three-active possibilities. Substitution of the two branch posteriors gives the stated piecewise analytic score and shows the sector maximum occurs at the symmetry axis. At that point the active pair formula reduces to the displayed radical. Independently, a fresh 5001-point scan of the full symmetry sector using the pair/triple Helstrom-dual formulas attained 0.8975940487368783 only at the symmetry axis, agreeing with the closed value to machine precision; the scan is corroborative, not the proof.

## originality

PASS

The closest current primary benchmark computes only a certified numerical interval for the exact same one-bit problem: its \(m=2\) row gives a 0.8976 see-saw lower bound and 0.905 SDP upper bound. The classical double-trine paper solves unrestricted one-way LOCC using a three-outcome Alice POVM and obtains the larger success \(1/2+\sqrt3/4\), so that theorem does not determine the binary-message optimum. Targeted Resultary searches using the exact decimal/radical and one-bit aliases returned no prior implication-equivalent published finding.

## value

PASS

This closes an explicitly visible certified numerical gap in a canonical nonlocal state-discrimination benchmark and quantifies exactly the operational cost of restricting Alice to one communicated bit. The result also identifies a simple optimal projective protocol and cleanly separates the \(m=2\) optimum from the known three-outcome one-way optimum, so it is a motivated exact communication-constrained invariant rather than an arbitrary finite optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
