---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For a fixed point pair, the \(\lambda\) blocks through it contribute \(\lambda(k-2)\) incidences outside the pair. Symmetric-design block intersections give exactly \(\lambda-2\) common outside points for every pair of these blocks, hence \(\sum_z\binom{m_z}{2}=\binom\lambda2(\lambda-2)\). Since \(m(m-1)\le\lambda(m-1)\), the union is at most \(\lambda(k-2)-(\lambda-1)(\lambda-2)\). A point outside this union gives the separated triple. In \(\mathrm{PG}(3,q)\), every three points lie in a hyperplane and direct substitution gives equality. The actual verifier was inspected and independently checks the projective examples for \(q=2,3\), but the proof is symbolic.

## originality

PASS

The motivating paper's Proposition V.1 gives for triples only the weaker union bound \(v-2>\lambda(k-2)\). Its complete Section V was inspected and it explicitly presents \(\mathrm{PG}(3,q)\) as a no-separated-triple family, but it does not make the mandatory-overlap correction. Resultary and targeted literature searches found no earlier statement of the corrected bound.

## value

PASS

The theorem sharpens the exact sufficient condition used in an open storage-design regime by a positive term for \(\lambda\ge3\), and an infinite projective family certifies the boundary. It is a natural structural lemma with a sharp extremal family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
