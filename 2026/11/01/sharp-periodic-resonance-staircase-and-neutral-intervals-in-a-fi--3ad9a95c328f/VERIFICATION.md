---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For all M>1, 0<alpha<1, for the four-branch fixed-point-free affine map and the strict itinerary of exactly k outer positive steps/one positive inner/k outer negative/one negative inner, the exact half return is G_k(x)=M alpha^k x-M sum_{j=0}^k alpha^j and full return H_k(x)=(M alpha^k)^2 x+M S_k(1-M alpha^k). For M alpha^k!=1 the unique fixed point X_k= M S_k/(1+M alpha^k) has strict itinerary exactly iff q_k=Σ_{j=1}^{k-1}alpha^-j<M-1. At M alpha^k=1 and q_k<M-1, the return is identity on J_k=(M(S_k-1),M), a continuum of exact least period 2(k+1) cycles. Otherwise its stability multiplier is (M alpha^k)^2. Monotonicity of q_k gives k<M cutoff, exact M=5 birth thresholds and exactly two attracting windows (k=1, alpha<1/5; k=2, 1/4<alpha<1/sqrt5). Independently iterated five strict cycles and 21 neutral sample points across three (M,k) pairs, including M=5 neutral windows. Finite trajectories are checks of the exact affine-return algebra, not a global period census. Boundaries and zero are explicitly excluded.

## originality

PASS

The originating four-branch map and numerical period-4/period-6 parameter observations are prior work. The exact all-M strict itinerary cutoff, stability staircase and intervals of neutral periodic points are finer statements not supplied by the numerical diagrams inspected. The earlier 2021 and 2022 primary mathematical texts were not obtained in full, so the priority of equivalent algebraic formulas is a named residual risk, not a default scientific failure.

## value

PASS

The specific fixed-point-free interval map has an experimentally meaningful staircase of orbital periods; exact birth, attraction, impossibility and neutral-interval thresholds fill a motivated analytical gap and supply boundary information experiments cannot distinguish. The scope is appropriately restricted to a natural symbolic itinerary rather than unsupported global chaos claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
