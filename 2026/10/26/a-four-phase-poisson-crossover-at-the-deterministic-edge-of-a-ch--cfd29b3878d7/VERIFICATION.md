---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The orbit offsets satisfy B_(Pd)+v_(Pd)=B_d; hence the center is constant at cycle steps. In Fourier variables the four-step transition is I+4(1−p_n)(G−I)+O((1−p_n)²), with the stated cyclic twirl G. The remainder times n vanishes, also when λ=0. The cyclic eigenvalues are g₀,g₁,g₂,g₁, and conjugating back to position with uniform initial direction gives the same four weights g₀,g₁,g₂,g₁. The multipliers from P^r are 1,i^r,(−1)^r,(−i)^r. This gives the stated characteristic function; continuity at zero gives weak convergence. At (π,π) the value is (−1)^r, and at (π,0) it is e^(−λ/2)cos(πr/2), proving exactly three distinct laws at every finite λ. For the center displacement the starting vector is the direction law at zero center displacement and the final direction is summed out; every column sum of G is g₀. This gives the orientation-independent compound-Poisson characteristic function, with g₀ the transform of the difference of two independent uniform square vertices. Equivalently, conditional on a fixed finite number of resets, the ordered reset slots have asymptotically independent uniform residues modulo four, by counting ordered slots in distinct four-step blocks. The fresh rotating-frame labels are independent uniform, and each independent uniform phase maps the previous label and fresh label to an independent uniform pair of absolute square vertices conditional on the past. Summing the jumps gives the same center limit. Summing the lag correlation p_n^k cos(kπ/2) with weight 2(n−k) gives the finite geometric-sum expression in the proof; its main term, constant term and terminal term tend respectively to λ, 1 and −e^(−λ)cos(πr/2). Finally the center jump covariance is I₂/2 and endpoint position offsets are bounded, giving the stated iterated Gaussian limit.

## originality

PASS

The same coin and fixed-parameter transport are prior work. The distinct part supported by the inspected comparisons is the unscaled rare-refresh limit, including the explicit residue-dependent position law and phase-independent compound-Poisson orbit-center displacement. The moment profile is a relatively direct finite-sum consequence of the known model's velocity correlations; it is not the main basis for novelty.

## value

PASS

The fixed-parameter diffusion coefficient vanishes at the deterministic edge and cannot describe the law at order-one refresh counts. This crossover calculation resolves that boundary: the position retains exactly three phase laws while the center removes the terminal phase and has independently identified lattice jumps. The formulas give a usable comparison across the deterministic, compound-Poisson and large-rate Gaussian regimes for a previously studied walk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
