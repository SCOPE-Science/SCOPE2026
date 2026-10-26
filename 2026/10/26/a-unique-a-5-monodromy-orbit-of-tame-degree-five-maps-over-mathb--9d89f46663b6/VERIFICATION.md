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
# Exact reproducibility

Run `python3 verify_symbolic.py`, `python3 verify_extensions.py`, and `python3 verify_pairwise.py` using Python 3 with the standard library; all three print `VERIFY_OK` when their assertions hold. No downloaded data or symbolic algebra packages are required.

A bit mask \(m\) represents \(\sum_{j=0}^5 (m_j)x^j\), and a pair of coprime masks gives a morphism of degree five upon homogenization. The first verifier tests every degree-five pair and all critical factors of degree at most four. The second evaluates local expansions over two separately constructed extension fields. The third checks literal set equality. Orbit enumeration is performed independently from extension-field arithmetic by the symbolic checker. The full list of 60 tame coefficient pairs and reference outputs are included.

The conceptual proof of \(A_5\) monodromy additionally uses the mathematical fact that tame inertia normally generates the geometric monodromy of a branched cover of \(\mathbf P^1\) and the lack of 15- or 30-order subgroups of \(A_5\). These are proved in the main writeup by reduction to unramified covers and the elementary subgroup argument; no machine computation substitutes for those infinite statements. Independent audit: not performed.
