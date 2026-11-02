---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS. For G=(Z/qZ)^n and z=r exp(iθ), direct group character sums yield λ_k=Re[(1+(q−1)z)^(n−k)(1−z)^k], multiplicity C(n,k)(q−1)^k, for all integer q>=2,n>=2 including composite q. Apart from the all-ones boundary (r=1,θ=0), factor arguments α≥0 and β≤0 have step δ=α−β<π. Their n+1 cosine arguments decrease in steps <π while straddling 0; if they all have nonnegative cosine, none can skip the full width-π negative strip, forcing nα and nβ into [−π/2,π/2]. This proves PSD exactly when r sin(θ+φ)<=sinφ and (q−1)r sin(θ−φ)<=sinφ, φ=π/(2n). Intersections of the two sine constraints yield binary two-island regime sinφ<r<=tanφ, and for q>=3 only n=2 with 1/sqrt2<r<=sqrt(1/2+1/(2(q−1)^2)). At contact n=2 the k=0,2 Fourier eigenvalues vanish and only k=1 remains, giving rank 2(q−1) and λ=q²/[2(q−1)]. Independent direct full-matrix eigenspectra for q∈{2,3,4}, n∈{2,4} in tested combinations match all algebraic levels; finite checks do not prove all parameters.

## originality

PASS

PASS, bounded best-of-knowledge. The standard finite-group character/Krawtchouk spectrum is prior mathematical machinery. The assessed new finding is the exact acute-sector two-sine PSD iff criterion, the disconnected/nonbinary n=2 island classification, and first-harmonic rank-collapse contact. Harrow–Kolla–Schulman (2012) proves a maximal L2 bound for spherical averages on hypercubes; Xu (2013) studies Hahn/Jacobi/Krawtchouk and nonnegative Poisson kernels. Neither available inspected theorem implies the exact complex-noise cosine-PSD phase diagram. An unindexed positive-definiteness theorem may still dominate; no search proves novelty.

## value

PASS

PASS. Exact positive-definiteness for a classical finite product-metric family is a natural harmonic-analysis question; its disconnected admissible-angle islands and sharp nonbinary dimension restriction are substantive phase transitions. The critical rank-2(q−1) orthogonal-projection identity is an exact structural consequence, not an arbitrary computed slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
