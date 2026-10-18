---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For a≥2,b≥1, the origin-symmetric root polytope lies in H=1⊥, dim d=2a+b−1. Weighted edge design C_t has mass t on AA class edges and 1−t on edges to B. Orthogonal A1/A2 contrasts, B contrasts, A-difference and A-vs-B contrast give eigenvalues (1+t)/(2a), (1−t)/b, (1+3t)/(2a), n(1−t)/(2ab) with multiplicities 2a−2,b−1,1,1. Hence determinant log F=(2a−2)log(1+t)+log(1+3t)+b log(1−t), strictly concave, derivative at 0 exactly 2a+1−b. The maximizer t=0 precisely b≥2a+1, otherwise unique positive quadratic radical. Leverage identity t lAA+(1−t)lAB=1, F'=d(lAA−lAB) proves both types contact for t>0; at t=0 AB gauge is one and AA gauge 4a/d≤1. A determinant/trace certificate and central-symmetry uniqueness establish global Löwner ellipsoid. The sharp subpolytope K_{2a,b} agrees for b≥2a+1. Independent SymPy checked derivative equality and contacts at (a,b)=(2,1),(2,4),(2,5),(2,6),(3,7),(3,9): t turns zero at boundary, AA gauge transitions from 1 to 8/9 or 6/7. Numeric verifier is only corroboration; symbolic concavity and leverage are the infinite proof.

## originality

PASS

Best-of-knowledge examination of actual statements, aliases and implications: the exact final claim is not established by the identified independent primary sources. Published general methods and covered special cases are credited; no failed search is being treated as proof of novelty, and inaccessible plausible papers are named as residual risks. The signed position checkpoint is not scientific evidence.

## value

PASS

An exact geometric screening threshold for genuine vertices of a canonical complete multipartite root polytope is a sharp structural result: above b=2a+1 a strict polytope enlargement becomes metrically invisible to the minimal ellipsoid. The explicit design, eigenvalues, volume and all contact orbits are motivated by optimizing Euclidean shape; not a renaming of lattice-equivalent combinatorial invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
