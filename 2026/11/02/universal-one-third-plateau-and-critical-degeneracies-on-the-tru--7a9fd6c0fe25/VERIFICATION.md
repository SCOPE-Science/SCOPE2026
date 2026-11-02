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

# Verification and limitations

The analysis derives the full ground-energy envelope from two exact local decompositions of the 12-spin Hamiltonian; it identifies all equality cases at \(h=K\) and \(h=K+2J\), then counts the resulting spin configurations by directed-edge and inclusion–exclusion arguments on \(K_4\). The calculation is exact for all real \(J,K>0\) and \(h\ge0\).

`verify_truncated_tetrahedron.py` is a standalone Python 3 standard-library checker. Running `python3 verify_truncated_tetrahedron.py` reconstructs the graph from 12 ordered pairs, enumerates every one of its 4096 binary spin assignments using integer/rational arithmetic, and checks energy minima, local minimizer characterizations, magnetization sectors and degeneracies for seven exchange choices and fields at each transition and in every intervening region. It also independently counts the five local equality classes.

A finite exhaustive checker validates the finite state space at the tested field parameters, while the triangle/bridge proof supplies the necessary argument for arbitrary positive real parameters. This package does not certify uniqueness in the worldwide literature, external validation, finite-temperature response, or quantum and thermodynamic-limit extensions.
