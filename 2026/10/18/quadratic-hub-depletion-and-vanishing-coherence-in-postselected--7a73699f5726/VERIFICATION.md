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

For the specified diagonal-inclusive jump convention, G is diag(m²+m,2,…,2). The completely positive Dyson expansion has positive weight for all connected jump paths for p(1−η)>0. Given nonzero PSD input, start from a positive diagonal entry and take paths (with an on-site jump if needed) whose jump times cluster near zero; the target vertex vectors after the remaining invertible no-jump propagator span the space. Continuity gives positive quadratic forms from those terms, hence positivity improvement. Perron–Frobenius gives a simple dominant exponent and attraction for every density matrix after trace normalization. The antisymmetric leaf rank-one projector has unjumped weight e^(−2pt); applying the strictly positive left Perron eigenfunctional to the nonzero positive jump correction gives λ>−2p. The trace-loss identity gives λ≤0. At η=0 balanced jump gains and losses make the generator unital, so the normalized identity is the unique limit. Direct commutator and diagonal jump evaluation independently reproduces all five matrix rows and the scalar equations in RESULT.md lines 47–77: for example the 0j commutator is (m−1)(u+iv)+a−b−(m−1)d. On −2p<λ≤0, q_m≤2(1−p)²/T_m=O(m⁻²) already without a lower bound on λ+2p. Thus for fixed 0<η<1 the first scalar equation gives x=(1−η)/(ηm)+O(m⁻²); the second pins λ near −p(1+η), a positive distance from −2p for all sufficiently large m. Now K_m=pm²/2+O(m) and b=(m+x)⁻¹. Substitution gives all coefficients and errors displayed, with the leaf-pair term m(m−1)|d| dominating the aggregate coherence at p<1 and the hub-leaf term O(m⁻²). For η=ξ/m, x tends to 1/(1+ξ), and λ tends to −pξ/(1+ξ); at p=1 the offdiagonals are exactly zero. The check is replayable from the stated generator, G, and the three offdiagonal equations, and does not depend on an inferred numerical root. check_star.py was inspected, not executed; its reported 216 finite checks are corroboration, not proof or a uniform double-limit claim.

## originality

PASS

The same conditioned equation and same single-particle Laplacian jumps are prior. The distinct result solves the conditional stationary problem for the degree-growing star, with simultaneous entrywise and aggregate coefficients and the efficiency crossover. The closest indexed star-degree law uses different jump and Hamiltonian conventions and gives a different power for the hub.

## value

PASS

A star isolates the effect of rapidly increasing jump intensity at a single hub. The explicit law distinguishes quadratic depletion from the unmonitored inverse-degree population, and shows that even the sum over all growing numbers of coherences tends to zero. The η=ξ/m crossover and the survival exponent specify when imperfect monitoring begins to change the stationary mass, adding quantitative content beyond finite-network localization examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
