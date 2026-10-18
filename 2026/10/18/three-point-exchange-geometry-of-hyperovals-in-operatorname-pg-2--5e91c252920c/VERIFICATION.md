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

# Reproducibility and checks

The included `verify_direct.py` checks the field polynomial construction, the 21 projective lines, the complete 54,264-candidate six-point enumeration, all 168-by-168 adjacency entries, 14,028 unordered pair overlaps, 4/5/16/11 common-neighbour values, three 56-vertex even-overlap classes, integer matrix annihilator and five spectral moments. It requires Python 3 with NumPy. Its exact JSON result is included as `direct_output.json`.

The independent `verify_quadrangles.py` instead uses a literal multiplication table and a different normalization, checks 2,520 four-arcs with unique hyperoval completion, all pair overlap/two-walk counts, and 168 breadth-first searches. It requires only standard Python 3. Its actual result is `quadrangle_output.json`.

To reproduce, execute `python3 verify_direct.py > direct_output.json` and `python3 verify_quadrangles.py > quadrangle_output.json` from the same directory. The shared canonical hyperoval-set digest is `02ec2a9578cdf81b7773f1feeda922c745a0e539c8dbce7a8f76e91cd61d3694`. Integer calculations are exact, not approximate eigenvalue estimates. Each program has assertions for the key numerical facts. These computations exhaust the explicitly finite domain; they do not constitute an infinite-family theorem.

Limitations: Only the Desarguesian order-four plane is covered. No independent external audit, proof-assistant formalization or publication-priority certification is claimed.
