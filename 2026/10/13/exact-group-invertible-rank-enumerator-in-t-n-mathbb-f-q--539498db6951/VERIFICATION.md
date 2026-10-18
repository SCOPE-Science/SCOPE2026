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

For upper-triangular A with k zero diagonal entries, group invertibility (Drazin index ≤1) is equivalent to semisimplicity of eigenvalue 0, hence rank A=n−k (its minimum rank). Partition the last diagonal entry: if nonzero, q^{n−1} unrestricted final-column choices preserve preceding rank; if zero, the column must lie in image B, of dimension n−k, yielding q^{n−k} choices. Induction gives q^{binom(n,2)−binom(k,2)} for every fixed diagonal. Choosing positions and nonzero values yields binom(n,r)(q−1)^r q^{binom(n,2)−binom(n−r,2)}. Independent modular-rank enumeration checked every 2^10 upper triangular 4x4 matrix over F2 and every 3^6 upper triangular 3x3 over F3, including fixed zero-position counts.

## originality

PASS

Mary's author-hosted full preprint addresses group inverse reverse-order laws and Lemma 3.14 asserts shape preservation of inverses for triangular matrices over Dedekind-finite rings, not counting upper-triangular completions. Hartwig–Shoaf provide invertibility conditions for bidiagonal and triangular Toeplitz special families; their full publisher PDF is about those restricted matrix shapes, not a finite-field T_n rank census. Meyer–Rose give Drazin index and block-form structural bounds, not an indexed exact upper-triangular count. Searches of completely regular/group elements and finite triangular semigroups found no full fixed-diagonal formula, but hidden semigroup enumeration remains priority risk.

## value

PASS

A full dimension- and rank-stratified exact census for a standard finite matrix semigroup is a natural invariant for generalized inverses. The fixed-diagonal position independence is a structural uniformity theorem, and the closed all-n formula is more than an isolated small-field table. No numerical claim about arbitrary coefficient rings is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
