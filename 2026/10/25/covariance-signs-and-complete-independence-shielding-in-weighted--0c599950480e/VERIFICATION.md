---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

At degree-two interior vertices the incident retained-edge indicators agree, forcing each path wholly present or absent. The two terminal even-degree conditions coincide and require even sum of full-path indicators. Relative path weights a_i=product p_e and b_i=product(1-p_e) yield independent Bernoulli(q_i=a_i/(a_i+b_i)) before parity restriction, and parity indicator (1+(-1)^sum)/2 gives exact normalization 1+T>0 (T=product(1-2q_i)) and all-subset marginals. Direct subtraction of E XiXj and product of marginals gives positive factor 4q_i(1-q_i)q_j(1-q_j)/(1+T)^2 times product of other biases. If an unmeasured bias vanishes, measured joint law is product; otherwise changing the parity of the other measured indicators changes Xi conditional odds (including the all-path support case), so no mutual independence. At homogeneous p each bias crosses sign at 1/2; sign (-1)^(m-2). Independent exact fractions for a hetero three-path network verify 29 marginal/covariance equalities and nonfair-edge balanced-path shielding; code elsewhere in source reports 2102 finite checks. Proof holds for any m and irrational interior p by algebra, not tests.

## originality

PASS

Best-of-knowledge PASS with overlapping antecedents. Grimmett–Janson establishes the general conditioned-even graph law; Klausen 2022 explicitly studies three/four-path theta network with partition functions and negative association of different whole-cycle events; Hansen–Klausen–Wildemann 2025 table enumerates eight configurations of a four-path network for terminal connectivity. Fixed small-network correlations can be deduced algebraically, so no claim that the parity law or all finite cases are new. These primary target statements do not directly supply the heterogeneous arbitrary-m sign factorization and iff full-subfamily independence shielding. A general parity-conditioned Bernoulli theorem might implicitly dominate; this remains a high-priority residual risk.

## value

PASS

Multipath theta networks are established test cases for FKG failure and nonmonotonicity in even-subgraph/Ising graphical representations. A complete all-m weighted covariance sign classification and exact independent-subfamily shielding criterion identify a mathematically motivated dependence boundary and explain odd-versus-even path-count reversal, stronger than a cheap partition-sum normalization or a single counterexample. The restriction to multipath graphs is natural but explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
