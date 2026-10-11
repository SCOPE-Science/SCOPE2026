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

For a three-vertex principal block, the determinant identity \(\det R=(1-x^2)(1-y^2)-(z-xy)^2\) makes the conditional LKJ density even about \(z=xy\), so \(\mathbb E[z\mid x,y]=xy\). Hansen's exact pairwise independence and variance \(\mathbb E[x^2]=1/\nu\) then give the triangle moment \(\nu^{-2}\). For any nontriangle set of three distinct edges, some graph vertex has odd degree, and conjugation by the corresponding diagonal sign matrix reverses the product while preserving the LKJ law, forcing expectation zero. The cubic trace is then the sum over ordered distinct vertex triples. I independently re-expanded the determinant and checked the normalization at representative parameters.

## originality

PASS

Hansen proves exact pairwise independence for distinct LKJ off-diagonal entries and develops the high-dimensional spectral limit, while explicitly leaving higher-order dependence present; the checked source does not state the exact triangle-supported third joint moment or the cubic-trace identity. Focused searches for \(\mathbb E[C_{12}C_{13}C_{23}]\), LKJ third moments, and triangle cumulants found no implication-equivalent published formula.

## value

PASS

The theorem pinpoints the first obstruction hidden beyond an exact pairwise-independence result and converts it into an explicit finite-dimensional spectral statistic that matches the third centered moment of the limiting law. This is a natural structural statistic of the LKJ ensemble, not a parameter-only restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
