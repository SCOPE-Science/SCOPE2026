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

# Verification and reproducibility

Run `python3 verify.py` using Python 3.9 or later and its standard library alone. The program uses exact rational arithmetic for each order \(2\leq M\leq12\). It constructs \(Q\), the positive normalized infection-rate polynomial \(P\), and the degree-\(M\) endemic equation; tests positivity of all normalized rates; verifies the prescribed alternating signs at all \(M\) rational interior sampling points, the negative sign at one, and the coefficient-by-coefficient identity with the complete-simplicial mean-field polynomial. The sign pattern and exact degree certify \(M\) distinct simple interior roots for each tested order, without floating-point root-finding. The test separately verifies that each rescaled infection pressure is positive.

The accompanying analytical inequalities prove the same sign conditions for **every integer order** and every sufficiently small positive rational perturbation parameter, and also establish the sharp upper bound on locally attracting positive states. The finite script does not establish the general theorem by enumeration and makes no claim about finite-population stochastic stationary distributions or nonhomogeneous hypergraph dynamics.

The source equation is equation (II.31) of arXiv:2309.12752v1; recovery is set to one, and the coefficient identification is \(s_j/j!=\lambda_{j-1}\). The original author's mean-field limit is taken as the definition of the deterministic equation under study, not re-certified here.
