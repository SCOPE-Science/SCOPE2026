---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Weighted adjacency B=J sum_j translation by e_j + K translation by all-ones is diagonal in Walsh characters χ_S, with λ_k=J(d−2k)+K(−1)^k. For fixed parity, λ_k drops by 4J as k rises by 2, so the only minimum candidates are k=d and k=d−1; comparing gives η=(−1)^d K/J and threshold η=1. Rayleigh lower bound Nλ_min/2 is attained by an actual Boolean character, giving the exact energy for all J>0, real K, d≥2. At equality a Boolean spin after multiplying by χ_D is affine a0+sum_j a_j z_j; f(z)^2=1 forces a0 a_j=0 and a_i a_j=0 for all i≠j, hence exactly one coefficient ±1. This rules out all other minimizers, giving 2,2(d+1),2d states. Averaging character products over the appropriate r mismatching coordinates gives the three Hamming correlation laws. Independent full enumeration of all 2^(2^d) spin states for d=2,3,4 at K/J∈{−3,−1,0,1,3} verified exact energy/minimizers/correlations. These checks corroborate the all-dimensional proof.

## originality

PASS

Qualified best-of-knowledge PASS for complete Boolean ground-state rigidity with all-real antipodal coupling threshold and exact Hamming two-point law on the two-shell (1,d) folded cube. Walsh spectral diagonalization, max-cut bounds, and two-domain antiferromagnetic patterns are old; the claim isolates a specified tunable sparse two-shell Hamiltonian and proves equality classification. Older association-scheme formulations might imply the spectral minimum but not automatically the Boolean equality-class enumeration.

## value

PASS

For a natural finite frustrated Ising family on folded hypercubes, the exact coupling-driven switch, complete labelled ground-state degeneracy and full distance-dependent zero-temperature correlations give a useful all-dimension phase classification. The subtle Boolean-equality proof rules out mixed eigenvectors, so the claim goes beyond reporting eigenvalues or a single minimizing example; no unsupported finite-temperature phase transition is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
