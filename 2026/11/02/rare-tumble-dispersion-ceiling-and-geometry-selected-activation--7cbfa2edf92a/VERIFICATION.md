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

For fixed positive D, the stationary tilted flux gives the stated u(F;D), including its sign. For the switched generator, project the Poisson equation onto the two subspaces centered in the respective frozen invariant densities. Sectorwise constants, even when their difference is of order 1/gamma, are killed by this projection. The centered coupling is a bounded perturbation of the two invertible elliptic operators, so both centered correctors are bounded in C^1 as gamma tends to zero. Integrating against the two frozen densities and summing cancels the divergent constants, giving the average frozen velocity plus O(gamma); their difference then sets the jump amplitude to the frozen velocity gap divided by 2 gamma (up to sign) plus O(1). The thermal martingale bracket stays bounded, while half the jump bracket has leading coefficient gap^2/(8 gamma); the bounded-in-time corrector does not affect the variance rate. Jensen is strict for shifts that are not periods of a nonconstant continuous U, a set of positive measure. Comparing with the flat denominator bounds each signed frozen velocity strictly by its force magnitude, and uniform convergence of the spatial exponential average at high D proves sharpness. In the locked triangle, lift the endpoints to x,y=x+s: the tilted potential rises on only one segment per period and falls on the other, so on an interval of length at most L the unique maximizing endpoint pair modulo translation is the full rising segment. Its four one-sided integrals give D^2 times the squared reciprocal-slope sum for each tilt. For the negative tilt, the numerator exp(vL/D) changes the exponent h+va to the reverse activation h-v(L-a). The gap adds the two signed magnitudes, so equal barriers yield four times a single-branch square. Independently, exact integration of the piecewise-linear phase at apex locations 0.35, 0.50 and 0.65 with L=h=1, v=0.5 agreed with both signed leading velocities within 0.1% for the three tested D values; at D=0.025 the exact-to-leading K ratio was 1.00944 at the off-center locations and approximately 1 at the center. These finite comparisons are separate from the rare-flip proof.

## originality

PASS

The fixed-tilt flux and bare telegraph variance factor are standard inputs, and the exact sawtooth model has prior steady-current analyses. The supported distinction is the rare-flip variance coefficient for additive symmetric forcing in the thermally diffusing periodic model at arbitrary fixed D, with a strict sharp bound for every nonconstant potential and locked triangular activation including the symmetric prefactor. The strongest available comparisons change the forcing mechanism, describe only means at the same parameters, or use a fixed-rate weak-amplitude expansion. None of those gives the arbitrary-amplitude singular variance limit and its consequences.

## value

PASS

The leading long-time dispersion is a natural transport observable not fixed by the stationary drift, and it diverges as the flip rate vanishes at fixed positive noise. The formula quantifies it using measurable frozen currents, identifies a strict free-particle ceiling beyond the weak-amplitude regime, and distinguishes the two activated directions and the equal-barrier prefactor in a standard locked geometry. This supplies a useful boundary law rather than another finite-parameter current calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
