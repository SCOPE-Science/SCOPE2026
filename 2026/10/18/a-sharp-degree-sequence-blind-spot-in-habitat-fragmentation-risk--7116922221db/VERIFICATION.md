---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility of the mathematical claim

Run `python verify_fragmentation.py` with standard Python 3. The script requires no external packages or remote resources. It computes the component count of each surviving induced subgraph in two independent ways, enumerates all Prüfer-labelled trees through six vertices with canonical isomorphism deduplication, and uses `fractions.Fraction` for exact equality comparisons.

The run reproduced six-vertex tree-type counts \((1,1,1,2,3,6)\), the unique degree-twin pair, and the fixed-four-survivor distributions \((4,8,2,1)\) and \((5,5,5,0)\) over component counts one through four. The first and second raw-moment difference coefficients were zero for every retained cardinality, while the third difference coefficient was six at cardinality four and zero elsewhere. Exact Bernoulli checks were also made for all trees through six vertices at retention probabilities \(1/3,1/2,3/4\), and the path–star fixed-budget variance gap was checked for every cardinality on trees with four through nine vertices.

The code's finite enumeration does not itself prove the all-order formulas; those are deduced from the forest identity, edge-pair covariance, and elementary degree inequalities in `RESULT.md`. The only finite completeness needed for the sharp third-moment threshold is the exhaustively enumerated tree isomorphism list through order six. No independent external validation has been performed.
