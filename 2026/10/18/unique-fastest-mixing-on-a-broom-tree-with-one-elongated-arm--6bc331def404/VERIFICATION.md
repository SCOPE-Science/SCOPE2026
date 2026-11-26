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

Averaging over the n leaves preserves stochastic feasibility and cannot increase the centered operator norm. For invariant weights, the leaf-contrast eigenvalue gives the lower bound 1−c. The zero-sum vector in RESULT.md lines 26–46 gives a competing Rayleigh bound 1−E/N; saturating the two hub inequalities bounds E by an affine function strictly decreasing in c for n≥3. Its value at c* is Nc*, forcing c=c* and saturation of both hub rows at any invariant optimum. At the candidate the quotient has eigenvalues 1 and μ* and a real-rooted quadratic factor; its vertex lies inside (−μ*,μ*) and the polynomial is positive at both endpoints. The leaf-contrast modes are exactly μ*, proving attainment. For an arbitrary optimizer the permutation average fixes the bridge, single spoke, and mean of the remaining spokes. One may either use the zero-trace positive semidefinite compression in lines 69–77 or apply the active Rayleigh equality to the same zero-sum vector: its energy is unchanged under the averaging, so it is an actual μ* eigenvector, and its nonzero leaf values and zero w coordinate force each remaining spoke weight to be c*. At n=2 the rational proposal has SLEM 4/5. For the alternative weights (1/2,1/2,1/4), the leaf-contrast eigenvalue is 3/4 and the transverse quotient polynomial is t³−t²/4−t/2+1/16; its signs at −4/5, 0, 1/4, 4/5 alternate, placing all three roots strictly inside. The separate exact check at /workspace/branches/21e5bd8a-9811-478f-985a-116b91d9270d/independent_record4.py corroborated the quotient identities and the boundary witness. The frozen verifier was inspected, not run. The result does not solve the n=2 optimum.

## originality

PASS

The distinct same-day double-star record supplies the identical rational candidate and its positive spectral-gap argument after formal singleton substitution; those are genuine overlaps. It does not establish the signed-end spectral bound at q=1 or uniqueness among all stochastic kernels. The exact SLEM and unrestricted uniqueness on that boundary survive the comparison, and neither same-day date establishes priority.

## value

PASS

This closes a natural boundary case of symmetric stochastic optimization on trees. The degree-one side defeats the available neighboring spectral bound, so the exact SLEM is not obtained by quoting the adjacent threshold. The proof also rules out all leaf-asymmetric optima rather than merely exhibiting one symmetric solution, and shows by exact comparison that the same construction ceases to be optimal at five vertices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
