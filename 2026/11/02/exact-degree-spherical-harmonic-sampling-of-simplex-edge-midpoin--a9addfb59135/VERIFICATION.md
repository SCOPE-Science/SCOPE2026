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

# Reproduction and limits

Run `python3 verify.py` with Python 3. The checker uses only its standard library and builds the 54 exact polynomial numerator sectors for every \(3\le k\le20\). It applies the rational-root theorem to the complete list of divisors of each primitive polynomial's constant term, after checking the small-prime factorization is complete. It uses exact Horner arithmetic throughout and rejects candidates with exact modular arithmetic; the only positive-dimensional parameter roots at integer \(n\ge5\) are \((k,\text{sector},n)=(3,1,8),(4,0,8),(5,0,16)\). It also checks the algebraic intersections needed in the conic argument. Expected first output line: `HYPERSIMPLEX_SAMPLING_CERTIFICATE_OK`.

The analytic Wronskian inequality in `RESULT.md` proves independence of the seven quadratic powers for every \(k\ge21\) and then uses the connected non-bipartite disjoint-pair graph to rule out all annihilators. This infinite argument is not computationally validated by the finite-degree run. The normalization and Gram formulas can be checked directly from the Gegenbauer addition formula and incidence-matrix spectrum. Independent validation has not been carried out.
