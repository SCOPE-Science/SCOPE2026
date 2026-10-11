---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For positive concurrence a Bell-diagonal state has a unique eigenvalue above one half; relabel it as \(p_1=(1+C)/2\) and write the other three masses as \(q_i\). The absolute correlation coordinates are exactly \(r_i=C+2q_i\), hence \(r_i\ge C\) and \(r_1+r_2+r_3=1+2C\), with the converse reconstruction \(q_i=(r_i-C)/2\). Ordering \(x\ge y\ge z\), Hilbert--Schmidt geometric discord is \((y^2+z^2)/4\) and the feasible slice is the triangle \(z\ge C\), \(y\ge z\), \(2y+z\le1+2C\). Its vertices give the lower value \(C^2/2\), the rank-three face value \((1+2C+5C^2)/16\), and the isotropic value \((1+2C)^2/18\). Convexity places the maximum at a vertex, and the difference factors as \((1-C)(13C-1)/144\), yielding the exact crossover \(C=1/13\). At \(C=0\), direct optimization on the separable octahedron gives lower zero and upper \(1/16\). Connectedness of the fixed-concurrence slice and continuity of discord prove that the full interval between endpoints is attained. The exact-rational verifier independently checks extremal families, crossover, and a large rational grid; the continuum theorem rests on the triangle proof.

## originality

PASS

Yao et al. give the Bell-diagonal geometric-discord formula and sharp bounds for a different optimization: CHSH Bell violation versus geometric discord. Their full text also quotes the sharp Bell-violation interval at fixed concurrence and records the Werner concurrence--discord relation, but it does not optimize Hilbert--Schmidt discord itself over the fixed-concurrence Bell-diagonal slice. In particular their Werner branch supplies only one feasible family, while the audited maximum switches from a rank-three face family to the isotropic family at the nontrivial value \(1/13\). Lang--Caves study tetrahedral Bell-diagonal geometry for entropy-based discord, a different invariant. Current Resultary and web searches for fixed concurrence, Bell-diagonal Hilbert--Schmidt discord, the exact envelope and the \(1/13\) crossover found no prior equivalent statement.

## value

PASS

Concurrence and geometric discord are standard, mathematically distinct correlation measures, and Bell-diagonal states are the canonical tetrahedral test family. A complete fixed-concurrence attainable interval with explicit extremizers and a genuine branch switch at \(1/13\) is a natural exact state-space classification. Its value is structural rather than dependent on the disputed operational status of Hilbert--Schmidt discord.

The dated certificate retains the supplied scientific assessment, sources and limitations.
