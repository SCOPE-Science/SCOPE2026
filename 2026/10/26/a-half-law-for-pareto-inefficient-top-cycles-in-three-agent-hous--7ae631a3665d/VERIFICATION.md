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

# Reproduction and verification

Run `python3 verify.py` with standard Python 3. The complete finite domain is the Cartesian product of all six strict house orders for each of three agents, comprising \(6^3=216\) profiles. Every profile has exactly six bijective assignments. The code uses integer rank comparisons to construct majority adjacency, Pareto dominance, and McKelvey covering, and checks the seven-atom count vector \((48,36,36,18,36,36,6)\) as well as the discrepancy counts \((108,36,36,36)\).

For every profile, it reconstructs the top cycle using both Floyd–Warshall Boolean closure and independent depth-first reachability; it reconstructs Pareto optimality using both direct all-assignment comparison and all serial-dictatorship priority orders; and it reconstructs the McKelvey uncovered set using both direct covering implications and two-hop majority paths with at least one strict edge. The resulting sets agree in every case and satisfy the exact set inclusions. It also explicitly tests all four two-agent strict-preference profiles for the minimality boundary.

No random sampling, floating-point approximation, or external data are used. The certificate establishes only the finite three-agent classification and the separate two-agent statement; it does not certify any extrapolation or publication priority.
