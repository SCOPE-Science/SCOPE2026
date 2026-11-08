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

Established the exact failure-witness equivalence: a selected 2-edge family fails domination iff contained in F_e, the 2n-4 edges meeting e other than e. Checked pair intersection sizes n-2 for intersecting witnesses and four for disjoint, and that only centered witness stars have higher intersections of at least four selected edges; their inclusion-exclusion generating sum yields U_{n,k} and the 3*binom(n,4) correction for k=4. Classifies all dominating triples as triangles and three-edge matchings. n=4 is 3K2. Independently enumerated full K(n,2) subsets for n=4,5,6,7 (2,131,008 total masks); coefficients match formula, including n=5 Petersen and n=7 initial coefficients (140,2205,15162,49854). This finite test corroborates but does not substitute for all-n inclusion-exclusion proof.

## originality

PASS

Best-of-knowledge uniform all-order all-cardinality coefficients for n>=6 are not expressed in the compared same-object works. The K(5,2) Petersen polynomial and minimum domination number 3 are explicitly already known. Complete enumeration requires nontrivial witness-overlap correction; generic incidence membership tests are not already a closed coefficient formula.

## value

PASS

An exact natural infinite family domination polynomial answers a more detailed structural counting question than minimum domination size and yields the sharp 2n-3 universal domination threshold with binom(n,2) extremal non-dominating sets. The 4-edge overlap term is an informative combinatorial obstruction rather than a cosmetic reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
