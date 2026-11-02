---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Independent reconstruction from the eight Git blobs (tree f279822b5b5856de10b8732739d4cd141caa19ea) confirms the exact claim for F,k>0 and every compact invariant Borel probability supported in (0,∞)^2. Invariance of antiderivatives H(u) and K(v)=∫ψ(v)/v gives E[udot|u]=0 and E[vdot/v|v]=0. They give E[v²|u]=F(1-u)/u and E[u|v]=(F+k)/v. Conditional orthogonality establishes covariance and both global/local velocity variance identities. If an activity defect vanishes, the corresponding coordinate is constant on every complete support orbit, forcing the second to be constant: equilibrium support exactly. Essential sup U of u>0 gives v≥(F+k)/U, then F(1−u)/u≥(F+k)^2/U² and the quadratic FU²−FU+(F+k)^2≤0, yielding Δ≥0, U≤(1+sqrtΔ)/2, and v≥(F+k)/u+. An independent SymPy exact check verified both pointwise residuals, the support-quadratic algebra and both rational positive equilibria at F=1/16, k=3/80 with Δ=9/25; stored VERIFY_OK was not treated as analytical proof. The face v=0 is intentionally excluded and Δ=0 is permitted.

## originality

PASS

Best-of-knowledge PASS for the exact two Gray–Scott fiberwise calibrations, kinetic-speed variance decompositions and invariant support envelope. The saddle-node condition and positive equilibria are conclusively classical prior art. A complete publicly available 2017 same-ODE analysis was read and did not yield the measure laws; an exact full-text review of the 2021 complete phase-portrait classification was blocked after lawful OA/preprint and institutional access attempts, so possible overlap is a recorded risk, not a manufactured noncoverage claim. Relevant other-system invariant-measure methods are already published and were not counted as Gray–Scott coverage. The identical indexed record was excluded from novelty evidence.

## value

PASS

The two concentrations and the autocatalytic transfer uv² are canonical observables of a natural reaction model with nontrivial homogeneous periodic dynamics. Beyond routine generator orthogonality, the paired calibrated conditional nullclines yield exact measurable kinetic activity and rigidity for all compact positive invariant probability measures without ergodicity, and the two-calibration essential-supremum argument yields explicit parameter-sharp concentration envelopes U≤u+ and v≥(F+k)/u+. The upper envelope is attained at the positive equilibrium (u+, (F+k)/u+), so it can test numerically estimated stationary phase portraits and periodic-orbit concentration bounds. This is a motivated structural invariant/constraint, not a new saddle-node theorem or broad dynamics classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
