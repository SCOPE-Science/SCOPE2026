---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Unitary Fourier diagonalization gives sums of two rate-weighted roots of unity, up to the shift convention. In a collision both indices differ. The nonzero root-of-unity chords must have parallel directions, so (j+j′)n−(k+k′)m is a multiple of mn. Coprimality and 1≤j+j′≤2m−3 (likewise for n) force sums m and n. Thus neither index is a self-conjugate frequency and each mode has at most one partner. Opposite signs of the two imaginary parts are necessary for positive rates, giving exactly the pairs and positive sine ratios stated. The two Fourier evaluation rows at inputs translated to (0,0),(u,v) lose rank exactly when 2ru/m−2sv/n is integral, equivalent by coprimality to both divisibilities. Simple modes never obstruct one input, repeated modes require two, and each coordinate adjacency clears the corresponding divisibility. Equal sines in (0,π) would force equal or supplementary angles, both excluded by the same modular argument at these indices; prime orders force zero displacement for a failure. An independent real-space eigensolver/PBH SVD checked 109 site sets including resonant composite orders and an equal-rate case (/workspace/branches/frozen_math_replay.py, argument 2). These numeric checks are bounded corroboration, not the analytic proof. The uploaded 82-digit checker was inspected, not executed.

## originality

PASS

Pass restricted to the exact positive-rate collision classification and all two-site placements on the stated directed family. Product eigenvalue sums, PBH eigenspace rank, Fourier modes, and the generic multiplicity-based actuator-count framework are not the original contribution. The strongest inspected related statements and indexed records do not give the directed coprime chord restriction or its exact resonance and placement formulas. Directly relevant specialist full-text access remains unresolved, so this is not a priority guarantee.

## value

PASS

Exact exceptions determine sensor or actuator placement in a natural directed lattice family. The criterion distinguishes truly inadequate displacements from adjacent or other successful pairs at resonance, handles all positive ratios rather than generic ones, and provides a concrete composite-order obstruction. This is useful beyond the generic eigenvalue-multiplicity principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
