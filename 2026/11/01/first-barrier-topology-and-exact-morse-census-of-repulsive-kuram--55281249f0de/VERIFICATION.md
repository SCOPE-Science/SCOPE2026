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

A triangular cactus assembled by attaching two new vertices per triangular block has global torus coordinates (phi_i,psi_i) after quotienting the common phase. Its energy is exactly a sum of e=cos phi+cos psi+cos(phi-psi). Solving sine stationarity gives exactly two minima at -3/2 with Hessian index0, three saddles at -1 index1, and one maximum at 3 index2, all nondegenerate; block-diagonal Hessian inertia yields (2+3zt+z9t2)^r. Chirality change crosses sin(phi-psi)=0 and forces e>=-1 on some block; holding others at ground energy proves barrier >=E*+1/2. Explicit path (s,-s), s from 2pi/3 to 4pi/3, reaches max -1 and proves equality for all pairs via sequential flips. Standard Morse handles yield 2^r contractible components below first saddle, then connected wedge of 3r2^(r-1)-2^r+1 circles before +1; only 0 and 1 handles appear. Friendship block swaps force equal Haar basin masses 2^-r, and Hessian L(G)/2 gives spectral gap 1/2 (r>=2) or 3/2 (r=1). Full vertex flow need not decouple.

## originality

PASS

The local six-state triangle equilibrium analysis is earlier Zhao–Zhou work, and general graph Laplacian inertia via cycle-space (Bronski–DeVille–Ferguson) is established. The mathematically combined all-size triangular-cactus Morse/energy census plus sharp universal pairwise chirality-switching minimax barrier and first-sublevel homotopy does not follow directly from inspected existing statements. Best-of-knowledge original; frustrated XY cactus literature may contain an equivalent via partition functions/barriers.

## value

PASS

For frustrated repulsive oscillator networks, counts of stable chirality patterns alone do not reveal the energy needed to switch, the first landscape topology change or basin symmetry. The arrangement-independent exact all-r polynomial, universal sharp barrier and nontrivial first Betti number are motivated structural results in an infinite family of graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
