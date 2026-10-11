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

The proof reconstructs. Modulo \(2m\), each residue is the union of two translates of \(H=\langle n,p\rangle\). For \(r\le m\) the second translate is absorbed and the maximum is the Hwang--Song value \(G_0\). Writing \(r=m+s\), symmetry of the two-generated numerical semigroup gives \(G_s=G_0+s(m^2-Q)-2m\lambda_H(sm-Q)\). The elementary lower bound \(\lambda_H(u)\ge u\) excludes every \(s\ge2\). At \(s=1\), the separate cases \(m-Q\in H\) and \(m-Q\notin H\) give a strictly positive correction. The crossed-form argument yields \(\lambda_H(d)=\min(an,bp)\) in the gap case. Independent exact shortest-path Frobenius calculations over a larger small-parameter grid reproduced the universal formula with no mismatch; the finite replay is corroborative, not the proof.

## originality

PASS

Originality passes. The complete Hwang--Song primary paper was read: for the coprime branch its main theorem and residue analysis assume \(m\ge 2Q\), while the audited theorem treats the disjoint adjacent band \(Q<m<2Q\) and identifies the new dominant residue and exact positive correction. Earlier Pythagorean-semigroup papers concern three-generator triples rather than this four-generator quadruple semigroup.

## value

PASS

The threshold \(m=2Q\) is built into the strongest published same-object theorem. Determining the entire immediately adjacent band, proving that the old formula fails at every admissible point there, and giving the exact one-residue correction is a natural boundary theorem for this structured Frobenius family rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
