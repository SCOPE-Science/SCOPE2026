---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For a generic Haar-random central normal u, every vertex of B(a)∩u^⊥ corresponds bijectively to a transversely intersected box edge. There are 2^(d-1) edges in each direction i. Gaussian representation u=G/||G|| gives the crossing event |Σ_{j!=i}ε_j a_jG_j|<a_i|G_i| for independent centered normals, so its probability is (2/π)arcsin[a_i/(Σa_j²)^(1/2)]. Summing exact indicators establishes E[V]=2^d/π Σ_i arcsin sqrt(p_i). For f(p)=arcsin sqrt p, f'(p)=1/[2sqrt(p(1-p))]; if x>y and x+y<1 then x(1-x)>y(1-y), hence f'(x)<f'(y). Every nontrivial balancing transfer increases the sum whenever d>=3 and all p_i>0; d>=4 in claimed scope. The cube is the unique maximizer; successive coordinate mergers give strict lower infimum 2^(d-1), attained only as a boundary limit. Taylor f''(1/d)=-(d-2)d²/[4(d-1)^(3/2)] gives deficit coefficient (2^d/π)(d-2)d²/[8(d-1)^(3/2)], and the 4-cube expectation is exactly 32/3. Independent 4D Gaussian edge-count Monte Carlo reproduced 10.6667 and asymmetric-case predicted values within sample error; the exact result and strict inequalities are analytic, not Monte Carlo consequences.

## originality

PASS

Best-of-knowledge original exact central, Haar-oriented rectangular-orthotope vertex expectation plus strict Schur concavity and sharp extremal shape. Swan 2016/2018 proves a constant 2^k for random k-flat with uniform *translation among intersecting positions*, a different law; here 2^(d-1) is merely a nonattained central-section infimum. Marichal–Mossinghoff derives volume integrals of central cube sections, not mean vertex number or orthotope shape ordering. Related published SCOPE d=4 cube face-vector distribution concerns fixed cube special case and does not cover continuous orthotope p-space.

## value

PASS

A natural combinatorial statistic of random central sections has an explicit all-dimensional formula and sharp geometry-of-numbers shape theorem. The 4D cube value and strict Schur ordering under diagonal constraint quantify central section complexity beyond volume-based slice results. The lower infimum differs meaningfully from translated-slice expectation although the numeric value agrees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
